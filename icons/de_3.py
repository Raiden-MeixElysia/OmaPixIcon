"""KDE Games. Family motif: a wooden framed game board (top-left) with the
game's hero piece breaking out of the frame at the lower right."""
from pix import icon
import math

LT = {'R': 'r', 'O': 'o', 'Y': 'y', 'G': 'g', 'C': 'c', 'B': 'b', 'M': 'm', 'N': 'n', 'P': 'p', 'S': 'w', 'W': 'W'}
DK = {'R': '1', 'O': '2', 'Y': '3', 'G': '4', 'C': '5', 'B': '6', 'M': '7', 'N': '8', 'P': '9', 'S': 's', 'W': 'w'}


def board(c, fill='G', x0=3, y0=3, x1=22, y1=22):
    """Wooden frame, inner play field at x0+2..x1-2."""
    c.rect(x0, y0, x1, y1, 'N')
    c.bevel(['N'])
    c.rect(x0 + 2, y0 + 2, x1 - 2, y1 - 2, fill)
    c.hline(x0 + 2, x1 - 2, y0 + 2, DK.get(fill, 'k'))
    c.vline(x0 + 2, y0 + 2, y1 - 2, DK.get(fill, 'k'))


def grid(c, x0, y0, n, step, col):
    for i in range(n + 1):
        c.vline(x0 + i * step, y0, y0 + n * step, col)
        c.hline(x0, x0 + n * step, y0 + i * step, col)


def ball(c, cx, cy, r, col):
    c.circle(cx, cy, r, col)
    c.circle(cx - r * 0.35, cy - r * 0.35, max(r * 0.35, 0.8), LT[col])


def tile(c, x0, y0, x1, y1, face='W', side='y'):
    c.rect(x0 + 1, y0 + 1, x1 + 1, y1 + 1, side)
    c.rect(x0, y0, x1, y1, face)


