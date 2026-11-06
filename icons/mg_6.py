"""Game launchers, emulators, streaming and gaming utilities."""
from pix import icon
import math


def big(c, x, y, art, col, k=2):
    lines = [l.strip() for l in art.strip('\n').split('\n')]
    for j, row in enumerate(lines):
        for i, ch in enumerate(row):
            if ch == '#':
                c.rect(x + i * k, y + j * k, x + i * k + k - 1, y + j * k + k - 1, col)


def dpad(c, x, y, col='k'):
    """5x5 d-pad, top-left x,y."""
    c.rect(x + 1, y, x + 3, y + 4, col) if False else None
    c.rect(x + 2, y, x + 2, y + 4, col)
    c.rect(x, y + 2, x + 4, y + 2, col)
    c.rect(x + 1, y + 1, x + 3, y + 3, col)


def screen(c, x0, y0, x1, y1, col='G', bezel='k'):
    c.rect(x0, y0, x1, y1, bezel)
    c.rect(x0 + 1, y0 + 1, x1 - 1, y1 - 1, col)
    c.dither(x0 + 1, y0 + 1, x1 - 1, y0 + 2, LIGHT.get(col, col), col)


LIGHT = {'G': 'g', 'C': 'c', 'B': 'b', 'M': 'm', 'Y': 'y', 'k': 's', 'g': 'W'}


# =================================================================== launchers

@icon('io.github.sharkwouter.Minigalaxy', ['minigalaxy'], 'games', 'Minigalaxy')
def minigalaxy(c):
    # ringed planet
    c.circle(16, 16, 9, 'M')
    c.bevel(['M'])
    c.hline(9, 20, 13, 'm')
    for t in range(0, 360, 1):
        a = math.radians(t)
        x, y = 13 * math.cos(a), 4 * math.sin(a)
        r = math.radians(-20)
        px_, py_ = 16 + x * math.cos(r) - y * math.sin(r), 16 + x * math.sin(r) + y * math.cos(r)
        if not (t > 200 and t < 340 and math.hypot(px_ - 16, py_ - 16) < 9):
            c.rect(int(px_), int(py_), int(px_), int(py_) + 1, 'Y')
    c.outline()


@icon('io.github.dummerle.rare', ['rare', 'Rare', 'legendary'], 'games', 'Rare')
def rare(c):
    # four-leaf clover
    for dx, dy in ((-5, -5), (5, -5), (-5, 5), (5, 5)):
        c.circle(16 + dx, 14 + dy, 5.5, 'G')
    c.bevel(['G'])
    c.line(16, 16, 21, 28, '4', 2)
    c.circle(16, 14, 2, 'g')
    c.outline()


@icon('io.github.Faugus.faugus-launcher', ['faugus-launcher', 'faugus'], 'games', 'Faugus Launcher')
def faugus(c):
    # fox head
    c.poly([(3, 3), (12, 9), (20, 9), (29, 3), (27, 16), (16, 29), (5, 16)], 'O')
    c.bevel(['O'])
    c.poly([(5, 16), (16, 29), (12, 18)], 'W')
    c.poly([(27, 16), (16, 29), (20, 18)], 'W')
    c.poly([(6, 6), (11, 9), (8, 12)], 'k'); c.poly([(26, 6), (21, 9), (24, 12)], 'k')
    c.rect(11, 15, 12, 16, 'K'); c.rect(20, 15, 21, 16, 'K')
    c.rect(15, 25, 17, 27, 'K')
    c.outline()


@icon('com.github.tkashkin.gamehub', ['gamehub', 'GameHub'], 'games', 'GameHub')
def gamehub(c):
    # hub: central node with four satellites
    for a in (45, 135, 225, 315):
        x, y = 16 + 9.5 * math.cos(math.radians(a)), 16 + 9.5 * math.sin(math.radians(a))
        c.line(16, 16, int(x), int(y), 'S', 2)
        c.circle(x, y, 5, 'B')
    c.circle(16, 16, 6.5, 'C')
    c.bevel(['C', 'B'])
    c.outline()


