"""Developer utilities: mobile/emulators, GNOME/KDE/Qt dev tools, profilers, hex/RE tools, hardware."""
import math
from pix import icon

DEV = 'dev'


def _phone(c, body='k', screen='b', x0=8, x1=23):
    c.rrect(x0, 3, x1, 28, body, 3)
    c.bevel([body], dark=False)
    c.rect(x0 + 2, 6, x1 - 2, 24, screen)
    c.hline(x0 + 5, x1 - 5, 26, 's')


def _qt(c, glyph):
    """Qt tool family: green Qt shield with a glyph in the corner."""
    c.poly([(9, 3), (29, 3), (29, 22), (23, 29), (3, 29), (3, 9)], 'G')
    c.bevel(['G'])
    glyph(c)


def _wave(c, y, col, pattern):
    x = 5
    lvl = 0
    for n in pattern:
        top = y if lvl else y + 4
        c.hline(x, x + n, top, col)
        x += n
        lvl ^= 1
        c.vline(x, y, y + 4, col)


# ====================================================================== mobile

@icon('android-emulator', ['emulator', 'android-sdk-emulator', 'android-emulator-bin', 'avd'], DEV,
      'Android Emulator')
def android_emulator(c):
    _phone(c, 'k', 'G')
    # android head
    c.ellipse(16, 16, 6, 5, 'W')
    c.rect(9, 16, 22, 20, 'G')
    c.rect(10, 16, 21, 19, 'W') if False else None
    c.pixels([(13, 14), (18, 14)], 'G')
    c.pixels([(11, 10), (20, 10)], 'W')
    c.outline()


@icon('scrcpy', ['scrcpy-bin', 'scrcpy-gui', 'guiscrcpy', 'scrcpy-git', 'in.srev.guiscrcpy'], DEV, 'scrcpy')
def scrcpy(c):
    # phone mirrored onto a monitor
    c.rect(3, 5, 23, 20, 'S')
    c.rect(5, 7, 21, 18, 'k')
    c.rect(11, 21, 15, 23, 'S')
    c.rect(7, 23, 19, 24, 'S')
    c.bevel(['S'])
    c.rrect(20, 10, 28, 27, 'G', 2)
    c.bevel(['G'])
    c.rect(22, 12, 26, 24, 'k')
    c.poly([(8, 12), (14, 12), (14, 10), (18, 13), (14, 16), (14, 14), (8, 14)], 'G')
    c.outline()


@icon('flutter', ['flutter-bin', 'flutter-sdk', 'flutter-target-linux'], DEV, 'Flutter')
def flutter(c):
    c.poly([(19, 3), (27, 3), (10, 20), (6, 16)], 'b')
    c.poly([(19, 15), (27, 15), (19, 23), (15, 19)], 'b')
    c.poly([(15, 19), (19, 23), (27, 29), (19, 29), (11, 23)], '6')
    c.bevel(['b'], dark=False)
    c.outline()


@icon('electron-fiddle', ['electron-fiddle-bin', 'com.electronjs.fiddle', 'Electron Fiddle'], DEV,
      'Electron Fiddle')
def electron_fiddle(c):
    # violin
    c.circle(13, 21, 7.5, 'N')
    c.circle(14, 12.5, 5.5, 'N')
    c.rect(16, 3, 18, 14, '8')
    c.rect(15, 2, 19, 4, '8') if False else None
    c.bevel(['N'])
    c.rect(11, 19, 11, 24, 'K'); c.rect(15, 19, 15, 24, 'K')
    c.line(19, 28, 29, 4, 'C')
    c.line(20, 28, 28, 9, 'c')
    c.outline()


@icon('electron', ['electron28', 'electron29', 'electron30', 'electron31', 'electron32', 'electron33', 'electron34',
                   'electron35', 'electron36', 'electron37'], DEV, 'Electron')
