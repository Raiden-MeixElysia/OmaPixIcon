"""More open-source games and engine re-implementations."""
from pix import icon
import math


@icon('openrct2', ['io.openrct2.OpenRCT2', 'OpenRCT2'], 'games', 'OpenRCT2')
def openrct2(c):
    # roller-coaster loop on stilts
    c.ring(16, 13, 10, 7.5, 'R')
    c.rect(3, 22, 28, 24, 'R')
    c.bevel(['R'])
    for x in (6, 12, 20, 26):
        c.vline(x, 25, 28, 's')
    c.rect(8, 19, 12, 21, 'Y')
    c.outline()


@icon('openloco', ['io.openloco.OpenLoco', 'OpenLoco'], 'games', 'OpenLoco')
def openloco(c):
    # front view of a locomotive with headlamp
    c.rrect(5, 4, 26, 24, 'B', 3)
    c.bevel(['B'])
    c.rect(8, 7, 23, 13, 'c')
    c.vline(15, 7, 13, 'B'); c.vline(16, 7, 13, 'B')
    c.circle(16, 19, 2.5, 'Y')
    c.poly([(3, 25), (29, 25), (25, 28.5), (7, 28.5)], 'k')
    c.outline()


@icon('devilutionx', ['org.diasurgical.DevilutionX', 'devilution'], 'games', 'DevilutionX')
def devilutionx(c):
    # flaming red pentagon rune
    c.poly([(16, 3), (28.5, 12), (24, 28), (8, 28), (3.5, 12)], '1')
    c.poly([(16, 6), (25.5, 13), (22, 25.5), (10, 25.5), (6.5, 13)], 'R')
    c.bevel(['R'], edge=('1',))
    c.poly([(16, 9), (20, 16), (18, 23), (14, 23), (12, 16)], 'O')
    c.poly([(16, 14), (18, 19), (16, 22), (14, 19)], 'Y')
    c.outline()


@icon('corsix-th', ['com.corsixth.corsixth', 'CorsixTH'], 'games', 'CorsixTH')
def corsixth(c):
    # hospital building with a red cross
    c.rect(4, 8, 27, 28, 'W')
    c.bevel(['W'])
    c.rect(4, 6, 27, 8, 'S')
    c.rect(13, 10, 18, 21, 'R'); c.rect(10, 13, 21, 18, 'R')
    c.rect(13, 23, 18, 28, 'C')
    c.outline()


@icon('fheroes2', ['io.github.ihhub.fheroes2', 'org.fheroes2.fheroes2'], 'games', 'fheroes2')
def fheroes2(c):
    # heraldic banner on a pole
    c.vline(4, 5, 28, 'N'); c.vline(5, 5, 28, 'N')
    c.poly([(6, 5), (28, 5), (28, 22), (17, 18), (6, 22)], 'B')
    c.bevel(['B'])
    c.poly([(17, 8), (20, 13), (17, 17), (14, 13)], 'Y')
    c.circle(4.5, 4, 1.2, 'Y')
    c.outline()


@icon('vcmi', ['eu.vcmi.VCMI', 'vcmilauncher'], 'games', 'VCMI')
def vcmi(c):
    # castle gate with two towers
    c.rect(3, 8, 10, 28, 'S'); c.rect(21, 8, 28, 28, 'S')
    for x in (3, 7, 21, 25):
        c.rect(x, 5, x + 2, 7, 'S')
    c.rect(10, 13, 21, 28, 'w')
    c.bevel(['S', 'w'])
    c.rect(13, 19, 18, 28, 'N')
    c.ellipse(15.5, 19.5, 2.5, 2, 'N')
    c.outline()


@icon('openxcom', ['OpenXcom', 'openxcom-extended', 'com.openxcom.OpenXcom'], 'games', 'OpenXcom')
def openxcom(c):
    # flying saucer
    c.ellipse(16, 12, 6, 5, 'c')
    c.rect(9, 12, 22, 14, '.') if False else None
    c.ellipse(16, 17, 13, 4.5, 'S')
    c.bevel(['S', 'c'])
    for x in (8, 13, 18, 23):
        c.px(x, 17, 'Y')
    c.poly([(11, 21), (21, 21), (25, 28), (7, 28)], 'g')
    c.outline()


