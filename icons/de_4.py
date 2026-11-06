"""GNOME core apps, GNOME developer/design tools and GNOME Games.
GNOME games share a family motif: the object sits on a soft grey table slab."""
from pix import icon
import math

LT = {'R': 'r', 'O': 'o', 'Y': 'y', 'G': 'g', 'C': 'c', 'B': 'b', 'M': 'm', 'N': 'n', 'P': 'p', 'W': 'W', 'k': 's'}


def play(c, x, y, h, col):
    m = h // 2
    for j in range(h):
        c.hline(x, x + (m - abs(j - m)), y + j, col)


def page(c, x0, y0, x1, y1, col='W', fold=5, fcol='w'):
    c.rect(x0, y0, x1, y1, col)
    for i in range(fold):
        c.hline(x1 - fold + 1 + i, x1, y0 + i, '.')
    for i in range(fold):
        c.hline(x1 - fold + 1, x1 - fold + 1 + i, y0 + i, fcol)


def slab(c, y=24, x0=3, x1=28):
    """GNOME-games table slab under the object."""
    c.rrect(x0, y, x1, y + 4, 'S', 2)
    c.hline(x0 + 2, x1 - 2, y, 'w')
    c.hline(x0 + 2, x1 - 2, y + 4, 's')


# ================================================================== core
@icon('org.gnome.Yelp', ['yelp', 'gnome-help', 'help-faq'], 'system', 'Help')
def yelp(c):
    # lifebuoy
    for i in range(4):
        c.arc(16, 16, 12.5, 6.5, i * 90 + 45 - 20, i * 90 + 45 + 20, 'W')
        c.arc(16, 16, 12.5, 6.5, i * 90 - 25, i * 90 + 25, 'R')
    c.bevel(['R', 'W'])
    c.outline()


@icon('org.gnome.Tour', ['gnome-tour'], 'system', 'Tour')
def tour(c):
    # hot-air balloon
    c.ellipse(16, 12, 11, 9.5, 'B')
    c.poly([(6, 15), (26, 15), (19, 22), (13, 22)], 'B')
    c.ellipse(16, 12, 4.5, 9.5, 'b')
    c.rect(15, 2, 16, 22, 'B') if False else None
    c.bevel(['B'])
    c.vline(13, 22, 23, 'N'); c.vline(18, 22, 23, 'N')
    c.rrect(12, 24, 19, 27, 'N', 1)
    c.hline(12, 19, 24, 'n')
    c.outline()


@icon('org.gnome.SimpleScan', ['simple-scan', 'org.gnome.DocumentScanner', 'document-scanner', 'scanner'],
      'utilities', 'Document Scanner')
def simplescan(c):
    c.rrect(3, 14, 28, 26, 'S', 2)
    c.bevel(['S'])
    page(c, 8, 3, 23, 17, 'W', 4)
    for y in (8, 11):
        c.hline(10, 20, y, 'S')
    c.rect(3, 17, 28, 18, 's')
    c.hline(5, 26, 21, 'C')
    c.px(25, 24, 'G')
    c.outline()


@icon('org.gnome.Photos', ['gnome-photos'], 'media', 'Photos')
def photos(c):
    c.rrect(3, 5, 28, 26, 'S', 2)
    c.bevel(['S'])
    c.rect(5, 7, 26, 24, 'O')
    c.rect(5, 7, 26, 15, 'o')
    c.circle(20, 12, 2.5, 'Y')
    c.poly([(5, 24.5), (5, 20), (12, 14), (18, 20), (21, 18), (26.5, 22), (26.5, 24.5)], '8')
    c.outline()


@icon('org.gnome.Notes', ['bijiben', 'gnome-notes'], 'office', 'Notes')
def gnome_notes(c):
    c.rect(4, 3, 24, 28, 'W')
    c.bevel(['W'])
    c.rect(4, 3, 24, 6, 'Y')
    for y in (10, 14, 18, 22):
        c.hline(7, 21, y, 'w')
    c.line(17, 26, 27, 16, 'O', 3)
    c.px(16, 28, 'k'); c.px(17, 28, 'n'); c.px(16, 27, 'n')
    c.outline()