def electron(c):
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'], dark=False)
    for k in range(3):
        a = math.radians(k * 60 + 30)
        for y in range(32):
            for x in range(32):
                dx, dy = x + .5 - 16, y + .5 - 16
                u = dx * math.cos(a) + dy * math.sin(a)
                v = -dx * math.sin(a) + dy * math.cos(a)
                d = (u / 10.5) ** 2 + (v / 4) ** 2
                if 0.6 < d <= 1.0:
                    c.px(x, y, 'C')
    c.circle(16, 16, 2, 'c')
    c.outline()


# ====================================================================== GNOME / Qt / KDE dev tools

@icon('org.gnome.Builder', ['gnome-builder', 'org.gnome.Builder.Devel'], DEV, 'GNOME Builder')
def gnome_builder(c):
    # hard hat over a code bracket
    c.ellipse(16, 14, 11, 10, 'Y')
    c.rect(3, 14, 28, 24, '.')
    c.rrect(3, 14, 28, 17, 'Y', 1)
    c.rect(14, 4, 17, 13, 'y')
    c.bevel(['Y'])
    c.sprite(7, 19, """
        ...##.......##...
        .##...........##.
        ##.............##
        .##...........##.
        ...##.......##...
    """, {'#': 'B'})
    c.outline()


@icon('org.gnome.Glade', ['glade', 'glade-3', 'glade-previewer'], DEV, 'Glade')
def glade(c):
    c.rrect(3, 4, 28, 27, 'W', 2)
    c.rect(3, 4, 28, 8, 'G')
    c.bevel(['W', 'G'])
    c.rect(5, 10, 12, 25, 'w')
    c.rect(14, 10, 26, 15, 'g')
    c.rect(14, 17, 26, 25, 'w')
    c.rrect(16, 21, 24, 24, 'G', 1)
    c.outline()


@icon('ar.xjuan.Cambalache', ['cambalache', 'Cambalache'], DEV, 'Cambalache')
def cambalache(c):
    # pile of toy bricks
    c.rect(3, 18, 14, 28, 'R')
    c.rect(15, 18, 28, 28, 'B')
    c.rect(8, 7, 22, 17, 'Y')
    for x in (5, 10):
        c.rect(x, 16, x + 2, 17, 'R')
    for x in (18, 23):
        c.rect(x, 16, x + 2, 17, 'B')
    for x in (10, 15, 19):
        c.rect(x, 5, x + 2, 6, 'Y')
    c.bevel(['R', 'B', 'Y'])
    c.outline()


@icon('org.gnome.dspy', ['d-spy', 'dspy', 'D-Spy'], DEV, 'D-Spy')
def dspy(c):
    # bus lines under a magnifier
    for y, col in ((8, 'B'), (14, 'M'), (20, 'G')):
        c.rect(3, y, 22, y + 3, col)
    c.bevel(['B', 'M', 'G'], dark=False)
    c.line(22, 22, 27, 27, 'k', 2)
    c.circle(19.5, 19.5, 6, 'K')
    c.circle(19.5, 19.5, 4.5, 'c')
    c.outline()


@icon('d-feet', ['org.gnome.d-feet', 'dfeet'], DEV, 'D-Feet')
def dfeet(c):
    for x0, y0 in ((3, 8), (17, 4)):
        c.ellipse(x0 + 5, y0 + 13, 5, 8, 'p')
        for i in range(4):
            c.circle(x0 + 2 + i * 2.5, y0 + 3, 1.6, 'p')
    c.bevel(['p'])
    c.outline()


@icon('org.gnome.Sysprof', ['sysprof', 'sysprof-cli'], DEV, 'Sysprof')
def sysprof(c):
    # flame graph
    rows = [(3, 28, 'R'), (3, 20, 'O'), (22, 28, 'O'), (4, 12, 'Y'), (14, 19, 'Y'), (23, 26, 'Y'), (5, 9, 'y')]
    ys = [23, 18, 18, 13, 13, 13, 8]
    for (x0, x1, col), y in zip(rows, ys):
        c.rect(x0, y, x1, y + 4, col)
    c.bevel(['R', 'O', 'Y'])
    c.outline()


