"""GNOME Circle and popular libadwaita apps."""
from pix import icon
import math

LT = {'R': 'r', 'O': 'o', 'Y': 'y', 'G': 'g', 'C': 'c', 'B': 'b', 'M': 'm', 'N': 'n', 'P': 'p', 'W': 'W', 'S': 'w', 'k': 's'}
DK = {'R': '1', 'O': '2', 'Y': '3', 'G': '4', 'C': '5', 'B': '6', 'M': '7', 'N': '8', 'P': '9', 'W': 'w', 'S': 's'}


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


def bubble(c, x0, y0, x1, y1, col, tail='l', r=3):
    c.rrect(x0, y0, x1, y1, col, r)
    if tail == 'l':
        c.poly([(x0 + 3, y1 - 1), (x0 + 9, y1 - 1), (x0 + 2, y1 + 5)], col)
    else:
        c.poly([(x1 - 9, y1 - 1), (x1 - 3, y1 - 1), (x1 - 2, y1 + 5)], col)


def disc(c, col, r=12.5):
    c.circle(16, 16, r, col)
    c.bevel([col])


# ================================================================== writing / reading


@icon('info.febvre.Komikku', ['komikku'], 'office', 'Komikku')
def komikku(c):
    c.rect(4, 3, 27, 28, 'W')
    c.bevel(['W'])
    c.rect(6, 5, 15, 13, 'R'); c.rect(17, 5, 25, 13, 'k'); c.rect(6, 15, 25, 26, 'R')
    bubble(c, 8, 17, 19, 21, 'W', 'l', 1)
    c.poly([(19, 7), (21, 11), (23, 7)], 'Y')
    c.outline()


@icon('io.gitlab.news_flash.NewsFlash', ['newsflash', 'com.gitlab.newsflash', 'news-flash'], 'web', 'NewsFlash')
def newsflash(c):
    disc(c, 'O')
    c.circle(10, 22, 2.5, 'W')
    c.arc(9, 23, 9, 6.5, 270, 360, 'W')
    c.arc(9, 23, 15, 12.5, 270, 360, 'W')
    c.outline()


@icon('com.belmoussaoud.ReadItLater', ['read-it-later'], 'web', 'Read It Later')
def readitlater(c):
    c.rrect(5, 3, 26, 28, 'B', 1)
    c.bevel(['B'])
    c.poly([(11, 3), (20, 3), (20, 22), (15.5, 18), (11, 22)], 'R')
    c.vline(11, 3, 21, 'r')
    c.outline()


@icon('app.drey.Biblioteca', ['biblioteca'], 'dev', 'Biblioteca')
def biblioteca(c):
    for x0, w, h, col in [(3, 5, 22, 'B'), (9, 4, 18, 'O'), (14, 5, 24, 'G'), (20, 4, 20, 'R')]:
        c.rect(x0, 28 - h, x0 + w - 1, 28, col)
        c.hline(x0, x0 + w - 1, 28 - h + 3, 'W')
    c.poly([(23, 10), (26, 9), (29, 27), (26, 28)], 'M')
    c.outline()


@icon('com.github.ADBeveridge.Raider', ['raider', 'file-shredder'], 'utilities', 'File Shredder')
def raider(c):
    page(c, 8, 3, 23, 14, 'W', 4)
    c.rrect(3, 12, 28, 19, 'R', 1)
    c.bevel(['R'])
    c.rect(5, 15, 26, 16, '1')
    for x in range(8, 24, 3):
        c.rect(x, 20, x + 1, 27 - (x % 5), 'W')
    c.outline()


@icon('fr.romainvigier.MetadataCleaner', ['metadata-cleaner'], 'utilities', 'Metadata Cleaner')
def metadatacleaner(c):
    page(c, 3, 3, 21, 26, 'W', 5)
    c.bevel(['W'])
    for y in (10, 14, 18):
        c.hline(6, 17, y, 'S')
    # broom
    c.line(27, 6, 19, 20, 'N', 2)
    c.poly([(15, 19), (21, 18), (25, 28), (14, 29)], 'Y')
    c.line(17, 22, 19, 28, '3'); c.line(20, 21, 22, 28, '3')
    c.outline()


