"""More KDE (Gear, Plasma Mobile, Maui) and GNOME ecosystem apps."""
from pix import icon
import math

LT = {'R': 'r', 'O': 'o', 'Y': 'y', 'G': 'g', 'C': 'c', 'B': 'b', 'M': 'm', 'N': 'n', 'P': 'p', 'W': 'W', 'S': 'w'}


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


def globe(c, cx, cy, r, col='B', land='G'):
    c.circle(cx, cy, r, col)
    c.bevel([col])
    c.poly([(cx - r * .6, cy - r * .5), (cx - r * .1, cy - r * .7), (cx, cy - r * .1),
            (cx - r * .4, cy + r * .2)], land)
    c.poly([(cx + r * .2, cy + r * .1), (cx + r * .7, cy - r * .1), (cx + r * .5, cy + r * .6),
            (cx + r * .1, cy + r * .5)], land)


# ================================================================== KDE
@icon('org.kde.konqueror', ['konqueror', 'kfm'], 'web', 'Konqueror')
def konqueror(c):
    # the classic "K" gear-blue globe with a lens ring
    globe(c, 16, 16, 12.5, 'B', 'G')
    c.ring(16, 16, 12.5, 11, '6')
    c.text(12, 12, 'K', 'W')
    c.outline()


@icon('org.kde.angelfish', ['angelfish'], 'web', 'Angelfish')
def angelfish(c):
    # angelfish body: tall diamond with fins
    c.poly([(16, 3), (24, 15), (16, 27), (6, 15)], 'C')
    c.poly([(16, 3), (11, 2.5), (13, 8)], 'C')
    c.poly([(16, 27), (11, 29), (13, 22)], 'C')
    c.poly([(23, 15), (29, 9), (28, 15), (29, 21)], 'c')
    c.bevel(['C'])
    c.vline(13, 7, 23, '5'); c.vline(18, 9, 21, '5')
    c.circle(9.5, 14, 1.2, 'k')
    c.outline()


@icon('org.kde.klettres', ['klettres'], 'education', 'KLettres')
def klettres(c):
    c.rrect(3, 3, 17, 17, 'R', 2)
    c.rrect(14, 14, 28, 28, 'B', 2)
    c.bevel(['R', 'B'])
    c.text(8, 6, 'A', 'W'); c.text(19, 17, 'B', 'W')
    c.outline()


@icon('org.kde.rocs', ['rocs'], 'education', 'Rocs')
def rocs(c):
    for a, b in [((8, 8), (24, 9)), ((8, 8), (11, 24)), ((24, 9), (22, 24)), ((11, 24), (22, 24)), ((8, 8), (22, 24))]:
        c.line(*a, *b, 'S', 2)
    for (x, y, col) in [(8, 8, 'R'), (24, 9, 'B'), (11, 24, 'G'), (22, 24, 'Y')]:
        c.circle(x, y, 4.5, col)
        c.px(x - 2, y - 2, LT[col])
    c.outline()


@icon('org.kde.kmouth', ['kmouth'], 'utilities', 'KMouth')
def kmouth(c):
    c.rrect(3, 4, 28, 21, 'W', 3)
    c.poly([(8, 20), (14, 20), (7, 28.5)], 'W')
    c.bevel(['W'])
    c.ellipse(16, 12.5, 7, 4, 'R')
    c.hline(10, 22, 12, '1')
    c.outline()


@icon('org.kde.kmousetool', ['kmousetool'], 'utilities', 'KMouseTool')
def kmousetool(c):
    c.sprite(5, 3, """
        #...........
        ##..........
        #W#.........
        #WW#........
        #WWW#.......
        #WWWW#......
        #WWWWW#.....
        #WWWWWW#....
        #WWWWWWW#...
        #WWWWWWWW#..
        #WWWWW####..
        #WW#WW#.....
        #W#.#WW#....
        ##..#WW#....
        #....#WW#...
        .....####...
    """, {'#': 'K'})
    c.circle(21, 22, 6.5, 'O')
    c.bevel(['O'])
    c.vline(21, 18, 22, 'W'); c.hline(21, 24, 22, 'W')
    c.outline()