@icon('org.kde.kcachegrind', ['kcachegrind', 'qcachegrind', 'valgrind', 'callgrind'], DEV, 'KCachegrind')
def kcachegrind(c):
    # treemap
    c.rect(3, 4, 28, 27, 'K')
    for x0, y0, x1, y1, col in ((4, 5, 16, 18, 'B'), (18, 5, 27, 11, 'G'), (18, 13, 27, 18, 'Y'),
                                (4, 20, 10, 26, 'R'), (12, 20, 27, 26, 'M')):
        c.rect(x0, y0, x1, y1, col)
    c.bevel(['B', 'G', 'Y', 'R', 'M'], dark=False)
    c.outline()


@icon('org.kde.heaptrack', ['heaptrack', 'heaptrack_gui'], DEV, 'Heaptrack')
def heaptrack(c):
    # stacked area chart rising
    c.rect(3, 4, 28, 27, 'W')
    c.bevel(['W'])
    for x in range(4, 28):
        h1 = int(4 + (x - 4) * 0.6)
        h2 = int(2 + (x - 4) * 0.25)
        c.vline(x, 26 - h1, 26, 'B')
        c.vline(x, 26 - h1 - h2, 25 - h1, 'O')
    c.outline()


@icon('com.kdab.Hotspot', ['hotspot', 'perf', 'hotspot-perf'], DEV, 'Hotspot')
def hotspot(c):
    # flame in a target
    c.circle(16, 16, 13, 'W')
    c.ring(16, 16, 13, 11, 'R')
    c.bevel(['W'])
    c.circle(16, 19, 6, 'O')
    c.poly([(16, 6), (21, 15), (11, 15)], 'O')
    c.circle(16, 20, 3, 'Y')
    c.outline()


@icon('org.qt-project.designer', ['designer', 'qtdesigner', 'designer-qt6', 'designer6', 'designer-qt5',
                                  'QtProject-designer'], DEV, 'Qt Designer')
def qtdesigner(c):
    def g(c):
        c.line(25, 12, 15, 22, 'O', 3)
        c.pixels([(14, 24), (15, 25), (14, 25)], 'k')
        c.rect(7, 7, 20, 9, 'W'); c.rect(7, 7, 9, 20, 'W')
    _qt(c, g)
    c.outline()


@icon('org.qt-project.linguist', ['linguist', 'linguist-qt6', 'linguist6', 'linguist-qt5',
                                  'QtProject-linguist'], DEV, 'Qt Linguist')
def qtlinguist(c):
    def g(c):
        c.rrect(15, 14, 28, 25, 'W', 3)
        c.poly([(18, 24), (22, 24), (17, 29)], 'W')
        c.text(7, 7, 'A', 'W')
        c.text(19, 17, 'Z', 'G', font=3)
    _qt(c, g)
    c.outline()


@icon('org.qt-project.assistant', ['assistant', 'assistant-qt6', 'assistant6', 'assistant-qt5',
                                   'QtProject-assistant'], DEV, 'Qt Assistant')
def qtassistant(c):
    def g(c):
        c.text(9, 8, '?', 'W', scale=2)
    _qt(c, g)
    c.outline()


@icon('org.kde.umbrello', ['umbrello', 'umbrello5'], DEV, 'Umbrello')
def umbrello(c):
    c.ellipse(16, 15, 13, 11, 'B')
    c.rect(2, 15, 30, 31, '.')
    c.bevel(['B'])
    for x in (8, 16, 24):
        c.circle(x, 16, 2.5, '.') if False else None
    c.rect(15, 15, 16, 26, 'S')
    c.ring(13, 26, 3, 1.5, 'S')
    c.rect(10, 22, 13, 26, '.')
    c.outline()


