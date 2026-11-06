"""Open-source games and GNOME/KDE casual games."""
from pix import icon
import math


def big(c, x, y, art, col, k=2):
    lines = [l.strip() for l in art.strip('\n').split('\n')]
    for j, row in enumerate(lines):
        for i, ch in enumerate(row):
            if ch == '#':
                c.rect(x + i * k, y + j * k, x + i * k + k - 1, y + j * k + k - 1, col)


def cube(c, cx, top, s, ct, cl, cr):
    h = s // 2
    c.poly([(cx, top), (cx + s, top + h), (cx, top + 2 * h), (cx - s, top + h)], ct)
    c.poly([(cx - s, top + h), (cx, top + 2 * h), (cx, top + 2 * h + s), (cx - s, top + h + s)], cl)
    c.poly([(cx, top + 2 * h), (cx + s, top + h), (cx + s, top + h + s), (cx, top + 2 * h + s)], cr)


# =================================================================== strategy / sim

@icon('openttd', ['org.openttd.OpenTTD', 'OpenTTD'], 'games', 'OpenTTD')
def openttd(c):
    # steam locomotive side view
    c.rect(3, 12, 20, 22, 'G')
    c.rect(14, 6, 22, 22, 'G')
    c.bevel(['G'])
    c.rect(16, 8, 20, 12, 'c')
    c.rect(6, 5, 9, 12, 'k')
    c.rect(5, 4, 10, 5, 'k')
    c.rect(22, 16, 28, 22, 'R')
    c.poly([(26, 22), (29, 26), (24, 26)], 'R') if False else None
    for x in (7, 14, 24):
        c.circle(x, 24.5, 3.5, 'k'); c.px(x, 24, 'S')
    c.outline()


@icon('0ad', ['com.play0ad.zeroad', '0ad-launcher', 'zeroad'], 'games', '0 A.D.')
def zeroad(c):
    # greek shield with spear
    c.line(24, 4, 8, 27, 'n', 2)
    c.circle(15, 17, 10.5, 'O')
    c.bevel(['O'])
    c.ring(15, 17, 10.5, 9, '2')
    c.circle(15, 17, 3, 'Y')
    c.poly([(24, 3), (28, 3), (26, 7)], 'w')
    c.outline()


@icon('supertuxkart', ['net.supertuxkart.SuperTuxKart', 'supertuxkart-git'], 'games', 'SuperTuxKart')
def supertuxkart(c):
    # kart with a penguin driver
    c.ellipse(16, 10, 6, 7, 'k')
    c.ellipse(16, 11, 4, 5, 'W')
    c.px(14, 8, 'K'); c.px(17, 8, 'K')
    c.poly([(14, 11), (18, 11), (16, 13)], 'Y')
    c.rrect(3, 16, 28, 23, 'R', 2)
    c.bevel(['R'])
    c.circle(7, 24, 3.5, 'k'); c.circle(25, 24, 3.5, 'k')
    c.outline()


@icon('supertux', ['supertux2', 'org.supertuxproject.SuperTux'], 'games', 'SuperTux')
def supertux(c):
    # penguin full body waving
    c.ellipse(16, 16, 10, 12.5, 'k')
    c.ellipse(16, 18, 7, 9.5, 'W')
    c.circle(13.5, 10, 2, 'W'); c.circle(18.5, 10, 2, 'W')
    c.px(14, 10, 'K'); c.px(18, 10, 'K')
    c.poly([(13, 13), (19, 13), (16, 16)], 'Y')
    c.poly([(7, 17), (3, 10), (8, 13)], 'k')
    c.rect(9, 27, 14, 28, 'Y'); c.rect(18, 27, 23, 28, 'Y')
    c.outline()