@icon('io.github.diegoivan.pdf_metadata_editor', ['paper-clip', 'paperclip'], 'office', 'Paper Clip')
def paperclip(c):
    page(c, 4, 5, 25, 28, 'R', 6, 'r')
    c.bevel(['R'])
    c.text(8, 18, 'PDF', 'W', font=3)
    c.sprite(16, 3, """
        .####.
        #....#
        #.##.#
        #.##.#
        #.##.#
        #.##.#
        #....#
        #....#
        .####.
    """, {'#': 'S'})
    c.outline()


@icon('io.github.fkinoshita.Telegraph', ['telegraph'], 'utilities', 'Telegraph')
def telegraph(c):
    # morse key
    c.rrect(3, 22, 28, 27, 'N', 1)
    c.bevel(['N'])
    c.poly([(5, 18), (25, 12), (26, 15), (6, 21)], 'S')
    c.circle(25, 12, 3.5, 'k')
    c.rect(8, 19, 10, 22, 'Y')
    c.sprite(4, 5, """
        ##.#.###.#
    """, {'#': 'Y'})
    c.outline()


@icon('dev.mufeed.Wordbook', ['wordbook'], 'office', 'Wordbook')
def wordbook(c):
    c.rrect(5, 3, 26, 28, 'M', 1)
    c.bevel(['M'])
    c.rect(5, 25, 26, 28, 'W'); c.hline(5, 26, 25, 'w')
    c.text(11, 8, 'W', 'W')
    c.rect(10, 18, 21, 19, '7')
    c.outline()


# ================================================================== audio / video
@icon('com.rafaelmardojai.Blanket', ['blanket'], 'media', 'Blanket')
def blanket(c):
    # folded quilt
    c.rect(3, 6, 28, 26, 'C')
    for x in range(3, 29, 6):
        c.vline(x + 5, 6, 26, '5')
    for y in (12, 19):
        c.hline(3, 28, y, '5')
    c.poly([(3, 6), (28, 6), (28, 11), (3, 15)], 'c')
    c.outline()


@icon('de.haeckerfelix.AudioSharing', ['audio-sharing'], 'media', 'Audio Sharing')
def audiosharing(c):
    c.arc(16, 19, 12.5, 10.5, 200, 340, 'B')
    c.arc(16, 19, 8.5, 6.5, 200, 340, 'B')
    c.bevel(['B'])
    c.rrect(10, 18, 21, 28, 'W', 2)
    c.circle(15.5, 23, 2.5, 'k')
    c.outline()


@icon('dev.bragefuglseth.Fretboard', ['fretboard'], 'media', 'Fretboard')
def fretboard(c):
    c.rect(5, 3, 26, 28, 'N')
    c.bevel(['N'])
    c.rect(5, 3, 26, 4, 'W')
    for y in (10, 16, 22):
        c.hline(5, 26, y, 'w')
    for x in (8, 12, 16, 20, 24):
        c.vline(x, 5, 28, 'S')
    c.circle(12.5, 13, 1.5, 'R'); c.circle(20.5, 19, 1.5, 'R'); c.circle(16.5, 7, 1.5, 'R')
    c.outline()


@icon('com.clarahobbs.chessclock', ['chess-clock'], 'utilities', 'Chess Clock')
def chessclock(c):
    c.rect(8, 4, 10, 6, 'R'); c.rect(21, 4, 23, 6, 'k')
    c.rrect(3, 7, 28, 26, 'N', 2)
    c.bevel(['N'])
    c.circle(10, 16.5, 5, 'W'); c.circle(22, 16.5, 5, 'W')
    c.vline(10, 13, 16, 'k'); c.line(22, 16, 25, 14, 'k')
    c.outline()


