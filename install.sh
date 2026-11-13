#!/bin/bash
# OmaPixIcon — one-click installer for Omarchy
#
#   curl -fsSL https://raw.githubusercontent.com/Raiden-MeixElysia/OmaPixIcon/main/install.sh | bash
#
# Installs the OmaIcon bar plugin, which ships this pack, and switches to OmaPixIcon.
# Options (append after `bash -s --` when piping):
#   --palette sync     recolour icons to the active Omarchy theme, and again on every theme switch (default)
#   --palette house    the hand-tuned OmaPix vintage palette, always
#   --palette dmg      4-shade 1989 handheld green
#   --palette <theme>  freeze to any built-in Omarchy theme palette (nord, gruvbox, tokyo-night …)
#   --no-desktop-fix   don't add launcher overrides for apps that hard-code an icon file path
#   --uninstall        remove everything and go back to Omarchy's icons
set -euo pipefail

PLUGIN_REPO="Raiden-MeixElysia/OmaIcon"
PLUGIN_ID="raiden-meixelysia.omaicon"
PLUGIN="$HOME/.config/omarchy/plugins/$PLUGIN_ID"
STATE="$HOME/.local/state/omapix"
APPS="$HOME/.local/share/applications"

PALETTE="sync"
DESKTOP_FIX=1
ACTION="install"
while (($#)); do
  case $1 in
    --palette) PALETTE=${2:?--palette needs a value}; shift ;;
    --palette=*) PALETTE=${1#*=} ;;
    --no-desktop-fix) DESKTOP_FIX=0 ;;
    --uninstall) ACTION="uninstall" ;;
    -h|--help) sed -n '2,13p' "$0" 2>/dev/null || true; exit 0 ;;
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

omaicon() { python3 -B "$PLUGIN/engine/omaicon.py" "$@"; }

# ---------------------------------------------------------------- uninstall
if [[ $ACTION == uninstall ]]; then
  say "Removing OmaPixIcon"
  [[ -f $PLUGIN/engine/omaicon.py ]] && omaicon remove
  if [[ -d $APPS ]]; then
    grep -l '^X-OmaPix-Override=true' "$APPS"/*.desktop 2>/dev/null | while read -r f; do rm -f "$f"; done
  fi
  if [[ -d $STATE/desktop-backup ]]; then
    cp -f "$STATE"/desktop-backup/*.desktop "$APPS/" 2>/dev/null || true
  fi
  rm -rf "$STATE"
  [[ -d $PLUGIN ]] && omarchy-plugin-remove "$PLUGIN_ID" --yes
  update-desktop-database "$APPS" >/dev/null 2>&1 || true
  say "Back to Omarchy's icons"
  exit 0
fi

# ---------------------------------------------------------------- install
banner
command -v python3 >/dev/null || { echo "python3 is required (it ships with Omarchy)"; exit 1; }
command -v omarchy-plugin-add >/dev/null || { echo "needs the Omarchy 4 shell plugin system"; exit 1; }

# 1. the OmaIcon plugin: it ships the pack and the engine
if [[ -d $PLUGIN/.git ]]; then
  omarchy-plugin-update "$PLUGIN_ID" --yes
else
  rm -rf "$PLUGIN"
  omarchy-plugin-add "https://github.com/$PLUGIN_REPO.git" --enable --yes
fi
# Installs before 2026-11 kept the engine, config and hook under the pack's name
[[ -d $HOME/.config/omapix && ! -d $HOME/.config/omaicon ]] && mv "$HOME/.config/omapix" "$HOME/.config/omaicon"
rm -rf "$HOME/.local/share/omapix" "$HOME/.config/omapix" "$HOME/.config/omarchy/hooks/theme-set.d/50-omapix-icons"
say "Added the Icons panel to the bar ${c_dim}${PLUGIN/#$HOME/~}${c_off}"

# 2. apps that hard-code an icon *file path* can't be themed — give them a named icon
if ((DESKTOP_FIX)); then
  mkdir -p "$APPS" "$STATE/desktop-backup"
  names=$(python3 -c 'import json,sys;d=json.load(open(sys.argv[1]));print("\n".join(n for v in d.values() for n in v["names"]))' "$PLUGIN/pack/data/icons.json")
  fixed=0
  for f in /usr/share/applications/*.desktop "$APPS"/*.desktop; do
    [[ -f $f ]] || continue
    icon=$(grep -m1 '^Icon=' "$f" | cut -d= -f2-) || true
    [[ $icon == /* ]] || continue
    stem=$(basename "$f" .desktop)
    cand=""
    # Per-install launchers (e.g. com.xd.cindy.user.h69297e92b23bcb60) carry a hash suffix
    unhashed=$stem
    [[ $stem =~ ^(.+)\.h[0-9a-f]{12,}$ ]] && unhashed=${BASH_REMATCH[1]}
    for n in "$stem" "${stem,,}" "$unhashed" "$(basename "${icon%.*}")" "${stem%-desktop}"; do
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

# 3. render and switch
say "Rendering every icon as crisp SVG (palette: $PALETTE)"
omaicon palette "$PALETTE"
count=$(python3 -c 'import json,sys;d=json.load(open(sys.argv[1]));print(len(d), sum(len(v["names"]) for v in d.values()))' "$PLUGIN/pack/data/icons.json")
say "Done — ${count% *} pixel icons covering ${count#* } icon names are live."
printf '%s  switch icons:  click the grid icon in the bar\n  uninstall:     curl …/install.sh | bash -s -- --uninstall%s\n' "$c_dim" "$c_off"