@icon('org.luanti.luanti', ['luanti', 'minetest', 'net.minetest.Minetest'], 'games', 'Luanti')
def luanti(c):
    # stone block with grass top & ore
    cube(c, 16, 3, 13, 'g', 'S', 's')
    c.poly([(3, 9.5), (16, 16), (16, 19), (3, 13)], 'G')
    c.poly([(16, 16), (29, 9.5), (29, 13), (16, 19)], '4')
    c.rect(8, 20, 9, 21, 'O'); c.rect(21, 22, 22, 23, 'C')
    c.outline()


@icon('xonotic', ['org.xonotic.Xonotic', 'xonotic-sdl', 'xonotic-glx'], 'games', 'Xonotic')
def xonotic(c):
    # sharp X emblem
    c.poly([(3, 3), (11, 3), (16, 11), (21, 3), (29, 3), (20, 16), (29, 29), (21, 29), (16, 21), (11, 29), (3, 29), (12, 16)], 'C')
    c.bevel(['C'])
    c.poly([(14, 14), (18, 14), (18, 18), (14, 18)], 'W') if False else None
    c.outline()


@icon('openra', ['openra-ra', 'openra-cnc', 'openra-d2k', 'net.openra.OpenRA'], 'games', 'OpenRA')
def openra(c):
    # radar dish sweep
    c.circle(16, 16, 13, 'k')
    c.ring(16, 16, 9, 8, '4'); c.ring(16, 16, 5, 4, '4')
    c.hline(4, 27, 16, '4'); c.vline(16, 4, 27, '4')
    c.arc(16, 16, 12, 0, 280, 330, 'G')
    c.px(22, 10, 'R'); c.px(10, 21, 'R')
    c.outline()


@icon('wesnoth', ['org.wesnoth.Wesnoth', 'wesnoth-1.18', 'wesnoth-1.16'], 'games', 'Battle for Wesnoth')
def wesnoth(c):
    # sword through a crown
    c.rect(15, 3, 16, 22, 'w')
    c.rect(10, 20, 21, 22, 'Y')
    c.rect(14, 23, 17, 28, 'N')
    c.bevel(['w'])
    c.poly([(5, 13), (9, 8), (12, 12), (16, 7), (20, 12), (23, 8), (27, 13), (25, 18), (7, 18)], 'Y')
    c.bevel(['Y'])
    c.rect(15, 12, 16, 17, 'w')
    c.px(16, 15, 'R')
    c.outline()


@icon('hedgewars', ['org.hedgewars.Hedgewars'], 'games', 'Hedgewars')
def hedgewars(c):
    # hedgehog
    for i in range(7):
        a = math.radians(170 + i * 30)
        c.poly([(16 + 6 * math.cos(a - .3), 18 + 6 * math.sin(a - .3)),
                (16 + 13 * math.cos(a), 18 + 13 * math.sin(a)),
                (16 + 6 * math.cos(a + .3), 18 + 6 * math.sin(a + .3))], '8')
    c.ellipse(16, 19, 11, 8, 'N')
    c.ellipse(23, 22, 5.5, 4.5, 'p')
    c.bevel(['N'])
    c.px(24, 20, 'K'); c.px(28, 23, 'K')
    c.outline()


@icon('mindustry', ['com.github.Anuken.Mindustry', 'Mindustry'], 'games', 'Mindustry')
def mindustry(c):
    # core block with conveyor arrows
    c.rect(3, 3, 28, 28, 's')
    c.bevel(['s'])
    c.rect(9, 9, 22, 22, 'O')
    c.bevel(['O'])
    c.rect(13, 13, 18, 18, 'y')
    for x in (5, 25):
        for y in range(6, 27, 5):
            c.px(x, y, 'Y')
    c.outline()


@icon('veloren', ['net.veloren.veloren', 'airshipper', 'net.veloren.airshipper'], 'games', 'Veloren')
def veloren(c):
    # voxel tree on a floating island
    c.poly([(5, 20), (27, 20), (22, 26), (16, 29), (10, 26)], 'N')
    c.rect(5, 18, 27, 20, 'G')
    c.bevel(['N'])
    c.rect(15, 11, 17, 18, '8')
    c.rect(8, 3, 24, 12, 'G')
    c.rect(10, 3, 22, 4, 'g')
    c.bevel(['G'])
    c.outline()