@icon('dev.bragefuglseth.Keypunch', ['keypunch'], 'utilities', 'Keypunch')
def keypunch(c):
    c.poly([(5, 7), (27, 7), (28.5, 25), (3.5, 25)], 'w')
    c.rect(5, 7, 27, 9, 'W')
    c.bevel(['w'])
    c.text(10, 12, 'A', 'B')
    c.rect(17, 12, 21, 18, 'k')
    c.rect(6, 22, 26, 25, 'S')
    c.outline()


# ================================================================== images / design


@icon('io.gitlab.adhami3310.Impression', ['impression'], 'system', 'Impression')
def impression(c):
    c.rrect(9, 3, 22, 25, 'S', 2)
    c.bevel(['S'])
    c.rect(11, 6, 20, 12, 'R')
    c.rect(11, 6, 20, 7, 'r')
    c.rect(13, 25, 18, 28, 'w')
    c.rect(14, 26, 15, 27, 'k'); c.rect(16, 26, 17, 27, 'k')
    c.text(13, 15, 'ISO', 'W', font=3) if False else c.rect(12, 16, 19, 21, 'k')
    c.px(15, 18, 'G'); c.px(16, 18, 'G')
    c.outline()


@icon('io.github.tfuxu.Halftone', ['halftone'], 'media', 'Halftone')
def halftone(c):
    c.circle(16, 16, 12.5, 'B')
    for j in range(5):
        for i in range(5):
            cx, cy = 7 + i * 4.5, 7 + j * 4.5
            r = 0.6 + (i + j) * 0.25
            c.circle(cx, cy, r, 'W')
    c.circle(16, 16, 13.5, '.') if False else None
    c.ring(16, 16, 14, 12.5, '.')
    c.outline()


@icon('io.github.nokse22.Exhibit', ['exhibit'], 'media', 'Exhibit')
def exhibit(c):
    c.rrect(3, 22, 28, 27, 'N', 1)
    c.bevel(['N'])
    c.poly([(16, 3), (25, 8), (25, 18), (16, 23), (7, 18), (7, 8)], 'B')
    c.poly([(16, 13), (25, 8), (25, 18), (16, 23)], '6')
    c.poly([(16, 3), (25, 8), (16, 13), (7, 8)], 'b')
    c.outline()


@icon('com.github.GradienceTeam.Gradience', ['gradience'], 'system', 'Gradience')
def gradience(c):
    for i, col in enumerate(['M', 'B', 'C', 'G', 'Y']):
        c.arc(16, 22, 13.5 - i * 2.2, 11.5 - i * 2.2, 180, 360, col)
    c.rect(3, 22, 28, 26, 'S') if False else None
    c.outline()


@icon('io.github.getnf.embellish', ['embellish'], 'system', 'Embellish')
def embellish(c):
    c.rrect(3, 3, 28, 28, 'k', 3)
    c.sprite(7, 7, """
        ..######......
        .##....##.....
        ##......##....
        ##......##....
        ##......##.##.
        ##......##.##.
        .##....##.....
        ..######......
    """, {'#': 'Y'})
    c.rect(7, 20, 24, 21, 'S'); c.rect(7, 23, 18, 24, 'S')
    c.outline()


@icon('com.rafaelmardojai.WebfontKitGenerator', ['webfont-kit-generator'], 'dev', 'Webfont Kit Generator')
def webfontkit(c):
    c.rrect(3, 7, 28, 27, 'N', 2)
    c.bevel(['N'])
    c.rect(3, 7, 28, 10, 'n')
    c.rect(13, 5, 18, 7, 'S')
    c.text(10, 13, 'AA', 'W') if False else c.text(8, 14, 'Aa', 'W')
    c.outline()


@icon('io.github.finefindus.Hieroglyphic', ['hieroglyphic'], 'dev', 'Hieroglyphic')
def hieroglyphic(c):
    c.rrect(5, 3, 26, 28, 'Y', 2)
    c.bevel(['Y'])
    c.sprite(9, 7, """
        ..####...
        .#....#..
        .#....#..
        ..####...
        ....#....
        .#######.
        ....#....
        ...#.#...
        ..#...#..
        .#.....#.
    """, {'#': '3'})
    c.rect(8, 23, 22, 24, '3')
    c.outline()


# ================================================================== productivity


