"""KDE Gear applications (part 1): graphics, internet, multimedia, office."""
from pix import icon
import math


def play(c, x, y, h, col):
    m = h // 2
    for j in range(h):
        c.hline(x, x + (m - abs(j - m)), y + j, col)


def page(c, x0, y0, x1, y1, col='W', fold=5, fcol='w'):
    """Paper sheet with a dog-eared top-right corner."""
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


# ================================================================== graphics


@icon('org.kde.kolorchooser', ['org.kde.kcolorchooser'], 'media', 'KColorChooser')
def kcolorchooser(c):
    cols = ['R', 'O', 'Y', 'G', 'C', 'B', 'M', 'P']
    for i, col in enumerate(cols):
        c.arc(16, 16, 12.5, 4, i * 45 - 90, i * 45 - 45, col)
    c.circle(16, 16, 4, 'W')
    c.circle(16, 16, 2, 'w')
    c.outline()


@icon('org.kde.kruler', ['kruler'], 'utilities', 'KRuler')
def kruler(c):
    c.poly([(3, 21), (21, 3), (28.5, 10.5), (10.5, 28.5)], 'Y')
    c.bevel(['Y'])
    for i in range(0, 15, 2):
        x, y = 6 + i, 21 - i
        ln = 3 if i % 4 == 0 else 2
        for k in range(ln):
            c.px(x + k, y + k, '3')
    c.outline()


@icon('org.kde.kmag', ['kmag'], 'utilities', 'KMag')
def kmag(c):
    c.line(19, 19, 25, 25, 'N', 4)
    c.line(20, 20, 26, 26, 'n')
    c.circle(13, 13, 10.5, 'S')
    c.bevel(['S'])
    c.circle(13, 13, 8.5, 'b')
    # magnified pixels
    for (x, y, col) in [(9, 9, 'R'), (13, 9, 'Y'), (9, 13, 'G'), (17, 13, 'R'), (13, 17, 'Y')]:
        c.rect(x, y, x + 3, y + 3, col)
    c.arc(13, 13, 7.5, 6, 200, 250, 'W')
    c.outline()


@icon('org.kde.skanlite', ['skanlite'], 'utilities', 'Skanlite')
def skanlite(c):
    # flatbed scanner, lid propped open
    c.poly([(5, 13), (8, 4), (28, 4), (26, 13)], 'S')
    c.bevel(['S'])
    c.rrect(3, 14, 28, 25, 'w', 1)
    c.bevel(['w'])
    c.rect(5, 15, 26, 18, 'k')
    c.hline(6, 25, 16, 'g'); c.hline(6, 25, 17, 'G')
    c.rect(5, 21, 8, 22, 's')
    c.px(25, 22, 'G')
    c.outline()


@icon('org.kde.skanpage', ['skanpage'], 'utilities', 'Skanpage')
def skanpage(c):
    page(c, 7, 3, 24, 18, 'W', 4)
    for y in (8, 11, 14):
        c.hline(10, 21, y, 'b')
    c.rrect(3, 16, 28, 27, 'B', 1)
    c.bevel(['B'])
    c.rect(5, 18, 26, 20, 'k')
    c.hline(6, 25, 19, 'c')
    c.rect(5, 23, 9, 24, '6')
    c.outline()


# ================================================================== internet


@icon('org.kde.akregator', ['akregator'], 'web', 'Akregator')
def akregator(c):
    # newspaper with an RSS wave
    c.rect(3, 6, 25, 26, 'W')
    c.rect(25, 10, 28, 26, 'w')
    c.bevel(['W'])
    c.rect(6, 9, 22, 11, 'k')
    c.circle(9, 22, 2, 'O')
    c.arc(8, 23, 7, 5, 270, 360, 'O')
    c.arc(8, 23, 11, 9, 270, 360, 'O')
    c.rect(15, 14, 22, 15, 'S'); c.rect(18, 18, 22, 19, 'S')
    c.outline()


@icon('org.kde.itinerary', ['itinerary', 'kde-itinerary'], 'office', 'Itinerary')
def itinerary(c):
    # boarding pass with a perforated stub
    c.rect(3, 7, 28, 24, 'B')
    c.bevel(['B'])
    c.rect(21, 7, 28, 24, 'b')
    for y in range(8, 24, 2):
        c.px(20, y, 'W')
    c.circle(3, 15.5, 2, '.'); c.circle(29, 15.5, 2, '.')
    c.sprite(7, 11, """
        ...#....
        ...##...
        #######.
        ########
        #######.
        ...##...
        ...#....
    """, {'#': 'W'})
    c.rect(23, 11, 26, 12, '6'); c.rect(23, 15, 25, 16, '6'); c.rect(23, 19, 26, 20, '6')
    c.outline()


