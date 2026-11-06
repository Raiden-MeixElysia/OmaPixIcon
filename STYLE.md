# OmaPix style guide

OmaPix is a 16-bit-console pixel icon theme for Omarchy. Every icon is a 32×32
grid of hand-placed pixels drawn in **palette slots, not colours**, so the
whole set can be palette-swapped to any Omarchy theme (like SNES sprites).

## The rules (non-negotiable — `build.py` checks the first four)

1. **Grid**: 32×32. The silhouette's longer side is **26–28 px including the
   outline** (draw fills inside ~3..28, the outline adds 1px each side).
   Short side ≥ 14. `finalize()` centres the art automatically.
   Optical sizing: circles/irregular shapes 28, full squares/rectangles 26–27.
2. **Silhouette = the object.** No squircle tiles, no background plates. A
   browser is a globe, a mail client is an envelope, a game launcher is a
   controller. Irregular outlines are the point of this pack.
3. **One outline**: call `c.outline()` (ink `K`, 4-neighbour → stepped corners)
   as the last drawing step. Every opaque edge must be closed by ink.
   Never draw the drop shadow (`%`); `finalize()` adds it.
4. **≤ 12 slots per icon**, typically 5–8. Few colours, used deliberately.
5. **Light from top-left.** Use `c.bevel([...])` on big fills: highlight tone on
   top/left edges, shade tone on bottom/right. Add at most 1–3 specular pixels
   (`W` or the light tone). No noise, no random pixels.
6. **Readable at 32px.** One idea per icon. Tiny text only via the built-in
   pixel fonts (`c.text(..., font=3)` 3×5, `font=5` 5×7, `scale=2` chunky).
   Big single letters/glyphs are fine for brand marks.
7. **Brand colour mapping**: pick the nearest hue slot (YouTube → `R`, Spotify →
   `G`, Telegram → `C`/`b`, Firefox → `O`+`M`…). Omarchy's own apps may use
   accent `A` (follows the theme accent).
8. **No anti-aliasing, no 1px orphan noise, no jaggy "doubles"** on curves —
   prefer the engine's circle/ellipse/poly, then clean by hand with `px`.
9. Inner detail lines use the *dark tone of the fill* (e.g. `1` on `R`) or `k`,
   not ink — keep ink for the silhouette (and very strong inner separations).

## Palette slots

| hue | dark | base | light |
|---|---|---|---|
| red | `1` | `R` | `r` |
| orange | `2` | `O` | `o` |
| yellow | `3` | `Y` | `y` |
| green | `4` | `G` | `g` |
| cyan | `5` | `C` | `c` |
| blue | `6` | `B` | `b` |
| magenta | `7` | `M` | `m` |
| brown | `8` | `N` | `n` |
| pink | `9` | `P` | `p` |
| accent | `0` | `A` | `a` |

Neutrals, darkest → lightest: `K` ink · `k` · `s` · `S` · `w` · `W` paper.
`.` transparent.

## Authoring

```python
from pix import icon

@icon('firefox', ['org.mozilla.firefox', 'firefox-esr'], 'web', 'Firefox')
def firefox(c):          # c is a fresh 32x32 Canvas
    c.circle(16, 16, 12, 'M')
    ...
    c.outline()
```

* `id` = the primary icon name. The list = every other `Icon=` name the app
  uses: native package, Flatpak app-id, common aliases. Correct names matter
  more than anything — a beautiful icon under a wrong name is invisible.
* Primitives: `px rect frame hline vline rrect(r=0..6) ellipse circle ring arc
  line(w=) poly tri flood sprite(ascii, cmap) text dither replace mirror_x
  flip_x shift paste bevel shade_below outline`. See `engine/pix.py`.
* `sprite()` blits ASCII art — great for glyphs and hand-tuned details.
* Build and look: `./build.py --only icons/web.py --sheet /tmp/web.png`.
