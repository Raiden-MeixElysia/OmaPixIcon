"""2D graphics: design, painting, animation, image viewers and optimisers."""
from pix import icon
import math


def big(c, x, y, art, col, k=2):
    lines = [l.strip() for l in art.strip('\n').split('\n')]
    for j, row in enumerate(lines):
        for i, ch in enumerate(row):
            if ch == '#':
                c.rect(x + i * k, y + j * k, x + i * k + k - 1, y + j * k + k - 1, col)


def photo(c, x0, y0, x1, y1, frame='W', sky='C', hill='G', sun='Y'):
    c.rect(x0, y0, x1, y1, frame)
    c.rect(x0 + 2, y0 + 2, x1 - 2, y1 - 2, sky)
    w = x1 - x0
    c.poly([(x0 + 2, y1 - 1.5), (x0 + 2 + w * .35, y0 + (y1 - y0) * .45), (x0 + w * .6, y1 - 1.5)], hill)
    c.poly([(x0 + w * .45, y1 - 1.5), (x0 + w * .7, y0 + (y1 - y0) * .55), (x1 - 1.5, y1 - 1.5)], DARKER[hill])
    c.circle(x1 - 5, y0 + 6, 2, sun)


DARKER = {'G': '4', 'B': '6', 'M': '7', 'O': '2', 'g': 'G', 'k': 'K', 'N': '8'}


def pencil(c, x0, y0, x1, y1, body='Y', tip='n'):
    """Diagonal pencil from tip (x0,y0) to end (x1,y1)."""
    c.line(x0 + 2, y0 - 2, x1, y1, body, 3)
    c.line(x0, y0, x0 + 2, y0 - 2, tip, 2)
    c.px(x0, y0 + 1, 'k')


# =================================================================== design

@icon('penpot', ['app.penpot.Penpot', 'penpot-desktop', 'penpot-webapp', 'com.sudovanilla.penpot-desktop'],
      'graphics', 'Penpot')
def penpot(c):
    # isometric open box (penpot mark)
    c.poly([(16, 9), (28, 15), (16, 21), (4, 15)], 'k')
    c.poly([(4, 15), (16, 21), (16, 29), (4, 23)], 'W')
    c.poly([(16, 21), (28, 15), (28, 23), (16, 29)], 'w')
    c.poly([(4, 15), (16, 9), (11, 3), (2.5, 8)], 'W')
    c.poly([(28, 15), (16, 9), (21, 3), (29.5, 8)], 'w')
    c.outline()


@icon('lunacy', ['com.icons8.Lunacy', 'lunacy-bin'], 'graphics', 'Lunacy')
def lunacy(c):
    # crescent moon cut by a pen nib
    c.circle(16, 16, 13, 'B')
    c.circle(21, 12, 10, '.')
    c.bevel(['B'])
    c.poly([(20, 16), (27, 20), (24, 28), (16, 23)], 'Y')
    c.line(22, 22, 25, 25, '3')
    c.outline()


@icon('com.github.akiraux.akira', ['akira'], 'graphics', 'Akira')
def akira(c):
    # bold triangle-A with a crossbar gap
    c.poly([(16, 3), (29, 28), (3, 28)], 'R')
    c.bevel(['R'])
    c.poly([(16, 12), (22, 24), (10, 24)], '.')
    c.rect(11, 19, 21, 21, 'R')
    c.outline()


@icon('org.glimpse_editor.Glimpse', ['glimpse'], 'graphics', 'Glimpse')
def glimpse(c):
    # eye peeking through a paper tear
    c.rect(3, 6, 28, 26, 'W')
    c.poly([(3, 12), (9, 15), (14, 11), (20, 15), (25, 11), (28, 14), (28, 21), (22, 18), (16, 22), (10, 18), (3, 21)], 'k')
    c.ellipse(16, 16.5, 6, 3, 'G')
    c.circle(16, 16.5, 1.5, 'K')
    c.bevel(['W'])
    c.outline()


@icon('photopea', ['photopea-webapp', 'com.photopea.Photopea', 'www.photopea.com'], 'graphics', 'Photopea')
def photopea(c):
    # pea pod 'P' in teal
    c.rrect(3, 3, 28, 28, 'C', 4)
    c.bevel(['C'])
    c.rect(9, 7, 13, 25, 'W')
    c.circle(16.5, 12.5, 6, 'W')
    c.circle(16.5, 12.5, 2.5, 'C')
    c.rect(13, 10, 16, 15, 'C')
    c.outline()