@icon('emudeck', ['EmuDeck', 'emudeck-bin'], 'games', 'EmuDeck')
def emudeck(c):
    # wide handheld with centre screen showing an E
    c.rrect(3, 8, 28, 24, 'k', 4)
    c.bevel(['k'])
    screen(c, 9, 10, 22, 21, 'M')
    big(c, 12, 12, """
        ####
        #...
        ###.
        #...
        ####
    """, 'W', 1) if False else c.text(13, 12, 'E', 'W', font=5)
    dpad(c, 4, 12, 's')
    c.circle(26, 13, 1, 's'); c.circle(26, 18, 1.5, 's')
    c.outline()


@icon('org.es_de.frontend', ['es-de', 'emulationstation-de', 'emulationstation', 'ES-DE'], 'games', 'ES-DE')
def esde(c):
    c.circle(16, 16, 13, 'R')
    c.bevel(['R'])
    c.circle(16, 16, 10, 'O')
    c.text(9, 12, 'ES', 'W', font=5)
    c.outline()


@icon('org.pegasus_frontend.Pegasus', ['pegasus-frontend', 'pegasus-fe', 'pegasus'], 'games', 'Pegasus')
def pegasus(c):
    # a single feathered wing
    for i, (y, x1) in enumerate(((5, 28), (10, 26), (15, 23), (20, 19), (25, 14))):
        c.rrect(3 + i, y, x1, y + 4, 'W' if i % 2 == 0 else 'w', 2)
    c.bevel(['W', 'w'])
    c.outline()


@icon('steamtinkerlaunch', ['SteamTinkerLaunch', 'stl'], 'games', 'Steam Tinker Launch')
def steamtinker(c):
    # wrench across a gear
    c.circle(13, 18, 7.5, 's')
    for a in range(0, 360, 45):
        x, y = 13 + 8.5 * math.cos(math.radians(a)), 18 + 8.5 * math.sin(math.radians(a))
        c.circle(x, y, 2, 's')
    c.circle(13, 18, 3, 'k')
    c.bevel(['s'])
    c.line(10, 24, 23, 10, 'w', 3)
    c.circle(24, 9, 4, 'w')
    c.rect(24, 5, 26, 8, '.')
    c.bevel(['w'])
    c.outline()


@icon('dev.lizardbyte.app.Sunshine', ['sunshine', 'sunshine-git'], 'games', 'Sunshine')
def sunshine(c):
    # sun rising behind a monitor
    c.circle(16, 14, 9, 'Y')
    for a in range(180, 361, 30):
        x, y = 16 + 12 * math.cos(math.radians(a)), 15 + 11 * math.sin(math.radians(a))
        c.rect(int(x) - 1, int(y) - 1, int(x), int(y), 'O')
    c.bevel(['Y'])
    c.rrect(5, 14, 26, 26, 'k', 1)
    c.rect(7, 16, 24, 24, 'B')
    c.rect(13, 27, 18, 28, 's')
    c.outline()


@icon('com.parsecgaming.parsec', ['parsec', 'parsecd', 'parsec-bin'], 'games', 'Parsec')
def parsec(c):
    # elongated orbit around a dot, teal
    for t in range(360):
        a = math.radians(t)
        x, y = 15.5 + 12 * math.cos(a), 16 + 6 * math.sin(a)
        c.rect(int(x), int(y), int(x) + 1, int(y) + 1, 'C')
    c.circle(16, 16, 4.5, 'M')
    c.bevel(['M'])
    c.circle(25, 10, 2.5, 'W')
    c.circle(16, 6, 1.5, 'c') if False else None
    c.outline()


@icon('io.github.streetpea.Chiaki4deck', ['chiaki', 're.chiaki.Chiaki', 'chiaki-ng', 'chiaki4deck',
                                          'io.github.streetpea.Chiaki-ng'], 'games', 'Chiaki')
def chiaki(c):
    # four face-button glyphs in a diamond
    c.poly([(16, 2.5), (29.5, 16), (16, 29.5), (2.5, 16)], 'k')
    c.poly([(16, 6), (19.5, 11), (12.5, 11)], 'G')
    c.ring(22.5, 16, 3, 1.5, 'R')
    c.rect(8, 14, 11, 17, 'P'); c.rect(9, 15, 10, 16, 'k')
    c.line(14, 19, 18, 23, 'B'); c.line(18, 19, 14, 23, 'B')
    c.outline()