@icon('dev.edfloreshz.Done', ['done'], 'office', 'Done')
def done(c):
    c.circle(16, 16, 12.5, 'G')
    c.bevel(['G'])
    c.circle(16, 16, 8.5, 'W')
    c.circle(16, 16, 6.5, 'g')
    c.sprite(12, 13, """
        .......#
        ......##
        #....##.
        ##..##..
        .####...
        ..##....
    """, {'#': 'W'})
    c.outline()


@icon('io.github.lainsce.Khronos', ['khronos'], 'utilities', 'Khronos')
def khronos(c):
    c.circle(16, 16, 12.5, 'M')
    c.bevel(['M'])
    c.circle(16, 16, 9, 'W')
    c.vline(16, 10, 16, 'k'); c.line(16, 16, 20, 19, 'k')
    for a in range(0, 360, 90):
        r = math.radians(a)
        c.px(16 + 7.5 * math.cos(r) - 0.5, 16 + 7.5 * math.sin(r) - 0.5, 'S')
    c.outline()


@icon('dev.Cogitri.Health', ['health'], 'utilities', 'Health')
def health(c):
    c.circle(10, 11, 7, 'R'); c.circle(22, 11, 7, 'R')
    c.poly([(3.5, 13), (28.5, 13), (16, 27)], 'R')
    c.bevel(['R'])
    c.sprite(6, 12, """
        .......#..........
        ......#.#.........
        #####.#..#.#######
        .....#...#.#......
        .........#.#......
        ..........#.......
    """, {'#': 'W'})
    c.outline()


@icon('io.github.idevecore.Valuta', ['valuta'], 'office', 'Valuta')
def valuta(c):
    c.circle(11, 11, 8.5, 'Y')
    c.circle(21, 21, 8.5, 'G')
    c.bevel(['Y', 'G'])
    c.text(9, 8, '$', '3') if False else c.sprite(8, 7, """
        .###.
        #....
        .##..
        ...#.
        ###..
    """, {'#': '3'})
    c.sprite(18, 17, """
        .###
        #...
        ###.
        #...
        .###
    """, {'#': '4'})
    c.outline()


@icon('com.github.alexhuntley.Plots', ['plots'], 'education', 'Plots')
def plots(c):
    c.rrect(3, 3, 28, 28, 'W', 2)
    c.bevel(['W'])
    c.vline(15, 5, 26, 'S'); c.hline(5, 26, 15, 'S')
    for x in range(5, 27):
        y = round(15 - 8 * math.sin((x - 5) / 21 * 2 * math.pi))
        c.rect(x, y, x, y + 1, 'B')
    c.outline()


@icon('se.sjoerd.Graphs', ['graphs'], 'education', 'Graphs')
def graphs(c):
    c.rrect(3, 3, 28, 28, 'k', 2)
    for i, (h, col) in enumerate([(8, 'B'), (14, 'G'), (11, 'Y'), (19, 'R')]):
        x = 6 + i * 5
        c.rect(x, 25 - h, x + 3, 25, col)
        c.hline(x, x + 3, 25 - h, LT[col])
    c.outline()


@icon('app.drey.Elastic', ['elastic'], 'dev', 'Elastic')
def elastic(c):
    c.rrect(3, 3, 28, 28, 'W', 2)
    c.bevel(['W'])
    for x in range(5, 27):
        t = (x - 5) / 21
        y = round(15 - 10 * math.exp(-2.5 * t) * math.cos(14 * t))
        y = max(5, min(25, y))
        c.rect(x, y, x, y + 1, 'M')
    c.hline(5, 26, 8, 'w') if False else None
    c.outline()


@icon('re.sonny.Workbench', ['workbench'], 'dev', 'Workbench')
def workbench(c):
    c.rect(3, 10, 28, 14, 'N')
    c.bevel(['N'])
    c.rect(5, 15, 7, 28, '8'); c.rect(24, 15, 26, 28, '8')
    c.rect(7, 21, 24, 22, '8')
    c.rect(8, 4, 12, 9, 'B'); c.rect(14, 6, 22, 9, 'O')
    c.outline()