@icon('org.gnome.Devhelp', ['devhelp'], DEV, 'Devhelp')
def devhelp(c):
    c.rect(5, 3, 26, 28, 'B')
    c.rect(5, 3, 8, 28, '6')
    c.bevel(['B'])
    c.rect(24, 5, 26, 27, 'W')
    c.text(12, 9, '?', 'W', scale=2) if False else c.text(13, 12, '?', 'W')
    c.outline()


@icon('org.zealdocs.Zeal', ['zeal', 'Zeal'], DEV, 'Zeal')
def zeal(c):
    # stack of docsets with a bolt
    for i, col in enumerate(['R', 'O', 'Y']):
        y = 20 - i * 6
        c.rect(4 + i * 2, y, 23 + i * 2, y + 6, col)
        c.rect(5 + i * 2, y + 4, 22 + i * 2, y + 5, 'W')
    c.bevel(['R', 'O', 'Y'])
    c.outline()


@icon('putty', ['putty-gtk', 'pterm'], DEV, 'PuTTY')
def putty(c):
    # two PCs linked by a lightning bolt
    c.rect(3, 4, 14, 13, 'w'); c.rect(5, 6, 12, 11, 'B')
    c.rect(17, 17, 28, 26, 'w'); c.rect(19, 19, 26, 24, 'B')
    c.rect(6, 14, 11, 15, 'S'); c.rect(20, 27, 25, 28, 'S')
    c.bevel(['w'])
    c.poly([(19, 3), (14, 12), (17, 12), (12, 20), (22, 9), (18, 9), (22, 3)], 'Y')
    c.outline()


@icon('filezilla', ['FileZilla', 'org.filezillaproject.Filezilla', 'filezilla-bin'], DEV, 'FileZilla')
def filezilla(c):
    c.rrect(3, 3, 28, 28, 'R', 3)
    c.bevel(['R'])
    c.rect(7, 7, 17, 10, 'W'); c.rect(7, 7, 10, 24, 'W'); c.rect(7, 14, 15, 17, 'W')
    c.poly([(16, 17), (25, 17), (25, 19), (20, 23), (25, 23), (25, 25), (16, 25), (16, 23), (21, 19), (16, 19)], 'W')
    c.outline()


# ====================================================================== diff / hex / reverse engineering

def _twodocs(c, a, b):
    c.rect(3, 4, 14, 27, 'W'); c.rect(17, 4, 28, 27, 'W')
    c.shade_below(['W'], 'w')
    for i in range(7):
        y = 7 + i * 3
        c.hline(5, 12, y, a if i in (2, 3) else 'S')
        c.hline(19, 26, y, b if i in (2, 3, 5) else 'S')


@icon('org.kde.kdiff3', ['kdiff3'], DEV, 'KDiff3')
def kdiff3(c):
    _twodocs(c, 'R', 'G')
    c.text(11, 12, '3', 'B') if False else None
    c.outline()


@icon('org.kde.kompare', ['kompare'], DEV, 'Kompare')
def kompare(c):
    _twodocs(c, 'B', 'O')
    c.poly([(12, 14), (20, 14), (20, 11), (24, 15.5), (20, 20), (20, 17), (12, 17)], 'B')
    c.outline()


@icon('io.github.mightycreak.Diffuse', ['diffuse'], DEV, 'Diffuse')
def diffuse(c):
    _twodocs(c, 'M', 'C')
    c.outline()


@icon('net.werwolv.ImHex', ['imhex', 'imhex-bin', 'ImHex'], DEV, 'ImHex')
def imhex(c):
    pts = [(16 + 13.5 * math.cos(math.radians(a)), 16 + 13.5 * math.sin(math.radians(a))) for a in range(0, 360, 60)]
    c.poly(pts, 'k')
    c.bevel(['k'], dark=False)
    for j in range(4):
        for i in range(4):
            col = 'C' if (i + j) % 3 else 'M'
            c.rect(8 + i * 4, 9 + j * 4, 9 + i * 4, 10 + j * 4, col)
    c.outline()


