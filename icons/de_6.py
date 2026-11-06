"""XFCE, MATE, Cinnamon/Linux Mint, LXQt and elementary OS applications."""
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


def photo(c, x0, y0, x1, y1, frame='W', sky='b', hill='G'):
    c.rect(x0, y0, x1, y1, frame)
    c.rect(x0 + 2, y0 + 2, x1 - 2, y1 - 2, sky)
    c.poly([(x0 + 2, y1 - 1.5), (x0 + 7, y1 - 8), (x0 + 11, y1 - 4), (x0 + 14, y1 - 6),
            (x1 - 1.5, y1 - 2.5), (x1 - 1.5, y1 - 1.5)], hill)


def mint_leaf(c, x, y, col='G'):
    """Linux Mint family badge: small rounded tab in the corner."""
    c.rrect(x, y, x + 8, y + 7, col, 2)
    c.bevel([col])
    c.sprite(x + 2, y + 2, """
        #.#.#
        #.#.#
        #...#
    """, {'#': 'W'})


# ================================================================== XFCE


@icon('org.xfce.xfburn', ['xfburn'], 'media', 'Xfburn')
def xfburn(c):
    c.circle(14, 16, 11.5, 'w')
    c.arc(14, 16, 11, 3, 200, 260, 'W')
    c.arc(14, 16, 11, 3, 20, 80, 'S')
    c.circle(14, 16, 3, 'S'); c.circle(14, 16, 1.5, '.')
    c.poly([(22, 29), (20, 22), (24, 16), (25, 20), (28.5, 14), (29, 29)], 'R')
    c.poly([(23, 29), (23, 24), (25.5, 22), (27, 26), (27, 29)], 'Y')
    c.outline()


@icon('org.xfce.catfish', ['catfish'], 'utilities', 'Catfish')
def catfish(c):
    c.ellipse(15, 16, 11, 7.5, 'B')
    c.poly([(23, 16), (29, 9), (29, 23)], 'B')
    c.bevel(['B'])
    c.circle(9, 14, 1.5, 'W'); c.px(9, 14, 'k')
    c.line(4, 17, 1, 20, 'k') if False else None
    for y in (18, 20):
        c.line(5, y - 1, 3, y + 2, 'k')
    c.line(13, 10, 17, 22, '6') if False else c.vline(17, 11, 21, '6')
    c.outline()


@icon('org.xfce.screenshooter', ['xfce4-screenshooter', 'org.xfce.Screenshooter'], 'utilities', 'Screenshooter')
def xscreenshooter(c):
    c.rrect(3, 9, 28, 26, 'S', 2)
    c.rect(8, 6, 14, 9, 'S')
    c.bevel(['S'])
    c.circle(16, 17, 6.5, 'k')
    c.circle(16, 17, 4.5, 'B')
    c.px(14, 15, 'W')
    c.rect(23, 12, 25, 13, 'Y')
    c.frame(5, 11, 10, 15, 'W') if False else None
    c.outline()


@icon('xfce4-notes', ['org.xfce.notes', 'xfce4-notes-plugin'], 'office', 'Notes')
def xnotes(c):
    c.poly([(5, 3), (27, 3), (27, 22), (20, 28), (5, 28)], 'Y')
    c.poly([(20, 28), (20, 22), (27, 22)], '3')
    c.bevel(['Y'])
    c.rect(13, 1, 18, 4, 'R') if False else c.circle(16, 5, 2, 'R')
    for y in (11, 15, 19):
        c.hline(8, 23, y, '3')
    c.outline()


@icon('org.xfce.Dictionary', ['xfce4-dict', 'org.xfce.dictionary'], 'office', 'Dictionary')
def xdict(c):
    c.rrect(5, 3, 26, 28, 'B', 1)
    c.bevel(['B'])
    c.rect(5, 25, 26, 28, 'W'); c.hline(5, 26, 25, 'w')
    c.circle(15, 13, 5.5, 'W'); c.circle(15, 13, 3.5, 'b')
    c.line(19, 17, 22, 20, 'W', 2)
    c.outline()