@icon('re.sonny.Commit', ['commit'], 'dev', 'Commit')
def commit(c):
    c.rrect(3, 6, 28, 25, 'k', 2)
    c.rect(6, 10, 17, 11, 'G')
    for y, x1 in [(14, 23), (17, 20), (20, 25)]:
        c.hline(6, x1, y, 's')
    c.rect(6, 13, 7, 15, 'W') if False else None
    c.outline()


@icon('re.sonny.Junction', ['junction'], 'system', 'Junction')
def junction(c):
    c.rect(14, 15, 17, 28, 'S')
    c.bevel(['S'])
    c.poly([(3, 5), (15, 5), (18, 8.5), (15, 12), (3, 12)], 'B')
    c.poly([(28, 12), (16, 12), (13, 15.5), (16, 19), (28, 19)], 'O')
    c.rect(14, 5, 17, 14, 'S') if False else None
    c.bevel(['B', 'O'])
    c.outline()


@icon('re.sonny.Tangram', ['tangram'], 'web', 'Tangram')
def tangram(c):
    c.poly([(3, 3), (16, 16), (3, 29)], 'R')
    c.poly([(3, 3), (29, 3), (16, 16)], 'Y')
    c.poly([(29, 3), (29, 16), (22.5, 9.5)], 'B')
    c.poly([(16, 16), (22.5, 9.5), (29, 16), (22.5, 22.5)], 'G')
    c.poly([(3, 29), (16, 16), (22.5, 22.5), (16, 29)], 'M')
    c.poly([(16, 29), (29, 16), (29, 29)], 'C')
    c.outline()


@icon('com.mardojai.ForgeSparks', ['forge-sparks'], 'dev', 'Forge Sparks')
def forgesparks(c):
    c.poly([(3, 16), (25, 16), (28.5, 20), (25, 23), (7, 23)], 'S')
    c.rect(11, 23, 20, 25, 's'); c.rrect(8, 26, 23, 28, 's', 1)
    c.bevel(['S'])
    for x, y in [(12, 8), (16, 5), (21, 9), (8, 11)]:
        c.sprite(x - 1, y - 1, """
            .#.
            ###
            .#.
        """, {'#': 'Y'})
    c.outline()


@icon('com.belmoussaoud.Decoder', ['decoder'], 'utilities', 'Decoder')
def decoder(c):
    c.rect(3, 3, 28, 28, 'W')
    for x0, y0 in [(3, 3), (21, 3), (3, 21)]:
        c.rect(x0, y0, x0 + 7, y0 + 7, 'k')
        c.frame(x0 + 1, y0 + 1, x0 + 6, y0 + 6, 'W')
    import random
    rnd = random.Random(7)
    for j in range(13, 27, 2):
        for i in range(13, 27, 2):
            if rnd.random() < 0.55:
                c.rect(i, j, i + 1, j + 1, 'k')
    for (x, y) in [(13, 5), (15, 7), (17, 5), (5, 13), (7, 15), (5, 17)]:
        c.rect(x, y, x + 1, y + 1, 'k')
    c.outline()


@icon('com.belmoussaoud.Obfuscate', ['obfuscate'], 'media', 'Obfuscate')
def obfuscate(c):
    c.rrect(3, 5, 28, 26, 'C', 2)
    c.bevel(['C'])
    c.rect(6, 9, 25, 22, 'W')
    for j in range(3):
        for i in range(4):
            if (i + j) % 2:
                c.rect(12 + i * 3, 11 + j * 3, 14 + i * 3, 13 + j * 3, 'k')
            else:
                c.rect(12 + i * 3, 11 + j * 3, 14 + i * 3, 13 + j * 3, 's')
    c.rect(8, 12, 10, 19, 'C')
    c.outline()


@icon('app.drey.Dialect', ['dialect', 'com.github.gi_lom.dialect'], 'utilities', 'Dialect')
def dialect(c):
    bubble(c, 3, 3, 20, 16, 'B', 'l')
    bubble(c, 12, 11, 28, 23, 'W', 'r')
    c.bevel(['B', 'W'])
    c.text(9, 6, 'A', 'W')
    c.sprite(17, 14, """
        ...#...
        #######
        ..#.#..
        .#...#.
        #.....#
    """, {'#': 'k'})
    c.outline()