@icon('org.kde.kontrast', ['kontrast'], 'dev', 'Kontrast')
def kontrast(c):
    c.rrect(3, 3, 28, 28, 'k', 2)
    c.poly([(3, 28.5), (28.5, 3), (28.5, 28.5)], 'W')
    c.rrect(3, 3, 28, 28, '.', 0) if False else None
    c.text(6, 6, 'A', 'W'); c.text(20, 18, 'A', 'k')
    c.outline()


@icon('org.kde.kjournaldbrowser', ['kjournaldbrowser', 'kjournald'], 'system', 'Journald Browser')
def kjournald(c):
    c.rrect(5, 3, 26, 28, 'N', 1)
    c.bevel(['N'])
    c.rect(8, 6, 23, 25, 'W')
    for i, col in enumerate(['G', 'G', 'Y', 'G', 'R', 'G']):
        y = 8 + i * 3
        c.px(9, y, col); c.px(10, y, col)
        c.hline(12, 21 - (i % 3) * 2, y, 'S')
    c.outline()


@icon('org.kde.ktrip', ['ktrip'], 'utilities', 'KTrip')
def ktrip(c):
    c.rrect(5, 3, 26, 23, 'G', 4)
    c.bevel(['G'])
    c.rect(8, 6, 23, 13, 'c')
    c.rect(8, 6, 23, 7, 'W')
    c.circle(10, 18, 1.5, 'Y'); c.circle(21, 18, 1.5, 'Y')
    c.rect(6, 24, 9, 27, 'k'); c.rect(22, 24, 25, 27, 'k')
    c.outline()


@icon('org.kde.plasma-welcome', ['plasma-welcome'], 'system', 'Welcome Center')
def plasmawelcome(c):
    # party balloon pair
    c.ellipse(11, 11, 6.5, 8, 'B'); c.ellipse(21, 13, 6.5, 8, 'M')
    c.bevel(['B', 'M'])
    c.px(8, 7, 'W'); c.px(18, 9, 'W')
    c.line(11, 19, 15, 28, 'S'); c.line(21, 21, 16, 28, 'S')
    c.outline()


@icon('org.kde.kdebugsettings', ['kdebugsettings'], 'dev', 'Debug Settings')
def kdebugsettings(c):
    c.ellipse(16, 17, 8, 10.5, 'R')
    c.circle(16, 7, 4, 'k')
    c.bevel(['R'])
    c.vline(16, 9, 27, 'k')
    for y in (12, 18, 24):
        c.line(8, y, 3, y - 2, 'k'); c.line(23, y, 28, y - 2, 'k')
    c.px(12, 14, 'k'); c.px(20, 14, 'k'); c.px(12, 21, 'k'); c.px(20, 21, 'k')
    c.outline()


@icon('org.kde.kgeotag', ['kgeotag'], 'media', 'KGeoTag')
def kgeotag(c):
    c.rect(3, 9, 22, 28, 'W')
    c.rect(5, 11, 20, 26, 'b')
    c.poly([(5, 26.5), (10, 18), (15, 23), (20.5, 19), (20.5, 26.5)], 'G')
    c.circle(22, 9, 6.5, 'R')
    c.poly([(16.5, 11), (27.5, 11), (22, 19)], 'R')
    c.bevel(['R'])
    c.circle(22, 9, 2.5, 'W')
    c.outline()


@icon('org.kde.kirogi', ['kirogi'], 'utilities', 'Kirogi')
def kirogi(c):
    # drone
    c.line(8, 8, 24, 24, 'S', 2); c.line(24, 8, 8, 24, 'S', 2)
    for x, y in [(7, 7), (25, 7), (7, 25), (25, 25)]:
        c.ellipse(x, y, 4.5, 1.8, 'k')
        c.ellipse(x, y, 3, 1, 's')
    c.rrect(12, 12, 20, 20, 'R', 2)
    c.bevel(['R'])
    c.circle(16, 16, 1.5, 'W')
    c.outline()