@icon('org.xfce.appfinder', ['xfce4-appfinder'], 'system', 'Application Finder')
def appfinder(c):
    for i in range(2):
        for j in range(2):
            col = [['B', 'G'], ['O', 'R']][j][i]
            c.rrect(3 + i * 9, 3 + j * 9, 10 + i * 9, 10 + j * 9, col, 1)
    c.line(21, 21, 25, 25, 'N', 3)
    c.circle(19, 19, 7.5, 'S')
    c.circle(19, 19, 5.5, 'c')
    c.arc(19, 19, 4.5, 3, 200, 250, 'W')
    c.outline()


@icon('org.xfce.powermanager', ['xfce4-power-manager', 'xfce4-power-manager-settings',
                                'mate-power-statistics', 'lxqt-powermanagement'], 'system', 'Power Manager')
def powermanager(c):
    c.rrect(6, 5, 25, 28, 'S', 2)
    c.rect(12, 3, 19, 5, 'S')
    c.bevel(['S'])
    c.rect(8, 7, 23, 26, 'k')
    c.rect(9, 15, 22, 25, 'G')
    c.hline(9, 22, 15, 'g')
    c.sprite(13, 9, """
        ...##
        ..##.
        .####
        ..##.
        .##..
    """, {'#': 'Y'})
    c.outline()


@icon('org.xfce.clipman', ['xfce4-clipman', 'xfce4-clipman-plugin', 'parcellite', 'clipit', 'copyq',
                           'com.github.hluk.copyq'], 'utilities', 'Clipboard')
def clipman(c):
    c.rrect(5, 5, 26, 28, 'N', 2)
    c.bevel(['N'])
    page(c, 8, 8, 23, 26, 'W', 4)
    for y in (13, 16, 19, 22):
        c.hline(10, 20, y, 'S')
    c.rrect(11, 3, 20, 8, 'S', 1)
    c.rect(14, 4, 17, 5, 'k')
    c.outline()


@icon('org.xfce.gigolo', ['gigolo'], 'system', 'Gigolo')
def gigolo(c):
    c.rrect(3, 6, 21, 21, 'S', 1)
    c.bevel(['S'])
    c.rect(5, 8, 19, 18, 'B')
    c.rect(10, 22, 14, 23, 's'); c.rect(7, 24, 17, 25, 'S')
    c.circle(22, 21, 7, 'C')
    c.bevel(['C'])
    c.ring(22, 21, 7, 0, 'C') if False else None
    c.ellipse(22, 21, 3, 7, '5') if False else c.vline(22, 15, 27, '5')
    c.hline(16, 28, 21, '5')
    c.outline()


@icon('org.xfce.panel', ['xfce4-panel', 'xfce4-panel-menu'], 'system', 'Panel')
def xpanel(c):
    c.rrect(3, 4, 28, 27, 'b', 1)
    c.rect(3, 22, 28, 27, 'k')
    c.rect(5, 24, 7, 25, 'B'); c.rect(10, 24, 12, 25, 'W'); c.rect(15, 24, 17, 25, 'W')
    c.rect(22, 24, 26, 25, 'S')
    c.rrect(7, 7, 20, 17, 'W', 1)
    c.rect(7, 7, 20, 8, 'B')
    c.outline()


@icon('org.xfce.about', ['xfce4-about', 'xfce'], 'system', 'About Xfce')
def xfce_about(c):
    # the Xfce mouse
    c.ellipse(15, 18, 11, 8, 'S')
    c.circle(8, 10, 4.5, 'S'); c.circle(15, 9, 4.5, 'S')
    c.bevel(['S'])
    c.circle(8, 10, 2.5, 'p'); c.circle(15, 9, 2.5, 'p')
    c.circle(6, 18, 1, 'k')
    c.px(3, 20, 'k')
    c.line(25, 22, 28, 26, 'S', 1)
    c.outline()


@icon('org.xfce.xfwm4', ['xfwm4', 'xfwm4-settings', 'org.xfce.xfwm4-settings'], 'system', 'Window Manager')
def xfwm4(c):
    c.rrect(9, 3, 28, 19, 'W', 1)
    c.rect(9, 3, 28, 6, 'S')
    c.rrect(3, 11, 22, 28, 'W', 1)
    c.rect(3, 11, 22, 14, 'B')
    c.bevel(['W', 'B', 'S'])
    c.px(20, 12, 'R'); c.px(18, 12, 'W')
    c.outline()