@icon('org.kde.okteta', ['okteta'], DEV, 'Okteta')
def okteta(c):
    c.rect(4, 3, 27, 28, 'W')
    c.bevel(['W'])
    c.rect(4, 3, 8, 28, 'B')
    for j in range(6):
        for i in range(4):
            c.hline(10 + i * 4, 11 + i * 4, 6 + j * 4, 'S' if (i + j) % 4 else 'B')
    c.outline()


@icon('org.gnome.GHex', ['ghex'], DEV, 'GHex')
def ghex(c):
    c.rect(4, 3, 27, 28, 'W')
    c.bevel(['W'])
    c.text(6, 6, '0F', 'B', font=3)
    c.text(16, 6, 'A3', 'S', font=3)
    c.text(6, 13, 'C7', 'S', font=3)
    c.text(16, 13, '1E', 'B', font=3)
    c.text(6, 20, '5D', 'B', font=3)
    c.text(16, 20, '9B', 'S', font=3)
    c.outline()


@icon('ghidra', ['org.ghidra_sre.Ghidra', 'ghidra-bin', 'Ghidra'], DEV, 'Ghidra')
def ghidra(c):
    # red dragon head
    c.poly([(5, 10), (3, 4), (11, 8)], 'R')
    c.poly([(13, 6), (16, 3), (18, 7)], 'R')
    c.rrect(4, 7, 20, 22, 'R', 5)
    c.poly([(16, 12), (28, 16), (28, 22), (14, 24)], 'R')
    c.rect(6, 20, 12, 28, 'R')
    c.bevel(['R'])
    c.rect(10, 12, 12, 13, 'Y'); c.px(11, 12, 'K')
    c.pixels([(25, 17), (26, 17)], '1')
    c.hline(16, 27, 20, '1')
    c.outline()


@icon('re.rizin.cutter', ['cutter', 'cutter-re', 'rz-cutter', 'Cutter'], DEV, 'Cutter')
def cutter(c):
    # utility knife blade
    c.poly([(3, 26), (18, 11), (24, 17), (9, 30)], 'S') if False else None
    c.poly([(3, 22), (17, 8), (23, 14), (9, 28)], 'k')
    c.poly([(17, 8), (27, 3), (29, 5), (23, 14)], 'w')
    c.bevel(['w'])
    c.line(19, 9, 24, 6, 'W')
    c.line(8, 21, 15, 14, 'R', 2)
    c.outline()


@icon('ida', ['ida64', 'ida-free', 'idafree', 'ida-pro', 'com.hex-rays.IDA', 'ida-free-bin'], DEV, 'IDA')
def ida(c):
    # portrait in an oval frame
    c.ellipse(16, 16, 12, 13, 'O')
    c.ellipse(16, 16, 10, 11, 'b')
    c.bevel(['O'])
    c.circle(16, 12, 4, 'n')
    c.ellipse(16, 24.5, 7, 5, 'M')
    c.ellipse(16, 16, 12, 14, '.') if False else None
    c.rect(11, 9, 21, 10, '8')
    c.outline()


# ====================================================================== security

@icon('burpsuite', ['burp', 'burpsuite-community', 'burpsuite-pro', 'com.portswigger.burp', 'burpsuite-bin',
                    'BurpSuiteCommunity'], DEV, 'Burp Suite')
def burpsuite(c):
    c.rrect(3, 3, 28, 28, 'O', 5)
    c.bevel(['O'])
    c.poly([(18, 5), (9, 17), (15, 17), (12, 27), (23, 13), (17, 13), (20, 5)], 'W')
    c.outline()


