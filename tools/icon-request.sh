#!/bin/bash
# OmaPixIcon — icon request exporter.
#
#   curl -fsSL https://raw.githubusercontent.com/Raiden-MeixElysia/OmaPixIcon/main/tools/icon-request.sh | bash
#
# Finds every launcher app on this machine that OmaPixIcon has no pixel icon for,
# and packs what the artist needs into ~/iconrequest.zip:
#   apps.tsv / apps.md      app name, Icon= name, desktop file, Exec, WM class, package, Flatpak id
#   desktop/<file>.desktop  the launcher files themselves
#   icons/<name>.<ext>      each app's current icon (largest SVG/PNG found), as a design reference
#   system.txt              Omarchy version and counts (no personal data)
#
# Read-only: it only writes ~/iconrequest.zip. It never changes your theme or desktop.
set -euo pipefail

OUT="${OMAPIX_REQUEST_OUT:-$HOME/iconrequest.zip}"
REPO="Raiden-MeixElysia/OmaPixIcon"
command -v python3 >/dev/null || { echo "python3 is required (it ships with Omarchy)"; exit 1; }

python3 -I - "$OUT" "$REPO" <<'PY'
import glob, json, os, re, subprocess, sys, urllib.request, zipfile, datetime

out, repo = sys.argv[1], sys.argv[2]
home = os.path.expanduser('~')

# ---- 1. which icon names does OmaPix already cover?
covered = {os.path.basename(p)[:-4] for p in glob.glob(f'{home}/.local/share/icons/OmaPixIcon/scalable/*/*.svg')}
src = 'installed theme'
if not covered:
    local = f'{home}/.local/share/omapix/data/icons.json'
    try:
        if os.path.exists(local):
            data = json.load(open(local))
            src = 'installed data'
        else:
            print('OmaPixIcon is not installed; downloading the current icon list…')
            url = f'https://raw.githubusercontent.com/{repo}/main/data/icons.json'
            data = json.load(urllib.request.urlopen(url, timeout=120))
            src = 'latest repo data'
        covered = {n for v in data.values() for n in v['names']}
    except Exception as e:
        sys.exit(f'Could not load the OmaPix icon list: {e}')

# ---- 2. every visible launcher on this machine
dirs = [f'{home}/.local/share/applications', f'{home}/.local/share/flatpak/exports/share/applications',
        '/var/lib/flatpak/exports/share/applications', '/var/lib/snapd/desktop/applications']
dirs += [os.path.join(d, 'applications') for d in
         os.environ.get('XDG_DATA_DIRS', '/usr/local/share:/usr/share').split(':') if d]
seen, apps = set(), []
for d in dirs:
    for f in sorted(glob.glob(os.path.join(d, '*.desktop'))):
        base = os.path.basename(f)
        if base in seen:          # first match wins, like the launcher
            continue
        seen.add(base)
        e, sec = {}, None
        try:
            for line in open(f, encoding='utf-8', errors='ignore'):
                line = line.strip()
                if line.startswith('['):
                    sec = line; continue
                if sec == '[Desktop Entry]' and '=' in line:
                    k, v = line.split('=', 1); e.setdefault(k.strip(), v.strip())
        except OSError:
            continue
        if e.get('Type') != 'Application':
            continue
        if e.get('NoDisplay', '').lower() == 'true' or e.get('Hidden', '').lower() == 'true':
            continue
        apps.append((f, e))

def has_icon(f, e):
    icon = e.get('Icon', '')
    if icon and not icon.startswith('/'):
        return icon in covered or os.path.splitext(icon)[0] in covered
    stem = os.path.basename(f)[:-8]
    return stem in covered or stem.lower() in covered

missing = [(f, e) for f, e in apps if not has_icon(f, e)]

# ---- 3. locate each app's current icon as a reference
roots = [f'{home}/.local/share/icons', f'{home}/.icons', f'{home}/.local/share/flatpak/exports/share/icons',
         '/var/lib/flatpak/exports/share/icons', '/usr/share/icons', '/usr/local/share/icons']