@icon('org.kde.kongress', ['kongress'], 'office', 'Kongress')
def kongress(c):
    # conference badge on a lanyard
    c.line(9, 4, 12, 9, 'R', 2)
    c.line(22, 4, 19, 9, 'R', 2)
    c.rrect(6, 9, 25, 29, 'W', 2)
    c.bevel(['W'])
    c.rect(13, 10, 18, 11, 's')
    c.rect(6, 13, 25, 16, 'R')
    c.circle(15.5, 21, 2.5, 'S')
    c.rect(11, 25, 20, 26, 'S')
    c.outline()


@icon('org.kde.krfb', ['krfb'], 'system', 'Desktop Sharing')
def krfb(c):
    c.rrect(3, 4, 28, 21, 'S', 1)
    c.bevel(['S'])
    c.rect(5, 6, 26, 19, 'B')
    c.rect(5, 6, 26, 7, 'b')
    c.rect(13, 22, 18, 24, 's')
    c.rect(8, 25, 23, 26, 'S')
    # share arrow
    c.sprite(10, 9, """
        .......##..
        ......####.
        #########..
        ##.....#...
        ##.........
        ##.........
        ##########.
    """, {'#': 'W'})
    c.outline()


# ================================================================== multimedia
@icon('org.kde.juk', ['juk'], 'media', 'JuK')
def juk(c):
    # jukebox: arched top, glowing window, speaker grille
    c.rect(5, 12, 26, 28, 'N')
    c.ellipse(15.5, 13, 10.5, 10, 'N')
    c.bevel(['N'])
    c.ellipse(15.5, 13, 7.5, 7, 'O')
    c.rect(8, 13, 23, 16, 'O')
    c.ellipse(15.5, 13, 5.5, 5, 'Y')
    c.rect(10, 13, 21, 16, 'Y')
    c.ellipse(15.5, 13, 3.5, 3, 'y')
    c.rect(9, 19, 22, 26, '8')
    for x in range(10, 22, 2):
        c.vline(x, 20, 25, 'n')
    c.outline()


@icon('org.kde.kmix', ['kmix'], 'media', 'KMix')
def kmix(c):
    # mixing desk: three faders
    c.rrect(3, 5, 28, 27, 'S', 1)
    c.bevel(['S'])
    for i, (x, y, col) in enumerate([(8, 15, 'G'), (15, 9, 'Y'), (22, 19, 'R')]):
        c.rect(x, 8, x + 1, 24, 'k')
        c.rect(x - 2, y, x + 3, y + 2, col)
        c.hline(x - 2, x + 3, y, {'G': 'g', 'Y': 'y', 'R': 'r'}[col])
    c.outline()


@icon('org.kde.kamoso', ['kamoso'], 'media', 'Kamoso')
def kamoso(c):
    # webcam ball on a stand
    c.rrect(9, 25, 22, 28, 'S', 1)
    c.rect(14, 20, 17, 25, 's')
    c.circle(16, 13, 9.5, 'W')
    c.bevel(['W'])
    c.circle(16, 13, 6, 'k')
    c.circle(16, 13, 4, 'B')
    c.circle(16, 13, 2, '6')
    c.px(14, 11, 'W'); c.px(15, 11, 'b')
    c.px(23, 8, 'R')
    c.outline()


@icon('org.kde.plasmatube', ['plasmatube'], 'media', 'PlasmaTube')
def plasmatube(c):
    # cathode-ray tube TV with a play glyph
    c.line(10, 3, 14, 7, 's'); c.line(22, 3, 18, 7, 's')
    c.rrect(3, 7, 28, 25, 'R', 2)
    c.bevel(['R'])
    c.rrect(5, 9, 21, 23, 'k', 2)
    play(c, 11, 12, 9, 'W')
    c.circle(24.5, 12, 1.5, '1'); c.circle(24.5, 17, 1.5, '1')
    c.rect(6, 26, 8, 27, 's'); c.rect(23, 26, 25, 27, 's')
    c.outline()


@icon('org.kde.kwave', ['kwave'], 'media', 'Kwave')
def kwave(c):
    c.rrect(3, 5, 28, 26, 'k', 2)
    c.hline(5, 26, 15, 's')
    hs = [1, 3, 6, 9, 5, 2, 7, 10, 8, 4, 2, 6, 9, 5, 3, 1, 4, 7, 3, 1]
    for i, h in enumerate(hs):
        x = 6 + i
        c.vline(x, 15 - h, 15 + h, 'C' if i % 2 else 'c')
    c.outline()


@icon('org.kde.k3b', ['k3b'], 'media', 'K3b')
def k3b(c):
    c.circle(16, 16, 12.5, 'w')
    c.arc(16, 16, 12, 4, 200, 260, 'W')
    c.arc(16, 16, 12, 4, 20, 80, 'S')
    c.arc(16, 16, 10, 7, 290, 340, 'c')
    c.circle(16, 16, 4, 'S')
    c.circle(16, 16, 2, '.')
    # flame
    c.poly([(20, 29), (19, 23), (22, 19), (23, 22), (26, 17), (28.5, 24), (27, 29)], 'O')
    c.poly([(21.5, 29), (22, 25), (24, 23), (25.5, 26), (25.5, 29)], 'Y')
    c.outline()