@icon('org.kde.krecorder', ['krecorder'], 'media', 'Recorder')
def krecorder(c):
    c.rrect(10, 3, 21, 18, 'S', 4)
    c.bevel(['S'])
    for y in (6, 9, 12, 15):
        c.hline(12, 19, y, 's')
    c.arc(15.5, 14, 9, 7, 0, 180, 'k')
    c.rect(15, 23, 16, 26, 'k')
    c.rrect(10, 26, 21, 28, 'k', 1)
    c.circle(25, 6, 2.5, 'R')
    c.outline()


@icon('org.kde.qrca', ['qrca'], 'utilities', 'Qrca')
def qrca(c):
    for x0, y0 in [(3, 3), (21, 3), (3, 21)]:
        c.rect(x0, y0, x0 + 7, y0 + 7, 'k')
        c.frame(x0 + 1, y0 + 1, x0 + 6, y0 + 6, 'W')
    c.rect(13, 13, 28, 28, 'W')
    for x, y in [(14, 14), (18, 16), (22, 14), (14, 20), (20, 22), (24, 19), (16, 25), (25, 25), (13, 6), (6, 13)]:
        c.rect(x, y, x + 1, y + 1, 'k')
    c.hline(3, 28, 16, 'R'); c.hline(3, 28, 17, 'r')
    c.outline()


@icon('org.kde.kalm', ['kalm'], 'utilities', 'Kalm')
def kalm(c):
    # lotus
    c.ellipse(16, 17, 4.5, 10, 'P')
    c.poly([(16, 26), (4, 12), (12, 15)], 'p')
    c.poly([(16, 26), (28, 12), (20, 15)], 'p')
    c.poly([(16, 27), (3, 21), (10, 20)], 'P')
    c.poly([(16, 27), (29, 21), (22, 20)], 'P')
    c.bevel(['P'])
    c.ellipse(16, 27, 10, 1.5, 'G')
    c.outline()


@icon('org.kde.hashomatic', ['hash-o-matic', 'org.kde.hash-o-matic'], 'utilities', 'Hash-o-Matic')
def hashomatic(c):
    c.rrect(3, 3, 28, 28, 'G', 3)
    c.bevel(['G'])
    c.sprite(8, 8, """
        ...##..##...
        ...##..##...
        ############
        ############
        ..##..##....
        ..##..##....
        ############
        ############
        .##..##.....
        .##..##.....
    """, {'#': 'W'})
    c.outline()


# ================================================================== Maui
@icon('org.kde.vvave', ['vvave'], 'media', 'Vvave')
def vvave(c):
    c.poly([(3, 6), (28.5, 6), (16, 28.5)], 'M')
    c.poly([(9, 6), (22.5, 6), (16, 18)], 'm')
    c.bevel(['M'])
    c.circle(16, 10, 2.5, 'W')
    c.outline()


@icon('org.kde.index', ['index', 'index-fm', 'org.maui.index'], 'system', 'Index')
def index_fm(c):
    c.rrect(3, 5, 13, 9, 'C', 1)
    c.rect(3, 7, 28, 27, 'C')
    c.bevel(['C'])
    c.rect(6, 12, 25, 24, 'c')
    c.rect(9, 15, 12, 18, 'W'); c.rect(15, 15, 18, 18, 'W'); c.rect(21, 15, 22, 18, 'W') if False else c.rect(19, 15, 22, 18, 'W')
    c.outline()


@icon('org.kde.nota', ['nota'], 'dev', 'Nota')
def nota(c):
    page(c, 5, 3, 26, 28, 'B', 6, 'b')
    c.bevel(['B'])
    c.sprite(9, 12, """
        ..#.......#..
        .#.........#.
        #...........#
        .#.........#.
        ..#.......#..
    """, {'#': 'W'})
    c.line(17, 11, 14, 17, 'W')
    c.outline()