@icon('menulibre', ['org.bluesabre.MenuLibre'], 'system', 'MenuLibre')
def menulibre(c):
    c.rrect(3, 3, 22, 28, 'W', 1)
    c.bevel(['W'])
    for i, col in enumerate(['R', 'G', 'B', 'O', 'M']):
        y = 6 + i * 4
        c.rect(5, y, 7, y + 2, col)
        c.hline(9, 19, y + 1, 'S')
    c.circle(22, 22, 5.5, 'S')
    c.circle(22, 22, 2, 'W')
    for a in range(0, 360, 60):
        r = math.radians(a)
        c.rect(round(22 + 6 * math.cos(r)) - 1, round(22 + 6 * math.sin(r)) - 1,
               round(22 + 6 * math.cos(r)), round(22 + 6 * math.sin(r)), 'S')
    c.outline()


@icon('mugshot', ['org.bluesabre.Mugshot'], 'system', 'Mugshot')
def mugshot(c):
    c.arc(23, 16, 5.5, 3, 270, 90, 'B')
    c.rrect(4, 6, 23, 27, 'B', 2)
    c.bevel(['B'])
    c.circle(13.5, 13, 3.5, 'W')
    c.rrect(8, 18, 19, 24, 'W', 2)
    c.outline()


@icon('lightdm-gtk-greeter-settings', ['lightdm-settings', 'lightdm'], 'system', 'Login Window')
def lightdm(c):
    c.rrect(3, 4, 28, 27, 'B', 1)
    c.bevel(['B'])
    c.circle(16, 11, 3.5, 'W')
    c.rrect(10, 17, 21, 20, 'W', 1)
    c.rrect(9, 22, 22, 25, 'k', 1)
    for x in (11, 14, 17):
        c.px(x, 23, 'W')
    c.outline()


# ================================================================== MATE
@icon('atril', ['org.mate.Atril', 'atril-previewer'], 'office', 'Atril')
def atril(c):
    page(c, 4, 3, 22, 28, 'W', 5)
    c.bevel(['W'])
    for y in (10, 13, 16, 19):
        c.hline(7, 18, y, 'S')
    c.circle(21, 21, 6.5, 'G')
    c.bevel(['G'])
    c.circle(21, 21, 4, 'W')
    c.circle(21, 21, 2, 'k')
    c.outline()


@icon('eom', ['org.mate.eom', 'mate-image-viewer'], 'media', 'Eye of MATE')
def eom(c):
    photo(c, 3, 9, 22, 28, 'W', 'b', 'G')
    c.ellipse(20, 10, 9, 6, 'W')
    c.circle(20, 10, 4, 'G')
    c.circle(20, 10, 2, 'k')
    c.px(19, 9, 'W')
    c.outline()


@icon('mate-control-center', ['org.mate.ControlCenter', 'mate-preferences-desktop'], 'system', 'MATE Control Center')
def matecc(c):
    c.circle(16, 16, 12.5, 'G')
    c.bevel(['G'])
    c.circle(16, 16, 8.5, 'g')
    c.sprite(9, 9, """
        ##....##....##
        ##....##....##
        ##....##....##
        ##....##....##
        ###..####..###
        ..############
        ...##########.
    """, {'#': 'W'})
    c.outline()


# ================================================================== Cinnamon / Linux Mint
@icon('xreader', ['org.x.reader'], 'office', 'Xreader')
def xreader(c):
    page(c, 4, 3, 24, 28, 'W', 6)
    c.bevel(['W'])
    c.rect(7, 10, 20, 15, 'b')
    for y in (18, 21, 24):
        c.hline(7, 20, y, 'S')
    mint_leaf(c, 19, 21)
    c.outline()


@icon('xviewer', ['org.x.viewer'], 'media', 'Xviewer')
def xviewer(c):
    photo(c, 3, 3, 26, 22, 'W', 'b', 'G')
    c.circle(20, 9, 2, 'Y')
    mint_leaf(c, 19, 20)
    c.outline()