@icon('org.gnome.Usage', ['gnome-usage'], 'system', 'Usage')
def usage(c):
    c.circle(16, 17, 12.5, 'S')
    c.arc(16, 17, 12.5, 0, 0, 180, '.')
    c.rect(3, 17, 28, 23, 'S')
    c.bevel(['S'])
    c.arc(16, 17, 10, 6, 180, 240, 'G')
    c.arc(16, 17, 10, 6, 240, 300, 'Y')
    c.arc(16, 17, 10, 6, 300, 360, 'R')
    c.line(16, 17, 21, 9, 'k')
    c.circle(16, 17, 2, 'k')
    c.outline()


@icon('org.gnome.Firmware', ['gnome-firmware'], 'system', 'Firmware')
def firmware(c):
    c.rect(8, 8, 23, 23, 'k')
    for i in range(4):
        x = 9 + i * 4
        for y0, y1 in [(4, 7), (24, 27)]:
            c.rect(x, y0, x + 1, y1, 'S')
        for x0, x1 in [(4, 7), (24, 27)]:
            c.rect(x0, 9 + i * 4, x1, 10 + i * 4, 'S')
    c.rect(11, 11, 20, 20, 'G')
    c.bevel(['G'])
    c.sprite(13, 13, """
        ..##..
        .####.
        ######
        ..##..
        ..##..
        ..##..
    """, {'#': 'W'})
    c.outline()


@icon('org.gnome.Calls', ['gnome-calls'], 'web', 'Calls')
def calls(c):
    c.sprite(3, 2, """
        .#####.................
        #######................
        #######................
        #######................
        ########...............
        ########...............
        ########...............
        .######................
        ..#####................
        ..#####................
        ...####................
        ....####...............
        .....####..............
        ......#####............
        .......######...#####..
        ........#############..
        ..........############.
        ............##########.
        ..............#########
        .................######
        ...................###.
        ....................##.
        ...................###.
        ..............########.
    """, {'#': 'G'})
    c.bevel(['G'])
    c.arc(10, 20, 17, 15, 290, 320, 'G') if False else None
    c.outline()


@icon('org.gnome.Dictionary', ['gnome-dictionary', 'accessories-dictionary'], 'office', 'Dictionary')
def dictionary(c):
    c.rrect(5, 3, 26, 28, 'R', 1)
    c.bevel(['R'])
    c.rect(5, 25, 26, 28, 'W'); c.hline(5, 26, 25, 'w')
    c.text(12, 8, 'A', 'Y')
    c.text(11, 16, 'Z', 'y', font=3) if False else c.rect(10, 17, 21, 18, '1')
    c.outline()


@icon('org.gnome.Crosswords', ['crosswords', 'gnome-crosswords'], 'games', 'Crosswords')
def crosswords(c):
    c.rect(3, 3, 28, 28, 'W')
    for i in range(6):
        c.vline(3 + i * 5, 3, 28, 'S'); c.hline(3, 28, 3 + i * 5, 'S')
    for x, y in [(1, 0), (3, 1), (0, 3), (2, 2), (4, 4), (2, 4)]:
        c.rect(4 + x * 5, 4 + y * 5, 7 + x * 5, 7 + y * 5, 'k')
    c.text(5, 5, 'A', 'B', font=3)
    c.text(15, 15, 'Z', 'B', font=3) if False else c.text(15, 5, 'B', 'B', font=3)
    c.outline()


# ================================================================== GNOME design tools


@icon('org.gnome.design.IconLibrary', ['icon-library'], 'dev', 'Icon Library')
def iconlibrary(c):
    c.rrect(3, 3, 28, 28, 'W', 2)
    c.bevel(['W'])
    c.circle(10, 10, 4, 'R')
    c.rect(17, 6, 24, 13, 'B')
    c.poly([(10, 17), (14, 25), (6, 25)], 'G')
    c.sprite(17, 17, """
        ..##..
        .####.
        ######
        ######
        .####.
        ..##..
    """, {'#': 'Y'})
    c.outline()


@icon('org.gnome.design.AppIconPreview', ['app-icon-preview'], 'dev', 'App Icon Preview')
def appiconpreview(c):
    c.rrect(3, 3, 28, 28, 'C', 6)
    c.bevel(['C'])
    c.rrect(9, 9, 22, 22, 'W', 3)
    c.rrect(12, 12, 19, 19, 'B', 1)
    c.outline()


