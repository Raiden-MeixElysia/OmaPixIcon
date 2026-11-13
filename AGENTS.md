# OmaPixIcon

A pixel-art icon pack for Omarchy. This repo is its source of truth. It reaches users through the [OmaIcon](https://github.com/Raiden-MeixElysia/OmaIcon) bar plugin, which carries a pinned copy of `engine/render.py` and `data/`.

## Layout

- `icons/*.py`: icon sources. `build.py` compiles them into `data/icons.json` and the gallery data in `docs/`.
- `engine/pix.py`: the drawing toolkit the sources use.
- `engine/render.py`: renders `data/icons.json` into a freedesktop icon theme under a palette. OmaIcon calls it.
- `docs/`: the GitHub Pages gallery.
- `install.sh`: adds OmaIcon with `omarchy plugin add`, re-points launchers that hard-code an icon file path (backups in `~/.local/state/omapix/desktop-backup/`, overrides marked `X-OmaPix-Override=true`), then runs OmaIcon's `omaicon.py palette`. `--uninstall` undoes it.
- `tools/icon-request.sh`: collects the launchers the pack doesn't cover.

## Rules

- Never run `install.sh` on the maintainer's machine. It changes the live desktop.
- `STYLE.md` is the drawing standard; `build.py` enforces it.
- A change to `engine/render.py` or `data/` reaches users only after `tools/sync-pack.sh` in OmaIcon and a push there.