@icon('io.photoflare.photoflare', ['photoflare'], 'graphics', 'Photoflare')
def photoflare(c):
    # four-point lens flare star
    c.poly([(16, 2), (19, 13), (30, 16), (19, 19), (16, 30), (13, 19), (2, 16), (13, 13)], 'Y')
    c.circle(16, 16, 6, 'O')
    c.circle(16, 16, 3.5, 'y')
    c.px(15, 15, 'W')
    c.outline()


@icon('com.github.maoschanz.drawing', ['drawing'], 'graphics', 'Drawing')
def drawing(c):
    # paper with a brush stroke
    c.rect(3, 8, 24, 28, 'W')
    c.bevel(['W'])
    c.line(6, 22, 12, 16, 'R', 2)
    c.line(12, 16, 17, 21, 'R', 2)
    c.poly([(16, 15), (27, 3), (29, 5), (18, 17)], 'N')
    c.poly([(14, 17), (16, 15), (18, 17), (15, 21)], 'S')
    c.outline()


@icon('org.tuxpaint.Tuxpaint', ['tuxpaint', 'tux4kids-tuxpaint'], 'graphics', 'Tux Paint')
def tuxpaint(c):
    # penguin head with a paintbrush
    c.ellipse(15, 16, 11, 12.5, 'k')
    c.ellipse(15, 19, 7.5, 8.5, 'W')
    c.circle(11.5, 12, 2.5, 'W'); c.circle(18.5, 12, 2.5, 'W')
    c.px(12, 12, 'K'); c.px(18, 12, 'K')
    c.poly([(12, 16), (18, 16), (15, 20)], 'Y')
    c.line(23, 26, 28, 10, 'N', 2)
    c.rect(26, 6, 29, 10, 'R')
    c.outline()


@icon('io.github.OpenToonz', ['opentoonz', 'OpenToonz', 'tahoma2d', 'org.tahoma2d.Tahoma2D'], 'graphics', 'OpenToonz')
def opentoonz(c):
    # hand-drawn cartoon eyes in a speech blob
    c.ellipse(16, 15, 13, 12, 'Y')
    c.bevel(['Y'])
    c.ellipse(11, 14, 4, 5.5, 'W'); c.ellipse(21, 14, 4, 5.5, 'W')
    c.circle(12, 15, 2, 'K'); c.circle(22, 15, 2, 'K')
    c.arc(16, 18, 6, 5, 30, 150, '2')
    c.outline()


@icon('org.synfig.SynfigStudio', ['synfigstudio', 'synfig', 'synfig-studio'], 'graphics', 'Synfig')
def synfig(c):
    # bezier curve with handles
    for t in range(0, 101):
        u = t / 100
        x = (1 - u) ** 3 * 4 + 3 * (1 - u) ** 2 * u * 8 + 3 * (1 - u) * u * u * 24 + u ** 3 * 26
        y = (1 - u) ** 3 * 26 + 3 * (1 - u) ** 2 * u * 4 + 3 * (1 - u) * u * u * 28 + u ** 3 * 5
        c.rect(int(x), int(y), int(x) + 1, int(y) + 1, 'O')
    c.line(5, 26, 9, 5, 'S'); c.line(26, 5, 23, 27, 'S')
    c.rect(8, 3, 11, 6, 'B'); c.rect(22, 25, 25, 28, 'B')
    c.rect(3, 25, 6, 28, 'W'); c.rect(25, 3, 28, 6, 'W')
    c.outline()


@icon('org.pencil2d.Pencil2D', ['pencil2d', 'Pencil2D'], 'graphics', 'Pencil2D')
def pencil2d(c):
    pencil(c, 4, 27, 26, 5, 'B', 'n')
    c.rect(25, 3, 28, 6, 'P')
    c.line(5, 18, 13, 26, 'w') if False else None
    c.bevel(['B'])
    c.outline()


@icon('enve', ['io.github.maurycyliebner.enve'], 'graphics', 'enve')
def enve(c):
    # stylised e on a keyframe diamond
    c.poly([(16, 2.5), (29.5, 16), (16, 29.5), (2.5, 16)], 'k')
    c.ring(16, 16, 8, 5, 'G')
    c.rect(10, 15, 22, 17, 'G')
    c.rect(18, 18, 24, 21, 'k')
    c.outline()