@icon('io.github.unknownskl.greenlight', ['greenlight', 'Greenlight'], 'games', 'Greenlight')
def greenlight(c):
    # traffic light, green lit
    c.rrect(9, 3, 22, 28, 'k', 3)
    c.bevel(['k'])
    c.circle(15.5, 8, 3, '1')
    c.circle(15.5, 15.5, 3, '3')
    c.circle(15.5, 23, 3.5, 'G')
    c.px(14, 21, 'g'); c.px(15, 21, 'W')
    c.rect(5, 6, 8, 9, 's'); c.rect(23, 6, 26, 9, 's')
    c.outline()


@icon('page.kramo.Cartridges', ['cartridges'], 'games', 'Cartridges')
def cartridges(c):
    # two stacked game carts
    for dx, dy, col in ((7, 0, 'M'), (0, 6, 'B')):
        c.rect(3 + dx, 3 + dy, 21 + dx, 22 + dy, col)
        c.rect(3 + dx, 3 + dy, 21 + dx, 5 + dy, LIGHT[col])
        c.rect(6 + dx, 9 + dy, 18 + dx, 17 + dy, 'W')
        for x in range(6 + dx, 19 + dx, 2):
            c.px(x, 21 + dy, DARKM[col])
    c.outline()


DARKM = {'M': '7', 'B': '6', 'R': '1', 'S': 's', 'w': 'S', 'N': '8', 'G': '4'}


@icon('org.gnome.World.Highscore', ['highscore', 'org.gnome.Games', 'gnome-games'], 'games', 'Highscore')
def highscore(c):
    # trophy cup
    c.poly([(8, 3), (24, 3), (23, 13), (16, 18), (9, 13)], 'Y')
    c.ring(7, 8, 4.5, 2.5, 'Y'); c.ring(25, 8, 4.5, 2.5, 'Y')
    c.rect(3, 3, 7, 7, '.') if False else None
    c.rect(14, 18, 17, 22, 'Y')
    c.rect(9, 23, 22, 27, 'N')
    c.bevel(['Y', 'N'])
    c.rect(13, 24, 18, 25, 'y')
    c.outline()


@icon('com.valvesoftware.SteamLink', ['steamlink', 'steam-link'], 'games', 'Steam Link')
def steamlink(c):
    # two chain links
    c.rrect(3, 9, 17, 22, 'B', 5)
    c.rrect(7, 13, 13, 18, '.', 2)
    c.rrect(14, 9, 28, 22, 'b', 5)
    c.rrect(18, 13, 24, 18, '.', 2)
    c.rect(14, 13, 16, 18, 'B')
    c.bevel(['B', 'b'])
    c.outline()


@icon('com.github.Matoking.protontricks', ['protontricks', 'protontricks-gui'], 'games', 'Protontricks')
def protontricks(c):
    # magician top hat + wand
    c.rect(9, 5, 22, 20, 'k')
    c.bevel(['k'])
    c.rect(9, 16, 22, 18, 'M')
    c.rrect(3, 20, 28, 24, 'k', 2)
    c.line(19, 27, 26, 20, 'k', 2)
    c.rect(26, 19, 27, 20, 'W')
    c.px(25, 5, 'Y'); c.px(27, 8, 'Y'); c.px(5, 8, 'Y')
    c.outline()


@icon('com.vysp3r.ProtonPlus', ['protonplus', 'ProtonPlus'], 'games', 'ProtonPlus')
def protonplus(c):
    # atom with a plus nucleus
    for a in (0, 60, 120):
        for t in range(0, 360, 2):
            r = math.radians(t)
            x, y = 12.5 * math.cos(r), 4.5 * math.sin(r)
            ra = math.radians(a)
            c.px(int(16 + x * math.cos(ra) - y * math.sin(ra)), int(16 + x * math.sin(ra) + y * math.cos(ra)), 'M')
    c.rect(14, 10, 17, 21, 'W'); c.rect(10, 14, 21, 17, 'W')
    c.outline()


@icon('com.github.mtkennerly.ludusavi', ['ludusavi'], 'games', 'Ludusavi')
def ludusavi(c):
    # floppy disk with a gamepad label
    c.poly([(3, 3), (24, 3), (28, 7), (28, 28), (3, 28)], 'B')
    c.bevel(['B'])
    c.rect(8, 3, 21, 11, 'w')
    c.rect(17, 5, 19, 9, 'B')
    c.rect(6, 15, 25, 28, 'W')
    c.rrect(9, 18, 22, 24, 'S', 2)
    c.rect(11, 20, 13, 22, 'k') if False else (c.hline(10, 13, 21, 'k'), c.vline(11, 20, 22, 'k') if False else c.vline(12, 20, 22, 'k'))
    c.px(19, 20, 'R'); c.px(20, 22, 'G')
    c.outline()