@icon('pix', ['org.x.pix'], 'media', 'Pix')
def pix(c):
    c.poly([(5, 3), (25, 6), (23, 20), (3, 17)], 'w')
    photo(c, 6, 8, 28, 26, 'W', 'O', 'N')
    c.circle(22, 13, 2, 'Y')
    mint_leaf(c, 3, 21)
    c.outline()


@icon('xplayer', ['org.x.player'], 'media', 'Xplayer')
def xplayer(c):
    c.rrect(3, 4, 27, 22, 'k', 2)
    c.rect(5, 6, 25, 20, 's')
    play(c, 12, 8, 11, 'W')
    mint_leaf(c, 19, 21)
    c.outline()


@icon('mintinstall', ['org.x.mintinstall', 'mintinstall-symbolic'], 'system', 'Software Manager')
def mintinstall(c):
    c.poly([(5, 10), (27, 10), (25, 28), (7, 28)], 'G')
    c.bevel(['G'])
    c.arc(16, 10, 6.5, 4.5, 180, 360, 'S')
    c.sprite(12, 14, """
        ..##..
        ..##..
        ..##..
        ######
        .####.
        ..##..
    """, {'#': 'W'})
    c.outline()


@icon('mintupdate', ['org.x.mintupdate', 'mintupdate-checking'], 'system', 'Update Manager')
def mintupdate(c):
    c.poly([(16, 3), (28, 8), (26, 21), (16, 29), (6, 21), (4, 8)], 'G')
    c.bevel(['G'])
    c.sprite(11, 9, """
        ...##...
        ..####..
        .######.
        ########
        ..####..
        ..####..
        ..####..
    """, {'#': 'W'})
    c.rect(13, 19, 18, 21, 'W') if False else None
    c.outline()


@icon('mintsources', ['org.x.mintsources', 'software-sources'], 'system', 'Software Sources')
def mintsources(c):
    c.ellipse(16, 7, 11, 3.5, 'G')
    c.rect(5, 7, 26, 25, 'G')
    c.ellipse(16, 25, 11, 3.5, 'G')
    c.bevel(['G'])
    c.ellipse(16, 7, 9, 1.8, 'g')
    for y in (13, 19):
        c.hline(6, 25, y, '4')
    c.px(22, 16, 'W'); c.px(22, 22, 'W')
    c.outline()


@icon('mintdrivers', ['org.x.mintdrivers', 'driver-manager'], 'system', 'Driver Manager')
def mintdrivers(c):
    c.rect(4, 7, 27, 22, 'G')
    c.bevel(['G'])
    c.rect(4, 23, 27, 25, 'Y')
    for x in range(5, 27, 2):
        c.px(x, 26, 'Y')
    c.rect(7, 10, 15, 18, 'k')
    c.rect(18, 10, 24, 12, '4'); c.rect(18, 15, 24, 17, '4')
    c.outline()


@icon('mintbackup', ['org.x.mintbackup'], 'system', 'Backup Tool')
def mintbackup(c):
    c.rrect(3, 10, 28, 28, 'G', 2)
    c.bevel(['G'])
    c.rect(3, 15, 28, 16, '4')
    c.rect(13, 13, 18, 18, 'S')
    c.arc(16, 10, 6.5, 4.5, 180, 360, 'S')
    c.outline()


@icon('sticky', ['org.x.sticky', 'sticky-notes'], 'office', 'Sticky Notes')
def sticky(c):
    c.poly([(7, 3), (28.5, 7), (25, 26), (4, 22)], 'G')
    c.rect(3, 9, 22, 28, 'Y')
    c.bevel(['Y', 'G'])
    for y in (14, 18, 22):
        c.hline(6, 19, y, '3')
    c.outline()


@icon('webapp-manager', ['org.x.webapp-manager'], 'web', 'Web Apps')
def webappmanager(c):
    c.circle(13, 13, 10, 'B')
    c.bevel(['B'])
    c.ellipse(13, 13, 4, 10, '6')
    c.ellipse(13, 13, 2, 10, 'B')
    c.hline(4, 22, 13, '6')
    for x0, y0, col in [(18, 18, 'G'), (24, 18, 'O'), (18, 24, 'R'), (24, 24, 'Y')]:
        c.rect(x0, y0, x0 + 4, y0 + 4, col)
    c.outline()