@icon('org.mattbas.Glaxnimate', ['glaxnimate'], 'graphics', 'Glaxnimate')
def glaxnimate(c):
    # bouncing ball with motion trail
    for i, (x, y, r) in enumerate(((6, 8, 2), (10, 15, 2.5), (14, 21, 3))):
        c.circle(x, y, r, 'm')
    c.circle(22, 20, 7, 'M')
    c.bevel(['M'])
    c.px(19, 16, 'W'); c.px(20, 16, 'm')
    c.rect(3, 27, 28, 28, 's')
    c.outline()


@icon('org.kde.kolourpaint', ['kolourpaint', 'kolourpaint4'], 'graphics', 'KolourPaint')
def kolourpaint(c):
    # paint bucket tipping
    c.poly([(4, 10), (16, 4), (22, 16), (10, 22)], 'w')
    c.bevel(['w'])
    c.poly([(5, 10), (17, 4), (16, 3), (5, 8)], 'S')
    c.arc(11, 7, 6, 5, 180, 330, 's')
    c.poly([(21, 14), (26, 18), (27, 27.5), (24, 27.5), (23, 22), (19, 18)], 'B')
    c.bevel(['B'])
    c.outline()


@icon('azpainter', [], 'graphics', 'AzPainter')
def azpainter(c):
    # fountain-pen nib
    c.poly([(16, 3), (25, 13), (21, 24), (11, 24), (7, 13)], 'k')
    c.poly([(16, 5), (23, 13), (20, 22), (12, 22), (9, 13)], 'C')
    c.bevel(['C'], edge=('k',))
    c.vline(16, 5, 14, 'k'); c.circle(16, 15.5, 1.5, 'k')
    c.rect(11, 25, 20, 28, 's')
    c.outline()


@icon('org.kde.gwenview', ['gwenview'], 'graphics', 'Gwenview')
def gwenview(c):
    # landscape photo with a round magnifier lens
    photo(c, 3, 5, 24, 22, 'W', 'C', 'G')
    c.bevel(['W'])
    c.ring(20, 19, 7.5, 5, 'k')
    c.circle(20, 19, 5, 'c')
    c.line(25, 24, 26, 25, 'k', 2)
    c.outline()


@icon('org.xfce.ristretto', ['ristretto'], 'graphics', 'Ristretto')
def ristretto(c):
    # espresso cup with a photo on the saucer
    c.rrect(6, 8, 21, 21, 'W', 2)
    c.ring(21, 13, 4.5, 2, 'W')
    c.bevel(['W'])
    c.rect(8, 9, 19, 11, 'N')
    c.ellipse(15, 24, 13, 3.5, 'w')
    c.rect(10, 13, 17, 18, 'C')
    c.poly([(10, 18), (13, 14), (17, 18)], 'G')
    c.outline()


@icon('org.gnome.gThumb', ['gthumb'], 'graphics', 'gThumb')
def gthumb(c):
    # thumbs-up holding a photo corner
    photo(c, 9, 3, 28, 17, 'W', 'B', 'G')
    c.poly([(4, 14), (9, 14), (12, 8), (15, 9), (14, 15), (21, 15), (22, 18), (20, 28), (4, 28)], 'p')
    c.bevel(['p', 'W'])
    c.vline(9, 15, 27, '9')
    c.outline()


@icon('org.geeqie.Geeqie', ['geeqie'], 'graphics', 'Geeqie')
def geeqie(c):
    # stacked photos fanned
    c.poly([(3, 8), (20, 3), (24, 18), (7, 23)], 'w')
    photo(c, 8, 10, 28, 28, 'W', 'C', 'G')
    c.bevel(['W', 'w'])
    c.outline()


@icon('org.nomacs.ImageLounge', ['nomacs', 'nomacs-qt6'], 'graphics', 'nomacs')
def nomacs(c):
    # blue square-n with a sunrise
    c.rrect(3, 3, 28, 28, 'B', 2)
    c.bevel(['B'])
    c.poly([(8, 25), (8, 8), (13, 8), (19, 18), (19, 8), (24, 8), (24, 25), (19, 25), (13, 15), (13, 25)], 'W')
    c.outline()


@icon('com.interversehq.qView', ['qview', 'qView'], 'graphics', 'qView')
def qview(c):
    # magnifier ring + q tail
    c.ring(14, 14, 11, 7, 'O')
    c.bevel(['O'])
    c.circle(14, 14, 7, 'y')
    c.circle(11, 11, 2, 'W')
    c.line(21, 21, 25, 25, 'O', 3)
    c.outline()