@icon('io.github.berarma.Oversteer', ['oversteer'], 'games', 'Oversteer')
def oversteer(c):
    # racing steering wheel
    c.ring(16, 16, 13, 9.5, 'k')
    c.bevel(['k'])
    c.rect(6, 15, 25, 18, 'k')
    c.rect(14, 18, 17, 26, 'k')
    c.rrect(12, 13, 19, 20, 's', 2)
    c.rect(15, 3, 16, 6, 'R')
    c.outline()


@icon('sc-controller', ['com.github.kozec.sc-controller', 'scc'], 'games', 'SC Controller')
def sccontroller(c):
    # Steam Controller: two round trackpads
    c.poly([(5, 8), (27, 8), (29, 24), (24, 28), (20, 22), (12, 22), (8, 28), (3, 24)], 'k')
    c.bevel(['k'])
    c.circle(10, 14, 4.5, 's'); c.circle(22, 14, 4.5, 's')
    c.circle(10, 14, 2.5, 'S'); c.circle(22, 14, 2.5, 'S')
    c.circle(16, 19, 1.5, 'B')
    c.outline()


@icon('io.github.radiolamp.mangojuice', ['mangojuice'], 'games', 'MangoJuice')
def mangojuice(c):
    # juice glass with a mango slice and straw
    c.poly([(7, 9), (25, 9), (23, 28), (9, 28)], 'w')
    c.poly([(8, 13), (24, 13), (23, 27), (9, 27)], 'O')
    c.bevel(['O'])
    c.line(18, 25, 24, 3, 'R', 2)
    c.ellipse(9, 9, 5, 4, 'Y')
    c.bevel(['Y'])
    c.outline()


# =================================================================== emulators

@icon('io.mgba.mGBA', ['mgba', 'mgba-qt', 'mGBA'], 'emulator', 'mGBA')
def mgba(c):
    # widescreen handheld, purple
    c.rrect(3, 8, 28, 24, 'M', 5)
    c.bevel(['M'])
    screen(c, 10, 10, 21, 20, 'G')
    dpad(c, 4, 13, 'k')
    c.circle(25, 14, 1.5, '7'); c.circle(23.5, 18, 1.5, '7')
    c.outline()


@icon('sameboy', ['io.github.sameboy', 'sameboy-gtk', 'gearboy', 'gambatte'], 'emulator', 'SameBoy')
def sameboy(c):
    # brick handheld, portrait
    c.rrect(7, 3, 24, 28, 'w', 1)
    c.rrect(7, 22, 24, 28, 'w', 3)
    c.bevel(['w'])
    c.rect(9, 4, 22, 14, 's')
    screen(c, 11, 5, 20, 13, 'g', 's')
    dpad(c, 9, 18, 'k')
    c.circle(21, 18, 1.2, 'M'); c.circle(19, 20, 1.2, 'M')
    c.hline(18, 21, 25, 'S'); c.hline(18, 21, 27, 'S')
    c.outline()


@icon('net.kuribo64.melonDS', ['melonds', 'melonDS'], 'emulator', 'melonDS')
def melonds(c):
    # half melon
    c.arc(16, 11, 13, 0, 0, 180, 'G')
    c.arc(16, 11, 11, 0, 0, 180, 'O')
    c.rect(3, 11, 28, 11, 'G') if False else None
    c.bevel(['G'])
    c.arc(16, 11, 4, 0, 0, 180, 'y')
    for a in (30, 60, 90, 120, 150):
        x, y = 16 + 7 * math.cos(math.radians(a)), 11 + 7 * math.sin(math.radians(a))
        c.px(int(x), int(y), 'k')
    c.outline()