@icon('bulky', ['org.x.bulky'], 'utilities', 'Bulky')
def bulky(c):
    for k, col in enumerate(['w', 'W', 'W']):
        x0, y0 = 3 + k * 3, 3 + k * 4
        c.rect(x0, y0, x0 + 15, y0 + 17, col)
    c.bevel(['W'])
    c.hline(12, 21, 14, 'S'); c.hline(12, 19, 17, 'S')
    c.line(17, 25, 25, 17, 'G', 3)
    c.px(16, 27, 'k'); c.px(17, 27, 'n'); c.px(16, 26, 'n')
    c.outline()


@icon('mintstick', ['org.x.mintstick', 'mintstick-format'], 'system', 'USB Image Writer')
def mintstick(c):
    c.rrect(9, 3, 22, 9, 'w', 1)
    c.rect(12, 5, 13, 6, 'k'); c.rect(18, 5, 19, 6, 'k')
    c.rrect(7, 9, 24, 28, 'G', 2)
    c.bevel(['G'])
    c.rect(11, 14, 20, 20, 'g')
    c.rect(13, 23, 18, 24, '4')
    c.outline()


@icon('mintreport', ['org.x.mintreport', 'system-reports'], 'system', 'System Reports')
def mintreport(c):
    c.rrect(5, 3, 26, 28, 'W', 1)
    c.bevel(['W'])
    c.rect(5, 3, 26, 7, 'G')
    for i, (h, col) in enumerate([(6, 'G'), (11, 'Y'), (8, 'G'), (14, 'R')]):
        x = 8 + i * 4
        c.rect(x, 25 - h, x + 2, 25, col)
    c.outline()


@icon('mintwelcome', ['org.x.mintwelcome', 'linuxmint-logo', 'distributor-logo-linuxmint'], 'system', 'Welcome Screen')
def mintwelcome(c):
    c.circle(16, 16, 12.5, 'G')
    c.bevel(['G'])
    c.sprite(8, 9, """
        ##..........
        ##..........
        ##..##..##..
        ##.#####.##.
        ##.##.##.##.
        ##.##.##.##.
        ##.##.##.##.
        .###########
        ..##########
    """, {'#': 'W'})
    c.outline()


@icon('cinnamon-settings', ['org.cinnamon.Settings', 'cinnamon-control-center', 'cinnamon'],
      'system', 'Cinnamon Settings')
def cinnamon_settings(c):
    # cinnamon roll spiral
    c.circle(16, 16, 12.5, 'N')
    c.bevel(['N'])
    pts = []
    for i in range(90):
        t = i / 89 * 3.0 * math.pi
        r = 1 + t * 1.1
        pts.append((16 + r * math.cos(t), 16 + r * math.sin(t)))
    for a, b in zip(pts, pts[1:]):
        c.line(round(a[0]), round(a[1]), round(b[0]), round(b[1]), 'o')
    c.outline()


# ================================================================== LXQt
@icon('lxqt-config', ['preferences-lxqt', 'lxqt-config-appearance'], 'system', 'LXQt Configuration')
def lxqt_config(c):
    c.rrect(3, 4, 28, 27, 'S', 1)
    c.bevel(['S'])
    c.rect(5, 6, 26, 25, 'W')
    for i, col in enumerate(['B', 'G', 'O']):
        y = 8 + i * 6
        c.hline(7, 24, y + 1, 'w')
        x = [12, 20, 9][i]
        c.rect(x - 1, y, x + 1, y + 2, col)
    c.outline()


@icon('lximage-qt', ['lximage'], 'media', 'LXImage')
def lximage(c):
    photo(c, 3, 5, 28, 26, 'B', 'W', 'C')
    c.circle(21, 11, 2.5, 'Y')
    c.bevel(['B'])
    c.outline()


@icon('lxqt-archiver', ['lxqt-archiver-qt'], 'utilities', 'LXQt Archiver')
def lxqt_archiver(c):
    c.rect(4, 9, 27, 28, 'N')
    c.poly([(4, 9), (8, 3), (23, 3), (27, 9)], 'n')
    c.bevel(['N'])
    c.rect(13, 3, 18, 28, 'B')
    c.rect(14, 3, 14, 28, 'b')
    c.rect(12, 13, 19, 17, 'S')
    c.outline()