@icon('widelands', ['org.widelands.Widelands'], 'games', 'Widelands')
def widelands(c):
    # wheat sheaf
    c.poly([(13, 14), (19, 14), (25, 28), (7, 28)], 'Y')
    c.bevel(['Y'])
    for x in (10, 14, 18, 22):
        c.ellipse(x + .5, 8, 2.2, 5, 'y')
    c.rect(10, 17, 22, 19, 'N')
    c.outline()


@icon('freeorion', ['org.freeorion.FreeOrion', 'FreeOrion'], 'games', 'FreeOrion')
def freeorion(c):
    # blue star with three orbiting dots
    c.ring(16, 16, 13, 12, 'B') if False else None
    for r in (12.5, 8.5):
        for t in range(0, 360, 3):
            a = math.radians(t)
            c.px(int(16 + r * math.cos(a)), int(16 + r * math.sin(a)), '6')
    c.circle(16, 16, 4.5, 'C')
    c.bevel(['C'])
    c.circle(24.5, 7, 2.2, 'G'); c.circle(9, 22, 2, 'O'); c.circle(4, 16, 1.5, 'M')
    c.outline()


@icon('flightgear', ['org.flightgear.FlightGear', 'fgfs', 'FlightGear'], 'games', 'FlightGear')
def flightgear(c):
    # propeller plane top-down
    c.rrect(14, 3, 17, 28, 'w', 1)
    c.rrect(3, 10, 28, 14, 'w', 1)
    c.rrect(10, 24, 21, 26, 'w', 1)
    c.bevel(['w'])
    c.rect(15, 6, 16, 9, 'B')
    c.hline(11, 20, 2, 'k') if False else None
    c.px(3, 12, 'R'); c.px(28, 12, 'G')
    c.outline()