@icon('org.desmume.DeSmuME', ['desmume', 'desmume-glade', 'desmume-cli'], 'emulator', 'DeSmuME')
def desmume(c):
    # open clamshell, two screens stacked
    c.rrect(6, 3, 25, 14, 'S', 2)
    c.rrect(6, 16, 25, 28, 'S', 2)
    c.bevel(['S'])
    screen(c, 10, 5, 21, 12, 'C')
    screen(c, 10, 18, 21, 26, 'C')
    c.rect(6, 14, 25, 15, 's')
    c.outline()


@icon('org.citra_emu.citra', ['citra', 'citra-qt', 'citra-emu'], 'emulator', 'Citra')
def citra(c):
    # lemon slice
    c.circle(16, 16, 13, 'Y')
    c.circle(16, 16, 11, 'y')
    for i in range(8):
        a = math.radians(i * 45)
        c.line(16, 16, int(16 + 10 * math.cos(a)), int(16 + 10 * math.sin(a)), 'W')
    c.circle(16, 16, 2, 'W')
    c.bevel(['Y'])
    c.outline()


@icon('io.github.lime3ds.Lime3DS', ['lime3ds', 'lime3ds-gui', 'lime-qt'], 'emulator', 'Lime3DS')
def lime3ds(c):
    # whole lime with leaf
    c.ellipse(15, 18, 12, 10, 'G')
    c.bevel(['G'])
    c.px(9, 13, 'g'); c.px(10, 12, 'g'); c.px(11, 12, 'W')
    c.poly([(16, 8), (26, 3), (24, 9)], '4')
    c.outline()


@icon('org.azahar_emu.Azahar', ['azahar', 'azahar-gui'], 'emulator', 'Azahar')
def azahar(c):
    # orange blossom: five white petals
    for i in range(5):
        a = math.radians(-90 + 72 * i)
        c.circle(16 + 8 * math.cos(a), 16 + 8 * math.sin(a), 5.5, 'W')
    c.bevel(['W'])
    c.circle(16, 16, 4, 'O')
    c.px(15, 15, 'Y')
    c.outline()


@icon('org.yuzu_emu.yuzu', ['yuzu', 'yuzu-mainline', 'yuzu-early-access', 'org.suyu_emu.suyu', 'suyu'],
      'emulator', 'yuzu / suyu')
def yuzu(c):
    # two detached half-pills, red + blue
    c.rrect(3, 3, 14, 28, 'B', 5)
    c.rrect(17, 3, 28, 28, 'R', 5)
    c.bevel(['B', 'R'])
    c.circle(8.5, 10, 2, 'k')
    c.circle(22.5, 19, 2, 'k')
    c.outline()


@icon('org.sudachi_emu.sudachi', ['sudachi'], 'emulator', 'Sudachi')
def sudachi(c):
    # small round green citrus cut in half
    c.circle(16, 17.5, 11.5, '4')
    c.circle(16, 17.5, 9.5, 'g')
    for i in range(6):
        a = math.radians(i * 60 + 30)
        c.line(16, 17, int(16 + 9 * math.cos(a)), int(17 + 9 * math.sin(a)), 'W')
    c.poly([(16, 6.5), (22, 3.5), (21, 7)], 'G')
    c.outline()


@icon('info.cemu.Cemu', ['cemu', 'Cemu'], 'emulator', 'Cemu')
def cemu(c):
    # tablet gamepad with sticks
    c.rrect(3, 8, 28, 24, 'w', 3)
    c.bevel(['w'])
    screen(c, 9, 10, 22, 20, 'C')
    c.circle(6, 12, 2, 'k'); c.circle(25, 12, 2, 'k')
    dpad(c, 4, 17, 's')
    c.circle(25.5, 19, 1.2, 'C')
    c.outline()


@icon('com.snes9x.Snes9x', ['snes9x', 'snes9x-gtk', 'snes9x-qt'], 'emulator', 'Snes9x')
def snes9x(c):
    # dog-bone pad with four coloured buttons
    c.circle(9, 16, 6.5, 'w'); c.circle(23, 16, 6.5, 'w')
    c.rect(9, 10, 23, 22, 'w')
    c.bevel(['w'])
    dpad(c, 5, 14, 'k')
    for x, y, col in ((23, 12, 'B'), (27, 16, 'R'), (19, 16, 'G'), (23, 20, 'Y')):
        c.circle(x - .5, y, 1.6, col) if False else c.rect(x - 1, y - 1, x, y, col)
    c.hline(13, 15, 18, 'S'); c.hline(17, 19, 18, 'S')
    c.outline()