def card(c, x0, y0, x1, y1, suit_col, suit):
    c.rrect(x0, y0, x1, y1, 'W', 1)
    c.hline(x0 + 1, x1 - 1, y1, 'w'); c.vline(x1, y0 + 1, y1 - 1, 'w')
    c.sprite(x0 + (x1 - x0) // 2 - 2, y0 + (y1 - y0) // 2 - 2, suit, {'#': suit_col})


HEART = """
.#.#.
#####
#####
.###.
..#..
"""
SPADE = """
..#..
.###.
#####
#####
..#..
"""
DIAMOND = """
..#..
.###.
#####
.###.
..#..
"""


@icon('org.kde.kmines', ['kmines'], 'games', 'KMines')
def kmines(c):
    board(c, 'w')
    grid(c, 5, 5, 3, 5, 'S')
    c.text(7, 6, '1', 'B', font=3); c.text(12, 11, '2', 'G', font=3); c.text(7, 16, '3', 'R', font=3)
    for a in range(0, 360, 45):
        r = math.radians(a)
        c.line(21, 21, 21 + 7.5 * math.cos(r), 21 + 7.5 * math.sin(r), 'k')
    c.circle(21, 21, 5.5, 'k')
    c.circle(19.5, 19.5, 1.5, 'S')
    c.outline()


@icon('org.kde.kpat', ['kpat'], 'games', 'KPatience')
def kpat(c):
    board(c, 'G')
    c.poly([(10, 12), (19, 8), (24, 26), (15, 29)], 'W')
    card(c, 15, 12, 28, 28, 'R', HEART)
    c.text(17, 14, 'A', 'R', font=3)
    c.outline()


@icon('org.kde.kmahjongg', ['kmahjongg'], 'games', 'KMahjongg')
def kmahjongg(c):
    board(c, 'G')
    tile(c, 6, 6, 12, 14, 'W', 'Y'); tile(c, 13, 6, 19, 14, 'W', 'Y')
    tile(c, 14, 13, 26, 27, 'W', 'Y')
    c.circle(20, 17, 2, 'R'); c.circle(20, 23, 2, 'G')
    c.px(9, 9, 'B'); c.px(9, 11, 'B'); c.px(16, 10, 'R')
    c.outline()


@icon('org.kde.ksudoku', ['ksudoku'], 'games', 'KSudoku')
def ksudoku(c):
    board(c, 'W')
    grid(c, 5, 5, 3, 5, 'S')
    c.text(7, 6, '5', 'B', font=3); c.text(17, 11, '3', 'B', font=3); c.text(12, 16, '8', 'S', font=3)
    c.rrect(16, 15, 28, 28, 'B', 1)
    c.bevel(['B'])
    c.text(20, 18, '9', 'W')
    c.outline()


@icon('org.kde.kblocks', ['kblocks'], 'games', 'KBlocks')
def kblocks(c):
    board(c, 'k')
    for x, y, col in [(5, 17, 'R'), (8, 17, 'R'), (11, 17, 'B'), (5, 14, 'Y'), (8, 6, 'Y'), (11, 6, 'Y')]:
        c.rect(x, y, x + 2, y + 2, col)
    for x, y in [(16, 16), (20, 16), (24, 16), (20, 20)]:
        c.rect(x, y, x + 3, y + 3, 'M')
        c.hline(x, x + 3, y, 'm'); c.vline(x, y, y + 3, 'm')
        c.hline(x, x + 3, y + 3, '7'); c.vline(x + 3, y, y + 3, '7')
    c.outline()


@icon('org.kde.knights', ['knights'], 'games', 'Knights')
def knights(c):
    board(c, 'w')
    for j in range(4):
        for i in range(4):
            if (i + j) % 2:
                c.rect(5 + i * 4, 5 + j * 4, 8 + i * 4, 8 + j * 4, 'n')
    c.sprite(17, 13, """
        ....##......
        ...####.....
        ..#######...
        .#########..
        .##.#######.
        ###########.
        ##...######.
        .....######.
        ....#######.
        ...#######..
        ...#######..
        ..#########.
        .##########.
        .###########
        .###########
        ............
    """, {'#': 'k'})
    c.px(21, 17, 'W')
    c.hline(20, 27, 25, 's')
    c.outline()


@icon('org.kde.kapman', ['kapman'], 'games', 'Kapman')
def kapman(c):
    board(c, 'k')
    c.rect(7, 7, 18, 8, 'B'); c.rect(7, 7, 8, 18, 'B'); c.rect(12, 12, 18, 13, 'B')
    for x in (11, 15):
        c.px(x, 10, 'Y')
    c.circle(20, 20, 8, 'Y')
    c.poly([(20, 20), (29, 14), (29, 26)], '.')
    c.bevel(['Y'])
    c.rect(19, 15, 20, 16, 'k')
    c.outline()


@icon('org.kde.kbounce', ['kbounce'], 'games', 'KBounce')
def kbounce(c):
    board(c, 'B')
    c.rect(5, 12, 20, 13, 'W')
    c.rect(12, 5, 13, 11, 'W')
    ball(c, 8.5, 8.5, 2.5, 'R')
    c.circle(21, 21, 7, 'O')
    c.arc(21, 21, 7, 0, 30, 60, '2')
    c.vline(21, 14, 28, '2'); c.hline(14, 28, 21, '2')
    c.bevel(['O'])
    c.outline()


@icon('org.kde.kgoldrunner', ['kgoldrunner'], 'games', 'KGoldrunner')
def kgoldrunner(c):
    board(c, 'k')
    for j, y in enumerate(range(5, 21, 4)):
        off = 0 if j % 2 else 2
        for x in range(5 + off, 20, 4):
            c.rect(x, y, x + 2, y + 2, 'R')
    # gold bars
    for x0, y0 in [(13, 23), (21, 23), (17, 18)]:
        c.poly([(x0, y0 + 5), (x0 + 1.5, y0), (x0 + 6.5, y0), (x0 + 8, y0 + 5)], 'Y')
        c.hline(x0 + 2, x0 + 6, y0, 'y')
    c.outline()


@icon('org.kde.klickety', ['klickety'], 'games', 'Klickety')
def klickety(c):
    board(c, 'k')
    cols = ['R', 'B', 'G', 'Y']
    for j in range(4):
        for i in range(4):
            col = cols[(i * 3 + j * 2 + i * j) % 4]
            c.rect(5 + i * 4, 5 + j * 4, 7 + i * 4, 7 + j * 4, col)
    for x, y, col in [(19, 19, 'R'), (24, 19, 'R'), (19, 24, 'G'), (24, 24, 'B')]:
        c.rect(x, y, x + 4, y + 4, col); c.hline(x, x + 4, y, LT[col]); c.vline(x, y, y + 4, LT[col])
    c.outline()


@icon('org.kde.kollision', ['kollision'], 'games', 'Kollision')
def kollision(c):
    board(c, 'W')
    ball(c, 9, 9, 3, 'R'); ball(c, 16, 15, 2.5, 'R')
    c.circle(21, 21, 7, 'B')
    c.bevel(['B'])
    c.circle(19, 19, 2, 'b'); c.px(18, 18, 'W')
    c.outline()


@icon('org.kde.kreversi', ['kreversi'], 'games', 'KReversi')
def kreversi(c):
    board(c, 'G')
    grid(c, 5, 5, 3, 5, '4')
    c.circle(10.5, 10.5, 2, 'W'); c.circle(15.5, 15.5, 2, 'W'); c.circle(15.5, 10.5, 2, 'k')
    c.ellipse(21, 24, 7.5, 4.5, 'W')
    c.ellipse(21, 21, 7.5, 4.5, 'k')
    c.ellipse(19, 20, 3, 1.5, 's')
    c.outline()


@icon('org.kde.bovo', ['bovo'], 'games', 'Bovo')
def bovo(c):
    board(c, 'W')
    grid(c, 5, 5, 3, 5, 'w')
    c.line(6, 6, 9, 9, 'B'); c.line(9, 6, 6, 9, 'B')
    c.line(11, 11, 14, 14, 'B'); c.line(14, 11, 11, 14, 'B')
    c.ring(21, 21, 7.5, 4, 'R')
    c.arc(21, 21, 7, 4.5, 200, 250, 'r')
    c.outline()


@icon('org.kde.granatier', ['granatier'], 'games', 'Granatier')
def granatier(c):
    board(c, 'G')
    for x, y in [(7, 7), (13, 7), (7, 13)]:
        c.rect(x, y, x + 3, y + 3, 'S'); c.px(x, y, 'w')
    c.circle(20, 21, 7.5, 'k')
    c.rect(19, 12, 22, 14, 's')
    c.line(21, 11, 24, 7, 'N')
    c.px(25, 6, 'Y'); c.px(26, 5, 'O'); c.px(24, 5, 'O')
    c.circle(17.5, 18.5, 2, 's')
    c.outline()


@icon('org.kde.palapeli', ['palapeli'], 'games', 'Palapeli')
def palapeli(c):
    board(c, 'b')
    c.rect(5, 5, 12, 12, 'Y'); c.circle(15, 8.5, 2.2, 'Y')
    c.rect(14, 15, 24, 25, 'G')
    c.circle(19, 13.5, 2.5, 'G'); c.circle(25.5, 20, 2.5, 'G'); c.circle(19, 25.5, 2, '.')
    c.bevel(['G'])
    c.outline()


@icon('org.kde.picmi', ['picmi'], 'games', 'Picmi')
def picmi(c):
    board(c, 'W')
    pat = ["1001", "1111", "0110", "1001"]
    for j, r in enumerate(pat):
        for i, b in enumerate(r):
            c.rect(5 + i * 4, 5 + j * 4, 7 + i * 4, 7 + j * 4, 'k' if b == '1' else 'w')
    c.line(16, 25, 26, 15, 'Y', 3)
    c.px(15, 27, 'k'); c.px(16, 27, 'n'); c.px(15, 26, 'n')
    c.outline()


@icon('org.kde.kajongg', ['kajongg'], 'games', 'Kajongg')
def kajongg(c):
    board(c, 'G')
    tile(c, 6, 6, 12, 14, 'W', 'Y')
    c.px(9, 10, 'R')
    c.rect(15, 16, 27, 28, 'W')
    c.bevel(['W'])
    for x, y in [(18, 19), (24, 19), (21, 22), (18, 25), (24, 25)]:
        c.rect(x - 1, y - 1, x, y, 'R')
    c.outline()


@icon('org.kde.kubrick', ['kubrick'], 'games', 'Kubrick')
def kubrick(c):
    board(c, 'S')
    cols = ['R', 'Y', 'B', 'G', 'O', 'W', 'B', 'R', 'G']
    for j in range(3):
        for i in range(3):
            x, y = 14 + i * 5, 14 + j * 5
            c.rect(x, y, x + 3, y + 3, cols[j * 3 + i])
    c.rect(13, 13, 28, 28, 'k') if False else None
    c.outline()
    c.replace('.', 'K', (13, 13, 28, 28))
    c.replace('S', 'S')


@icon('org.kde.kiriki', ['kiriki'], 'games', 'Kiriki')
def kiriki(c):
    board(c, 'G')
    c.rect(6, 6, 13, 13, 'W')
    c.px(8, 8, 'k'); c.px(11, 11, 'k')
    c.rrect(15, 15, 28, 28, 'R', 2)
    c.bevel(['R'])
    for x, y in [(18, 18), (24, 18), (21, 21), (18, 24), (24, 24)]:
        c.rect(x - 1, y, x, y + 1, 'W')
    c.outline()


@icon('org.kde.lskat', ['lskat'], 'games', 'LSkat')
def lskat(c):
    board(c, 'B')
    c.poly([(10, 13), (18, 9), (25, 25), (16, 29)], 'W')
    card(c, 14, 13, 27, 28, 'k', SPADE)
    c.text(16, 15, 'K', 'k', font=3)
    c.outline()


@icon('org.kde.kdiamond', ['kdiamond'], 'games', 'KDiamond')
def kdiamond(c):
    board(c, 'k')
    for x, y, col in [(6, 6, 'R'), (11, 6, 'G'), (16, 6, 'Y'), (6, 11, 'B'), (11, 11, 'Y'), (6, 16, 'G')]:
        c.sprite(x, y, DIAMOND, {'#': col})
    c.poly([(13, 18), (17, 14), (25, 14), (29, 18), (21, 29)], 'C')
    c.poly([(13, 18), (29, 18), (21, 29)], '5')
    c.poly([(17, 14), (21, 18), (25, 14)], 'c')
    c.outline()


@icon('org.kde.ksnakeduel', ['ksnakeduel', 'ktron'], 'games', 'KSnakeDuel')
def ksnakeduel(c):
    board(c, 'k')
    c.hline(6, 15, 7, 'B'); c.vline(15, 7, 12, 'B'); c.hline(9, 15, 12, 'B')
    c.vline(6, 10, 19, 'R'); c.hline(6, 12, 19, 'R')
    c.rect(14, 15, 27, 18, 'G')
    c.rect(24, 15, 27, 28, 'G')
    c.rect(15, 24, 27, 27, 'G')
    c.bevel(['G'])
    c.rect(15, 15, 16, 16, 'k')
    c.outline()


@icon('org.kde.ktuberling', ['ktuberling'], 'games', 'KTuberling')
def ktuberling(c):
    board(c, 'C')
    c.ellipse(20, 20, 8.5, 9.5, 'N')
    c.bevel(['N'])
    c.circle(17, 17, 2, 'W'); c.circle(23, 17, 2, 'W')
    c.px(17, 17, 'k'); c.px(23, 17, 'k')
    c.ellipse(20, 23.5, 3, 1.5, 'R')
    c.px(15, 26, '8'); c.px(25, 13, '8')
    c.outline()


@icon('org.kde.kanagram', ['kanagram'], 'games', 'Kanagram')
def kanagram(c):
    board(c, 'B')
    c.rect(6, 6, 10, 10, 'W'); c.rect(12, 8, 16, 12, 'W')
    c.text(7, 7, 'A', 'k', font=3); c.text(13, 9, 'R', 'k', font=3)
    c.rrect(15, 15, 28, 28, 'Y', 1)
    c.bevel(['Y'])
    c.text(19, 18, 'G', '3')
    c.outline()


@icon('org.kde.khangman', ['khangman'], 'games', 'KHangMan')
def khangman(c):
    board(c, 'b')
    c.vline(7, 6, 19, 'N'); c.hline(7, 15, 6, 'N'); c.vline(15, 7, 9, 'k')
    c.circle(15.5, 11.5, 2, 'W')
    c.rrect(14, 17, 28, 28, 'W', 1)
    c.bevel(['W'])
    for x in (16, 20, 24):
        c.hline(x, x + 2, 26, 'k')
    c.text(16, 20, 'A', 'B', font=3)
    c.outline()


@icon('org.kde.blinken', ['blinken'], 'games', 'Blinken')
def blinken(c):
    board(c, 'k')
    for x, y, col in [(8, 8, 'R'), (16, 8, 'G')]:
        c.circle(x, y, 2.5, col)
    c.circle(20, 20, 8.5, 'k')
    c.arc(20, 20, 8, 2, 180, 270, 'R')
    c.arc(20, 20, 8, 2, 270, 360, 'G')
    c.arc(20, 20, 8, 2, 0, 90, 'B')
    c.arc(20, 20, 8, 2, 90, 180, 'Y')
    c.vline(19, 12, 27, 'k'); c.vline(20, 12, 27, 'k') if False else None
    c.circle(20, 20, 2.5, 's')
    c.outline()


@icon('org.kde.kbreakout', ['kbreakout'], 'games', 'KBreakout')
def kbreakout(c):
    board(c, 'k')
    for j, col in enumerate(['R', 'O', 'Y']):
        for i in range(4):
            c.rect(5 + i * 4, 5 + j * 3, 7 + i * 4, 6 + j * 3, col)
    ball(c, 21.5, 17.5, 3, 'W') if False else c.circle(20, 17, 2.5, 'W')
    c.rrect(10, 24, 28, 28, 'B', 2)
    c.bevel(['B'])
    c.outline()


@icon('org.kde.katomic', ['katomic'], 'games', 'KAtomic')
def katomic(c):
    board(c, 'B')
    c.line(13, 13, 22, 22, 'W', 2); c.line(22, 13, 22, 22, 'W', 2)
    ball(c, 10, 10, 3.5, 'R')
    c.circle(22.5, 12, 3, 'Y')
    ball(c, 22, 22, 6, 'G')
    c.outline()


@icon('org.kde.kblackbox', ['kblackbox'], 'games', 'KBlackBox')
def kblackbox(c):
    board(c, 'S')
    c.rect(13, 13, 28, 28, 'k')
    c.rect(13, 13, 28, 13, 's'); c.vline(13, 13, 28, 's')
    c.line(5, 9, 12, 9, 'R'); c.line(9, 5, 9, 12, 'Y')
    c.circle(20.5, 20.5, 3, 'R')
    c.px(19, 19, 'r')
    c.outline()


@icon('org.kde.kfourinline', ['kfourinline'], 'games', 'Four-in-a-Row')
def kfourinline(c):
    board(c, 'W')
    c.circle(8.5, 8.5, 2, 'R'); c.circle(13.5, 13.5, 2, 'Y')
    c.rect(12, 12, 28, 28, 'B')
    c.bevel(['B'])
    cols = ['.', 'R', 'Y', 'R', '.', 'Y', 'R', 'Y', 'R']
    for j in range(3):
        for i in range(3):
            c.circle(16 + i * 5, 16 + j * 5, 2, cols[j * 3 + i] if cols[j * 3 + i] != '.' else 'k')
    c.outline()


@icon('org.kde.killbots', ['killbots'], 'games', 'Killbots')
def killbots(c):
    board(c, 'G')
    grid(c, 5, 5, 3, 5, '4')
    c.vline(21, 11, 13, 'S'); c.circle(21, 10.5, 1.5, 'R')
    c.rrect(14, 14, 28, 28, 'S', 2)
    c.bevel(['S'])
    c.rect(16, 18, 26, 21, 'k')
    c.rect(17, 19, 18, 20, 'R'); c.rect(23, 19, 24, 20, 'R')
    c.hline(18, 24, 25, 'k')
    c.outline()


@icon('org.kde.kjumpingcube', ['kjumpingcube'], 'games', 'KJumpingCube')
def kjumpingcube(c):
    board(c, 'w')
    c.rect(6, 6, 11, 11, 'R'); c.rect(13, 6, 18, 11, 'B'); c.rect(6, 13, 11, 18, 'B')
    c.px(8, 8, 'W'); c.px(15, 8, 'W'); c.px(16, 9, 'W')
    c.rrect(14, 14, 28, 28, 'R', 1)
    c.bevel(['R'])
    for x, y in [(17, 17), (24, 17), (17, 24), (24, 24)]:
        c.rect(x, y, x + 1, y + 1, 'W')
    c.outline()


@icon('org.kde.klines', ['klines'], 'games', 'Kolor Lines')
def klines(c):
    board(c, 'S')
    grid(c, 5, 5, 3, 5, 's')
    for x, y, col in [(8, 8, 'G'), (13, 13, 'Y')]:
        c.circle(x, y, 2, col)
    for x, y, col in [(15, 25, 'R'), (21, 25, 'R'), (25, 19, 'B')]:
        ball(c, x, y, 3.5, col)
    c.outline()


@icon('org.kde.knavalbattle', ['knavalbattle', 'kbattleship'], 'games', 'Naval Battle')
def knavalbattle(c):
    board(c, 'B')
    grid(c, 5, 5, 3, 5, 'b')
    c.rect(11, 11, 14, 14, 'R')
    c.rect(18, 13, 19, 19, 'k'); c.rect(20, 15, 23, 19, 'S')
    c.poly([(9, 20), (29, 20), (26, 26), (12, 26)], 'S')
    c.bevel(['S'])
    c.hline(11, 27, 22, 'w')
    c.outline()


@icon('org.kde.knetwalk', ['knetwalk'], 'games', 'KNetWalk')
def knetwalk(c):
    board(c, 'k')
    c.hline(7, 18, 9, 'C'); c.vline(9, 9, 18, 'C'); c.vline(16, 9, 14, 'C')
    c.rect(8, 16, 10, 18, 'Y'); c.rect(15, 8, 17, 10, 'Y')
    c.rrect(14, 14, 28, 24, 'w', 1)
    c.bevel(['w'])
    c.rect(16, 16, 26, 22, 'B')
    c.rect(19, 25, 23, 26, 's'); c.rect(16, 27, 26, 28, 'S')
    c.outline()


@icon('org.kde.kolf', ['kolf'], 'games', 'Kolf')
def kolf(c):
    board(c, 'G')
    c.ellipse(16, 17, 3, 1.5, 'k')
    c.vline(15, 6, 16, 'W')
    c.poly([(16, 6), (21, 8), (16, 10)], 'R')
    c.circle(21, 22, 7, 'W')
    c.bevel(['W'])
    for x, y in [(19, 19), (23, 19), (21, 22), (18, 24), (24, 24)]:
        c.px(x, y, 'w')
    c.outline()


@icon('org.kde.konquest', ['konquest'], 'games', 'Konquest')
def konquest(c):
    board(c, 'k')
    for x, y in [(7, 14), (14, 6), (18, 11)]:
        c.px(x, y, 'W')
    c.circle(10, 9, 3, 'R')
    c.circle(21, 21, 7.5, 'B')
    c.bevel(['B'])
    c.poly([(17, 17), (22, 16), (20, 21), (16, 21)], 'G')
    c.poly([(22, 22), (25, 21), (25, 25), (22, 26)], 'G')
    c.outline()


@icon('org.kde.kshisen', ['kshisen'], 'games', 'Shisen-Sho')
def kshisen(c):
    board(c, 'G')
    tile(c, 5, 5, 10, 12, 'W', 'Y')
    c.circle(7.5, 8.5, 1.5, 'B')
    c.line(8, 14, 8, 20, 'R'); c.line(8, 20, 15, 20, 'R')
    tile(c, 15, 13, 26, 27, 'W', 'Y')
    c.circle(20.5, 20, 3.5, 'B')
    c.circle(20.5, 20, 1.5, 'W')
    c.outline()


@icon('org.kde.ksirk', ['ksirk'], 'games', 'KsirK')
def ksirk(c):
    board(c, 'b')
    c.poly([(6, 7), (12, 6), (13, 11), (9, 14), (6, 12)], 'G')
    c.poly([(14, 13), (19, 12), (19, 18), (15, 19)], 'O')
    c.vline(18, 9, 28, 'N')
    c.poly([(19, 9), (28.5, 12), (19, 16)], 'R')
    c.bevel(['R'])
    c.rrect(14, 26, 23, 28, 'S', 1)
    c.outline()


@icon('org.kde.kspaceduel', ['kspaceduel'], 'games', 'KSpaceDuel')
def kspaceduel(c):
    board(c, 'k')
    for x, y in [(7, 7), (12, 15), (17, 6), (6, 18)]:
        c.px(x, y, 'W')
    c.circle(12, 11, 2.5, 'Y')
    c.poly([(28.5, 12), (24, 24), (12, 28.5), (16, 20)], 'w')
    c.poly([(13, 23), (12, 18), (16, 20)], 'R')
    c.poly([(22, 28), (16, 26), (20, 23)], 'R')
    c.circle(22, 18, 2, 'B')
    c.bevel(['w'])
    c.outline()


@icon('org.kde.ksquares', ['ksquares'], 'games', 'KSquares')
def ksquares(c):
    board(c, 'W')
    for j in range(4):
        for i in range(4):
            c.px(6 + i * 4, 6 + j * 4, 'k')
    c.rect(6, 6, 10, 10, 'R') if False else c.frame(6, 6, 10, 10, 'R')
    c.rect(14, 14, 28, 28, 'B')
    c.bevel(['B'])
    c.frame(17, 17, 25, 25, 'W')
    for x, y in [(17, 17), (25, 17), (17, 25), (25, 25)]:
        c.rect(x - 1, y - 1, x + 1, y + 1, 'W')
    c.outline()


@icon('org.kde.ksokoban', ['ksokoban', 'org.kde.skladnik', 'skladnik'], 'games', 'Sokoban')
def ksokoban(c):
    board(c, 'S')
    for x, y in [(6, 6), (6, 10), (10, 6)]:
        c.rect(x, y, x + 2, y + 2, 'R')
    c.circle(15, 15, 1.5, 'Y')
    c.rect(14, 14, 28, 28, 'O')
    c.bevel(['O'])
    c.frame(16, 16, 26, 26, '2')
    c.line(16, 16, 26, 26, '2'); c.line(26, 16, 16, 26, '2')
    c.outline()


@icon('org.kde.kigo', ['kigo'], 'games', 'Kigo')
def kigo(c):
    board(c, 'O')
    grid(c, 5, 5, 3, 5, '2')
    c.circle(10.5, 10.5, 2, 'k'); c.circle(15.5, 10.5, 2, 'W')
    c.ellipse(21, 22, 7.5, 6, 'W')
    c.ellipse(19, 20, 3, 2, 'W')
    c.bevel(['W'])
    c.ellipse(13.5, 17, 4, 3.5, 'k') if False else None
    c.outline()


@icon('org.kde.bomber', ['bomber'], 'games', 'Bomber')
def bomber(c):
    board(c, 'b')
    for x, h in [(5, 6), (9, 10), (13, 4), (17, 8)]:
        c.rect(x, 21 - h, x + 2, 20, 'S')
    c.poly([(12, 22), (26, 20), (29, 23), (26, 26), (12, 25)], 'R')
    c.poly([(18, 21), (22, 16), (24, 16), (23, 21)], '1')
    c.poly([(12, 21), (14, 18), (15, 22)], 'R')
    c.bevel(['R'])
    c.outline()


@icon('org.kde.kbackgammon', ['kbackgammon'], 'games', 'KBackgammon')
def kbackgammon(c):
    board(c, 'W')
    for i in range(4):
        x = 5 + i * 4
        c.poly([(x, 5), (x + 3, 5), (x + 1.5, 12)], 'R' if i % 2 else 'k')
        c.poly([(x, 21), (x + 3, 21), (x + 1.5, 14)], 'k' if i % 2 else 'R')
    c.ellipse(21, 23, 7, 3.5, 'k')
    c.ellipse(21, 20.5, 7, 3.5, 'R')
    c.ellipse(19, 19.5, 3, 1.2, 'r')
    c.outline()