@icon('osu-lazer', ['sh.ppy.osu', 'osu', 'osu!', 'osu-lazer-bin'], 'games', 'osu!lazer')
def osu(c):
    # hit circle with approach ring
    c.circle(16, 16, 13, 'P')
    c.bevel(['P'])
    c.ring(16, 16, 11, 9.5, 'W')
    c.text(9, 13, 'OSU', 'W', font=3)
    c.outline()


@icon('stepmania', ['itgmania', 'outfox', 'com.stepmania.StepMania'], 'games', 'StepMania')
def stepmania(c):
    # four dance arrows
    c.poly([(16, 3), (22, 9), (19, 9), (19, 13), (13, 13), (13, 9), (10, 9)], 'B')
    c.poly([(16, 29), (22, 23), (19, 23), (19, 19), (13, 19), (13, 23), (10, 23)], 'M')
    c.poly([(3, 16), (9, 10), (9, 13), (13, 13), (13, 19), (9, 19), (9, 22)], 'R')
    c.poly([(29, 16), (23, 10), (23, 13), (19, 13), (19, 19), (23, 19), (23, 22)], 'G')
    c.rect(14, 14, 18, 18, 'k')
    c.outline()


@icon('fofix', ['frets-on-fire', 'fretsonfire', 'yarg', 'clone-hero', 'clonehero'], 'games', 'Frets on Fire')
def fretsonfire(c):
    # guitar fret highway with five gems
    c.poly([(11, 3), (21, 3), (29, 28), (3, 28)], 'k')
    for i in range(1, 5):
        c.line(11 + i * 2, 3, 3 + i * 5.2, 28, 's')
    for i, col in enumerate(('G', 'R', 'Y', 'B', 'O')):
        c.ellipse(5.5 + i * 5.3, 24, 2.3, 1.6, col)
    c.outline()


@icon('en-croissant', ['org.encroissant.app', 'lichess', 'lichess-webapp', 'en-croissant-bin'], 'games',
      'En Croissant')
def chess(c):
    # knight piece
    c.poly([(9, 22), (11, 13), (8, 15), (6, 13), (10, 6), (13, 3), (15, 5), (20, 5), (24, 10), (25, 22)], 'w')
    c.bevel(['w'])
    c.rrect(6, 22, 26, 28, 'w', 1)
    c.hline(6, 26, 22, 'S')
    c.px(14, 9, 'K'); c.line(8, 14, 10, 13, 'S')
    c.shade_below(['w'], 'S')
    c.outline()


@icon('pingus', ['org.seul.pingus'], 'games', 'Pingus')
def pingus(c):
    # small penguin with a digging shovel
    c.ellipse(13, 17, 8, 11, 'k')
    c.ellipse(13, 19, 5, 8, 'W')
    c.circle(11, 10, 1.5, 'W'); c.circle(15, 10, 1.5, 'W')
    c.poly([(11, 13), (15, 13), (13, 15)], 'O')
    c.line(19, 18, 27, 6, 'N', 2)
    c.poly([(19, 19), (25, 20), (22, 28), (17, 25)], 'S')
    c.outline()


@icon('neverball', ['neverputt', 'com.neverball.Neverball'], 'games', 'Neverball')
def neverball(c):
    # shiny ball on a tilted tile
    c.poly([(3, 22), (16, 16), (29, 22), (16, 28)], 'G')
    c.bevel(['G'])
    c.circle(16, 13, 9, 'B')
    c.bevel(['B'])
    c.circle(13, 10, 3, 'b'); c.px(12, 9, 'W')
    c.outline()