@icon('dev.bsnes.bsnes', ['bsnes', 'bsnes-hd', 'bsnes-plus'], 'emulator', 'bsnes')
def bsnes(c):
    # grey cartridge with ridges and label
    c.poly([(5, 3), (26, 3), (26, 22), (28, 22), (28, 28), (3, 28), (3, 22), (5, 22)], 'S')
    c.bevel(['S'])
    c.rect(8, 6, 23, 18, 'W')
    c.rect(9, 7, 22, 12, 'M')
    c.text(13, 13, 'B', 'k', font=3) if False else None
    for x in range(6, 26, 3):
        c.vline(x, 23, 26, 's')
    c.outline()


@icon('dev.ares.ares', ['ares', 'higan', 'ares-emu'], 'emulator', 'ares')
def ares(c):
    # greek war helmet with crest
    c.poly([(9, 3), (24, 3), (27, 6), (22, 8), (12, 8)], 'R')
    c.ellipse(16, 17, 10.5, 9.5, 'Y')
    c.rect(6, 17, 26, 28, 'Y')
    c.bevel(['Y', 'R'])
    c.rect(10, 15, 22, 18, 'K')
    c.rect(14, 18, 17, 28, 'K')
    c.rect(6, 28, 13, 28, '3') if False else None
    c.outline()


@icon('ca.mesen.Mesen', ['mesen', 'Mesen', 'mesen2', 'nestopia', 'org.nestopia.Nestopia'], 'emulator', 'Mesen')
def mesen(c):
    # flat rectangular pad, red round buttons
    c.rect(3, 9, 28, 22, 'w')
    c.rect(5, 11, 26, 20, 'k')
    c.bevel(['w'])
    dpad(c, 6, 13, 'S')
    c.circle(21, 17, 1.8, 'R'); c.circle(25, 17, 1.8, 'R')
    c.hline(13, 14, 17, 'S'); c.hline(16, 17, 17, 'S')
    c.outline()


@icon('fceux', ['com.fceux.FCEUX'], 'emulator', 'FCEUX')
def fceux(c):
    # light-gun pistol
    c.rect(3, 8, 24, 14, 'O')
    c.rect(24, 9, 28, 13, 'O')
    c.poly([(14, 14), (22, 14), (23, 27), (17, 27)], 'O')
    c.bevel(['O'])
    c.arc(13.5, 15, 4, 2.5, 0, 180, '2')
    c.rect(4, 9, 6, 10, 'k')
    c.outline()


@icon('com.github.Rosalie241.RMG', ['RMG', 'rmg', 'mupen64plus', 'mupen64plus-qt', 'm64p', 'simple64'],
      'emulator', 'Rosalie\'s Mupen GUI')
def rmg(c):
    # three-pronged controller
    c.rrect(3, 7, 28, 15, 'S', 3)
    c.rrect(3, 10, 9, 25, 'S', 2)
    c.rrect(13, 10, 18, 28, 'S', 2)
    c.rrect(22, 10, 28, 25, 'S', 2)
    c.bevel(['S'])
    dpad(c, 4, 9, 'k')
    c.circle(15.5, 15, 1.5, 'k')
    c.rect(23, 9, 24, 10, 'B'); c.rect(25, 11, 26, 12, 'G')
    c.rect(20, 8, 21, 9, 'Y')
    c.outline()


@icon('org.flycast.Flycast', ['flycast', 'flycast-dc'], 'emulator', 'Flycast')
def flycast(c):
    # orange swirl
    c.circle(16, 16, 13, 'W')
    c.bevel(['W'])
    for t in range(0, 700):
        a = t / 80.0
        r = 1.5 + a * 1.35
        x, y = 16 + r * math.cos(a), 16 + r * math.sin(a)
        c.rect(int(x), int(y), int(x), int(y), 'O')
        c.px(int(x + .7), int(y), 'O')
    c.outline()


@icon('redream', ['io.recompiled.redream', 'redream-bin'], 'emulator', 'redream')
def redream(c):
    # memory-card with tiny LCD (VMU style)
    c.rrect(7, 3, 24, 28, 'R', 4)
    c.bevel(['R'])
    screen(c, 10, 6, 21, 14, 'g', 'k')
    dpad(c, 9, 18, 'k')
    c.circle(20.5, 19, 1.2, 'W'); c.circle(22.5, 22, 1.2, 'W')
    c.outline()