@icon('XnViewMP', ['xnviewmp', 'com.xnview.XnViewMP', 'xnview'], 'graphics', 'XnView MP')
def xnview(c):
    # aperture eye: X over a photo
    photo(c, 3, 5, 28, 27, 'k', 'b', 'G', 'Y')
    c.line(6, 8, 25, 24, 'W', 2); c.line(25, 8, 6, 24, 'W', 2)
    c.outline()


@icon('io.github.blissd.Fotema', ['fotema'], 'graphics', 'Fotema')
def fotema(c):
    # polaroid with a heart photo
    c.rect(4, 3, 27, 28, 'W')
    c.bevel(['W'])
    c.rect(6, 5, 25, 21, 'M')
    for cx in (12.5, 18.5):
        c.circle(cx, 11, 3.5, 'P')
    c.poly([(9, 12), (22, 12), (15.5, 19)], 'P')
    c.outline()


@icon('net.fasterland.converseen', ['converseen'], 'graphics', 'Converseen')
def converseen(c):
    # two photo cards with a swap arrow
    photo(c, 3, 3, 16, 14, 'W', 'C', 'G')
    photo(c, 15, 17, 28, 28, 'W', 'P', 'M')
    c.poly([(19, 4), (26, 4), (26, 13), (29, 13), (24.5, 16.5), (20, 13), (23, 13), (23, 7), (19, 7)], 'O')
    c.outline()


@icon('com.github.huluti.Curtail', ['curtail'], 'graphics', 'Curtail')
def curtail(c):
    # photo squeezed by a clamp
    photo(c, 6, 8, 25, 24, 'W', 'C', 'G')
    c.rect(3, 3, 28, 6, 'R'); c.rect(3, 25, 28, 28, 'R')
    c.bevel(['R'])
    c.rect(15, 3, 16, 29, '1') if False else None
    c.outline()


@icon('trimage', [], 'graphics', 'Trimage')
def trimage(c):
    # photo with scissors-trimmed corner
    c.poly([(3, 3), (22, 3), (28, 9), (28, 28), (3, 28)], 'W')
    c.rect(5, 5, 21, 26, 'B')
    c.rect(5, 11, 26, 26, 'B')
    c.poly([(5, 26), (12, 14), (19, 26)], 'G')
    c.circle(20, 17, 2, 'Y')
    c.poly([(22, 3), (28, 9), (22, 9)], 'S')
    c.outline()


@icon('io.gitlab.theevilskeleton.Upscaler', ['upscaler'], 'graphics', 'Upscaler')
def upscaler(c):
    # small pixel image becoming a large one
    c.rect(3, 15, 13, 28, 'k')
    c.rect(4, 16, 12, 27, 'C')
    for x in range(4, 13, 3):
        for y in range(16, 28, 3):
            if (x + y) % 2:
                c.rect(x, y, x + 1, y + 1, 'B')
    c.rect(15, 3, 28, 28, 'W')
    c.rect(17, 5, 26, 26, 'C')
    c.poly([(17, 26), (21, 16), (26, 26)], 'G')
    c.poly([(5, 11), (5, 6), (10, 6)], 'G')
    c.outline()


@icon('io.gitlab.adhami3310.Converter', ['switcheroo', 'converter'], 'graphics', 'Switcheroo')
def switcheroo(c):
    # two arrows swapping around an image corner
    c.rrect(3, 3, 28, 28, 'M', 3)
    c.bevel(['M'])
    c.poly([(7, 11), (19, 11), (19, 7), (25, 13), (19, 19), (19, 15), (7, 15)], 'W')
    c.poly([(25, 20), (13, 20), (13, 17), (7, 22), (13, 27), (13, 24), (25, 24)], 'm')
    c.outline()


@icon('io.gitlab.gregorni.Letterpress', ['letterpress'], 'graphics', 'Letterpress')
def letterpress(c):
    # ASCII-art picture: text characters forming a face
    c.rect(3, 4, 28, 27, 'k')
    for y in range(6, 26, 4):
        for x in range(5, 26, 4):
            d = math.hypot(x - 15, y - 15)
            c.text(x, y, '8' if d < 6 else '+' if d < 9 else '-', 'G' if d < 6 else '4', font=3)
    c.outline()


@icon('com.github.finefindus.eyedropper', ['eyedropper'], 'graphics', 'Eyedropper')
def eyedropper(c):
    c.line(5, 26, 16, 15, 'c', 3)
    c.poly([(3, 29), (5, 25), (7, 27)], 'C')
    c.rrect(15, 9, 23, 17, 's', 1)
    c.circle(23, 8, 5.5, 'R')
    c.bevel(['R', 's'])
    c.outline()