def find_icon(name):
    if not name:
        return None
    if name.startswith('/'):
        return name if os.path.isfile(name) else None
    best, score = None, -1
    for r in roots:
        for pat in (f'{r}/*/*/*/{name}.svg', f'{r}/*/*/*/{name}.png', f'{r}/*/*/{name}.svg', f'{r}/*/*/{name}.png'):
            for p in glob.glob(pat):
                if '/OmaPixIcon/' in p or 'symbolic' in p:
                    continue
                m = re.search(r'/(\d+)x\d+', p)
                s = 10000 if p.endswith('.svg') else int(m[1]) if m else 1
                if s > score:
                    best, score = p, s
    if best is None:
        for ext in ('svg', 'png', 'xpm'):
            p = f'/usr/share/pixmaps/{name}.{ext}'
            if os.path.isfile(p):
                return p
    return best

def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:
        return ''

rows = []
for f, e in missing:
    pkg = ''
    if f.startswith('/usr/'):
        lines = run(['pacman', '-Qoq', f]).splitlines()
        pkg = lines[0] if lines else ''
    flatpak = os.path.basename(f)[:-8] if '/flatpak/' in f else ''
    rows.append(dict(name=e.get('Name', ''), icon=e.get('Icon', ''), desktop=os.path.basename(f),
                     path=f, exec=e.get('Exec', ''), wmclass=e.get('StartupWMClass', ''),
                     package=pkg, flatpak=flatpak, ref=find_icon(e.get('Icon', ''))))

if not rows:
    print(f'Every launcher app on this machine already has an OmaPix icon ({len(apps)} apps checked). Nothing to request.')
    sys.exit(0)

# ---- 4. write the zip
cols = ['name', 'icon', 'desktop', 'package', 'flatpak', 'wmclass', 'exec']
tsv = '\t'.join(cols) + '\n' + ''.join('\t'.join(r[c].replace('\t', ' ') for c in cols) + '\n' for r in rows)
md = ['| App | Icon= name | Desktop file | Package | Flatpak | WM class |', '|---|---|---|---|---|---|']
md += [f"| {r['name']} | `{r['icon'] or '(none)'}` | `{r['desktop']}` | {r['package']} | {r['flatpak']} | {r['wmclass']} |"
       for r in rows]
omarchy = run(['omarchy-version'])
if not omarchy and os.path.exists('/usr/share/omarchy/version'):
    omarchy = open('/usr/share/omarchy/version').read().strip()
system = (f"generated: {datetime.datetime.now().isoformat(timespec='seconds')}\n"
          f"omarchy: {omarchy or 'unknown'}\n"
          f"omapix installed: {os.path.isdir(home + '/.local/share/icons/OmaPixIcon')}\n"
          f"compared against: {src} ({len(covered)} icon names)\n"
          f"apps checked: {len(apps)}, missing: {len(rows)}\n")

with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('iconrequest/apps.tsv', tsv)
    z.writestr('iconrequest/apps.md', '\n'.join(md) + '\n')
    z.writestr('iconrequest/system.txt', system)
    for r in rows:
        try:
            z.write(r['path'], f"iconrequest/desktop/{r['desktop']}")
        except OSError:
            pass
        if r['ref']:
            ext = os.path.splitext(r['ref'])[1] or '.png'
            raw = r['icon'] if r['icon'] and not r['icon'].startswith('/') else r['desktop'][:-8]
            key = re.sub(r'[^\w.-]+', '_', raw)
            try:
                if os.path.getsize(r['ref']) < 5_000_000:
                    z.write(r['ref'], f'iconrequest/icons/{key}{ext}')
            except OSError:
                pass

print(f'{len(rows)} app(s) without an OmaPix icon:')
for r in rows:
    print(f"  - {r['name']}  (Icon={r['icon'] or 'none'})")
print(f'\nSaved {out}')
print(f'Open an issue and drag the zip into it:\n  https://github.com/{repo}/issues/new?template=icon-request.yml')
PY