@icon('pcsx-redux', ['pcsx-redux-git', 'pcsx-redux-bin', 'pcsxr', 'pcsx-reloaded'], 'emulator', 'PCSX-Redux')
def pcsxredux(c):
    # grey disc console with lid circle and two ports
    c.rect(3, 8, 28, 24, 'w')
    c.bevel(['w'])
    c.circle(12, 15, 6, 'S')
    c.circle(12, 15, 2, 's')
    c.rect(21, 11, 25, 13, 'S'); c.rect(21, 15, 25, 17, 'S')
    c.rect(5, 21, 9, 22, 's'); c.rect(14, 21, 18, 22, 's')
    c.px(23, 20, 'G')
    c.outline()


@icon('app.xemu.xemu', ['xemu'], 'emulator', 'xemu')
def xemu(c):
    # green orb with a bold X
    c.circle(16, 16, 13, 'G')
    c.bevel(['G'])
    c.circle(12, 11, 3, 'g')
    c.line(9, 9, 22, 23, 'W', 3); c.line(22, 9, 9, 23, 'W', 3)
    c.outline()


@icon('xenia', ['xenia-canary', 'jp.xenia.Xenia', 'xenia_canary'], 'emulator', 'Xenia')
def xenia(c):
    # ring of light, four quadrants
    c.circle(16, 16, 13, 'k')
    c.ring(16, 16, 10, 6.5, 'G')
    for a in (45, 135, 225, 315):
        c.line(16, 16, int(16 + 12 * math.cos(math.radians(a))), int(16 + 12 * math.sin(math.radians(a))), 'k', 2)
    c.circle(16, 16, 4, 's')
    c.circle(16, 16, 2.5, 'g')
    c.outline()


@icon('vita3k', ['org.vita3k.Vita3K', 'Vita3K'], 'emulator', 'Vita3K')
def vita3k(c):
    # pill-shaped handheld with wide screen, two sticks
    c.rrect(3, 9, 28, 23, 'k', 6)
    c.bevel(['k'])
    screen(c, 9, 11, 22, 21, 'B')
    c.circle(6, 18, 1.5, 's'); c.circle(25, 18, 1.5, 's')
    c.px(5, 13, 'S'); c.px(26, 13, 'S')
    c.outline()


@icon('net.shadps4.shadPS4', ['shadps4', 'shadPS4', 'shadps4-qt'], 'emulator', 'shadPS4')
def shadps4(c):
    # slim slanted console slab, blue light strip
    c.poly([(5, 10), (29, 10), (27, 16), (3, 16)], 'k')
    c.poly([(3, 17), (27, 17), (25, 23), (2.5, 23)], 'k')
    c.poly([(3, 16), (27, 16), (27, 17), (3, 17)], 'b')
    c.bevel(['k'])
    c.outline()


@icon('org.mamedev.MAME', ['mame', 'mame-tools', 'qmc2', 'groovymame'], 'emulator', 'MAME')
def mame(c):
    # arcade cabinet
    c.poly([(7, 3), (24, 3), (24, 12), (27, 18), (27, 28), (5, 28), (5, 18), (7, 12)], 'B')
    c.bevel(['B'])
    c.rect(7, 3, 24, 6, 'Y')
    screen(c, 9, 8, 22, 15, 'k', 'K')
    c.text(10, 9, 'MAME', 'Y', font=3) if False else None
    c.poly([(5, 18), (27, 18), (25, 21), (7, 21)], 'S')
    c.rect(10, 16, 11, 18, 'k'); c.rect(10, 15, 11, 15, 'R')
    c.px(18, 18, 'R'); c.px(21, 18, 'G')
    c.outline()


@icon('dosbox', ['dosbox-x', 'com.dosbox.DOSBox', 'com.dosbox_x.DOSBox-X', 'dosbox-svn'], 'emulator', 'DOSBox')
def dosbox(c):
    # cardboard box labelled DOS
    c.poly([(3, 9), (12, 4), (29, 7), (20, 12)], 'n')
    c.poly([(3, 9), (20, 12), (20, 28), (3, 24)], 'N')
    c.poly([(20, 12), (29, 7), (29, 23), (20, 28)], '8')
    c.text(5, 15, 'DOS', 'W', font=3)
    c.outline()


