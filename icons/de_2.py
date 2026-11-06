"""KDE Gear applications (part 2): education, science, development, utilities."""
from pix import icon


def page(c, x0, y0, x1, y1, col='W', fold=5, fcol='w'):
    c.rect(x0, y0, x1, y1, col)
    for i in range(fold):
        c.hline(x1 - fold + 1 + i, x1, y0 + i, '.')
    for i in range(fold):
        c.hline(x1 - fold + 1, x1 - fold + 1 + i, y0 + i, fcol)


def window(c, x0, y0, x1, y1, bar='B', body='W'):
    c.rect(x0, y0, x1, y1, body)
    c.rect(x0, y0, x1, y0 + 3, bar)
    c.bevel([bar])


def magnifier(c, cx, cy, r, glass='c'):
    c.line(cx + r - 1, cy + r - 1, cx + r + 4, cy + r + 4, 'N', 3)
    c.circle(cx, cy, r + 1.5, 'S')
    c.circle(cx, cy, r, glass)
    c.arc(cx, cy, r - 1, r - 2.5, 200, 250, 'W')


# ================================================================== utilities
@icon('org.kde.kfind', ['kfind'], 'utilities', 'KFind')
def kfind(c):
    c.rrect(3, 5, 13, 9, 'O', 1)
    c.rect(3, 7, 26, 24, 'O')
    c.rect(3, 11, 26, 24, 'Y')
    c.bevel(['Y'])
    c.hline(3, 26, 11, 'y')
    c.line(22, 22, 26, 26, 'N', 3)
    c.circle(19, 19, 6.5, 'S')
    c.circle(19, 19, 5, 'c')
    c.arc(19, 19, 4, 2.5, 200, 250, 'W')
    c.outline()


@icon('org.kde.kronometer', ['kronometer'], 'utilities', 'Kronometer')
def kronometer(c):
    c.rect(14, 3, 17, 5, 'S')
    c.rect(12, 3, 19, 3, 'w')
    c.line(24, 6, 26, 8, 'S', 2)
    c.circle(16, 17, 11.5, 'W')
    c.bevel(['W'])
    c.ring(16, 17, 11.5, 10, 'S')
    c.arc(16, 17, 8, 0, 270, 340, 'b')
    c.vline(16, 10, 17, 'k')
    c.line(16, 17, 21, 12, 'R')
    c.px(16, 17, 'k')
    c.outline()


@icon('org.kde.ktimer', ['ktimer'], 'utilities', 'KTimer')
def ktimer(c):
    # hourglass
    c.rrect(6, 3, 25, 5, 'N', 1)
    c.rrect(6, 26, 25, 28, 'N', 1)
    c.poly([(8, 6), (24, 6), (24, 8), (17.5, 16), (24, 24), (24, 26), (8, 26), (8, 24), (14.5, 16), (8, 8)], 'c')
    c.poly([(11, 10), (21, 10), (16, 15)], 'Y')
    c.poly([(16, 19), (21.5, 25.5), (10.5, 25.5)], 'Y')
    c.vline(16, 15, 21, 'Y')
    c.bevel(['N'])
    c.vline(9, 7, 9, 'W')
    c.outline()


@icon('org.kde.kalarm', ['kalarm'], 'utilities', 'KAlarm')
def kalarm(c):
    c.circle(8, 8.5, 4.5, 'R'); c.circle(24, 8.5, 4.5, 'R')
    c.line(8, 25, 6, 27, 's', 2); c.line(23, 25, 25, 27, 's', 2)
    c.circle(16, 17, 10.5, 'R')
    c.bevel(['R'])
    c.circle(16, 17, 8, 'W')
    c.vline(16, 11, 17, 'k'); c.hline(16, 20, 17, 'k')
    c.rect(15, 4, 16, 6, 's')
    c.outline()


@icon('org.kde.kteatime', ['kteatime'], 'utilities', 'KTeaTime')
def kteatime(c):
    # teapot: body, spout, handle, lid knob
    c.poly([(3, 12), (6, 12), (10, 18), (8, 20)], 'G')
    c.arc(24, 18, 5.5, 3, 270, 90, 'G')
    c.ellipse(16, 19, 9, 8, 'G')
    c.rect(7, 24, 25, 26, 'G')
    c.ellipse(16, 11, 6, 2.5, 'g')
    c.rect(15, 6, 17, 9, 'g')
    c.bevel(['G'])
    c.hline(9, 23, 21, '4')
    c.outline()