@icon('org.kde.shelf', ['shelf'], 'office', 'Shelf')
def shelf(c):
    for x0, w, h, col in [(4, 5, 20, 'O'), (10, 4, 16, 'R'), (15, 5, 22, 'B')]:
        c.rect(x0, 26 - h, x0 + w - 1, 25, col)
        c.hline(x0, x0 + w - 1, 26 - h + 2, 'W')
    c.poly([(20, 9), (23, 8), (27, 25), (24, 25.5)], 'G')
    c.rrect(3, 26, 28, 28, 'N', 1)
    c.outline()


@icon('org.kde.clip', ['clip'], 'media', 'Clip')
def clip(c):
    c.circle(16, 16, 12.5, 'R')
    c.bevel(['R'])
    c.circle(16, 16, 8.5, 'k')
    play(c, 14, 11, 11, 'W')
    c.outline()


@icon('org.kde.station', ['station'], 'system', 'Station')
def station(c):
    c.rrect(3, 4, 28, 27, 'k', 3)
    c.rect(3, 4, 28, 8, 'M')
    c.rect(3, 4, 28, 4, 'm')
    c.sprite(6, 11, """
        #.......
        .#......
        ..#.....
        .#......
        #...####
    """, {'#': 'W'})
    c.outline()


@icon('org.kde.pix', ['org.maui.pix'], 'media', 'Pix (Maui)')
def maui_pix(c):
    c.rrect(3, 5, 28, 26, 'O', 3)
    c.bevel(['O'])
    c.rect(6, 8, 25, 23, 'Y')
    c.poly([(6, 23.5), (11, 14), (16, 20), (19, 17), (25.5, 23.5)], 'M')
    c.circle(20, 12, 2, 'W')
    c.outline()


@icon('org.kde.buho', ['buho'], 'office', 'Buho')
def buho(c):
    # owl
    c.ellipse(16, 17, 11, 11, 'N')
    c.poly([(5, 4), (12, 9), (6, 12)], 'N'); c.poly([(27, 4), (20, 9), (26, 12)], 'N')
    c.bevel(['N'])
    c.circle(11.5, 14, 4, 'W'); c.circle(20.5, 14, 4, 'W')
    c.circle(11.5, 14, 2, 'k'); c.circle(20.5, 14, 2, 'k')
    c.poly([(14.5, 18), (17.5, 18), (16, 21.5)], 'Y')
    c.ellipse(16, 25, 6, 3, 'n')
    c.outline()


@icon('org.kde.bonsai', ['bonsai'], 'dev', 'Bonsai')
def bonsai(c):
    c.circle(11, 10, 6, 'G'); c.circle(20, 8, 6, 'G'); c.circle(23, 15, 4.5, 'G')
    c.bevel(['G'])
    c.line(16, 21, 13, 13, 'N', 2); c.line(17, 19, 21, 14, 'N')
    c.poly([(6, 21), (26, 21), (23, 28), (9, 28)], 'R')
    c.bevel(['R'])
    c.outline()


@icon('org.kde.strike', ['strike'], 'dev', 'Strike')
def strike(c):
    c.poly([(19, 2.5), (6, 18), (15, 18), (12, 29.5), (26, 13), (17, 13)], 'Y')
    c.bevel(['Y'])
    c.outline()


@icon('org.kde.fiery', ['fiery'], 'web', 'Fiery')
def fiery(c):
    c.poly([(16, 3), (25, 13), (26, 21), (21, 28), (11, 28), (6, 21), (7, 13), (11, 17), (12, 9)], 'R')
    c.poly([(17, 12), (22, 19), (20, 27), (12, 27), (11, 21), (14, 22)], 'O')
    c.poly([(16, 19), (19, 23), (18, 27), (14, 27), (14, 23)], 'Y')
    c.outline()