@icon('org.gnome.design.Contrast', ['contrast'], 'dev', 'Contrast')
def contrast(c):
    c.circle(16, 16, 12.5, 'W')
    c.arc(16, 16, 12.5, 0, 90, 270, 'k')
    c.text(9, 13, 'A', 'W', font=3) if False else None
    c.text(7, 12, 'A', 'W'); c.text(19, 12, 'A', 'k')
    c.outline()


@icon('org.gnome.design.Typography', ['typography'], 'dev', 'Typography')
def typography(c):
    c.sprite(4, 4, """
        ......####......
        ......####......
        .....######.....
        .....##.###.....
        ....###..###....
        ....##...###....
        ...###....###...
        ...##.....###...
        ..############..
        ..############..
        .###.......###..
        .##.........###.
        ###.........###.
        ##...........###
    """, {'#': 'k'})
    c.rect(3, 21, 28, 23, 'R')
    c.outline()


@icon('org.gnome.design.Lorem', ['lorem'], 'dev', 'Lorem')
def lorem(c):
    page(c, 5, 3, 26, 28, 'W', 6)
    c.bevel(['W'])
    c.text(8, 6, 'L', 'B', scale=1)
    for y, x1 in [(15, 23), (18, 21), (21, 23), (24, 16)]:
        c.hline(8, x1, y, 'S')
    c.outline()


@icon('org.gnome.design.Emblem', ['emblem'], 'dev', 'Emblem')
def emblem(c):
    c.poly([(16, 3), (28, 8), (26, 21), (16, 29), (6, 21), (4, 8)], 'M')
    c.bevel(['M'])
    c.circle(16, 15, 5, 'W')
    c.circle(16, 15, 2.5, 'Y')
    c.outline()


# ================================================================== GNOME World


@icon('org.gnome.World.Secrets', ['secrets', 'gnome-passwordsafe', 'org.gnome.PasswordSafe'], 'system', 'Secrets')
def secrets(c):
    c.arc(16, 12, 8.5, 5, 180, 360, 'S')
    c.rect(7, 12, 9, 14, 'S'); c.rect(23, 12, 25, 14, 'S')
    c.rrect(4, 14, 27, 28, 'k', 2)
    c.bevel(['S'])
    for x in (8, 13, 18, 23):
        c.rect(x, 20, x + 1, 21, 'W')
    c.outline()


@icon('org.gnome.World.Iotas', ['iotas'], 'office', 'Iotas')
def iotas(c):
    c.rrect(5, 3, 26, 28, 'W', 2)
    c.bevel(['W'])
    c.rect(9, 7, 11, 23, 'B')
    c.rect(9, 7, 9, 23, 'b')
    for y in (8, 13, 18, 23):
        c.hline(14, 23, y, 'S')
    c.outline()


@icon('org.gnome.World.Citations', ['citations'], 'office', 'Citations')
def citations(c):
    c.rrect(3, 5, 28, 26, 'Y', 3)
    c.bevel(['Y'])
    c.sprite(7, 9, """
        .###....###..
        ####...####..
        ####...####..
        .###....###..
        ..##.....##..
        .##.....##...
        ##.....##....
    """, {'#': '3'})
    c.outline()


@icon('org.gnome.Gtranslator', ['gtranslator'], 'dev', 'Translation Editor')
def gtranslator(c):
    c.rrect(3, 3, 21, 19, 'B', 2)
    c.rrect(11, 11, 28, 28, 'Y', 2)
    c.bevel(['B', 'Y'])
    c.text(8, 6, 'A', 'W')
    c.sprite(15, 15, """
        ..##.....
        #######..
        ..#..#...
        .#...#...
        #...##...
        ....#....
        ...#.....
    """, {'#': 'k'})
    c.outline()


@icon('org.gnome.Recipes', ['gnome-recipes'], 'office', 'Recipes')
def recipes(c):
    c.ellipse(16, 8, 9, 5.5, 'W')
    c.circle(9, 10, 4, 'W'); c.circle(23, 10, 4, 'W')
    c.rect(9, 10, 22, 22, 'W')
    c.bevel(['W'])
    c.rect(9, 18, 22, 22, 'w')
    c.rect(6, 23, 25, 27, 'O')
    c.bevel(['O'])
    c.outline()