@icon('org.kde.kweather', ['kweather'], 'utilities', 'KWeather')
def kweather(c):
    c.circle(20, 10, 6.5, 'Y')
    c.bevel(['Y'])
    c.circle(9, 15, 5, 'W'); c.circle(16, 12, 6, 'W'); c.circle(23, 16, 4, 'W')
    c.rrect(4, 14, 27, 20, 'W', 3)
    c.bevel(['W'])
    for x, y in [(8, 23), (14, 24), (20, 23), (11, 27), (17, 28), (23, 27)]:
        c.vline(x, y, y + 1, 'B')
    c.outline()


@icon('org.kde.francis', ['francis'], 'utilities', 'Francis')
def francis(c):
    # pomodoro tomato
    c.ellipse(16, 18, 12.5, 10.5, 'R')
    c.bevel(['R'])
    c.sprite(9, 5, """
        ......##......
        ......##......
        .###.####.###.
        ..##########..
        ...##.##.##...
        ...#..#...#...
    """, {'#': 'G'})
    c.px(9, 13, 'r'); c.px(8, 14, 'r')
    c.outline()


@icon('org.kde.knotes', ['knotes'], 'utilities', 'KNotes')
def knotes(c):
    c.rect(4, 4, 27, 27, 'Y')
    for i in range(7):
        c.hline(27 - 6 + i, 27, 27 - 6 + i, '.') if False else None
    c.poly([(20, 28), (28, 20), (28, 28)], '.')
    c.poly([(20, 28), (21, 21), (28, 20)], '3')
    c.bevel(['Y'])
    c.rect(4, 4, 27, 7, 'O')
    for y in (11, 14, 17):
        c.hline(7, 23, y, '3')
    c.outline()


@icon('org.kde.keysmith', ['keysmith'], 'system', 'Keysmith')
def keysmith(c):
    c.circle(10, 10, 7.5, 'Y')
    c.circle(10, 10, 2.5, '.')
    c.line(14, 14, 26, 26, 'Y', 3)
    c.rect(19, 23, 21, 26, 'Y'); c.rect(23, 21, 25, 24, 'Y') if False else c.rect(23, 19, 26, 21, 'Y')
    c.bevel(['Y'])
    c.outline()


@icon('org.kde.kgpg', ['kgpg'], 'system', 'KGpg')
def kgpg(c):
    c.arc(16, 12, 8, 5, 180, 360, 'S')
    c.rect(8, 12, 10, 14, 'S'); c.rect(21, 12, 23, 14, 'S')
    c.rrect(4, 14, 27, 28, 'Y', 2)
    c.bevel(['Y', 'S'])
    c.circle(16, 20, 2.5, 'k')
    c.rect(15, 21, 16, 25, 'k')
    c.outline()


@icon('org.kde.kdf', ['kdf', 'kwikdisk'], 'system', 'KDiskFree')
def kdf(c):
    c.rrect(3, 15, 28, 27, 'S', 2)
    c.bevel(['S'])
    c.rect(6, 23, 16, 24, 's')
    c.px(24, 23, 'G')
    c.circle(16, 10, 7.5, 'W')
    c.arc(16, 10, 7.5, 0, 270, 30, 'G')
    c.ring(16, 10, 7.5, 6.5, 'w')
    c.outline()


@icon('org.kde.krename', ['krename'], 'utilities', 'KRename')
def krename(c):
    page(c, 4, 3, 22, 28, 'W', 5)
    c.bevel(['W'])
    c.text(7, 9, 'A', 'B')
    c.text(13, 17, 'B', 'G')
    c.line(9, 17, 11, 19, 'S')
    # pencil
    c.line(18, 25, 27, 16, 'O', 3)
    c.line(19, 26, 28, 17, 'o') if False else None
    c.px(17, 27, 'k'); c.px(18, 27, 'n'); c.px(17, 26, 'n')
    c.outline()


@icon('org.kde.isoimagewriter', ['isoimagewriter'], 'system', 'ISO Image Writer')
def isoimagewriter(c):
    c.rrect(14, 4, 28, 18, 'w', 1)
    c.rect(17, 7, 19, 9, 'k'); c.rect(23, 7, 25, 9, 'k')
    c.rrect(10, 14, 28, 28, 'B', 2) if False else c.rrect(12, 15, 28, 28, 'B', 2)
    c.circle(10, 18, 7.5, 'W')
    c.arc(10, 18, 7, 2, 200, 250, 'c')
    c.circle(10, 18, 2, 'S')
    c.bevel(['B'])
    c.outline()