# ================================================================== GNOME ecosystem
@icon('org.gnome.Tecla', ['tecla'], 'system', 'Keyboard Layout Viewer')
def tecla(c):
    c.rrect(3, 7, 28, 25, 'w', 2)
    c.bevel(['w'])
    for j in range(3):
        for i in range(4):
            x, y = 6 + i * 5 + j, 9 + j * 5
            c.rrect(x, y, x + 3, y + 3, 'W', 0)
            c.hline(x, x + 3, y + 3, 'S')
    c.text(6, 10, 'Q', 'B', font=3) if False else c.px(6, 10, 'B')
    c.outline()


@icon('fr.romainvigier.zap', [], 'media', 'Zap')
def zap(c):
    c.rrect(3, 3, 28, 28, 'W', 3)
    c.bevel(['W'])
    for i, col in enumerate(['R', 'Y', 'G', 'B']):
        x, y = 6 + (i % 2) * 11, 6 + (i // 2) * 11
        c.rrect(x, y, x + 8, y + 8, col, 2)
        c.hline(x + 2, x + 6, y, LT[col])
    c.outline()


@icon('io.github.fabrialberio.pinapp', ['pinapp', 'pins'], 'system', 'Pins')
def pinapp(c):
    c.circle(16, 11, 7.5, 'R')
    c.bevel(['R'])
    c.circle(13.5, 8.5, 2, 'r')
    c.rect(15, 18, 16, 27, 'S')
    c.px(15, 29, 'k') if False else None
    c.outline()


@icon('io.github.lainsce.Colorway', ['colorway'], 'dev', 'Colorway')
def colorway(c):
    cx, cy, R = 5, 27, 23
    for i, col in enumerate(['R', 'O', 'Y', 'G', 'B']):
        a0 = math.radians(-90 + i * 18)
        a1 = math.radians(-90 + i * 18 + 16)
        c.poly([(cx, cy), (cx + R * math.cos(a0), cy + R * math.sin(a0)),
                (cx + R * math.cos(a1), cy + R * math.sin(a1))], col)
    c.circle(5.5, 26.5, 2, 'W')
    c.outline()


@icon('app.drey.Damask', ['damask'], 'system', 'Damask')
def damask(c):
    c.rect(3, 5, 28, 26, 'M')
    c.bevel(['M'])
    for x, y in [(9, 11), (22, 11), (15.5, 20)]:
        c.sprite(round(x) - 3, y - 3, """
            ...#...
            ..###..
            .##.##.
            ##...##
            .##.##.
            ..###..
            ...#...
        """, {'#': 'm'})
    c.outline()


@icon('io.github.bytezz.IPLookup', ['iplookup', 'ip-lookup'], 'web', 'IP Lookup')
def iplookup(c):
    globe(c, 13, 13, 10.5, 'C', 'G')
    c.line(20, 20, 25, 25, 'N', 3)
    c.circle(13, 13, 10.5, 'C') if False else None
    c.rrect(14, 21, 28, 28, 'k', 1) if False else None
    c.outline()


@icon('io.github.jeffshee.Hidamari', ['hidamari'], 'system', 'Hidamari')
def hidamari(c):
    c.rrect(3, 4, 28, 22, 'S', 1)
    c.bevel(['S'])
    c.rect(5, 6, 26, 20, 'O')
    c.rect(5, 6, 26, 11, 'o')
    c.circle(21, 13, 3.5, 'Y')
    c.rect(5, 16, 26, 20, 'M')
    play(c, 11, 9, 7, 'W')
    c.rect(13, 23, 18, 24, 's'); c.rect(9, 25, 22, 26, 'S')
    c.outline()


@icon('re.sonny.Eloquent', ['eloquent'], 'office', 'Eloquent')
def eloquent(c):
    c.rrect(3, 3, 28, 22, 'G', 4)
    c.poly([(8, 21), (14, 21), (7, 28.5)], 'G')
    c.bevel(['G'])
    c.sprite(9, 7, """
        ............#
        ...........##
        ##........##.
        .##......##..
        ..##....##...
        ...##..##....
        ....####.....
        .....##......
    """, {'#': 'W'})
    c.outline()


@icon('re.sonny.Playhouse', ['playhouse'], 'dev', 'Playhouse')
def playhouse(c):
    c.poly([(16, 3), (28.5, 13), (3.5, 13)], 'R')
    c.rect(6, 13, 25, 28, 'Y')
    c.bevel(['R', 'Y'])
    c.rect(12, 18, 19, 28, 'O')
    play(c, 14, 20, 5, 'W')
    c.outline()


@icon('io.github.nate_xyz.Conjure', ['conjure'], 'media', 'Conjure')
def conjure(c):
    # magic wand + sparkle
    c.line(5, 25, 18, 12, 'k', 3)
    c.line(5, 25, 8, 22, 'W', 3)
    c.sprite(18, 3, """
        ....#....
        ....#....
        ...###...
        #########
        ...###...
        ....#....
        ....#....
    """, {'#': 'Y'})
    c.px(26, 15, 'M'); c.px(11, 7, 'M')
    c.outline()


@icon('io.github.seadve.Delineate', ['delineate'], 'dev', 'Delineate')
def delineate(c):
    c.line(9, 9, 22, 9, 'S', 2); c.line(9, 9, 9, 22, 'S', 2); c.line(22, 9, 22, 22, 'S', 2)
    for x, y, col in [(9, 9, 'B'), (22, 9, 'G'), (9, 22, 'O'), (22, 22, 'M')]:
        c.rrect(x - 5, y - 5, x + 5, y + 5, col, 2)
        c.hline(x - 3, x + 3, y - 5, LT[col])
    c.outline()


@icon('io.gitlab.idevecore.Pomodoro', [], 'utilities', 'Pomodoro')
def pomodoro(c):
    c.ellipse(16, 18, 12.5, 10.5, 'O')
    c.bevel(['O'])
    c.sprite(11, 5, """
        ....##....
        ....##....
        ###.##.###
        .########.
        ..#....#..
    """, {'#': 'G'})
    c.circle(16, 18.5, 5, 'W')
    c.vline(16, 15, 18, 'k'); c.hline(16, 18, 18, 'k')
    c.outline()


@icon('org.gnome.gitlab.cheywood.Buffer', ['buffer'], 'office', 'Buffer')
def buffer(c):
    page(c, 5, 3, 26, 28, 'w', 0)
    c.bevel(['w'])
    for y, x1 in [(7, 22), (10, 18), (13, 22), (16, 15)]:
        c.hline(8, x1, y, 'S')
    c.rect(8, 20, 23, 25, 'Y')
    c.hline(8, 23, 20, 'y')
    c.outline()


@icon('io.github.ronniedroid.concessio', ['concessio'], 'system', 'Concessio')
def concessio(c):
    c.rrect(3, 5, 28, 26, 'k', 2)
    c.text(6, 10, '7', 'G', font=3); c.text(12, 10, '5', 'G', font=3); c.text(18, 10, '5', 'G', font=3)
    c.text(6, 17, 'RWX', 'W', font=3)
    c.outline()


@icon('net.natesales.Aviator', ['aviator'], 'media', 'Aviator')
def aviator(c):
    c.poly([(3, 15), (28.5, 5), (18, 27), (14, 18)], 'W')
    c.poly([(14, 18), (28.5, 5), (17, 22)], 'w')
    c.bevel(['W'])
    c.line(14, 18, 28, 5, 'S')
    c.outline()


@icon('io.github.lainsce.Notejot', ['notejot', 'com.github.lainsce.notejot'], 'office', 'Notejot')
def notejot(c):
    c.poly([(8, 3), (28.5, 6), (25, 26), (5, 22)], 'O')
    c.rect(3, 8, 22, 28, 'Y')
    c.bevel(['Y', 'O'])
    for y in (13, 17, 21):
        c.hline(6, 19, y, '3')
    c.outline()