@icon('qps', ['lxqt-qps'], 'system', 'Qps')
def qps(c):
    c.rrect(3, 4, 28, 27, 'k', 2)
    for i, y in enumerate((8, 12, 16, 20)):
        c.rect(6, y, 6 + [16, 9, 13, 5][i], y + 2, ['G', 'Y', 'G', 'R'][i])
    c.rect(6, 23, 25, 24, 's')
    c.outline()


@icon('obconf-qt', ['obconf', 'openbox'], 'system', 'Openbox Settings')
def obconf(c):
    c.rect(3, 6, 28, 26, 'W')
    c.bevel(['W'])
    c.rect(3, 6, 28, 9, 'k')
    c.rect(24, 7, 26, 8, 'R')
    c.ring(16, 18, 6, 3.5, 'S')
    for a in range(0, 360, 45):
        r = math.radians(a)
        c.rect(round(16 + 6.5 * math.cos(r)) - 1, round(18 + 6.5 * math.sin(r)) - 1,
               round(16 + 6.5 * math.cos(r)), round(18 + 6.5 * math.sin(r)), 'S')
    c.outline()


# ================================================================== elementary OS
@icon('io.elementary.code', ['org.pantheon.scratch', 'scratch-text-editor'], 'dev', 'Code')
def ecode(c):
    c.rrect(3, 4, 28, 27, 'k', 2)
    c.rect(3, 4, 28, 7, 's')
    c.sprite(6, 11, """
        ..#.............
        .#..............
        #......####.....
        .#..............
        ..#.......######
    """, {'#': 'G'})
    c.hline(6, 18, 19, 'B'); c.hline(9, 22, 22, 'O')
    c.outline()


@icon('io.elementary.files', ['pantheon-files', 'org.pantheon.files'], 'system', 'Files')
def efiles(c):
    c.rrect(3, 5, 13, 9, 'B', 1)
    c.rect(3, 7, 28, 27, 'B')
    c.rect(3, 11, 28, 27, 'b')
    c.bevel(['b'])
    c.hline(3, 28, 11, 'c')
    c.rect(12, 17, 19, 18, '6')
    c.outline()


@icon('io.elementary.music', ['org.pantheon.noise', 'noise'], 'media', 'Music')
def emusic(c):
    c.circle(16, 16, 12.5, 'O')
    c.bevel(['O'])
    c.sprite(9, 8, """
        ......#######
        ....#########
        ....##.....##
        ....#......##
        ....#......##
        ..###....####
        .####...#####
        .####...####.
        ..##.....##..
    """, {'#': 'W'})
    c.outline()


@icon('io.elementary.videos', ['pantheon-videos', 'org.pantheon.audience'], 'media', 'Videos')
def evideos(c):
    c.rect(3, 6, 28, 25, 'k')
    for x in range(5, 28, 4):
        c.rect(x, 7, x + 1, 8, 'w'); c.rect(x, 23, x + 1, 24, 'w')
    c.rect(5, 10, 26, 21, 'R')
    c.rect(5, 10, 26, 11, 'r')
    play(c, 13, 12, 7, 'W')
    c.outline()


@icon('io.elementary.photos', ['org.pantheon.photos', 'shotwell-elementary'], 'media', 'Photos')
def ephotos(c):
    c.poly([(3, 7), (21, 3), (24, 18), (6, 22)], 'w')
    photo(c, 8, 9, 28, 28, 'W', 'C', 'G')
    c.circle(22, 14, 2, 'W')
    c.outline()


@icon('io.elementary.mail', ['org.pantheon.mail', 'pantheon-mail'], 'web', 'Mail')
def email(c):
    c.poly([(16, 3), (28, 12), (28, 27), (3, 27), (3, 12)], 'B')
    c.rect(7, 7, 24, 22, 'W')
    c.poly([(3, 12), (16, 21), (28, 12), (28, 27), (3, 27)], 'b')
    c.line(3, 27, 13, 19, '6'); c.line(28, 27, 19, 19, '6')
    c.hline(10, 21, 11, 'S'); c.hline(10, 18, 14, 'S')
    c.outline()


