"""Science, maths, astronomy, GIS and TeX."""
from pix import icon
import math


# ================================================================ helpers

def disc(c, col, r=13, cx=16, cy=16):
    c.circle(cx, cy, r, col)
    c.bevel([col])


def g(c, x, y, art, col='W'):
    c.sprite(x, y, art, {'#': col, '+': 'w'})


def ctext(c, s, col, cy=16, scale=2, font=5, cx=16):
    w = c.text_width(s, font, scale)
    h = (7 if font == 5 else 5) * scale
    c.text(int(round(cx - w / 2)), int(round(cy - h / 2)), s, col, font, scale)


def star(c, cx, cy, ro, ri, col, n=5, rot=-90):
    pts = []
    for i in range(n * 2):
        r = ro if i % 2 == 0 else ri
        a = math.radians(rot + i * 180 / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    c.poly(pts, col)


def calc_body(c, col, screen='c'):
    c.rrect(6, 3, 26, 28, col, 2)
    c.bevel([col])
    c.rect(9, 6, 23, 11, screen)
    for y in (14, 18, 22):
        for x in (9, 14, 19):
            c.rect(x, y, x + 3, y + 2, 'W')
    c.rect(19, 22, 22, 24, 'O')


def tex_page(c, col, glyph_fn):
    c.poly([(5, 3), (20, 3), (27, 10), (27, 29), (5, 29)], 'W')
    c.bevel(['W'])
    c.poly([(19, 3), (27, 11), (19, 11)], 'w')
    glyph_fn()


# ================================================================ maths

@icon('wolfram-alpha', ['wolframalpha', 'wolfram-alpha-webapp', 'wolframalpha.com'], 'science', 'Wolfram|Alpha')
def wolfram_alpha(c):
    disc(c, 'O')
    star(c, 16, 16.5, 10, 5, 'W', 8, -90)
    c.circle(16, 16.5, 2.5, 'O')
    c.outline()


@icon('wolfram-mathematica', ['mathematica', 'wolfram', 'wolfram-engine', 'com.wolfram.Mathematica',
                              'wolframnb'], 'science', 'Mathematica')
def mathematica(c):
    star(c, 16, 16, 13, 6.5, 'R', 7, -90)
    c.bevel(['R'])
    star(c, 16, 16, 6.5, 3.5, '1', 7, -90 + 180 / 7)
    c.outline()


@icon('matlab', ['MATLAB', 'com.mathworks.matlab', 'matlab-desktop', 'mathworks-matlab'], 'science', 'MATLAB')
def matlab(c):
    # the L-shaped membrane peak
    c.poly([(3, 19), (11, 13), (15, 15), (21, 3), (29, 24), (24, 28), (17, 20), (12, 23)], 'O')
    c.poly([(3, 19), (11, 13), (15, 15), (12, 23)], 'B')
    c.poly([(21, 3), (29, 24), (24, 28), (20, 16)], '2')
    c.bevel(['O', 'B'])
    c.outline()


@icon('org.octave.Octave', ['octave', 'gnu-octave', 'octave-gui'], 'science', 'GNU Octave')
def octave(c):
    disc(c, 'B')
    c.ring(16, 16, 9, 6.5, 'W')
    c.arc(16, 16, 13, 0, 300, 360, 'O')
    c.poly([(16, 16), (29, 8), (29, 16)], 'O')
    c.circle(16, 16, 9, 'B'); c.ring(16, 16, 9, 6.5, 'W')
    c.outline()


@icon('wxmaxima', ['io.github.wxmaxima_developers.wxMaxima', 'maxima', 'wxMaxima', 'xmaxima'], 'science',
      'wxMaxima')
def wxmaxima(c):
    c.rrect(3, 3, 28, 28, 'Y', 3)
    c.bevel(['Y'])
    g(c, 7, 8, """
        #......#.....##
        ##....##....##.
        #.#..#.#....#..
        #..##..#..#####
        #......#....#..
        #......#....#..
        #......#...##..
    """, 'k')
    c.rect(7, 19, 24, 20, 'R')
    c.rect(7, 23, 18, 24, '3')
    c.outline()


@icon('sagemath', ['sage', 'sage-notebook', 'org.sagemath.SageMath'], 'science', 'SageMath')
def sagemath(c):
    # sage leaf
    c.poly([(16, 3), (24, 9), (26, 18), (20, 26), (16, 29), (12, 26), (6, 18), (8, 9)], 'G')
    c.bevel(['G'])
    c.vline(16, 7, 27, '4')
    for y in (11, 16, 21):
        c.line(16, y + 3, 21, y, '4'); c.line(16, y + 3, 11, y, '4')
    c.outline()


@icon('scilab', ['org.scilab.Scilab', 'scilab-bin'], 'science', 'Scilab')
def scilab(c):
    c.circle(16, 16, 13, 'R')
    c.arc(16, 16, 13, 0, 0, 180, 'O')
    c.bevel(['R', 'O'])
    c.ring(16, 16, 7, 5, 'W')
    c.circle(16, 16, 2, 'W')
    c.outline()


@icon('geogebra', ['org.geogebra.GeoGebra', 'geogebra-classic', 'geogebra-6', 'geogebra-bin', 'geogebra-webapp'],
      'science', 'GeoGebra')
def geogebra(c):
    c.ellipse(16, 16, 11.5, 9.5, '.')
    c.ring(16, 16, 11, 9, 'M')
    for y in range(32):
        for x in range(32):
            dx, dy = (x + .5 - 16) / 11.5, (y + .5 - 16) / 9.5
            d = dx * dx + dy * dy
            if 0.68 < d <= 1.0:
                c.px(x, y, 'M')
            elif c.get(x, y) == 'M':
                c.px(x, y, '.')
    for (x, y) in ((5.5, 13), (12, 6.5), (23, 8), (26.5, 19), (14, 25.5)):
        c.circle(x, y, 3, 'W')
        c.ring(x, y, 3, 1.8, 'k')
    c.outline()


@icon('desmos', ['desmos-webapp', 'desmos.com'], 'science', 'Desmos')
def desmos(c):
    c.rrect(3, 3, 28, 28, 'G', 4)
    c.bevel(['G'])
    c.rect(6, 15, 25, 15, 'g'); c.rect(15, 6, 15, 25, 'g')
    pts = [(x, 15 - int(round(7 * math.sin((x - 6) / 19 * 2 * math.pi)))) for x in range(6, 26)]
    for (a, b), (cc, d) in zip(pts, pts[1:]):
        c.line(a, b, cc, d, 'W')
        c.line(a, b + 1, cc, d + 1, 'W')
    c.outline()


@icon('org.gnome.Genius', ['gnome-genius', 'genius'], 'science', 'Genius')
def genius(c):
    c.circle(16, 13, 10, 'Y')
    c.rect(11, 21, 21, 27, 'S')
    c.bevel(['Y', 'S'])
    c.hline(11, 21, 23, 's'); c.hline(11, 21, 25, 's')
    c.rect(13, 28, 19, 28, 's')
    c.line(13, 15, 16, 19, '3'); c.line(19, 15, 16, 19, '3')
    c.px(10, 8, 'W'); c.px(11, 7, 'W')
    c.outline()


@icon('kalker', ['io.github.paddim8.kalker', 'kalker-bin'], 'science', 'Kalker')
def kalker(c):
    c.rrect(3, 5, 28, 26, 'k', 2)
    c.bevel(['k'])
    g(c, 6, 9, """
        #.........
        .#........
        ..#.......
        .#........
        #.........
    """, 'G')
    ctext(c, 'FX', 'W', 19, 2, 3, 19)
    c.outline()


# ================================================================ astronomy / earth

@icon('org.stellarium.Stellarium', ['stellarium'], 'science', 'Stellarium')
def stellarium(c):
    c.circle(16, 16, 13, '6')
    for y in range(32):
        for x in range(32):
            if c.get(x, y) == '6' and y >= 21:
                c.px(x, y, 'G')
    c.bevel(['6', 'G'])
    star(c, 11, 10, 3, 1.3, 'Y', 5)
    c.pixels([(20, 7), (23, 12), (17, 15), (24, 17), (8, 17)], 'W')
    c.outline()


@icon('celestia', ['space.celestiaproject.celestia', 'celestia-qt', 'celestia-gtk'], 'science', 'Celestia')
def celestia(c):
    ring = set()
    for y in range(32):
        for x in range(32):
            dx, dy = x + .5 - 16, y + .5 - 16
            a = (dx / 13.5) ** 2 + (dy / 4) ** 2
            b = (dx / 10.5) ** 2 + (dy / 2.2) ** 2
            if a <= 1 and b > 1:
                ring.add((x, y))
    for x, y in ring:
        c.px(x, y, 'Y')
    c.circle(16, 16, 9.5, 'B')
    c.bevel(['B'])
    c.poly([(9, 13), (14, 9), (15, 14), (11, 17)], 'G')
    c.poly([(18, 18), (23, 13), (24, 19)], 'G')
    for x, y in ring:
        if y >= 16:
            c.px(x, y, 'Y')
    c.bevel(['Y'], light=False)
    c.outline()


@icon('org.kde.kstars', ['kstars'], 'science', 'KStars')
def kstars(c):
    # telescope on a tripod
    c.line(13, 17, 7, 27, 'S', 2); c.line(14, 17, 21, 27, 'S', 2); c.line(14, 17, 14, 27, 's', 1)
    c.poly([(3, 16), (20, 7), (23, 12), (6, 21)], 'w')
    c.poly([(19, 6), (25, 3), (27.5, 8), (22, 11)], 'B')
    c.bevel(['w', 'B'])
    c.outline()


@icon('org.kde.kalzium', ['kalzium'], 'science', 'Kalzium')
def kalzium(c):
    # periodic table tile + flask
    c.rrect(3, 3, 22, 22, 'B', 1)
    c.bevel(['B'])
    c.text(5, 5, 'H', 'W', 5, 1)
    c.text(14, 5, '1', 'b', 3, 1)
    c.rect(14, 15, 18, 26, 'w')
    c.poly([(13, 18), (19, 18), (28, 28), (6, 28)], 'w')
    c.poly([(11, 22), (21, 22), (27, 28), (7, 28)], 'G')
    c.bevel(['w', 'G'])
    c.outline()


@icon('org.qgis.qgis', ['qgis', 'qgis-ltr', 'qgis-git', 'qgis-bin'], 'science', 'QGIS')
def qgis(c):
    # the Q map-pin
    c.circle(15, 15, 12, 'G')
    c.poly([(19, 21), (23, 19), (29, 27), (25, 29)], 'G')
    c.bevel(['G'])
    c.circle(15, 15, 6.5, 'W')
    c.circle(15, 15, 3, 'Y')
    c.poly([(19, 21), (23, 19), (29, 27), (25, 29)], 'Y')
    c.bevel(['Y'])
    c.outline()


@icon('grass', ['org.osgeo.grass', 'grass-gis', 'grass78', 'grass82', 'grass84'], 'science', 'GRASS GIS')
def grass(c):
    c.ellipse(16, 25, 13, 4, 'N')
    for x0, top, col in ((5, 10, 'G'), (9, 4, 'g'), (14, 7, 'G'), (19, 3, 'g'), (24, 9, 'G')):
        c.poly([(x0, 26), (x0 + 3, top), (x0 + 5, 26)], col)
    c.bevel(['N', 'G'])
    c.outline()


@icon('josm', ['org.openstreetmap.josm', 'josm-latest', 'josm-snapshot'], 'science', 'JOSM')
def josm(c):
    c.rrect(3, 3, 28, 28, 'g', 3)
    c.bevel(['g'])
    c.line(6, 22, 12, 12, 'B', 2); c.line(12, 12, 20, 18, 'B', 2); c.line(20, 18, 25, 7, 'B', 2)
    for x, y in ((6, 22), (12, 12), (20, 18), (25, 7)):
        c.rect(x - 1, y - 1, x + 2, y + 2, 'W')
        c.frame(x - 1, y - 1, x + 2, y + 2, 'k')
    c.outline()


@icon('gramps', ['org.gramps_project.Gramps', 'gramps-git'], 'science', 'Gramps')
def gramps(c):
    # family tree
    c.rect(15, 7, 16, 22, 'N')
    c.line(16, 14, 8, 9, 'N', 2); c.line(15, 14, 23, 9, 'N', 2)
    c.circle(16, 9, 6, 'G')
    c.circle(8, 12, 5, 'G'); c.circle(24, 12, 5, 'G')
    c.circle(11, 18, 4, 'G'); c.circle(21, 18, 4, 'G')
    c.bevel(['G'])
    c.rect(14, 20, 17, 26, 'N')
    c.rect(9, 26, 22, 28, 'N')
    c.bevel(['N'])
    c.outline()


@icon('avogadro2', ['org.openchemistry.Avogadro2', 'avogadro'], 'science', 'Avogadro')
def avogadro(c):
    c.line(10, 20, 17, 13, 'S', 2); c.line(17, 13, 24, 18, 'S', 2); c.line(17, 13, 17, 5, 'S', 2)
    c.circle(16.5, 15, 6.5, 'R')
    c.circle(8, 22, 5, 'W'); c.circle(24.5, 21, 4.5, 'W'); c.circle(17, 6, 3.5, 'W')
    c.bevel(['R', 'W'])
    c.px(15, 11, 'r'); c.px(14, 12, 'r')
    c.outline()


@icon('pymol', ['org.pymol.PyMOL', 'pymol-open-source'], 'science', 'PyMOL')
def pymol(c):
    # protein ribbon helix
    for i in range(5):
        y = 5 + i * 5
        c.ellipse(16, y + 2, 11, 2.6, 'M' if i % 2 else 'C')
    c.bevel(['M', 'C'], light=False)
    c.line(5, 7, 27, 12, 'W')
    c.outline()


@icon('jmol', ['org.jmol.Jmol', 'jmol-bin'], 'science', 'Jmol')
def jmol(c):
    c.line(8, 8, 16, 16, 'S', 2); c.line(24, 8, 16, 16, 'S', 2); c.line(16, 16, 16, 25, 'S', 2)
    c.circle(16, 16, 6, 'B')
    c.circle(7, 7, 4, 'R'); c.circle(25, 7, 4, 'R'); c.circle(16, 25.5, 4, 'G')
    c.bevel(['B', 'R', 'G'], light=False)
    c.px(14, 13, 'W'); c.px(5, 5, 'W'); c.px(23, 5, 'W')
    c.outline()


@icon('org.kde.labplot2', ['labplot2', 'labplot', 'org.kde.labplot'], 'science', 'LabPlot')
def labplot(c):
    c.rect(3, 4, 28, 27, 'W')
    c.bevel(['W'])
    c.vline(6, 6, 24, 'k'); c.hline(6, 26, 24, 'k')
    for x, h, col in ((9, 7, 'B'), (13, 12, 'B'), (17, 9, 'B'), (21, 15, 'B')):
        c.rect(x, 24 - h, x + 2, 23, col)
    c.line(8, 18, 12, 12, 'R'); c.line(12, 12, 17, 15, 'R'); c.line(17, 15, 25, 7, 'R')
    c.outline()


# ================================================================ TeX / typesetting

@icon('texstudio', ['org.texstudio.TeXstudio', 'TeXstudio', 'texstudio-git'], 'science', 'TeXstudio')
def texstudio(c):
    c.rrect(3, 5, 28, 26, 'G', 3)
    c.bevel(['G'])
    g(c, 6, 10, """
        #####.........##.
        ..#.......##..#..
        ..#..###...##.#..
        ..#..#.....##....
        ..#..###..#..#...
        ..#..#....#..#...
        ..#..###..#...#..
    """)
    c.rect(19, 10, 23, 11, '.')
    c.outline()


@icon('texmaker', ['net.xm1math.Texmaker', 'Texmaker'], 'science', 'Texmaker')
def texmaker(c):
    tex_page(c, 'W', lambda: None)
    c.text(8, 12, 'TEX', 'R', 5, 1)
    c.rect(8, 20, 23, 20, 'S'); c.rect(8, 23, 19, 23, 'S')
    c.outline()


@icon('lyx', ['org.lyx.LyX', 'LyX'], 'science', 'LyX')
def lyx(c):
    c.rrect(3, 3, 28, 28, 'B', 3)
    c.bevel(['B'])
    g(c, 6, 9, """
        #.....#...#.#...#
        #......#.#...#.#.
        #.......#.....#..
        #.......#....#.#.
        #.......#...#...#
        #####...#........
    """)
    c.rect(6, 20, 25, 21, 'O')
    c.outline()


@icon('overleaf', ['overleaf-webapp', 'overleaf.com', 'overleaf-desktop'], 'science', 'Overleaf')
def overleaf(c):
    # the leaf
    c.ellipse(16, 16, 12, 12.5, 'G')
    c.ellipse(11, 11, 7, 7, '.')
    c.bevel(['G'])
    c.circle(12.5, 19.5, 4, 'W')
    c.circle(12.5, 19.5, 2.5, 'G')
    c.outline()


@icon('org.cvfosammmm.Setzer', ['setzer'], 'science', 'Setzer')
def setzer(c):
    # composing stick with sorts
    c.rrect(3, 19, 28, 27, 'N', 1)
    c.bevel(['N'])
    for i, x in enumerate((5, 10, 15, 20)):
        c.rect(x, 5 + (i % 2) * 3, x + 3, 18, 'S')
    c.bevel(['S'])
    for i, x in enumerate((5, 10, 15, 20)):
        c.rect(x + 1, 6 + (i % 2) * 3, x + 2, 8 + (i % 2) * 3, 'k')
    c.rect(25, 9, 27, 18, 'B'); c.bevel(['B'])
    c.outline()


@icon('gummi', ['gummi-git'], 'science', 'Gummi')
def gummi(c):
    c.ellipse(16, 17, 11, 11, 'R')
    c.circle(10, 7, 4, 'R'); c.circle(22, 7, 4, 'R')
    c.bevel(['R'])
    c.circle(12, 14, 1.5, 'K'); c.circle(20, 14, 1.5, 'K')
    c.arc(16, 18, 4, 2.5, 30, 150, '1')
    c.pixels([(8, 11), (9, 10)], 'r')
    c.outline()


@icon('typst', ['typst-webapp', 'typst.app', 'tinymist'], 'science', 'Typst')
def typst(c):
    c.rrect(3, 3, 28, 28, 'C', 5)
    c.bevel(['C'])
    g(c, 10, 6, """
        ...###...
        ...###...
        #########
        #########
        ...###...
        ...###...
        ...###...
        ...###...
        ...###...
        ...####.#
        ....#####
        .....###.
    """)
    c.shift(0, 1)
    c.outline()


# ================================================================ more science / teaching

@icon('gnuradio-grc', ['gnuradio-companion', 'gnuradio', 'org.gnuradio.grc', 'gnuradio-grc-bin'], 'science',
      'GNU Radio Companion')
def gnuradio(c):
    c.rrect(3, 5, 28, 26, 'k', 3)
    c.bevel(['k'])
    for x in range(5, 27):
        y = 15 + int(round(6 * math.sin((x - 5) / 21 * 4 * math.pi) * (1 - abs(x - 16) / 14)))
        c.rect(x, y, x, y + 1, 'G')
    c.hline(5, 26, 22, '4')
    c.outline()


@icon('fiji', ['sc.fiji.fiji', 'imagej', 'ImageJ', 'net.imagej.ImageJ', 'fiji-bin', 'imagej2'], 'science',
      'Fiji / ImageJ')
def fiji(c):
    cells = [(0, 0, 'C'), (1, 0, 'B'), (2, 0, 'M'), (0, 1, 'M'), (0, 2, 'Y'), (1, 2, 'G'), (0, 3, 'G'),
             (2, 2, 'B'), (2, 3, 'C')]
    for i, j, col in cells:
        c.rrect(4 + i * 8, 3 + j * 6, 10 + i * 8, 8 + j * 6, col, 1)
    c.bevel(['C', 'B', 'M', 'Y', 'G'], light=False)
    c.outline()


@icon('cloudcompare', ['org.cloudcompare.CloudCompare', 'CloudCompare', 'cloudcompare-bin'], 'science',
      'CloudCompare')
def cloudcompare(c):
    c.ellipse(16, 20, 13, 7.5, 'B')
    c.circle(13, 13, 8, 'B')
    c.circle(22, 16, 6, 'B')
    c.bevel(['B'])
    for (x, y) in ((9, 12), (13, 9), (17, 12), (21, 15), (12, 16), (16, 18), (24, 19), (8, 20), (20, 22), (12, 23),
                   (25, 23), (16, 25)):
        c.rect(x, y, x + 1, y + 1, 'Y')
    c.outline()


@icon('gaiasky', ['de.uni_heidelberg.zah.GaiaSky', 'gaia-sky', 'GaiaSky'], 'science', 'Gaia Sky')
def gaiasky(c):
    disc(c, 'k')
    for t in range(0, 360, 6):
        for arm in (0, 180):
            a = math.radians(t + arm)
            r = 1.5 + t / 360 * 10.5
            c.px(16 + r * math.cos(a), 16 + r * math.sin(a) * 0.8, 'M' if t > 120 else 'm')
    c.circle(16, 16, 2.5, 'y')
    c.outline()


@icon('openboard', ['ch.openboard.OpenBoard', 'OpenBoard', 'openboard-bin'], 'education', 'OpenBoard')
def openboard(c):
    c.rect(3, 4, 28, 23, 'N')
    c.rect(5, 6, 26, 21, '4')
    c.bevel(['N'])
    c.line(8, 17, 12, 10, 'W'); c.line(12, 10, 16, 17, 'W'); c.line(10, 14, 14, 14, 'W')
    c.text(18, 11, '+1', 'w', 3, 1)
    c.line(9, 24, 6, 28, 'N', 2); c.line(22, 24, 25, 28, 'N', 2)
    c.outline()


@icon('gpredict', ['net.oz9aec.Gpredict', 'gpredict-git'], 'science', 'Gpredict')
def gpredict(c):
    # satellite
    c.rect(4, 12, 10, 19, 'B'); c.rect(22, 12, 28, 19, 'B')
    c.hline(4, 10, 15, '6'); c.vline(7, 12, 19, '6'); c.hline(22, 28, 15, '6'); c.vline(25, 12, 19, '6')
    c.rect(10, 15, 22, 16, 'S')
    c.rrect(12, 10, 20, 21, 'w', 1)
    c.bevel(['w'])
    c.line(16, 9, 16, 4, 'S'); c.rect(15, 3, 17, 4, 'R')
    c.arc(16, 24, 5, 3.5, 30, 150, 'Y')
    c.outline()


@icon('klavaro', ['klavaro-git'], 'education', 'Klavaro')
def klavaro(c):
    c.rrect(3, 9, 28, 26, 'w', 2)
    c.bevel(['w'])
    for j, y in enumerate((12, 16)):
        for x in range(5 + j, 26, 4):
            c.rect(x, y, x + 2, y + 2, 'S')
    c.rect(9, 20, 22, 22, 'S')
    c.rrect(10, 3, 21, 11, 'O', 1)
    c.bevel(['O'])
    c.text(14, 4, 'K', 'W', 3, 1)
    c.outline()


@icon('tipp10', ['com.gitlab.tipp10.tipp10', 'TIPP10'], 'education', 'TIPP10')
def tipp10(c):
    c.rrect(3, 4, 28, 27, 'B', 3)
    c.bevel(['B'])
    ctext(c, '10', 'W', 13, 2, 3)
    for x in range(6, 26, 4):
        c.rect(x, 21, x + 2, 23, 'b')
    c.outline()