@icon('org.kde.kmenuedit', ['kmenuedit'], 'system', 'Menu Editor')
def kmenuedit(c):
    c.rrect(3, 3, 21, 28, 'W', 1)
    c.bevel(['W'])
    for i, col in enumerate(['B', 'G', 'O', 'M', 'R']):
        y = 6 + i * 4
        c.rect(5, y, 7, y + 2, col)
        c.hline(9, 18, y + 1, 'S')
    c.line(16, 25, 25, 16, 'Y', 3)
    c.px(15, 27, 'k'); c.px(16, 27, 'n'); c.px(15, 26, 'n')
    c.outline()


@icon('org.kde.khelpcenter', ['khelpcenter', 'help-browser', 'help-contents'], 'system', 'Help Center')
def khelpcenter(c):
    c.rrect(5, 3, 26, 28, 'B', 1)
    c.bevel(['B'])
    c.rect(5, 25, 26, 28, 'W')
    c.hline(5, 26, 25, 'w')
    c.vline(7, 3, 24, '6')
    c.sprite(12, 7, """
        .####.
        ##..##
        ....##
        ...##.
        ..##..
        ......
        ..##..
    """, {'#': 'W'})
    c.outline()


# ================================================================== development


# ================================================================== science / maths
@icon('org.kde.kig', ['kig'], 'education', 'Kig')
def kig(c):
    c.poly([(4, 27), (27, 27), (13, 6)], 'b')
    c.poly([(8, 25), (23, 25), (13.5, 11)], 'W')
    c.circle(16, 16, 9, '.') if False else None
    c.ring(16, 18, 10.5, 9.5, 'B')
    c.bevel(['b'])
    for x, y in [(4, 26), (26, 26), (13, 6)]:
        c.rect(x - 1, y - 1, x + 1, y + 1, 'R')
    c.outline()


@icon('org.kde.kalgebra', ['kalgebra', 'kalgebramobile', 'org.kde.kalgebramobile'], 'education', 'KAlgebra')
def kalgebra(c):
    # wireframe cube on 3D axes
    c.poly([(3, 11), (11, 3), (29, 3), (29, 21), (21, 29), (3, 29)], 'b')
    c.rect(3, 11, 20, 28, 'B')
    c.poly([(3, 11), (11, 3), (29, 3), (21, 11)], 'c')
    c.poly([(21, 11), (29, 3), (29, 21), (21, 29)], '6')
    c.bevel(['B'])
    c.outline()


@icon('org.kde.kmplot', ['kmplot'], 'education', 'KmPlot')
def kmplot(c):
    c.rect(3, 4, 28, 27, 'W')
    c.bevel(['W'])
    for x in range(6, 28, 4):
        c.vline(x, 5, 26, 'w')
    for y in range(7, 27, 4):
        c.hline(4, 27, y, 'w')
    c.vline(15, 5, 26, 'S'); c.hline(4, 27, 19, 'S')
    import math as m
    prev = None
    for x in range(4, 28):
        y = round(19 - 0.075 * (x - 15.5) ** 2 * -1 - 12 + 12) if False else round(25 - 0.085 * (x - 15.5) ** 2 * -1 - 18)
        y = round(8 + 0.1 * (x - 15.5) ** 2)
        if 5 <= y <= 26:
            c.rect(x, y, x, y + 1, 'R')
    c.outline()


@icon('org.kde.kgeography', ['kgeography'], 'education', 'KGeography')
def kgeography(c):
    # desk globe on an arm and stand
    c.arc(15, 14, 12, 10.5, 30, 230, 'Y')
    c.circle(15, 14, 9, 'B')
    c.bevel(['B'])
    c.poly([(9, 8), (14, 7), (15, 12), (11, 15), (8, 13)], 'G')
    c.poly([(17, 15), (22, 13), (22, 19), (18, 21)], 'G')
    c.rect(14, 24, 16, 26, 'Y')
    c.rrect(8, 26, 22, 28, 'N', 1)
    c.outline()