@icon('io.elementary.calendar', ['maya-calendar', 'org.pantheon.maya'], 'office', 'Calendar')
def ecalendar(c):
    c.rrect(3, 5, 28, 28, 'W', 2)
    c.bevel(['W'])
    c.rect(3, 5, 28, 11, 'R')
    c.rect(8, 3, 9, 7, 's'); c.rect(22, 3, 23, 7, 's')
    c.text(10, 15, '31', 'k')
    c.outline()


@icon('io.elementary.tasks', ['org.pantheon.tasks'], 'office', 'Tasks')
def etasks(c):
    c.rrect(5, 3, 26, 28, 'W', 2)
    c.bevel(['W'])
    for i, col in enumerate(['G', 'B', 'S']):
        y = 7 + i * 7
        c.circle(10, y + 1.5, 2.5, col)
        c.hline(14, 23, y + 1, 'S')
    c.px(9, 8, 'W'); c.px(10, 9, 'W'); c.px(11, 7, 'W')
    c.outline()


@icon('io.elementary.appcenter', ['org.pantheon.appcenter', 'appcenter'], 'system', 'AppCenter')
def appcenter(c):
    c.rrect(4, 9, 27, 28, 'B', 3)
    c.bevel(['B'])
    c.arc(16, 9, 6.5, 4.5, 180, 360, 'S')
    c.sprite(9, 14, """
        ..#....#....#..
        ..#....#....#..
        .###..###..###.
        ...............
        .....#####.....
        .....#####.....
        ......###......
        .......#.......
    """, {'#': 'W'})
    c.replace('W', 'b', (9, 14, 24, 16))
    c.outline()


@icon('io.elementary.camera', ['org.pantheon.camera', 'pantheon-camera'], 'media', 'Camera')
def ecamera(c):
    c.rrect(3, 9, 28, 26, 'S', 3)
    c.rect(10, 6, 21, 9, 'S')
    c.bevel(['S'])
    c.circle(16, 17.5, 7, 'k')
    c.circle(16, 17.5, 5, 'M')
    c.circle(16, 17.5, 2.5, '7')
    c.px(14, 15, 'W')
    c.rect(23, 12, 25, 13, 'W')
    c.outline()


@icon('io.elementary.calculator', ['org.pantheon.calculator', 'pantheon-calculator'], 'utilities', 'Calculator')
def ecalculator(c):
    c.rrect(6, 3, 25, 28, 'S', 2)
    c.bevel(['S'])
    c.rect(8, 5, 23, 10, 'G')
    c.rect(8, 5, 23, 5, 'g')
    for j in range(4):
        for i in range(4):
            col = 'O' if i == 3 else 'W'
            c.rect(8 + i * 4, 13 + j * 4, 10 + i * 4, 15 + j * 4, col)
    c.outline()


@icon('io.elementary.screenshot', ['org.pantheon.screenshot', 'screenshot-tool'], 'utilities', 'Screenshot')
def escreenshot(c):
    c.rrect(3, 5, 28, 26, 'B', 2)
    c.bevel(['B'])
    c.rect(5, 7, 26, 24, 'b')
    for (x, y, dx, dy) in [(7, 9, 1, 1), (24, 9, -1, 1), (7, 22, 1, -1), (24, 22, -1, -1)]:
        c.hline(x, x + 3 * dx, y, 'W'); c.vline(x, y, y + 3 * dy, 'W')
    c.circle(16, 16, 2.5, 'W')
    c.outline()


@icon('io.elementary.settings', ['io.elementary.switchboard', 'switchboard', 'org.pantheon.switchboard'],
      'system', 'System Settings')
def eswitchboard(c):
    c.rrect(3, 3, 28, 28, 'S', 3)
    c.bevel(['S'])
    for i, col in enumerate(['B', 'G', 'O', 'M']):
        x, y = 6 + (i % 2) * 11, 6 + (i // 2) * 11
        c.rrect(x, y, x + 8, y + 8, col, 2)
        c.hline(x + 2, x + 6, y, LT[col])
    c.outline()
