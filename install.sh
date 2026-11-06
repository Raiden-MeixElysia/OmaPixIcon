#!/bin/bash
# OmaPixIcon — one-click installer for Omarchy
#
#   curl -fsSL https://raw.githubusercontent.com/Raiden-MeixElysia/OmaPixIcon/main/install.sh | bash
#
# Options (append after `bash -s --` when piping):
#   --palette sync     recolour icons to the active Omarchy theme, and again on every theme switch (default)
#   --palette house    the hand-tuned OmaPix vintage palette, always
#   --palette dmg      4-shade 1989 handheld green
#   --palette <theme>  freeze to any built-in Omarchy theme palette (nord, gruvbox, tokyo-night …)
#   --no-desktop-fix   don't add launcher overrides for apps that hard-code an icon file path
#   --uninstall        remove everything and restore your previous icon theme
set -euo pipefail

REPO="Raiden-MeixElysia/OmaPixIcon"
BRANCH="main"
SRC="$HOME/.local/share/omapix"
THEME_DIR="$HOME/.local/share/icons/OmaPixIcon"
STATE="$HOME/.local/state/omapix"
CONF="$HOME/.config/omapix/config"
HOOK="$HOME/.config/omarchy/hooks/theme-set.d/50-omapix-icons"
APPS="$HOME/.local/share/applications"
OMARCHY_THEME="$HOME/.local/state/omarchy/current/theme"

PALETTE="sync"
DESKTOP_FIX=1
ACTION="install"
while (($#)); do
  case $1 in
    --palette) PALETTE=${2:?--palette needs a value}; shift ;;
    --palette=*) PALETTE=${1#*=} ;;
    --no-desktop-fix) DESKTOP_FIX=0 ;;
    --uninstall) ACTION="uninstall" ;;
    -h|--help) sed -n '2,15p' "$0" 2>/dev/null || true; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
  shift
done

c_acc=$'\e[38;5;79m'; c_dim=$'\e[2m'; c_off=$'\e[0m'
say() { printf '%s▌%s %s\n' "$c_acc" "$c_off" "$*"; }
banner() {
  printf '%s' "$c_acc"
  cat <<'EOF'

   ▄▀▀▀▄ █▄ ▄█ ▄▀▀▀▄ █▀▀▀▄  ▀█▀  █   █   ▀█▀ ▄▀▀▀▄ ▄▀▀▀▄ █▄  █
   █   █ █ █ █ █▄▄▄█ █▄▄▄▀   █    ▀▄▀     █  █     █   █ █ ▀▄█
   █   █ █   █ █   █ █       █   ▄▀ ▀▄    █  █     █   █ █   █
    ▀▀▀  ▀   ▀ ▀   ▀ ▀      ▀▀▀  ▀   ▀   ▀▀▀  ▀▀▀   ▀▀▀  ▀   ▀
EOF
  printf '%s   hand-placed 32px pixel icons · palette-swapped to your Omarchy theme%s\n\n' "$c_dim" "$c_off"
}

set_icon_theme() { gsettings set org.gnome.desktop.interface icon-theme "$1" 2>/dev/null || true; }
restart_shell() { command -v omarchy-restart-shell >/dev/null && (omarchy-restart-shell >/dev/null 2>&1 &) || true; }