# ================================================================== GNOME Games (table slab family)
@icon('org.gnome.Chess', ['gnome-chess'], 'games', 'Chess')
def gchess(c):
    slab(c)
    c.sprite(9, 3, """
        ....####....
        ...######...
        ...######...
        ....####....
        ..########..
        ....####....
        ....####....
        ....####....
        ...######...
        ...######...
        ..########..
        .##########.
        .##########.
        ############
        ############
    """, {'#': 'k'})
    c.vline(13, 4, 20, 's') if False else c.vline(13, 7, 15, 's')
    c.rect(4, 22, 27, 23, 'W') if False else None
    c.outline()


@icon('org.gnome.Mines', ['gnome-mines'], 'games', 'Mines')
def gmines(c):
    slab(c)
    for a in range(0, 360, 45):
        r = math.radians(a)
        c.line(16, 13, 16 + 9.5 * math.cos(r), 13 + 9.5 * math.sin(r), 'k')
    c.circle(16, 13, 7.5, 'k')
    c.circle(13.5, 10.5, 2, 's')
    c.px(12, 9, 'W')
    c.outline()


@icon('org.gnome.Sudoku', ['gnome-sudoku'], 'games', 'Sudoku')
def gsudoku(c):
    c.rect(3, 3, 28, 28, 'W')
    for i in range(1, 9):
        x = 3 + round(i * 25 / 9)
        c.vline(x, 3, 28, 'w'); c.hline(3, 28, x, 'w')
    for x in (11, 20):
        c.rect(x, 3, x, 28, 'k'); c.rect(3, x, 28, x, 'k')
    c.text(5, 4, '5', 'B'); c.text(14, 13, '3', 'B'); c.text(22, 22, '9', 'R')
    c.text(22, 4, '1', 'S'); c.text(5, 21, '7', 'S')
    c.outline()


@icon('org.gnome.Mahjongg', ['gnome-mahjongg'], 'games', 'Mahjongg')
def gmahjongg(c):
    slab(c)
    for x0, y0 in [(4, 9), (16, 9), (10, 3)]:
        c.rect(x0 + 1, y0 + 1, x0 + 11, y0 + 15, 'Y')
        c.rect(x0, y0, x0 + 10, y0 + 14, 'W')
    c.circle(15.5, 7, 2, 'R'); c.circle(15.5, 12, 2, 'G')
    c.px(8, 15, 'B'); c.px(8, 19, 'B'); c.px(23, 16, 'R'); c.px(23, 19, 'R')
    c.outline()


@icon('org.gnome.Quadrapassel', ['quadrapassel'], 'games', 'Quadrapassel')
def quadrapassel(c):
    def blk(x, y, col):
        c.rect(x, y, x + 5, y + 5, col)
        c.hline(x, x + 5, y, LT[col]); c.vline(x, y, y + 5, LT[col])
    for x, y, col in [(10, 3, 'M'), (10, 9, 'M'), (16, 9, 'M'), (10, 15, 'M'),
                      (4, 21, 'B'), (10, 21, 'O'), (16, 21, 'O'), (22, 21, 'G'), (22, 15, 'G')]:
        blk(x, y, col)
    c.outline()


@icon('org.gnome.TwentyFortyEight', ['gnome-2048'], 'games', 'GNOME 2048')
def g2048(c):
    c.rrect(3, 3, 28, 28, 'n', 2)
    for j in range(2):
        for i in range(2):
            col = [['Y', 'O'], ['w', 'R']][j][i]
            c.rrect(5 + i * 12, 5 + j * 12, 14 + i * 12, 14 + j * 12, col, 1)
    c.text(8, 7, '2', 'k', font=5) if False else c.text(8, 8, '2', 'k', font=3) if False else None
    c.text(8, 7, '2', 'W'); c.text(20, 7, '4', 'W'); c.text(8, 19, '8', 'k'); c.text(20, 19, '8', 'W')
    c.outline()