@icon('teeworlds', ['ddnet', 'DDNet', 'org.ddnet.DDNet', 'com.teeworlds.Teeworlds'], 'games', 'Teeworlds / DDNet')
def teeworlds(c):
    # round tee with feet and eyes
    c.circle(16, 14, 11.5, 'O')
    c.bevel(['O'])
    c.ellipse(9, 26, 5, 2.5, 'n'); c.ellipse(23, 26, 5, 2.5, 'n')
    c.rect(17, 10, 19, 15, 'W'); c.rect(21, 10, 23, 15, 'W')
    c.rect(18, 12, 19, 14, 'K'); c.rect(22, 12, 23, 14, 'K')
    c.outline()


@icon('warzone2100', ['net.wz2100.wz2100', 'wz2100'], 'games', 'Warzone 2100')
def warzone2100(c):
    # tracked combat robot with turret
    c.rrect(3, 20, 28, 27, 'k', 3)
    for x in range(6, 27, 4):
        c.circle(x + .5, 23.5, 1.5, 's')
    c.rect(7, 13, 24, 19, 'G')
    c.bevel(['G'])
    c.rect(12, 8, 19, 13, 'G')
    c.rect(19, 9, 28, 10, 's')
    c.outline()


@icon('freeciv', ['freeciv-gtk3.22', 'freeciv-gtk4', 'freeciv-qt', 'freeciv-sdl2', 'org.freeciv.gtk322',
                  'org.freeciv.qt', 'freeciv-client'], 'games', 'Freeciv')
def freeciv(c):
    # globe on a pedestal with a flag
    c.circle(16, 14, 10.5, 'B')
    c.bevel(['B'])
    c.poly([(10, 9), (15, 7), (17, 12), (13, 15), (9, 13)], 'G')
    c.poly([(18, 15), (23, 14), (22, 20), (18, 21)], 'G')
    c.rect(11, 25, 20, 28, 'N')
    c.rect(15, 24, 16, 25, 'N')
    c.outline()


@icon('unciv', ['io.github.yairm210.unciv', 'Unciv'], 'games', 'Unciv')
def unciv(c):
    # hexagon tile with a city tower
    pts = [(16 + 13 * math.cos(math.radians(a)), 16 + 13 * math.sin(math.radians(a))) for a in range(30, 390, 60)]
    c.poly(pts, 'G')
    c.bevel(['G'])
    c.rect(12, 11, 19, 22, 'y')
    c.rect(12, 9, 13, 10, 'y'); c.rect(15, 9, 16, 10, 'y'); c.rect(18, 9, 19, 10, 'y')
    c.rect(15, 17, 16, 22, 'N')
    c.outline()


@icon('openmw', ['org.openmw.OpenMW', 'openmw-launcher', 'openmw-cs'], 'games', 'OpenMW')
def openmw(c):
    # crescent + star rune stone
    c.rrect(5, 3, 26, 28, 'S', 5)
    c.bevel(['S'])
    c.circle(16, 15, 7, 'W')
    c.circle(19, 13, 6, 'S')
    c.px(21, 20, 'Y'); c.px(20, 21, 'Y'); c.px(22, 21, 'Y'); c.px(21, 22, 'Y'); c.px(21, 21, 'y')
    c.outline()


@icon('gzdoom', ['org.zdoom.GZDoom', 'uzdoom', 'lzdoom', 'chocolate-doom', 'prboom-plus', 'dsda-doom',
                 'crispy-doom'], 'games', 'GZDoom')
def gzdoom(c):
    # horned demon skull
    c.poly([(3, 3), (9, 9), (7, 13)], 'w'); c.poly([(29, 3), (23, 9), (25, 13)], 'w')
    c.ellipse(16, 14, 10.5, 9.5, 'R')
    c.rect(10, 20, 22, 28, 'R')
    c.bevel(['R', 'w'])
    c.poly([(9, 11), (14, 13), (10, 16)], 'Y'); c.poly([(23, 11), (18, 13), (22, 16)], 'Y')
    for x in range(11, 22, 2):
        c.rect(x, 23, x, 26, 'W')
    c.hline(11, 21, 22, 'K'); c.hline(11, 21, 27, '1')
    c.outline()