@icon('org.kde.step', ['step'], 'education', 'Step')
def step(c):
    c.rect(3, 3, 28, 5, 'N')
    c.bevel(['N'])
    c.line(16, 6, 22, 19, 'S')
    c.line(9, 6, 9, 19, 'w') if False else None
    c.circle(22.5, 21.5, 5, 'R')
    c.bevel(['R'])
    c.px(20, 19, 'r')
    for i, (x, y) in enumerate([(9, 21), (6, 18)]):
        c.circle(x, y, 2 - i * 0.5, 'w')
    c.outline()


@icon('org.kde.cantor', ['cantor'], 'education', 'Cantor')
def cantor(c):
    window(c, 3, 4, 28, 27, 'M', 'k')
    c.sprite(9, 11, """
        ##########
        ##......##
        .##.......
        ..##......
        ...##.....
        ..##......
        .##.......
        ##......##
        ##########
    """, {'#': 'W'})
    c.rect(21, 18, 25, 19, 'g')
    c.outline()


@icon('org.kde.kbruch', ['kbruch'], 'education', 'KBruch')
def kbruch(c):
    c.circle(15, 17, 11.5, 'O')
    c.arc(15, 17, 11.5, 0, 270, 360, '.')
    c.bevel(['O'])
    c.poly([(17, 15), (17, 3.5), (28.5, 15)], 'Y')
    c.bevel(['Y'])
    c.outline()


# ================================================================== learning
@icon('org.kde.kturtle', ['kturtle'], 'education', 'KTurtle')
def kturtle(c):
    for x, y in [(8, 10), (24, 10), (8, 22), (24, 22)]:
        c.circle(x, y, 3, 'g')
    c.circle(16, 5.5, 3, 'g')
    c.px(16, 26, 'g'); c.px(16, 27, 'g')
    c.ellipse(16, 16, 9.5, 10, 'G')
    c.bevel(['G'])
    c.sprite(12, 10, """
        ..##..
        .#..#.
        #....#
        #....#
        .#..#.
        ..##..
    """, {'#': '4'})
    c.hline(10, 13, 16, '4'); c.hline(18, 21, 16, '4') if False else None
    c.px(14, 4, 'k'); c.px(17, 4, 'k')
    c.outline()


@icon('org.kde.ktouch', ['ktouch'], 'education', 'KTouch')
def ktouch(c):
    c.rrect(3, 9, 28, 24, 'S', 1)
    c.bevel(['S'])
    for j, (y, off) in enumerate([(11, 5), (15, 6), (19, 7)]):
        for i in range(6):
            c.rect(off + i * 3 + j, y, off + i * 3 + j + 1, y + 2, 'W')
    c.rect(9, 22, 22, 22, 'W') if False else None
    c.rect(11, 19, 20, 21, 'W')
    c.rect(14, 15, 15, 17, 'B')
    c.outline()


@icon('org.kde.parley', ['parley'], 'education', 'Parley')
def parley(c):
    c.poly([(9, 3), (28.5, 6), (26, 22), (7, 19)], 'B')
    c.bevel(['B'])
    c.rrect(3, 10, 23, 27, 'W', 1)
    c.bevel(['W'])
    c.text(6, 14, 'A', 'R')
    c.sprite(13, 16, """
        ....
        .##.
        ...#
        .###
        #..#
        .###
    """, {'#': 'R'})
    c.outline()


@icon('org.kde.kwordquiz', ['kwordquiz'], 'education', 'KWordQuiz')
def kwordquiz(c):
    c.rrect(3, 3, 28, 22, 'O', 3)
    c.poly([(8, 21), (14, 21), (7, 28.5)], 'O')
    c.bevel(['O'])
    c.sprite(12, 6, """
        .####.
        ##..##
        ....##
        ...##.
        ..##..
        ......
        ..##..
    """, {'#': 'W'})
    c.outline()


@icon('org.kde.artikulate', ['artikulate'], 'education', 'Artikulate')
def artikulate(c):
    # lips
    c.ellipse(16, 16, 13, 7.5, 'R')
    c.bevel(['R'])
    c.ellipse(16, 16.5, 9, 2.5, 'k')
    c.rect(9, 15, 23, 15, 'W')
    c.px(16, 9, '.'); c.px(15, 9, '1'); c.px(16, 10, '1') if False else c.px(16, 9, 'K')
    c.outline()