@icon('app.drey.Warp', ['warp-share', 'magic-wormhole'], 'utilities', 'Warp')
def warp(c):
    c.circle(16, 16, 12.5, 'M')
    c.circle(16, 16, 9.5, '7')
    c.circle(16, 16, 6.5, 'k')
    c.arc(16, 16, 12.5, 10, 200, 260, 'm')
    c.sprite(13, 12, """
        ..#..
        .###.
        #####
        ..#..
        ..#..
        ..#..
        ..#..
        ..#..
    """, {'#': 'W'})
    c.outline()


@icon('dev.geopjr.Collision', ['collision'], 'utilities', 'Collision')
def collision(c):
    c.poly([(3, 16), (9, 13), (6, 5), (14, 10), (16, 3), (19, 10), (27, 6), (23, 14), (29, 18),
            (22, 20), (25, 28), (17, 22), (12, 29), (11, 21), (4, 24), (8, 18)], 'O')
    c.poly([(9, 16), (13, 13), (16, 8), (18, 14), (23, 16), (18, 19), (15, 24), (13, 19)], 'Y')
    c.text(13, 14, '#', 'k', font=3) if False else c.rect(14, 14, 17, 17, 'W')
    c.outline()


@icon('io.github.giantpinkrobots.flatsweep', ['flatsweep'], 'system', 'Flatsweep')
def flatsweep(c):
    c.line(25, 3, 15, 17, 'N', 2)
    c.poly([(9, 15), (19, 15), (25, 28), (3, 28)], 'Y')
    c.bevel(['Y'])
    c.rect(9, 15, 19, 17, 'R')
    for x in (8, 12, 16, 20):
        c.vline(x, 21, 27, '3')
    c.outline()


@icon('io.github.flattool.Ignition', ['ignition'], 'system', 'Ignition')
def ignition(c):
    c.circle(16, 16, 12.5, 'k')
    c.ring(16, 16, 12.5, 11, 's')
    c.poly([(16, 6), (22, 15), (20, 24), (12, 24), (10, 15), (13, 11), (14, 15)], 'O')
    c.poly([(16, 14), (19, 19), (18, 24), (14, 24), (13, 19)], 'Y')
    c.outline()


@icon('com.rafaelmardojai.SharePreview', ['share-preview'], 'web', 'Share Preview')
def sharepreview(c):
    c.rrect(3, 4, 28, 27, 'W', 2)
    c.bevel(['W'])
    c.rect(5, 6, 26, 16, 'B')
    c.circle(12, 11, 2.5, 'b')
    c.rect(5, 19, 20, 20, 'k'); c.rect(5, 23, 24, 24, 'S')
    c.outline()


@icon('de.schmidhuberj.DieBahn', ['diebahn', 'railway'], 'utilities', 'Railway')
def railway(c):
    c.rrect(6, 3, 25, 24, 'R', 3)
    c.bevel(['R'])
    c.rect(9, 6, 22, 13, 'b')
    c.rect(9, 6, 22, 7, 'c')
    c.circle(10.5, 19, 1.5, 'Y'); c.circle(21.5, 19, 1.5, 'Y')
    c.line(9, 25, 6, 27, 'k', 2); c.line(22, 25, 25, 27, 'k', 2)
    c.outline()


@icon('io.gitlab.liferooter.TextPieces', ['textpieces', 'com.github.liferooter.textpieces'], 'dev', 'Text Pieces')
def textpieces(c):
    c.rect(3, 4, 20, 14, 'G')
    c.circle(11.5, 15, 3, 'G')
    c.rect(11, 17, 28, 27, 'B')
    c.circle(19.5, 17, 2.5, 'B')
    c.bevel(['G', 'B'])
    c.text(5, 6, 'T', 'W')
    c.rect(14, 21, 25, 22, 'W')
    c.outline()