@icon('quakespasm', ['ioquake3', 'yquake2', 'vkquake', 'ironwail', 'quake', 'darkplaces', 'io.github.ioquake3'],
      'games', 'Quake ports')
def quake(c):
    # nail-shaped emblem: circle with a spike
    c.arc(16, 12, 12, 8, 30, 150, 'N') if False else None
    c.arc(16, 11, 12.5, 8, 15, 165, 'N')
    c.poly([(13, 3), (19, 3), (17, 29), (15, 29)], 'N')
    c.bevel(['N'])
    c.vline(16, 4, 27, 'n')
    c.outline()


@icon('xmoto', ['net.sourceforge.xmoto'], 'games', 'X-Moto')
def xmoto(c):
    # dirt bike
    c.circle(8, 22, 5, 'k'); c.circle(24, 22, 5, 'k')
    c.circle(8, 22, 2, 's'); c.circle(24, 22, 2, 's')
    c.poly([(8, 19), (14, 13), (22, 13), (25, 21), (16, 21)], 'R')
    c.bevel(['R'])
    c.line(21, 13, 24, 7, 's', 2)
    c.circle(16, 9, 3.5, 'Y')
    c.outline()


@icon('frozen-bubble', ['org.frozen_bubble.FrozenBubble', 'frozenbubble'], 'games', 'Frozen Bubble')
def frozenbubble(c):
    # bubble cluster
    for x, y, col in ((8, 9, 'B'), (16, 9, 'R'), (24, 9, 'G'), (12, 16, 'Y'), (20, 16, 'B'), (16, 23, 'M')):
        c.circle(x, y, 4.5, col)
        c.px(x - 2, y - 2, 'W')
    c.outline()


@icon('pioneer', ['net.pioneerspacesim.Pioneer'], 'games', 'Pioneer')
def pioneer(c):
    # spacecraft over a planet arc
    c.ellipse(16, 30, 13, 7, 'B')
    c.rect(0, 28, 31, 31, '.')
    c.poly([(16, 3), (22, 17), (16, 14), (10, 17)], 'w')
    c.bevel(['w'])
    c.poly([(13, 15), (19, 15), (16, 21)], 'O')
    c.outline()


@icon('io.github.endless_sky.endless_sky', ['endless-sky', 'endless_sky'], 'games', 'Endless Sky')
def endlesssky(c):
    # starfield circle with a ship streak
    c.circle(16, 16, 13, 'k')
    for x, y in ((8, 8), (22, 6), (25, 18), (10, 22), (18, 26), (6, 15)):
        c.px(x, y, 'W')
    c.poly([(9, 21), (23, 9), (20, 15), (25, 13), (12, 23)], 'C')
    c.outline()


@icon('naev', ['org.naev.Naev'], 'games', 'Naev')
def naev(c):
    # planet with a ring of asteroids
    c.circle(16, 16, 10, 'O')
    c.bevel(['O'])
    c.dither(6, 18, 26, 20, '2', 'O', only='O')
    for i in range(10):
        a = math.radians(i * 36)
        c.rect(round(15.5 + 12 * math.cos(a)), round(15.5 + 12 * math.sin(a)), round(15.5 + 12 * math.cos(a)) + 1,
               round(15.5 + 12 * math.sin(a)) + 1, 'S')
    c.outline()


@icon('cataclysm-dda', ['org.cataclysmdda.CataclysmDDA', 'cataclysm-tiles', 'cataclysm'], 'games', 'Cataclysm: DDA')
def cataclysm(c):
    # cracked boulder of rubble
    c.poly([(4, 18), (9, 7), (19, 4), (28, 12), (27, 25), (15, 29), (5, 26)], 'N')
    c.bevel(['N'])
    c.line(13, 6, 15, 14, 'K'); c.line(15, 14, 11, 21, 'K'); c.line(15, 14, 23, 17, 'K')
    c.px(20, 9, 'G'); c.px(9, 23, 'G')
    c.outline()