@icon('io.github.dosbox-staging', ['dosbox-staging', 'dosbox-staging-git'], 'emulator', 'DOSBox Staging')
def dosboxstaging(c):
    # CRT showing a C:\> prompt
    c.rrect(3, 4, 28, 23, 'w', 2)
    c.bevel(['w'])
    c.rect(5, 6, 26, 20, 'K')
    c.text(7, 9, 'C:', 'S', font=3) if False else c.text(7, 9, 'C', 'S', font=3)
    c.px(11, 10, 'S'); c.px(11, 12, 'S')
    c.text(13, 9, '>', 'S', font=3)
    c.rect(17, 12, 19, 13, 'G')
    c.rect(9, 24, 22, 28, 'S')
    c.outline()


@icon('org.scummvm.ScummVM', ['scummvm', 'ScummVM'], 'emulator', 'ScummVM')
def scummvm(c):
    # treasure chest with green glow
    c.rect(3, 15, 28, 28, 'N')
    c.ellipse(15.5, 15, 12.5, 7, 'N')
    c.rect(3, 15, 28, 15, 'N')
    c.bevel(['N'])
    c.hline(3, 28, 15, 'K')
    c.vline(9, 9, 28, 'Y'); c.vline(22, 9, 28, 'Y')
    c.rect(14, 13, 17, 18, 'Y')
    c.px(15, 16, 'k')
    c.outline()


@icon('stella', ['io.github.stella_emu.Stella', 'Stella'], 'emulator', 'Stella')
def stella(c):
    # joystick: black base, stick, red button
    c.rrect(3, 18, 28, 28, 'k', 2)
    c.bevel(['k'])
    c.rect(14, 6, 17, 20, 's')
    c.circle(15.5, 7, 3.5, 'k')
    c.circle(7, 18, 3, 'R')
    c.px(6, 17, 'r')
    c.outline()


@icon('hatari', ['org.tuxfamily.hatari', 'hatariui'], 'emulator', 'Hatari')
def hatari(c):
    # wedge keyboard computer with floppy slot
    c.poly([(3, 15), (28, 11), (28, 26), (3, 26)], 'w')
    c.bevel(['w'])
    for y in (16, 19, 22):
        c.hline(5, 20, y, 'S')
    c.rect(22, 18, 26, 19, 'k')
    c.rect(14, 4, 27, 10, 'B') if False else None
    c.outline()


@icon('vice', ['x64sc', 'x64', 'org.vice_emu.x64sc', 'vice-x64sc', 'vice-emu'], 'emulator', 'VICE')
def vice(c):
    # brown bread-bin keyboard
    c.poly([(3, 26), (5, 11), (26, 11), (28, 26)], 'N')
    c.bevel(['N'])
    for y in (14, 17, 20):
        for x in range(7, 25, 2):
            c.px(x, y, 'n')
    c.hline(10, 21, 23, 'n')
    c.rect(24, 12, 25, 12, 'R')
    c.outline()


@icon('fs-uae', ['fs-uae-launcher', 'net.fsuae.FS-UAE', 'amiberry'], 'emulator', 'FS-UAE')
def fsuae(c):
    # checkered bouncing ball
    c.circle(16, 16, 13, 'W')
    for y in range(32):
        for x in range(32):
            if c.get(x, y) == 'W':
                dx, dy = x + .5 - 16, y + .5 - 16
                a = math.atan2(dx, math.sqrt(max(169 - dx * dx - dy * dy, .1)))
                b = math.asin(max(-1, min(1, dy / 13)))
                if (int((a + 2) * 2.5) + int((b + 2) * 2.5)) % 2:
                    c.px(x, y, 'R')
    c.outline()


@icon('net._86box._86Box', ['86box', '86Box'], 'emulator', '86Box')
def box86(c):
    # beige tower PC
    c.rect(8, 3, 23, 28, 'y')
    c.bevel(['y'])
    c.rect(10, 6, 21, 8, 'n'); c.rect(10, 10, 21, 12, 'n')
    c.rect(12, 15, 19, 16, 'n')
    c.px(20, 24, 'G'); c.px(18, 24, 'R')
    c.vline(23, 4, 27, '3')
    c.outline()