@icon('zaproxy', ['org.zaproxy.ZAP', 'owasp-zap', 'zaproxy-bin', 'ZAP'], DEV, 'ZAP')
def zaproxy(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.poly([(19, 3), (8, 18), (15, 18), (11, 29), (24, 13), (17, 13), (22, 3)], 'Y')
    c.outline()


@icon('zenmap', ['nmap', 'nmap-zenmap', 'zenmap-root', 'org.nmap.Zenmap'], DEV, 'Zenmap')
def zenmap(c):
    # radar eye
    c.ellipse(16, 16, 13.5, 9, 'W')
    c.bevel(['W'])
    c.circle(16, 16, 7, 'G')
    c.ring(16, 16, 5, 4, '4')
    c.line(16, 16, 21, 12, 'g')
    c.circle(16, 16, 1.5, 'K')
    c.outline()


@icon('metasploit', ['msfconsole', 'metasploit-framework', 'msfgui', 'msf', 'armitage'], DEV, 'Metasploit')
def metasploit(c):
    c.poly([(4, 4), (28, 4), (28, 17), (16, 29), (4, 17)], 'B')
    c.bevel(['B'])
    c.poly([(8, 9), (12, 9), (16, 15), (20, 9), (24, 9), (24, 21), (20, 21), (20, 15), (16, 20), (12, 15),
            (12, 21), (8, 21)], 'W')
    c.outline()


@icon('bettercap', ['bettercap-ui', 'bettercap-bin'], DEV, 'bettercap')
def bettercap(c):
    # baseball cap
    c.ellipse(16, 17, 11, 11, 'R')
    c.rect(4, 17, 28, 30, '.')
    c.rrect(3, 17, 28, 22, 'R', 2)
    c.poly([(16, 17), (29, 17), (29, 22), (14, 22)], 'k')
    c.rect(29, 15, 31, 23, '.')
    c.bevel(['R'])
    c.rect(15, 6, 16, 7, '1')
    c.vline(15, 8, 16, '1')
    c.outline()


@icon('hashcat', ['hashcat-gui', 'hashcat-bin'], DEV, 'hashcat')
def hashcat(c):
    c.poly([(4, 13), (5, 3), (12, 9)], 'O')
    c.poly([(28, 13), (27, 3), (20, 9)], 'O')
    c.ellipse(16, 17, 12, 11, 'O')
    c.bevel(['O'])
    c.sprite(10, 13, """
        .#..#.
        ######
        .#..#.
        ######
        .#..#.
    """, {'#': 'K'})
    c.pixels([(8, 15), (9, 15), (22, 15), (23, 15)], 'K') if False else None
    c.rect(7, 13, 8, 14, 'K'); c.rect(23, 13, 24, 14, 'K')
    c.outline()


@icon('johnny', ['john', 'john-the-ripper', 'johntheripper', 'jtr'], DEV, 'John the Ripper')
def johnny(c):
    # top hat
    c.rrect(8, 3, 23, 22, 'k', 1)
    c.rrect(3, 22, 28, 27, 'k', 2)
    c.bevel(['k'], dark=False)
    c.rect(8, 17, 23, 20, 'R')
    c.outline()


@icon('maltego', ['maltego-ce', 'com.paterva.maltego', 'Maltego'], DEV, 'Maltego')
def maltego(c):
    for x0, y0, x1, y1 in ((16, 6, 7, 16), (16, 6, 25, 14), (7, 16, 12, 25), (25, 14, 22, 24), (7, 16, 25, 14)):
        c.line(x0, y0, x1, y1, 's', 2)
    for (x, y), col in (((16, 6), 'B'), ((7, 16), 'C'), ((25, 14), 'C'), ((12, 25), 'B'), ((22, 24), 'w')):
        c.circle(x + .5, y + .5, 3.5, col)
    c.bevel(['B', 'C'])
    c.outline()


@icon('ettercap', ['ettercap-gtk', 'ettercap-graphical', 'ettercap-ng'], DEV, 'Ettercap')
def ettercap(c):
    # spider in a web
    c.ring(16, 16, 13, 12, 'S')
    for k in range(8):
        a = math.radians(k * 45)
        c.line(16, 16, 16 + 12 * math.cos(a), 16 + 12 * math.sin(a), 'S')
    c.ring(16, 16, 7.5, 6.5, 'S')
    c.circle(16, 14, 3, 'k'); c.circle(16, 19, 4, 'k')
    for d in (-1, 1):
        c.line(16 + d * 3, 15, 16 + d * 7, 11, 'k'); c.line(16 + d * 3, 19, 16 + d * 8, 21, 'k')
    c.pixels([(15, 13), (17, 13)], 'R')
    c.outline()


@icon('ipscan', ['angryip', 'angryipscanner', 'angry-ip-scanner', 'org.angryip.ipscan', 'ipscan-bin'], DEV,
      'Angry IP Scanner')
def ipscan(c):
    c.circle(16, 16, 13, 'R')
    c.bevel(['R'])
    c.line(7, 9, 13, 12, 'K', 2); c.line(24, 9, 18, 12, 'K', 2)
    c.rect(9, 13, 12, 15, 'W'); c.rect(19, 13, 22, 15, 'W')
    c.rect(10, 14, 11, 15, 'K'); c.rect(20, 14, 21, 15, 'K')
    c.arc(16, 25, 6, 4, 200, 340, 'K')
    c.outline()


@icon('mitmproxy', ['mitmweb', 'mitmproxy-bin'], DEV, 'mitmproxy')
def mitmproxy(c):
    # man in the middle: two arrows through a dark core
    c.poly([(3, 9), (20, 9), (20, 5), (28, 11.5), (20, 18), (20, 14), (3, 14)], 'R')
    c.poly([(28, 18), (11, 18), (11, 14), (3, 20.5), (11, 27), (11, 23), (28, 23)], 'B')
    c.bevel(['R', 'B'])
    c.circle(16, 16, 4, 'k')
    c.outline()


@icon('caido', ['caido-desktop', 'caido-bin', 'Caido'], DEV, 'Caido')
def caido(c):
    c.rrect(3, 3, 28, 28, 'k', 5)
    c.bevel(['k'], dark=False)
    c.arc(16, 16, 9, 5.5, 45, 315, 'O')
    c.rect(19, 13, 25, 18, 'k')
    c.outline()


@icon('sqlmap', ['sqlmap-git'], DEV, 'sqlmap')
def sqlmap(c):
    # syringe
    c.line(6, 26, 10, 22, 'S')
    c.poly([(9, 19), (20, 8), (24, 12), (13, 23)], 'W')
    c.poly([(12, 18), (18, 12), (21, 15), (15, 21)], 'R')
    c.line(21, 6, 26, 11, 'S', 2)
    c.line(23, 9, 27, 5, 'S', 2)
    c.line(25, 3, 29, 7, 'S', 2)
    c.bevel(['W'])
    c.outline()


@icon('xhydra', ['hydra', 'thc-hydra', 'hydra-gtk'], DEV, 'Hydra')
def xhydra(c):
    # three-headed serpent
    for x, top in ((7, 7), (16, 4), (25, 7)):
        c.rect(x - 2, top + 3, x + 1, 22, 'G')
        c.circle(x, top + 2, 3.5, 'G')
    c.rrect(4, 18, 27, 28, 'G', 4)
    c.bevel(['G'])
    for x, top in ((7, 7), (16, 4), (25, 7)):
        c.px(x, top + 1, 'R')
    c.outline()


@icon('autopsy', ['autopsy-forensics', 'org.sleuthkit.autopsy'], DEV, 'Autopsy')
def autopsy(c):
    # magnifier over a fingerprint
    c.circle(13, 13, 10, 'W')
    for r in (8, 5.5, 3):
        c.ring(13, 14, r, r - 1, 'S')
    c.ring(13, 13, 10, 8, 'B')
    c.line(20, 20, 26, 26, 'N', 3)
    c.bevel(['B'])
    c.outline()


# ====================================================================== hardware / creative coding

@icon('com.flipperdevices.qFlipper', ['qflipper', 'qFlipper', 'qflipper-bin'], DEV, 'qFlipper')
def qflipper(c):
    c.rrect(3, 7, 28, 25, 'O', 5)
    c.bevel(['O'])
    c.rect(6, 10, 18, 20, 'o')
    c.rect(7, 11, 17, 19, 'K')
    c.sprite(8, 13, """
        .##......
        ####.#.#.
        #########
    """, {'#': 'O'})
    c.circle(23, 15, 3.5, 'W')
    c.circle(23, 15, 1.5, 'O')
    c.outline()


@icon('platformio', ['platformio-ide', 'pio', 'platformio-core'], DEV, 'PlatformIO')
def platformio(c):
    # ant head
    c.line(11, 8, 7, 2, 'k', 2); c.line(20, 8, 24, 2, 'k', 2)
    c.circle(16, 17, 11, 'O')
    c.bevel(['O'])
    c.circle(11.5, 15, 3.5, 'W'); c.circle(20.5, 15, 3.5, 'W')
    c.rect(11, 15, 12, 16, 'K'); c.rect(20, 15, 21, 16, 'K')
    c.hline(13, 18, 23, '2')
    c.outline()


@icon('org.sigrok.PulseView', ['pulseview', 'sigrok', 'PulseView'], DEV, 'PulseView')
def pulseview(c):
    c.rrect(3, 4, 28, 27, 'k', 2)
    c.bevel(['k'], dark=False)
    _wave(c, 7, 'G', [4, 3, 6, 2, 5])
    _wave(c, 14, 'Y', [2, 5, 3, 4, 7])
    _wave(c, 21, 'C', [6, 2, 2, 6, 5])
    c.outline()


@icon('io.github.gtkwave.GTKWave', ['gtkwave', 'GTKWave'], DEV, 'GTKWave')
def gtkwave(c):
    c.rect(3, 4, 28, 27, 'W')
    c.bevel(['W'])
    _wave(c, 7, 'B', [3, 3, 3, 3, 3, 3, 3])
    _wave(c, 14, 'R', [6, 6, 6])
    _wave(c, 21, 'G', [2, 4, 8, 2, 5])
    c.outline()


@icon('logisim-evolution', ['logisim', 'com.cburch.logisim', 'logisim-evolution-bin'], DEV, 'Logisim')
def logisim(c):
    # AND gate
    c.rect(8, 6, 15, 26, 'G')
    c.circle(15, 16, 10, 'G')
    c.rect(3, 6, 15, 26, '.') if False else None
    c.bevel(['G'])
    c.rect(3, 10, 7, 11, 'k'); c.rect(3, 21, 7, 22, 'k')
    c.rect(26, 15, 28, 16, 'k')
    c.outline()


@icon('processing', ['processing-ide', 'org.processing.processingide', 'processing4'], DEV, 'Processing')
def processing(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.poly([(8, 8), (18, 13), (8, 18)], 'W')
    c.rect(8, 21, 22, 23, 'W')
    c.outline()


@icon('love', ['love2d', 'org.love2d.love2d', 'love-11'], DEV, 'LÖVE')
def love(c):
    c.circle(16, 16, 13, 'P')
    c.arc(16, 16, 13, 0, 200, 20, 'C') if False else None
    for y in range(32):
        for x in range(32):
            if c.get(x, y) == 'P' and x + y > 34:
                c.px(x, y, 'C')
    c.bevel(['P', 'C'])
    c.circle(12, 13, 3.5, 'W'); c.circle(20, 13, 3.5, 'W')
    c.poly([(8.5, 14), (23.5, 14), (16, 23)], 'W')
    c.outline()