@icon('org.kde.gcompris', ['gcompris', 'gcompris-qt', 'net.gcompris.gcompris'], 'education', 'GCompris')
def gcompris(c):
    def blk(x, y, col, ch):
        c.rect(x, y, x + 11, y + 11, col)
        c.bevel([col])
        c.text(x + 3, y + 2, ch, 'W', font=5)
    blk(3, 17, 'R', 'A')
    blk(17, 17, 'B', 'B')
    blk(10, 4, 'G', 'C')
    c.outline()


@icon('org.kde.minuet', ['minuet'], 'education', 'Minuet')
def minuet(c):
    # piano keyboard
    c.rect(3, 7, 28, 25, 'W')
    c.bevel(['W'])
    c.rect(3, 7, 28, 9, 'M')
    for x in range(7, 28, 4):
        c.vline(x, 10, 25, 'S')
    for x in (5, 9, 17, 21, 25):
        c.rect(x, 10, x + 2, 18, 'k')
    c.outline()


@icon('org.kde.kiten', ['kiten'], 'education', 'Kiten')
def kiten(c):
    c.rrect(5, 3, 26, 28, 'R', 1)
    c.bevel(['R'])
    c.rect(5, 25, 26, 28, 'W')
    c.sprite(10, 7, """
        ##########..
        #........#..
        #........#..
        ##########..
        #........#..
        #........#..
        ##########..
    """, {'#': 'W'})
    c.rect(10, 7, 11, 13, 'W'); c.rect(18, 7, 19, 13, 'W')
    c.hline(10, 19, 8, 'W'); c.hline(10, 19, 12, 'W')
    c.outline()


@icon('org.kde.arianna', ['arianna'], 'office', 'Arianna')
def arianna(c):
    # open book
    c.poly([(3, 8), (15, 9), (15, 27), (3, 25)], 'W')
    c.poly([(17, 9), (29, 8), (29, 25), (17, 27)], 'W')
    c.rect(15, 9, 16, 27, 'S')
    c.poly([(3, 25), (15, 27), (17, 27), (29, 25), (29, 27), (17, 29), (15, 29), (3, 27)], 'B')
    for y in (12, 15, 18, 21):
        c.line(5, y, 13, y + 1, 'w'); c.line(18, y + 1, 26, y, 'w')
    c.outline()


@icon('org.kde.peruse', ['peruse'], 'office', 'Peruse')
def peruse(c):
    c.rect(5, 3, 26, 28, 'W')
    c.bevel(['W'])
    c.rect(7, 5, 15, 14, 'Y'); c.rect(17, 5, 24, 14, 'b'); c.rect(7, 16, 24, 26, 'R')
    c.rrect(9, 18, 19, 22, 'W', 1)
    c.px(11, 23, 'W')
    c.outline()


@icon('org.kde.koko', ['koko'], 'media', 'Koko')
def koko(c):
    c.poly([(3, 9), (19, 4), (23, 18), (7, 23)], 'w')
    c.rect(9, 10, 28, 27, 'W')
    c.rect(11, 12, 26, 23, 'C')
    c.circle(22, 15.5, 1.5, 'W')
    c.poly([(11, 23.5), (16, 16), (21, 23.5)], '5')
    c.bevel(['W'])
    c.outline()


@icon('org.kde.tellico', ['tellico'], 'office', 'Tellico')
def tellico(c):
    # books on a shelf
    for x0, w, h, col in [(4, 4, 18, 'R'), (9, 3, 21, 'B'), (13, 5, 17, 'G'), (19, 3, 20, 'Y')]:
        c.rect(x0, 25 - h, x0 + w - 1, 24, col)
        c.hline(x0, x0 + w - 1, 25 - h + 3, 'W')
    c.poly([(22, 9), (25, 8), (28.5, 24.5), (25.5, 25)], 'C')
    c.rect(3, 25, 28, 27, 'N')
    c.bevel(['N'])
    c.outline()


@icon('org.kde.merkuro.contact', ['merkuro-contact'], 'office', 'Merkuro Contacts')
def merkuro_contact(c):
    c.rrect(3, 6, 28, 26, 'C', 2)
    c.bevel(['C'])
    c.circle(11, 13, 3.5, 'W')
    c.rrect(5, 17, 17, 23, 'W', 2)
    for y in (11, 15, 19):
        c.hline(19, 25, y, '5')
    c.outline()