@icon('net.sourceforge.ExtremeTuxRacer', ['etr', 'extremetuxracer', 'tuxracer'], 'games', 'Extreme Tux Racer')
def tuxracer(c):
    # sliding penguin down a snowy slope
    c.poly([(3, 18), (29, 28), (3, 28)], 'W')
    c.bevel(['W'])
    c.ellipse(16, 15, 10, 5, 'k')
    c.ellipse(16, 17, 7, 2.5, 'W')
    c.circle(25, 14, 3, 'k')
    c.poly([(27, 14), (30, 15), (27, 16)], 'Y')
    c.px(25, 13, 'W')
    c.outline()


@icon('armagetronad', ['org.armagetronad.ArmagetronAdvanced', 'armagetron'], 'games', 'Armagetron Advanced')
def armagetron(c):
    # light-cycle trails on a grid
    c.rect(3, 3, 28, 28, 'k')
    for i in range(3, 29, 5):
        c.hline(3, 28, i, 's'); c.vline(i, 3, 28, 's')
    c.line(4, 25, 15, 25, 'C', 2); c.line(15, 25, 15, 10, 'C', 2)
    c.line(27, 6, 21, 6, 'O', 2); c.line(21, 6, 21, 18, 'O', 2)
    c.rect(14, 8, 17, 10, 'c'); c.rect(20, 18, 23, 20, 'o')
    c.outline()


@icon('com.shatteredpixel.shatteredpixeldungeon', ['shattered-pixel-dungeon', 'shatteredpd'], 'games',
      'Shattered Pixel Dungeon')
def shatteredpd(c):
    # cracked stone key-stone / dungeon door
    c.rect(4, 10, 27, 28, 's')
    c.ellipse(15.5, 11, 11.5, 8, 's')
    c.bevel(['s'])
    c.rect(9, 12, 22, 28, 'N')
    c.ellipse(15.5, 13, 6.5, 5, 'N')
    c.vline(15, 9, 28, '8'); c.vline(16, 9, 28, '8')
    c.px(19, 20, 'Y')
    c.outline()


@icon('red-eclipse', ['redeclipse', 'net.redeclipse.RedEclipse'], 'games', 'Red Eclipse')
def redeclipse(c):
    c.circle(16, 16, 13, 'R')
    c.circle(19, 13, 11, '.')
    c.circle(19, 13, 10, 'k')
    c.bevel(['R'])
    c.outline()


@icon('assaultcube', ['net.cubers.assault.AssaultCube', 'assaultcube-client'], 'games', 'AssaultCube')
def assaultcube(c):
    # crosshair over a cube
    cube(c, 16, 3, 12, 'S', 's', 'k')
    c.ring(16, 15.5, 6, 4.8, 'R')
    c.vline(16, 7, 11, 'R'); c.vline(16, 20, 24, 'R'); c.hline(8, 12, 15, 'R'); c.hline(20, 24, 15, 'R')
    c.outline()


@icon('openarena', ['ws.openarena.OpenArena', 'openarena-server'], 'games', 'OpenArena')
def openarena(c):
    # arena ring with flame core
    c.ring(16, 16, 13, 9, 'S')
    c.bevel(['S'])
    c.poly([(16, 6), (21, 14), (20, 22), (12, 22), (11, 14)], 'O')
    c.poly([(16, 12), (18, 17), (16, 21), (14, 17)], 'Y')
    c.outline()


@icon('net.sourceforge.lbreakout2', ['lbreakout2', 'lbreakouthd'],
      'games', 'LBreakout')
def lbreakout(c):
    for j, col in enumerate(('R', 'O', 'Y', 'G')):
        for i in range(4):
            if (i, j) in ((1, 2), (2, 3), (3, 3)):
                continue
            c.rect(3 + i * 7, 3 + j * 4, 7 + i * 7, 5 + j * 4, col)
    c.circle(18, 22, 2, 'W')
    c.rrect(9, 26, 22, 28, 'C', 1)
    c.outline()