@icon('org.gnome.Aisleriot', ['sol', 'aisleriot', 'gnome-aisleriot'], 'games', 'AisleRiot Solitaire')
def aisleriot(c):
    c.poly([(3, 9), (13, 3.5), (21, 18), (11, 24)], 'W')
    c.rrect(12, 6, 26, 26, 'W', 1)
    c.bevel(['W'])
    c.sprite(16, 12, """
        .#.#.
        #####
        #####
        .###.
        ..#..
    """, {'#': 'R'})
    c.text(14, 8, 'A', 'R', font=3) if False else None
    c.rect(14, 8, 15, 9, 'R')
    c.poly([(7, 9), (9, 8), (10, 10), (8, 11)], 'k')
    c.outline()


@icon('org.gnome.Tali', ['tali'], 'games', 'Tali')
def tali(c):
    slab(c)
    c.rrect(3, 9, 15, 21, 'W', 2)
    c.rrect(15, 4, 28, 17, 'R', 2)
    c.bevel(['W', 'R'])
    for x, y in [(6, 12), (9, 15), (12, 18)]:
        c.rect(x - 1, y - 1, x, y, 'k')
    for x, y in [(18, 7), (24, 7), (18, 13), (24, 13)]:
        c.rect(x, y, x + 1, y + 1, 'W')
    c.outline()


@icon('org.gnome.Robots', ['gnome-robots'], 'games', 'Robots')
def grobots(c):
    slab(c, 24)
    c.vline(16, 5, 6, 's'); c.circle(16, 4.5, 1.5, 'R')
    c.rrect(7, 7, 24, 17, 'S', 2)
    c.bevel(['S'])
    c.rect(10, 9, 13, 12, 'C'); c.rect(18, 9, 21, 12, 'C')
    c.hline(11, 20, 15, 'k')
    c.rect(10, 18, 21, 23, 's')
    c.outline()


@icon('org.gnome.Nibbles', ['gnome-nibbles'], 'games', 'Nibbles')
def gnibbles(c):
    c.rect(3, 22, 21, 27, 'G')
    c.rect(16, 10, 21, 27, 'G')
    c.rect(16, 10, 28, 15, 'G')
    c.bevel(['G'])
    c.rect(24, 11, 25, 12, 'k')
    c.circle(7, 9, 4, 'R'); c.px(7, 4, 'G'); c.px(8, 3, 'G')
    c.outline()


@icon('org.gnome.Klotski', ['gnome-klotski'], 'games', 'Klotski')
def gklotski(c):
    c.rect(3, 3, 28, 28, 'n')
    for x0, y0, x1, y1, col in [(5, 5, 9, 14, 'B'), (11, 5, 20, 14, 'R'), (22, 5, 26, 14, 'B'),
                                (5, 16, 9, 26, 'Y'), (11, 16, 15, 20, 'G'), (16, 16, 20, 20, 'G'),
                                (22, 16, 26, 26, 'Y')]:
        c.rect(x0, y0, x1, y1, col)
        c.hline(x0, x1, y0, LT[col])
    c.outline()


@icon('org.gnome.Reversi', ['iagno', 'org.gnome.Iagno', 'gnome-reversi'], 'games', 'Reversi')
def greversi(c):
    slab(c)
    c.ellipse(16, 17, 11, 5.5, 'W')
    c.ellipse(16, 14, 11, 5.5, 'k')
    c.ellipse(13, 12, 5, 2, 's')
    c.outline()


@icon('org.gnome.Tetravex', ['gnome-tetravex'], 'games', 'Tetravex')
def tetravex(c):
    def sq(x, y, t, r, b, l):
        c.poly([(x, y), (x + 12, y), (x + 6, y + 6)], t)
        c.poly([(x + 12, y), (x + 12, y + 12), (x + 6, y + 6)], r)
        c.poly([(x, y + 12), (x + 12, y + 12), (x + 6, y + 6)], b)
        c.poly([(x, y), (x, y + 12), (x + 6, y + 6)], l)
    sq(3, 3, 'R', 'B', 'G', 'Y')
    sq(16, 3, 'O', 'G', 'R', 'B')
    sq(3, 16, 'G', 'Y', 'B', 'O')
    sq(16, 16, 'R', 'M', 'Y', 'Y')
    c.outline()
    c.vline(15, 3, 28, 'K'); c.hline(3, 28, 15, 'K')