@icon('org.kde.amarok', ['amarok'], 'media', 'Amarok')
def amarok(c):
    # wolf head in profile on a blue disc
    c.circle(16, 16, 12.5, 'B')
    c.bevel(['B'])
    c.poly([(8, 25), (9, 14), (11, 7), (14, 11), (17, 9), (19, 5), (21, 11), (27, 17),
            (24, 19), (19, 18), (18, 25)], 'W')
    c.replace('W', '.', (0, 0, 31, 0))
    c.px(19, 13, 'k')
    c.hline(23, 26, 17, 'w')
    c.outline()


# ================================================================== office
def calligra_doc(c, col, glyph):
    page(c, 5, 3, 26, 28, 'W', 6)
    c.rect(5, 23, 20, 28, col)
    c.rect(5, 23, 20, 23, {'B': 'b', 'G': 'g', 'O': 'o', 'M': 'm', 'R': 'r'}[col])
    glyph()


@icon('calligrawords', ['org.kde.calligrawords', 'calligra-words'], 'office', 'Calligra Words')
def calligrawords(c):
    def g():
        for y in (10, 13, 16, 19):
            c.hline(8, 23 if y != 19 else 17, y, 'S')
        c.hline(8, 17, 7, 'B')
    calligra_doc(c, 'B', g)
    c.outline()


@icon('calligrasheets', ['org.kde.calligrasheets', 'calligra-sheets'], 'office', 'Calligra Sheets')
def calligrasheets(c):
    def g():
        c.rect(8, 9, 23, 20, 'w')
        for x in (8, 13, 18, 23):
            c.vline(x, 9, 20, 'G')
        for y in (9, 13, 17, 20):
            c.hline(8, 23, y, 'G')
    calligra_doc(c, 'G', g)
    c.outline()


@icon('calligrastage', ['org.kde.calligrastage', 'calligra-stage'], 'office', 'Calligra Stage')
def calligrastage(c):
    def g():
        c.rect(8, 9, 23, 19, 'o')
        c.rect(10, 15, 11, 17, 'O'); c.rect(14, 13, 15, 17, 'O'); c.rect(18, 11, 19, 17, 'O')
    calligra_doc(c, 'O', g)
    c.outline()


@icon('karbon', ['org.kde.karbon', 'calligrakarbon'], 'office', 'Karbon')
def karbon(c):
    # vector pen nib with bezier handles
    c.line(4, 24, 27, 24, 's')
    c.rect(3, 23, 5, 25, 'W'); c.rect(26, 23, 28, 25, 'W')
    c.poly([(16, 3), (24, 13), (19, 26), (13, 26), (8, 13)], 'M')
    c.bevel(['M'])
    c.vline(16, 9, 19, '7')
    c.circle(16, 15, 1.5, 'W')
    c.outline()


@icon('calligraplan', ['org.kde.calligraplan', 'calligra-plan'], 'office', 'Calligra Plan')
def calligraplan(c):
    c.rrect(3, 5, 28, 26, 'W', 1)
    c.bevel(['W'])
    c.rect(3, 5, 28, 8, 'M')
    for y, x0, x1, col in [(11, 5, 13, 'B'), (15, 10, 20, 'G'), (19, 16, 25, 'O'), (23, 7, 17, 'M')]:
        c.rect(x0, y, x1, y + 2, col)
    c.outline()


@icon('org.kde.kile', ['kile'], 'office', 'Kile')
def kile(c):
    page(c, 5, 3, 26, 28, 'W', 6)
    c.bevel(['W'])
    c.text(7, 11, 'TEX', 'G', font=5)
    c.rect(7, 21, 23, 22, 'S')
    c.rect(7, 24, 18, 25, 'S')
    c.outline()


@icon('org.kde.lokalize', ['lokalize'], 'dev', 'Lokalize')
def lokalize(c):
    bubble(c, 3, 3, 19, 15, 'B', 'l')
    bubble(c, 12, 12, 28, 24, 'O', 'r')
    c.bevel(['B', 'O'])
    c.text(7, 6, 'A', 'W')
    c.text(18, 15, 'B', 'W')
    c.outline()


@icon('org.kde.kphotoalbum', ['kphotoalbum'], 'media', 'KPhotoAlbum')
def kphotoalbum(c):
    c.rrect(3, 4, 28, 27, 'R', 1)
    c.bevel(['R'])
    c.vline(5, 5, 26, '1')
    c.rect(9, 8, 24, 21, 'W')
    c.rect(11, 10, 22, 19, 'b')
    c.poly([(11, 19.5), (15, 13), (19, 19.5)], 'G')
    c.circle(20, 13, 1.5, 'Y')
    c.outline()