@icon('gpick', ['org.gpick.gpick', 'gpick-color-picker'], 'graphics', 'Gpick')
def gpick(c):
    # colour wheel wedges with a picker crosshair
    cols = ['R', 'O', 'Y', 'G', 'C', 'B', 'M', 'P']
    for i, col in enumerate(cols):
        c.arc(16, 16, 13, 0, i * 45, i * 45 + 45, col)
    c.circle(16, 16, 5, 'W')
    c.circle(16, 16, 3, 'k')
    c.outline()


@icon('nl.hjdskes.gcolor3', ['gcolor3', 'gcolor2', 'color-picker', 'org.gnome.design.Palette', 'kcolorchooser'],
      'graphics', 'Color Picker')
def gcolor3(c):
    # paint swatch fan
    for i, col in enumerate(('R', 'Y', 'G', 'B')):
        a = math.radians(-110 + i * 22)
        x1, y1 = 6 + 22 * math.cos(a + math.pi / 2), 26 + 22 * math.sin(a + math.pi / 2)
        pass
    for i, col in enumerate(('B', 'G', 'Y', 'R')):
        ox = i * 5
        c.poly([(4 + ox, 28), (4 + ox, 6 + i * 1.5), (9 + ox, 3 + i * 1.5), (9 + ox, 28)], col)
        c.vline(4 + ox, 6 + i, 28, LIGHTMAP[col])
    c.poly([(24, 10), (28, 12), (28, 28), (24, 28)], 'M')
    c.rect(4, 26, 28, 28, 'w')
    c.circle(6.5, 27, 1, 'k')
    c.outline()


LIGHTMAP = {'B': 'b', 'G': 'g', 'Y': 'y', 'R': 'r', 'M': 'm'}


@icon('hyprpicker', [], 'graphics', 'hyprpicker')
def hyprpicker(c):
    # magnifier loupe showing big pixels + crosshair
    c.circle(14, 14, 11, 'k')
    for i in range(4):
        for j in range(4):
            col = ('A', 'a', 'C', 'B')[(i + j) % 4]
            c.rect(6 + i * 4, 6 + j * 4, 9 + i * 4, 9 + j * 4, col)
    for y in range(32):
        for x in range(32):
            if c.get(x, y) not in '.' and math.hypot(x + .5 - 14, y + .5 - 14) > 9:
                c.px(x, y, 'k')
    c.rect(13, 13, 14, 14, 'W')
    c.line(22, 22, 25, 25, 'k', 3)
    c.outline()


@icon('net.scribus.Scribus', ['scribus', 'scribus-ng'], 'graphics', 'Scribus')
def scribus(c):
    # quill pen over an open layout page
    c.rect(3, 8, 24, 28, 'W')
    c.bevel(['W'])
    c.rect(5, 10, 13, 16, 'B')
    c.hline(15, 22, 11, 'S'); c.hline(15, 22, 14, 'S')
    for y in (19, 22, 25):
        c.hline(5, 22, y, 'S')
    c.poly([(14, 21), (26, 3), (29, 4), (17, 22)], 'O')
    c.poly([(26, 3), (29, 4), (29, 8), (24, 9)], 'y')
    c.px(14, 22, 'k')
    c.outline()


@icon('birdfont', ['org.birdfont.BirdFont'], 'graphics', 'BirdFont')
def birdfont(c):
    # bird whose body is a big 'a' glyph
    c.circle(15, 18, 10, 'C')
    c.poly([(22, 14), (29, 10), (25, 17)], 'O')
    c.poly([(4, 16), (3, 8), (10, 12)], 'C')
    c.bevel(['C'])
    c.circle(19, 13, 1.5, 'K')
    c.ring(13, 20, 4.5, 2, 'W')
    c.rect(17, 16, 18, 25, 'W')
    c.outline()


@icon('fontmatrix', ['org.fontmatrix.Fontmatrix'], 'graphics', 'Fontmatrix')
def fontmatrix(c):
    # grid of glyph tiles
    for i, ch in enumerate('AGRB'):
        x, y = 3 + (i % 2) * 13, 3 + (i // 2) * 13
        c.rect(x, y, x + 12, y + 12, 'W' if i in (0, 3) else 'k')
        c.text(x + 4, y + 3, ch, 'k' if i in (0, 3) else 'W', font=5) if False else c.text(x + 4, y + 3, ch, 'k' if i in (0, 3) else 'W', font=5)
    c.outline()
