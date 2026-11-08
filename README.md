<p align="center"><img src="docs/banner.png" alt="OmaPix Icon" width="100%"></p>

# OmaPix Icon

**[Open the live gallery →](https://raiden-meixelysia.github.io/OmaPixIcon/)** Browse all 1,910 icons, switch between 25 palettes and inspect each pixel.

<p align="center"><a href="https://raiden-meixelysia.github.io/OmaPixIcon/"><img src="docs/gallery.png" alt="The OmaPix gallery with CRT scanlines on" width="100%"></a></p>

## Request an icon

Missing a pixel icon for an app you use? Run this on your Omarchy machine:

```bash
curl -fsSL https://raw.githubusercontent.com/Raiden-MeixElysia/OmaPixIcon/main/tools/icon-request.sh | bash
```

It finds every app in your launcher that OmaPixIcon doesn't cover yet and saves `~/iconrequest.zip`. The zip contains each app's name, `Icon=` name, `.desktop` file, package or Flatpak id, and its current icon as a reference. It only reads your launchers and changes nothing on your system.

Then **[open an icon request →](https://github.com/Raiden-MeixElysia/OmaPixIcon/issues/new?template=icon-request.yml)** and drag `iconrequest.zip` into the form.

If you'd rather not run the script, open the request anyway and include:
- the app's name and where you got it (AUR, Flatpak, AppImage, web app)
- the `Icon=` line from its `.desktop` file (`grep ^Icon= ~/.local/share/applications/<app>.desktop /usr/share/applications/<app>.desktop`)
- a link to the official logo

A 16-bit pixel-art icon theme for [Omarchy](https://omarchy.org). Every icon is a
**64×64 high-resolution pixel sprite**, shipped as crisp SVG with an irregular silhouette (the object
itself, never a rounded-square tile), a single ink outline, top-left lighting and
a hard drop shadow, like a sprite from a 1993 cartridge.

Pixels are stored as **palette slots** (`R` red, `r` light red, `1` dark red, `K`
ink …) rather than RGB. The renderer maps those slots to a palette at install
time, so the set can be palette-swapped the way SNES sprites were. In **sync**
mode it re-colours itself to your Omarchy theme every time you switch themes.

<p align="center"><img src="docs/palettes.png" alt="One icon set, many Omarchy palettes" width="100%"></p>

**[Live gallery with palette switcher and pixel inspector →](https://raiden-meixelysia.github.io/OmaPixIcon/)**

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/Raiden-MeixElysia/OmaPixIcon/main/install.sh | bash
```

That's it. The installer:

1. renders the theme into `~/.local/share/icons/OmaPixIcon` as SVG, razor-sharp at any size and HiDPI scale
2. sets it as the GTK/Qt icon theme; the dock and launcher pick it up live, without restarting the Omarchy shell (if your shell version can't rescan icons, it falls back to a shell restart; set `RESTART_SHELL=always` or `never` in `~/.config/omapix/config` to override)
3. drops a hook in `~/.config/omarchy/hooks/theme-set.d/` so it survives (and follows) theme switches
4. re-points the few launchers that hard-code an icon *file path* to a themed icon name (reversible)

Python 3 is the only dependency, and Omarchy already ships it. No ImageMagick, Inkscape or PIL needed.

### Palettes

| option | what you get |
|---|---|
| `--palette sync` *(default)* | Re-coloured to the active Omarchy theme, and again on every switch |
| `--palette house` | The hand-tuned OmaPix vintage palette |
| `--palette dmg` | Four shades of 1989 handheld green |
| `--palette nord`, `gruvbox`, `tokyo-night`, … | Pinned to any of the 23 built-in Omarchy theme palettes |

```bash
curl -fsSL https://raw.githubusercontent.com/Raiden-MeixElysia/OmaPixIcon/main/install.sh | bash -s -- --palette house
curl -fsSL https://raw.githubusercontent.com/Raiden-MeixElysia/OmaPixIcon/main/install.sh | bash -s -- --uninstall
```

Uninstalling restores your previous icon theme and every launcher it touched.

## What's covered

Every application that ships with Omarchy 4.5 (Hype, Monologue, Gliff, Signed,
Omasnap, Omacut, Omawrite, Aether, the default web apps, LibreOffice …), plus
about 1,900 icons in total (7,300+ icon names): the most-used Linux apps across browsers, chat, dev tools,
terminals, media, graphics, games and system utilities, plus a pixel *places*
set (folders, home, trash, drives), Chinese apps (WeChat, QQ, Feishu/Lark, DingTalk, WPS, Bilibili, Kimi, Doubao, the deepin/UOS suite …), AI desktops (Claude, ChatGPT, DeepSeek, Cherry Studio, LM Studio, Ollama …), and the KDE, GNOME, XFCE and elementary catalogues. Anything not
covered falls back to your Omarchy Yaru variant.

<p align="center"><img src="docs/sheet.png" alt="Full icon sheet" width="100%"></p>

## How it's made

```
icons/*.py        icon sources: drawing code on a 32×32 canvas (primitives + ASCII sprites)
engine/pix.py     pixel engine: shapes, pixel fonts, auto-outline, bevel lighting, centring, checks
build.py          compiles sources → data/icons.json (palette-indexed pixels) + gallery data
engine/render.py  pure-stdlib PNG/SVG writer + palette mapping (house / dmg / any colors.toml)
install.sh        one-click installer + Omarchy theme-switch hook
STYLE.md          the rules every icon follows
```

`build.py` enforces the style mechanically: the silhouette's long side must be 26–28 px,
the outline must be closed, and an icon may use at most 12 palette slots. That's why the
whole set reads as one family at the same visual size.

### Add or tweak an icon

```python
# icons/mine.py
from pix import icon

@icon('my-app', ['com.example.MyApp'], 'dev', 'My App')
def my_app(c):
    c.circle(16, 16, 12, 'B')
    c.text(12, 12, 'M', 'W')
    c.bevel(['B'])
    c.outline()
```

```bash
./build.py --only icons/mine.py --sheet /tmp/mine.png   # preview
./build.py && ./install.sh                               # rebuild + reinstall locally
```

## License

[MIT](LICENSE), for both the code and the artwork. Brand icons are pixel reinterpretations of
trademarks that belong to their owners, included for identification in the
spirit of other freedesktop icon themes.