# ---------------------------------------------------------------- uninstall
if [[ $ACTION == uninstall ]]; then
  say "Removing OmaPixIcon"
  prev="Yaru-blue"
  [[ -f $OMARCHY_THEME/icons.theme ]] && prev=$(<"$OMARCHY_THEME/icons.theme")
  [[ -f $STATE/previous-icon-theme ]] && prev=$(<"$STATE/previous-icon-theme")
  rm -f "$HOOK"
  if [[ -d $APPS ]]; then
    grep -l '^X-OmaPix-Override=true' "$APPS"/*.desktop 2>/dev/null | while read -r f; do rm -f "$f"; done
  fi
  if [[ -d $STATE/desktop-backup ]]; then
    cp -f "$STATE"/desktop-backup/*.desktop "$APPS/" 2>/dev/null || true
  fi
  rm -rf "$THEME_DIR" "$SRC" "$STATE" "$(dirname "$CONF")"
  set_icon_theme "$prev"
  restart_shell
  update-desktop-database "$APPS" >/dev/null 2>&1 || true
  say "Restored icon theme: $prev"
  exit 0
fi

# ---------------------------------------------------------------- install
banner
command -v python3 >/dev/null || { echo "python3 is required (it ships with Omarchy)"; exit 1; }

# 1. sources: use this checkout if we're run from one, else fetch the repo
here="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || true)"
mkdir -p "$SRC"
if [[ -n $here && -f $here/data/icons.json && -f $here/engine/render.py ]]; then
  say "Using local checkout $here"
  [[ $here != "$SRC" ]] && rm -rf "$SRC" && mkdir -p "$SRC" && cp -r "$here/engine" "$here/data" "$SRC/"
else
  say "Downloading $REPO"
  tmp=$(mktemp -d)
  curl -fsSL "https://codeload.github.com/$REPO/tar.gz/refs/heads/$BRANCH" | tar -xz -C "$tmp"
  rm -rf "$SRC" && mkdir -p "$SRC"
  cp -r "$tmp"/*/engine "$tmp"/*/data "$SRC/"
  rm -rf "$tmp"
fi

# 2. remember what to restore
mkdir -p "$STATE" "$(dirname "$CONF")"
current=$(gsettings get org.gnome.desktop.interface icon-theme 2>/dev/null | tr -d "'" || true)
if [[ -n $current && $current != OmaPixIcon && ! -f $STATE/previous-icon-theme ]]; then
  echo "$current" >"$STATE/previous-icon-theme"
fi
printf 'PALETTE=%s\n' "$PALETTE" >"$CONF"

# 3. render the theme
inherit="Yaru-blue"
[[ -f $OMARCHY_THEME/icons.theme ]] && inherit=$(head -n1 "$OMARCHY_THEME/icons.theme")
args=(--palette house)
case $PALETTE in
  sync) [[ -f $OMARCHY_THEME/colors.toml ]] && args=(--colors "$OMARCHY_THEME/colors.toml") ;;
  *) args=(--palette "$PALETTE") ;;
esac
say "Rendering every icon as crisp SVG (palette: $PALETTE)"
new="$THEME_DIR.new"
rm -rf "$new"
python3 "$SRC/engine/render.py" --out "$new" --inherits "$inherit,Yaru,Adwaita,hicolor" "${args[@]}" | sed "s/^/  /"
rm -rf "$THEME_DIR" && mv "$new" "$THEME_DIR"
# No icon-theme.cache: GTK rejects caches for themes this large, and a stale
# cache would pin old colours. GTK and Qt read the SVG folder directly.
rm -f "$THEME_DIR/icon-theme.cache" "$THEME_DIR/.icon-theme.cache"

# 4. theme-switch hook: Omarchy resets the icon theme on every switch; put ours back
mkdir -p "$(dirname "$HOOK")"
cat >"$HOOK" <<'HOOK_EOF'
#!/bin/bash
# OmaPixIcon — re-apply (and in sync mode re-colour) pixel icons after an Omarchy theme switch.
# Installed by OmaPixIcon/install.sh. Remove with: install.sh --uninstall
SRC="$HOME/.local/share/omapix"
THEME_DIR="$HOME/.local/share/icons/OmaPixIcon"
OT="$HOME/.local/state/omarchy/current/theme"
[[ -f $SRC/engine/render.py ]] || exit 0
PALETTE=sync
[[ -f $HOME/.config/omapix/config ]] && source "$HOME/.config/omapix/config"
inherit="Yaru-blue"
[[ -f $OT/icons.theme ]] && inherit=$(head -n1 "$OT/icons.theme")
if [[ $PALETTE == sync && -f $OT/colors.toml ]]; then
  new="$THEME_DIR.new"; rm -rf "$new"
  python3 "$SRC/engine/render.py" --out "$new" --colors "$OT/colors.toml" --inherits "$inherit,Yaru,Adwaita,hicolor" >/dev/null &&
    rm -rf "$THEME_DIR" && mv "$new" "$THEME_DIR"
  rm -f "$THEME_DIR/icon-theme.cache" "$THEME_DIR/.icon-theme.cache"
  # Running GTK/Qt apps only reload icons when the theme *name* changes, and it is
  # still "OmaPixIcon". Flip to the fallback theme and back so they repaint now.
  gsettings set org.gnome.desktop.interface icon-theme "$inherit"
  sleep 0.3
  gsettings set org.gnome.desktop.interface icon-theme OmaPixIcon
  (omarchy-restart-shell >/dev/null 2>&1 &)
else
  sed -i "s/^Inherits=.*/Inherits=$inherit,Yaru,Adwaita,hicolor/" "$THEME_DIR/index.theme" 2>/dev/null
  gsettings set org.gnome.desktop.interface icon-theme OmaPixIcon
fi
HOOK_EOF
chmod +x "$HOOK"
say "Installed theme-switch hook ${c_dim}${HOOK/#$HOME/~}${c_off}"

# 5. apps that hard-code an icon *file path* can't be themed — give them a named icon
if ((DESKTOP_FIX)); then
  mkdir -p "$APPS" "$STATE/desktop-backup"
  names=$(python3 -c 'import json,sys;d=json.load(open(sys.argv[1]));print("\n".join(n for v in d.values() for n in v["names"]))' "$SRC/data/icons.json")
  fixed=0
  for f in /usr/share/applications/*.desktop "$APPS"/*.desktop; do
    [[ -f $f ]] || continue
    icon=$(grep -m1 '^Icon=' "$f" | cut -d= -f2-) || true
    [[ $icon == /* ]] || continue
    stem=$(basename "$f" .desktop)
    cand=""
    for n in "$stem" "${stem,,}" "$(basename "${icon%.*}")" "${stem%-desktop}"; do
      grep -qxF "$n" <<<"$names" && { cand=$n; break; }
    done
    [[ -n $cand ]] || continue
    target="$APPS/$(basename "$f")"
    if [[ $f == "$APPS"/* ]]; then
      cp -n "$f" "$STATE/desktop-backup/" 2>/dev/null || true
      sed -i "0,/^Icon=.*/s##Icon=$cand#" "$f"
    elif [[ ! -e $target ]]; then
      sed "0,/^Icon=.*/s##Icon=$cand#" "$f" >"$target"
      printf 'X-OmaPix-Override=true\n' >>"$target"
    else
      continue
    fi
    fixed=$((fixed + 1))
  done
  update-desktop-database "$APPS" >/dev/null 2>&1 || true
  ((fixed)) && say "Re-pointed $fixed launcher(s) that used hard-coded icon paths"
fi

# 6. activate
set_icon_theme OmaPixIcon
restart_shell
count=$(python3 -c 'import json,sys;d=json.load(open(sys.argv[1]));print(len(d), sum(len(v["names"]) for v in d.values()))' "$SRC/data/icons.json")
say "Done — ${count% *} pixel icons covering ${count#* } icon names are live."
printf '%s  switch palettes: curl …/install.sh | bash -s -- --palette house|sync|dmg|nord|…\n  uninstall:       curl …/install.sh | bash -s -- --uninstall%s\n' "$c_dim" "$c_off"