@icon('org.gnome.LightsOff', ['lightsoff', 'gnome-lightsoff'], 'games', 'Lights Off')
def lightsoff(c):
    c.rect(3, 3, 28, 28, 'k')
    on = ["101", "010", "110"]
    for j, r in enumerate(on):
        for i, b in enumerate(r):
            x, y = 5 + i * 8, 5 + j * 8
            c.rrect(x, y, x + 6, y + 6, 'G' if b == '1' else 's', 1)
            if b == '1':
                c.hline(x + 1, x + 5, y, 'g')
    c.outline()


@icon('org.gnome.SwellFoop', ['swell-foop'], 'games', 'Swell Foop')
def swellfoop(c):
    slab(c)
    for x, y, col in [(8, 18, 'R'), (16, 18, 'B'), (24, 18, 'R'), (12, 11.5, 'G'), (20, 11.5, 'Y')]:
        c.circle(x, y, 4, col)
    c.circle(16, 6, 3, 'M')
    c.outline()


@icon('org.gnome.Hitori', ['hitori'], 'games', 'Hitori')
def hitori(c):
    c.rect(3, 3, 28, 28, 'W')
    for i in range(1, 3):
        c.vline(3 + i * 8 + (i - 1), 3, 28, 'S') if False else None
    for x in (11, 20):
        c.vline(x, 3, 28, 'S')
    for y in (11, 20):
        c.hline(3, 28, y, 'S')
    c.rect(12, 3, 19, 10, 'k'); c.rect(3, 12, 10, 19, 'k'); c.rect(21, 21, 28, 28, 'k')
    c.text(5, 4, '1', 'B'); c.text(22, 4, '3', 'B'); c.text(14, 13, '2', 'B'); c.text(5, 21, '3', 'B')
    c.outline()


@icon('org.gnome.five-or-more', ['five-or-more', 'gnome-five-or-more'], 'games', 'Five or More')
def fiveormore(c):
    c.rect(3, 3, 28, 28, 'w')
    for i in range(1, 5):
        c.vline(3 + i * 5, 3, 28, 'S'); c.hline(3, 28, 3 + i * 5, 'S')
    for i in range(5):
        c.circle(6 + i * 5, 26 - i * 5, 2, 'R')
    c.circle(11, 6, 2, 'B'); c.circle(26, 21, 2, 'G')
    c.outline()


@icon('org.gnome.Taquin', ['gnome-taquin'], 'games', 'Taquin')
def taquin(c):
    c.rect(3, 3, 28, 28, 'N')
    c.bevel(['N'])
    for j in range(3):
        for i in range(3):
            if (i, j) == (2, 2):
                continue
            x, y = 5 + i * 8, 5 + j * 8
            c.rect(x, y, x + 6, y + 6, 'n')
            c.hline(x, x + 6, y + 6, '8')
            c.text(x + 2, y + 1, str(j * 3 + i + 1), '8', font=3)
    c.rect(21, 21, 27, 27, '8')
    c.outline()


@icon('org.gnome.Atomix', ['atomix'], 'games', 'Atomix')
def atomix(c):
    c.line(10, 10, 21, 21, 'S', 2); c.line(21, 10, 10, 21, 'S', 2)
    c.circle(16, 16, 6, 'R')
    for x, y, col in [(8, 8, 'B'), (24, 8, 'W'), (8, 24, 'W'), (24, 24, 'B')]:
        c.circle(x, y, 4.5, col)
    c.bevel(['R', 'B', 'W'])
    c.outline()


@icon('org.gnome.Four-in-a-row', ['four-in-a-row', 'gnome-four-in-a-row'], 'games', 'Four in a Row')
def fourinarow(c):
    c.rect(3, 4, 28, 24, 'B')
    c.rect(3, 25, 7, 28, 'B'); c.rect(24, 25, 28, 28, 'B')
    c.bevel(['B'])
    cols = ['k', 'k', 'Y', 'k', 'k', 'R', 'Y', 'k', 'R', 'R', 'Y', 'Y']
    for j in range(3):
        for i in range(4):
            c.circle(7 + i * 6, 8 + j * 6, 2.2, cols[j * 4 + i])
    c.outline()
