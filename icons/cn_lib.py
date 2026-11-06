"""Shared drawing helpers for the cn_* icon files (Chinese & Asian software).
This module registers no icons itself."""
from pix import Canvas  # noqa: F401


def g(c, x, y, art, col, extra=None):
    """Blit an ASCII glyph: '#' -> col, other chars via extra map."""
    m = {'#': col}
    m.update(extra or {})
    c.sprite(x, y, art, m)


def gc(c, art, col, cx=16, cy=16, extra=None):
    """Blit a glyph centred on (cx, cy) (pixel-edge coords)."""
    lines = [l for l in art.strip('\n').split('\n')]
    ind = min((len(l) - len(l.lstrip())) for l in lines if l.strip())
    lines = [l[ind:].rstrip() for l in lines]
    w = max(len(l) for l in lines)
    h = len(lines)
    g(c, int(cx - w / 2), int(cy - h / 2), art, col, extra)


def disc(c, col, r=13, cx=16, cy=16):
    c.circle(cx, cy, r, col)
    c.bevel([col])


def bubble(c, col, x0=3, y0=4, x1=28, y1=23, tail='left', r=6):
    """Speech bubble with a tail at the bottom."""
    c.rrect(x0, y0, x1, y1, col, r)
    if tail == 'left':
        c.poly([(x0 + 4, y1 - 2), (x0 + 11, y1 - 1), (x0 + 3, y1 + 5)], col)
    elif tail == 'right':
        c.poly([(x1 - 10, y1 - 1), (x1 - 3, y1 - 2), (x1 - 2, y1 + 5)], col)
    elif tail == 'mid':
        c.poly([(13, y1), (20, y1), (16, y1 + 5)], col)


def round_bubble(c, col, cx=15, cy=15, rx=12.5, ry=11, tail='left'):
    c.ellipse(cx, cy, rx, ry, col)
    if tail == 'left':
        c.poly([(cx - rx * .55, cy + ry * .55), (cx - rx * .1, cy + ry * .85), (cx - rx * .8, cy + ry + 3.5)], col)
    else:
        c.poly([(cx + rx * .55, cy + ry * .55), (cx + rx * .1, cy + ry * .85), (cx + rx * .8, cy + ry + 3.5)], col)


def doc(c, col, fold='w', x0=6, y0=3, x1=26, y1=28, ear=6, paper=None):
    """Document page with a folded top-right corner."""
    c.rect(x0, y0, x1, y1, col)
    for i in range(ear):
        c.hline(x1 - ear + 1 + i, x1, y0 + i, '.')
    c.bevel([col])
    for i in range(ear):
        c.hline(x1 - ear + 1, x1 - ear + 1 + i, y0 + i, fold)
    c.hline(x1 - ear + 1, x1, y0 + ear, fold if paper is None else paper)


def cloud(c, col, dy=0):
    c.circle(10, 19 + dy, 6.5, col)
    c.circle(17, 13 + dy, 8.5, col)
    c.circle(23.5, 18 + dy, 6, col)
    c.rrect(4, 18 + dy, 28, 25 + dy, col, 3)


def tile(c, col, r=5, x0=3, y0=3, x1=28, y1=28):
    """Only for brand marks that genuinely are rounded squares."""
    c.rrect(x0, y0, x1, y1, col, r)
    c.bevel([col])


def shield(c, col, x0=5, x1=26, y0=3, y1=29):
    w = x1 - x0
    c.rect(x0, y0, x1, y0 + 14, col)
    c.poly([(x0, y0 + 14), (x1 + 1, y0 + 14), (x1 + 1 - w * .15, y0 + 20), (x0 + (w + 1) / 2, y1 + 1),
            (x0 + w * .15, y0 + 20)], col)
    c.bevel([col])


def hexagon(c, col, cx=16, cy=16, r=13):
    import math
    pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
    c.poly(pts, col)
    c.bevel([col])


def diamond(c, col, cx=16, cy=16, r=13.5):
    c.poly([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], col)
    c.bevel([col])


def play(c, x, y, h, col):
    """Right-pointing play triangle of height h (odd) at top-left x,y."""
    half = h // 2
    for j in range(h):
        w = half - abs(j - half)
        c.hline(x, x + w, y + j, col)


def note(c, x, y, col, h=12):
    """Eighth note: head at bottom-left."""
    c.vline(x + 4, y, y + h - 2, col)
    c.vline(x + 5, y, y + h - 2, col)
    c.line(x + 6, y, x + 9, y + 3, col, 2)
    c.ellipse(x + 3, y + h - 1, 3.2, 2.4, col)


def monitor(c, body='S', screen='k', x0=3, y0=4, x1=28, y1=22, stand=True):
    c.rrect(x0, y0, x1, y1, body, 2)
    c.bevel([body])
    c.rect(x0 + 2, y0 + 2, x1 - 2, y1 - 2, screen)
    if stand:
        c.rect(13, y1 + 1, 18, y1 + 3, body)
        c.rrect(8, y1 + 4, 23, y1 + 5, body, 1)