@icon('speed-dreams', ['org.speed_dreams.SpeedDreams', 'speed-dreams-2'], 'games', 'Speed Dreams')
def speeddreams(c):
    # checkered flag
    c.vline(4, 3, 28, 's'); c.vline(5, 3, 28, 's')
    for y in range(4, 20):
        for x in range(6, 29):
            off = int(2 * math.sin((x - 6) / 4.0))
            yy = y + off
            if 4 <= y <= 19:
                c.px(x, yy, 'k' if ((x - 6) // 4 + (y - 4) // 4) % 2 else 'W')
    c.outline()


@icon('stuntrally', ['org.stuntrally.StuntRally', 'stuntrally3', 'sr-editor'], 'games', 'Stunt Rally')
def stuntrally(c):
    # rally car leaping over a ramp
    c.poly([(3, 28), (14, 20), (14, 28)], 'N')
    c.poly([(9, 13), (13, 8), (22, 7), (28, 11), (27, 16), (10, 18)], 'O')
    c.bevel(['O'])
    c.poly([(14, 9), (21, 8), (23, 11), (15, 12)], 'c')
    c.circle(12, 18, 3, 'k'); c.circle(24, 16, 3, 'k')
    c.outline()


@icon('nethack', ['nethack-x11', 'nethack-qt', 'angband', 'crawl', 'crawl-tiles', 'dcss'], 'games', 'Roguelikes')
def nethack(c):
    # the @ adventurer in a dungeon tile
    c.rect(3, 3, 28, 28, 'k')
    for x in range(5, 27, 4):
        c.px(x, 5, 's'); c.px(x, 26, 's')
    c.ring(15.5, 15.5, 8, 6, 'Y')
    c.circle(15.5, 15.5, 3, 'Y')
    c.circle(15.5, 15.5, 1.3, 'k')
    c.rect(19, 15, 22, 21, 'Y')
    c.rect(19, 21, 23, 21, 'k')
    c.outline()


@icon('dwarffortress', ['dwarf-fortress', 'df', 'lnp'], 'games', 'Dwarf Fortress')
def dwarffortress(c):
    # pickaxe over a rough gem
    c.poly([(9, 18), (16, 13), (23, 18), (16, 28)], 'C')
    c.poly([(9, 18), (16, 13), (16, 18)], 'c')
    c.bevel(['C'])
    c.line(5, 14, 23, 3, 'N', 2) if False else None
    c.arc(16, 15, 13, 10, 200, 340, 'w')
    c.line(16, 3, 16, 12, 'N', 2)
    c.outline()


@icon('vintagestory', ['Vintagestory', 'vintage-story', 'at.vintagestory.VintageStory'], 'games', 'Vintage Story')
def vintagestory(c):
    # clay pot with a sprouting plant
    c.poly([(8, 13), (24, 13), (26, 19), (22, 28), (10, 28), (6, 19)], 'O')
    c.rect(7, 11, 25, 13, '2')
    c.bevel(['O'])
    c.hline(8, 24, 20, '2')
    c.vline(16, 3, 10, 'G')
    c.poly([(16, 6), (10, 3), (12, 8)], 'G'); c.poly([(16, 5), (22, 2.5), (20, 7)], 'g')
    c.outline()


@icon('cockatrice', ['org.cockatrice.Cockatrice', 'oracle', 'servatrice'], 'games', 'Cockatrice')
def cockatrice(c):
    # three fanned trading cards
    for i, (dx, col) in enumerate(((-7, 'B'), (0, 'G'), (7, 'R'))):
        x0 = 9 + dx * 6 // 7
        c.rect(x0, 5 + abs(dx) // 2, x0 + 13, 27 - abs(dx) // 3, 'k')
        c.rect(x0 + 1, 6 + abs(dx) // 2, x0 + 12, 26 - abs(dx) // 3, col)
        c.rect(x0 + 2, 8 + abs(dx) // 2, x0 + 11, 15 + abs(dx) // 2, 'W')
    c.outline()


@icon('org.urbanterror.UrbanTerror', ['urbanterror', 'urban-terror', 'Quake3-UrT'], 'games', 'Urban Terror')
def urbanterror(c):
    # spray-paint can with a tag splash
    c.rrect(5, 9, 16, 28, 'G', 2)
    c.bevel(['G'])
    c.rect(8, 5, 13, 8, 'S'); c.rect(9, 3, 11, 4, 'k')
    c.rect(5, 14, 16, 17, '4')
    for x, y, r in ((22, 6, 2.5), (25, 12, 3), (20, 12, 1.5), (27, 5, 1.5)):
        c.circle(x, y, r, 'O')
    c.outline()


@icon('opentyrian', ['com.github.opentyrian.OpenTyrian', 'opentyrian2000'], 'games', 'OpenTyrian')
def opentyrian(c):
    # vertical shooter ship with exhaust
    c.poly([(16, 3), (20, 13), (28, 21), (20, 22), (16, 25), (12, 22), (4, 21), (12, 13)], 'S')
    c.bevel(['S'])
    c.rect(15, 9, 16, 14, 'C')
    c.poly([(14, 25), (18, 25), (16, 29)], 'O')
    c.outline()


@icon('tremulous', ['tremulous-tremded', 'net.tremulous.Tremulous'], 'games', 'Tremulous')
def tremulous(c):
    # alien claw-mark scratches in a green shield
    c.poly([(4, 4), (28, 4), (28, 16), (16, 29), (4, 16)], '4')
    c.bevel(['4'])
    for i in range(3):
        c.line(9 + i * 5, 7, 13 + i * 5, 22 - i * 2, 'g', 2)
    c.outline()


@icon('ufoai', ['ufoai-client', 'org.ufoai.UFOAI'], 'games', 'UFO: Alien Invasion')
def ufoai(c):
    # alien head
    c.ellipse(16, 13, 11, 10.5, 'g')
    c.poly([(8, 18), (24, 18), (16, 29)], 'g')
    c.bevel(['g'])
    c.poly([(8, 12), (14, 15), (13, 19), (8, 17)], 'K')
    c.poly([(24, 12), (18, 15), (19, 19), (24, 17)], 'K')
    c.px(10, 14, 'W'); c.px(22, 14, 'W')
    c.outline()
