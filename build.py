#!/usr/bin/env python3
"""
Compile icon sources (icons/*.py) into palette-indexed pixel data.

  ./build.py                      # build everything -> data/icons.json
  ./build.py --sheet out.png      # + review contact sheet (needs ImageMagick)
  ./build.py --only icons/web.py  # build a single source file (for authoring)
  ./build.py --palette nord       # sheet in an Omarchy theme palette
"""
import argparse, importlib.util, json, os, glob, subprocess, sys, tempfile, traceback

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, 'engine'))
import pix  # noqa: E402
import render  # noqa: E402


def load(paths):
    for p in paths:
        spec = importlib.util.spec_from_file_location(os.path.basename(p)[:-3], p)
        mod = importlib.util.module_from_spec(spec)
        before = set(pix.REGISTRY)
        spec.loader.exec_module(mod)
        for k in set(pix.REGISTRY) - before:
            pix.REGISTRY[k]['src'] = os.path.relpath(p, ROOT)


def sheet(ids, data, pal, out, cols=12, scale=4):
    tmp = tempfile.mkdtemp()
    files = []
    for i in ids:
        f = os.path.join(tmp, f'{len(files):04d}.png')
        open(f, 'wb').write(render.render_png(data[i]['rows'], pal, 64 * scale // 2))
        files += ['-label', i, f]
    subprocess.run(['magick', 'montage', *files, '-tile', f'{cols}x', '-geometry', '+6+6',
                    '-background', '#3a3f4b', '-fill', '#e8e8e8', '-pointsize', '11', out], check=True)


def write_gallery_data(data):
    """Everything the web gallery needs, as one script (works from file:// too)."""
    themes = json.load(open(os.path.join(ROOT, 'data', 'omarchy-themes.json')))
    payload = dict(
        icons={k: dict(l=v['label'], c=v['cat'], n=v['names'], s=v['src'], r=v['rows']) for k, v in data.items()},
        themes={k: {kk: vv for kk, vv in t.items() if not kk.startswith(('hyprland', 'active'))}
                for k, t in themes.items()},
        house=render.HOUSE, shadow=list(render.SHADOW_RGBA), font5=pix.FONT5, font3=pix.FONT3,
    )
    with open(os.path.join(ROOT, 'docs', 'omapix-data.js'), 'w') as f:
        f.write('window.OMAPIX=' + json.dumps(payload, separators=(',', ':')) + ';\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', nargs='*')
    ap.add_argument('--sheet')
    ap.add_argument('--palette', default='house')
    ap.add_argument('--cols', type=int, default=12)
    ap.add_argument('--scale', type=int, default=4)
    ap.add_argument('--no-write', action='store_true')
    a = ap.parse_args()
    paths = a.only or sorted(glob.glob(os.path.join(ROOT, 'icons', '*.py')))
    load(paths)
    data, warns, names_seen = {}, 0, {}
    for iid, meta in pix.REGISTRY.items():
        try:
            c = pix.build_one(iid)
        except Exception:
            print(f'[ERROR] {iid} ({meta.get("src")})'); traceback.print_exc(); warns += 1
            continue
        for w in pix.check(c):
            print(f'[warn] {iid}: {w}'); warns += 1
        for n in meta['names']:
            if n in names_seen:
                print(f'[warn] name "{n}" used by {names_seen[n]} and {iid}'); warns += 1
            names_seen[n] = iid
        data[iid] = dict(label=meta['label'], cat=meta['cat'], names=meta['names'],
                         context='places' if meta['cat'] == 'places' else 'apps',
                         src=meta.get('src'), rows=pix.hires(c.rows()))
    print(f'{len(data)} icons, {len(names_seen)} names, {warns} warnings')
    if not a.no_write and not a.only:
        with open(os.path.join(ROOT, 'data', 'icons.json'), 'w') as f:
            json.dump(data, f, separators=(',', ':'))
        write_gallery_data(data)
    if a.sheet:
        sheet(list(data), data, render.resolve_palette(a.palette), a.sheet, a.cols, a.scale)
        print('sheet ->', a.sheet)


if __name__ == '__main__':
    main()
