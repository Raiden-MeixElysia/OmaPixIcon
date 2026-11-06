from pix import icon
"""Chinese & Asian software V: game launchers, vendor tools, dev tools, browsers."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cn_lib import g, gc, disc, bubble, round_bubble, doc, cloud, tile, shield, hexagon, diamond, play, monitor  # noqa: E402


# ================================================================ game launchers

@icon('hoyoplay', ['com.mihoyo.hoyoplay', 'hyp', 'hoyoplay-launcher', 'mihoyo-launcher', 'HoYoPlay',
                   'com.hoyoverse.hoyoplay'], 'games', 'HoYoPlay')
def hoyoplay(c):
    # rounded play-triangle "H" mark in HoYo blue
    c.rrect(3, 3, 28, 28, 'B', 6)
    c.bevel(['B'])
    c.rect(9, 9, 11, 22, 'W'); c.rect(20, 9, 22, 22, 'W')
    c.rect(12, 15, 19, 16, 'W')
    c.circle(21.5, 7.5, 2.5, 'Y')
    c.outline()


def _star4(c, cx, cy, r, col):
    c.poly([(cx, cy - r), (cx + r * .3, cy - r * .3), (cx + r, cy), (cx + r * .3, cy + r * .3), (cx, cy + r),
            (cx - r * .3, cy + r * .3), (cx - r, cy), (cx - r * .3, cy - r * .3)], col)


@icon('an-anime-game-launcher', ['moe.launcher.an-anime-game-launcher', 'aagl', 'an-anime-game-launcher-bin',
                                 'an-anime-game-launcher-git', 'anime-game-launcher'], 'games',
      'An Anime Game Launcher')
def aagl(c):
    # the wish star in gold on a dark orb
    c.circle(16, 16, 13, '6')
    c.bevel(['6'])
    _star4(c, 16, 16, 11, 'Y')
    c.bevel(['Y'], dark=False)
    c.circle(16, 16, 2.5, 'W')
    c.outline()


@icon('the-honkers-railway-launcher', ['moe.launcher.the-honkers-railway-launcher', 'honkers-railway-launcher',
                                       'the-honkers-railway-launcher-bin'], 'games', 'The Honkers Railway Launcher')
def honkers_railway(c):
    # a train ticket / pass
    c.rrect(3, 7, 28, 25, 'M', 2)
    c.circle(3, 16, 3, '.'); c.circle(29, 16, 3, '.')
    c.bevel(['M'])
    for y in range(9, 24, 3):
        c.px(21, y, 'm')
    _star4(c, 12, 16, 6, 'Y')
    c.outline()


@icon('honkers-launcher', ['moe.launcher.honkers-launcher', 'honkers-launcher-bin'], 'games', 'Honkers Launcher')
def honkers(c):
    # a crescent blade
    c.circle(16, 16, 13, 'R')
    c.circle(20, 12, 10.5, '.')
    c.bevel(['R'])
    _star4(c, 21, 11, 5, 'W')
    c.outline()


@icon('sleepy-launcher', ['moe.launcher.sleepy-launcher', 'sleepy-launcher-bin'], 'games', 'Sleepy Launcher')
def sleepy(c):
    # a chunky "Z" on a yellow hazard plate
    hexagon(c, 'Y', 16, 16, 13.5)
    c.rect(9, 9, 22, 11, 'k')
    c.poly([(19, 11), (22.5, 11), (12.5, 21), (9, 21)], 'k')
    c.rect(9, 21, 22, 23, 'k')
    c.outline()


@icon('wavey-launcher', ['moe.launcher.wavey-launcher', 'wavey-launcher-bin'], 'games', 'Wavey Launcher')
def wavey(c):
    disc(c, 'C', 13)
    for y in (11, 16, 21):
        for x in range(6, 26):
            import math
            yy = y + round(1.5 * math.sin((x - 6) / 3))
            c.px(x, yy, 'W'); c.px(x, yy + 1, 'W')
    c.outline()


@icon('genshin-impact', ['genshinimpact', 'yuanshen', 'com.mihoyo.genshinimpact', 'genshin', 'GenshinImpact'],
      'games', 'Genshin Impact')
def genshin(c):
    # anemo-style feather crest
    c.poly([(16, 2.5), (25, 12), (16, 29.5), (7, 12)], 'G')
    c.bevel(['G'])
    c.poly([(16, 7), (21, 12), (16, 24), (11, 12)], 'Y')
    c.vline(16, 9, 22, '3')
    c.outline()


@icon('honkai-star-rail', ['starrail', 'com.mihoyo.hkrpg', 'star-rail', 'StarRail', 'hkrpg'], 'games',
      'Honkai: Star Rail')
def star_rail(c):
    c.circle(16, 16, 13, '6')
    c.ring(16, 16, 11, 9.5, 'b')
    c.bevel(['6'])
    _star4(c, 16, 16, 9, 'W')
    c.line(6, 24, 26, 8, 'Y')
    c.outline()


@icon('zenless-zone-zero', ['zzz', 'zenlesszonezero', 'com.mihoyo.nap', 'ZenlessZoneZero'], 'games',
      'Zenless Zone Zero')
def zzz(c):
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'], dark=False)
    c.ring(16, 16, 9.5, 6, 'Y')
    c.line(9, 23, 23, 9, 'k', 3)
    c.line(10, 22, 22, 10, 'G')
    c.outline()


@icon('netease-uu', ['uu-booster', 'com.netease.uu', 'uu-accelerator', 'uu-booster-bin', 'netease-uu-booster'],
      'games', 'NetEase UU')
def netease_uu(c):
    disc(c, 'k', 13)
    for x in (7, 17):
        c.rect(x, 9, x + 2, 19, 'G')
        c.rect(x + 6, 9, x + 8, 19, 'G') if False else None
    c.rect(7, 9, 9, 20, 'G'); c.rect(13, 9, 15, 20, 'G'); c.rect(7, 20, 15, 22, 'G')
    c.rect(17, 9, 19, 20, 'G'); c.rect(23, 9, 25, 20, 'G'); c.rect(17, 20, 25, 22, 'G')
    c.outline()


@icon('watt-toolkit', ['steam++', 'steampp', 'com.steampp.app', 'watt-toolkit-bin', 'Watt Toolkit',
                       'net.steampp.app', 'steam-plus-plus'], 'games', 'Watt Toolkit')
def watt_toolkit(c):
    # lightning bolt on a gear-ish disc
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.poly([(18, 4), (9, 17), (15, 17), (13, 28), (23, 14), (17, 14)], 'Y')
    c.bevel(['Y'], dark=False)
    c.outline()


@icon('wegame', ['com.tencent.wegame', 'wegame-bin', 'tencent-wegame', 'WeGame'], 'games', 'WeGame')
def wegame(c):
    # game pad in WeGame orange
    c.rrect(3, 9, 28, 22, 'O', 5)
    c.circle(8, 22, 5, 'O'); c.circle(23, 22, 5, 'O')
    c.bevel(['O'])
    c.rect(6, 14, 11, 15, 'W'); c.rect(8, 12, 9, 17, 'W')
    c.rect(21, 12, 22, 13, 'W'); c.rect(24, 15, 25, 16, 'W')
    c.outline()


@icon('heybox', ['xiaoheihe', 'com.max.xiaoheihe', 'heybox-desktop'], 'games', 'Heybox')
def heybox(c):
    # little black box with a smile
    c.poly([(16, 3), (28, 9), (16, 15), (4, 9)], 's')
    c.poly([(4, 9), (16, 15), (16, 29), (4, 23)], 'k')
    c.poly([(16, 15), (28, 9), (28, 23), (16, 29)], 'K')
    c.replace('K', 'k', (16, 9, 28, 29))
    c.rect(8, 17, 9, 18, 'W'); c.rect(12, 19, 13, 20, 'W')
    c.rect(20, 19, 21, 20, 'R'); c.rect(24, 17, 25, 18, 'R')
    c.vline(16, 15, 28, 'K')
    c.outline()


@icon('hmcl', ['org.jackhuang.hmcl', 'hmcl-bin', 'hmcl-stable', 'HMCL', 'hmcl-dev', 'hello-minecraft-launcher'],
      'games', 'HMCL')
def hmcl(c):
    # grass-block cube
    c.poly([(16, 3), (28, 9), (16, 15), (4, 9)], 'G')
    c.poly([(4, 9), (16, 15), (16, 29), (4, 23)], 'N')
    c.poly([(16, 15), (28, 9), (28, 23), (16, 29)], '8')
    c.poly([(4, 9), (16, 15), (16, 18), (4, 12)], '4')
    c.poly([(16, 15), (28, 9), (28, 12), (16, 18)], '4')
    c.px(8, 17, 'n'); c.px(11, 21, 'n'); c.px(20, 22, 'N'); c.px(24, 18, 'N')
    c.outline()


@icon('xmcl', ['xmcl-launcher', 'x-minecraft-launcher', 'app.xmcl.voxelum', 'xmcl-bin', 'xmcl-appimage'], 'games',
      'X Minecraft Launcher')
def xmcl(c):
    c.poly([(16, 3), (28, 9), (16, 15), (4, 9)], 'c')
    c.poly([(4, 9), (16, 15), (16, 29), (4, 23)], 'C')
    c.poly([(16, 15), (28, 9), (28, 23), (16, 29)], '5')
    c.line(7, 15, 13, 24, 'W', 2); c.line(13, 15, 7, 24, 'W', 2)
    c.outline()


@icon('netease-mumu', ['mumu', 'mumu-player', 'com.netease.mumu', 'mumuplayer'], 'games', 'MuMu Player')
def mumu(c):
    # green android-ish phone with a cow nose
    c.rrect(7, 3, 24, 28, 'k', 3)
    c.rect(9, 6, 22, 23, 'G')
    c.bevel(['G'])
    c.ellipse(15.5, 17, 5, 3.5, 'p')
    c.px(13, 17, '9'); c.px(17, 17, '9')
    c.rect(11, 10, 12, 11, 'K'); c.rect(19, 10, 20, 11, 'K')
    c.hline(13, 18, 26, 's')
    c.outline()


@icon('leigod', ['leigod-accelerator', 'leishen', 'com.leigod.accelerator'], 'games', 'Leigod Accelerator')
def leigod(c):
    shield(c, 'R', 5, 26, 3, 28)
    c.poly([(18, 6), (10, 17), (15, 17), (13, 25), (21, 14), (16, 14)], 'Y')
    c.outline()


# ================================================================ vendor & hardware

@icon('huawei-pc-manager', ['huawei-pcmanager', 'pcmanager', 'com.huawei.pcmanager', 'huawei-manager',
                            'huawei-share'], 'system', 'Huawei PC Manager')
def huawei_pc_manager(c):
    # the Huawei petal fan
    import math
    for d in (-95, -57, -19, 19, 57, 95):
        a = math.radians(-90 + d)
        ca, sa = math.cos(a), math.sin(a)
        px_, py_ = -sa, ca
        bx, by = 16 + 2 * ca, 22 + 2 * sa
        c.poly([(bx, by), (16 + 8 * ca + 3 * px_, 22 + 8 * sa + 3 * py_), (16 + 14 * ca, 22 + 14 * sa),
                (16 + 8 * ca - 3 * px_, 22 + 8 * sa - 3 * py_)], 'R')
    c.circle(16, 22, 2, 'R')
    c.bevel(['R'])
    c.outline()


@icon('micloud', ['xiaomi-cloud', 'mi-cloud', 'com.xiaomi.micloud', 'xiaomi-micloud'], 'web', 'Xiaomi Cloud')
def micloud(c):
    cloud(c, 'O', 1)
    c.bevel(['O'])
    c.rect(9, 15, 10, 22, 'W'); c.rect(9, 15, 16, 16, 'W'); c.rect(15, 15, 16, 22, 'W')
    c.rect(12, 18, 13, 22, 'W'); c.rect(19, 15, 20, 22, 'W')
    c.outline()


@icon('xiaomi-interconnect', ['mi-share', 'xiaomi-mishare', 'com.xiaomi.interconnect', 'xiaomi-hyperconnect'],
      'system', 'Xiaomi Interconnect')
def xiaomi_interconnect(c):
    c.rrect(3, 3, 28, 28, 'O', 6)
    c.bevel(['O'])
    c.ring(12, 16, 5, 3, 'W'); c.ring(20, 16, 5, 3, 'W')
    c.arc(20, 16, 5, 3, 120, 240, 'O')
    c.ring(12, 16, 5, 3, 'W') if False else None
    c.outline()


@icon('welink', ['com.huawei.welink', 'huawei-welink', 'welink-bin'], 'chat', 'WeLink')
def welink(c):
    round_bubble(c, 'R', 16, 15, 13, 11)
    c.bevel(['R'])
    g(c, 7, 11, """
        #...#...#.####
        #...#...#.#...
        .#.#.#.#..###.
        .#.#.#.#..#...
        ..#...#...####
    """, 'W')
    c.outline()


@icon('deveco-studio', ['deveco', 'huawei-deveco-studio', 'com.huawei.deveco', 'deveco-studio-bin'], 'dev',
      'DevEco Studio')
def deveco(c):
    hexagon(c, 'k', 16, 16, 13.5)
    c.bevel(['k'], dark=False)
    g(c, 8, 11, """
        ..#.......#..
        .#.........#.
        #...........#
        .#.........#.
        ..#.......#..
    """, 'R')
    c.line(17, 9, 14, 22, 'W', 2)
    c.outline()


@icon('creality-print', ['CrealityPrint', 'creality-print-bin', 'com.creality.print', 'creality-slicer'], 'graphics',
      'Creality Print')
def creality_print(c):
    # 3D printer gantry
    c.rect(4, 4, 6, 28, 'S'); c.rect(25, 4, 27, 28, 'S')
    c.rect(4, 4, 27, 6, 'S')
    c.rect(9, 11, 22, 13, 'k')
    c.rect(14, 13, 17, 17, 'B')
    c.rect(15, 18, 16, 18, 'O')
    c.rect(8, 22, 23, 24, 'w')
    c.rect(12, 19, 19, 21, 'O')
    c.rect(3, 25, 28, 28, 'B')
    c.bevel(['B', 'S'])
    c.outline()


# ================================================================ dev tools

@icon('apifox', ['apifox-bin', 'Apifox', 'com.apifox.app', 'apifox-appimage'], 'dev', 'Apifox')
def apifox(c):
    # fox head
    c.poly([(3, 3), (11, 8), (7, 16)], 'M')
    c.poly([(29, 3), (21, 8), (25, 16)], 'M')
    c.poly([(4, 10), (28, 10), (16, 29)], 'M')
    c.ellipse(16, 13, 10, 6, 'M')
    c.bevel(['M'])
    c.poly([(10, 17), (22, 17), (16, 27)], 'W')
    c.rect(10, 13, 11, 14, 'K'); c.rect(20, 13, 21, 14, 'K')
    c.rect(15, 25, 16, 26, 'K')
    c.outline()


@icon('apipost', ['apipost-bin', 'ApiPost', 'apipost7'], 'dev', 'Apipost')
def apipost(c):
    # paper-plane in a circle
    disc(c, 'O', 13)
    c.poly([(7, 15), (25, 8), (19, 24), (15, 18)], 'W')
    c.line(15, 18, 24, 9, '2')
    c.outline()


@icon('hbuilderx', ['hbuilder-x', 'HBuilderX', 'hbuilderx-bin', 'io.dcloud.hbuilderx'], 'dev', 'HBuilderX')
def hbuilderx(c):
    hexagon(c, 'G', 16, 16, 13.5)
    c.rect(9, 9, 11, 22, 'W'); c.rect(20, 9, 22, 22, 'W')
    c.rect(12, 15, 19, 16, 'W')
    c.outline()


@icon('wechat-devtools', ['wechat-web-devtools', 'wechat-devtools-bin', 'wechat-devtools-wine',
                          'com.tencent.wechat.devtools'], 'dev', 'WeChat DevTools')
def wechat_devtools(c):
    round_bubble(c, 'G', 16, 14, 13, 11)
    c.bevel(['G'])
    g(c, 7, 9, """
        ...#.......#.#...
        ..#.......#...#..
        .#.......#.....#.
        #.......#.......#
        .#.....#.......#.
        ..#...#.......#..
        ...#.#.......#...
    """, 'W')
    c.outline()


@icon('tiny-rdm', ['tinyrdm', 'tiny-rdm-bin', 'com.tinyrdm.TinyRDM', 'TinyRDM'], 'dev', 'Tiny RDM')
def tiny_rdm(c):
    for i, y in enumerate((20, 14, 8)):
        c.ellipse(16, y + 2, 12, 4.5, 'R')
        c.rect(4, y, 27, y + 2, 'R')
        c.ellipse(16, y, 12, 4.5, 'r' if i == 2 else 'R')
        c.hline(5, 26, y + 4, '1') if i < 2 else None
    c.bevel(['R'])
    c.ellipse(16, 8, 8, 2.5, 'W')
    c.outline()


@icon('switchhosts', ['SwitchHosts', 'io.github.oldj.SwitchHosts', 'switchhosts-bin', 'switch-hosts'], 'dev',
      'SwitchHosts')
def switchhosts(c):
    c.rrect(3, 9, 28, 22, 'G', 6)
    c.bevel(['G'])
    c.circle(21.5, 15.5, 5, 'W')
    c.bevel(['W'], light=False)
    c.text(6, 13, 'ON', '4', font=3, gap=1) if False else c.rect(7, 14, 12, 17, 'g')
    c.outline()


@icon('electerm', ['electerm-bin', 'org.electerm.electerm', 'Electerm', 'electerm-appimage'], 'dev', 'electerm')
def electerm(c):
    c.rrect(3, 4, 28, 27, 'k', 3)
    c.bevel(['k'], dark=False)
    c.rect(3, 4, 28, 7, 'C')
    c.rrect(3, 4, 28, 7, 'C', 3)
    c.rect(3, 6, 28, 7, 'C')
    c.text(7, 12, 'E', 'C', font=5)
    c.hline(14, 22, 18, 'c')
    c.outline()


@icon('windterm', ['WindTerm', 'windterm-bin', 'com.kingtoolbox.windterm'], 'dev', 'WindTerm')
def windterm(c):
    c.rrect(3, 4, 28, 27, 'B', 3)
    c.bevel(['B'])
    c.rect(5, 8, 26, 25, 'k')
    import math
    for y in (12, 17):
        for x in range(7, 24):
            c.px(x, y + round(math.sin((x - 7) / 2.5)), 'c')
    c.hline(7, 15, 22, 'W')
    c.outline()


@icon('finalshell', ['FinalShell', 'finalshell-bin', 'com.hostbuf.finalshell'], 'dev', 'FinalShell')
def finalshell(c):
    # a scallop shell
    c.poly([(16, 27), (3, 12), (8, 5), (16, 3), (24, 5), (29, 12)], 'O')
    c.bevel(['O'])
    for x in (9, 13, 19, 23):
        c.line(16, 26, x, 5, '2')
    c.rrect(12, 25, 19, 28, 'o', 1)
    c.outline()


@icon('notepad--', ['notepad---', 'notepadmm', 'com.hmja.notepadmm', 'notepad--bin', 'ndd'], 'dev', 'Notepad--')
def notepadmm(c):
    c.rect(5, 5, 24, 28, 'G')
    c.bevel(['G'])
    c.rect(8, 8, 21, 25, 'W')
    for x in (8, 12, 16, 20):
        c.rect(x, 3, x + 1, 6, 'S')
    c.rect(10, 15, 13, 16, 'G'); c.rect(16, 15, 19, 16, 'G')
    c.hline(10, 19, 11, 'w'); c.hline(10, 17, 20, 'w')
    c.line(28, 13, 21, 24, 'Y', 2)
    c.outline()


@icon('qtscrcpy', ['QtScrcpy', 'qtscrcpy-bin', 'com.github.barry_ran.QtScrcpy'], 'utilities', 'QtScrcpy')
def qtscrcpy(c):
    c.rrect(3, 7, 18, 24, 'S', 1)
    c.rect(5, 9, 16, 21, 'G')
    c.rrect(18, 3, 28, 28, 'k', 2)
    c.rect(20, 6, 26, 24, 'G')
    c.bevel(['G'])
    c.hline(22, 24, 26, 's')
    c.outline()


@icon('escrcpy', ['Escrcpy', 'escrcpy-bin', 'org.viarotel.escrcpy', 'escrcpy-appimage'], 'utilities', 'Escrcpy')
def escrcpy(c):
    c.rrect(8, 3, 23, 28, 'k', 3)
    c.rect(10, 6, 21, 24, 'B')
    c.bevel(['B'])
    c.poly([(13, 12), (18, 15), (13, 18)], 'W')
    c.hline(14, 17, 26, 's')
    c.outline()


@icon('qoder', ['qoder-bin', 'Qoder', 'com.qoder.ide'], 'dev', 'Qoder')
def qoder(c):
    c.ring(15, 15, 12, 7.5, 'G')
    c.poly([(19, 19), (23, 17), (29, 26), (25, 28)], 'G')
    c.bevel(['G'])
    c.outline()


@icon('codebuddy', ['codebuddy-ide', 'tencent-codebuddy', 'codebuddy-bin', 'CodeBuddy'], 'dev', 'CodeBuddy')
def codebuddy(c):
    # little robot head
    c.rect(15, 3, 16, 6, 'S'); c.circle(16, 3.5, 1.8, 'C')
    c.rrect(4, 7, 27, 26, 'C', 4)
    c.rect(4, 7, 27, 26, 'C') if False else None
    c.rect(3, 13, 3, 19, 'S'); c.rect(28, 13, 28, 19, 'S')
    c.bevel(['C'])
    c.rrect(7, 11, 24, 21, 'k', 2)
    g(c, 9, 14, """
        ..#.......#..
        .#.........#.
        ..#.......#..
    """, 'c')
    c.hline(14, 17, 17, 'c')
    c.outline()


@icon('rubick', ['Rubick', 'rubick-bin', 'com.rubick.app'], 'utilities', 'Rubick')
def rubick(c):
    # Rubik's cube
    c.poly([(16, 3), (28, 9), (16, 15), (4, 9)], 'Y')
    c.poly([(4, 9), (16, 15), (16, 29), (4, 23)], 'R')
    c.poly([(16, 15), (28, 9), (28, 23), (16, 29)], 'B')
    for t in (1 / 3, 2 / 3):
        c.line(4 + 12 * t, 9 + 6 * t, 4 + 12 * t, 23 + 6 * t, '1')
        c.line(4, 9 + 14 * t, 16, 15 + 14 * t, '1')
        c.line(16 + 12 * t, 15 - 6 * t, 16 + 12 * t, 29 - 6 * t, '6')
        c.line(16, 15 + 14 * t, 28, 9 + 14 * t, '6')
        c.line(4 + 12 * t, 9 - 6 * t, 16 + 12 * t, 15 - 6 * t, '3')
        c.line(16 - 12 * t, 3 + 6 * t, 28 - 12 * t, 9 + 6 * t, '3')
    c.outline()


@icon('alist', ['alist-desktop', 'alist-bin', 'openlist', 'openlist-desktop', 'AList'], 'web', 'AList')
def alist(c):
    # stacked list cards with the "A" ribbon
    c.poly([(16, 2.5), (28.5, 27), (21, 27), (16, 15), (11, 27), (3.5, 27)], 'B')
    c.bevel(['B'])
    c.rect(8, 20, 23, 22, 'C')
    c.outline()


@icon('gopeed', ['Gopeed', 'com.gopeed.Gopeed', 'gopeed-bin', 'gopeed-appimage', 'com.gopeed.gopeed'], 'web',
      'Gopeed')
def gopeed(c):
    disc(c, 'C', 13)
    c.rect(14, 7, 17, 17, 'W')
    c.poly([(9, 15), (22.5, 15), (16, 23)], 'W')
    c.hline(9, 22, 25, 'W') if False else None
    c.outline()


# ================================================================ browsers

@icon('qqbrowser', ['com.tencent.qqbrowser', 'qq-browser', 'qqbrowser-bin', 'tencent-qqbrowser'], 'web',
      'QQ Browser')
def qqbrowser(c):
    c.circle(16, 16, 13, 'B')
    c.arc(16, 16, 13, 6, 160, 300, 'C')
    c.arc(16, 16, 13, 6, 300, 30, 'Y')
    c.bevel(['B', 'C', 'Y'])
    c.circle(16, 16, 5, 'W')
    c.outline()


@icon('browser360', ['360browser', 'browser360-cn-stable', 'com.360.browser-stable', '360-browser',
                     'browser360-cn', 'qihoo-360-browser'], 'web', '360 Browser')
def browser360(c):
    c.circle(16, 16, 13, 'G')
    c.bevel(['G'])
    c.ring(16, 16, 9, 6.5, 'Y')
    c.circle(16, 16, 4, 'W')
    c.arc(16, 16, 13, 10.5, 200, 260, 'g')
    c.outline()


@icon('maxthon', ['maxthon-browser', 'maxthon-browser-stable', 'com.maxthon.browser'], 'web', 'Maxthon')
def maxthon(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.rect(8, 10, 10, 22, 'W'); c.rect(21, 10, 23, 22, 'W')
    c.line(10, 10, 15, 17, 'W', 2); c.line(21, 10, 16, 17, 'W', 2)
    c.outline()


@icon('cent-browser', ['centbrowser', 'centbrowser-bin', 'com.centbrowser.CentBrowser'], 'web', 'Cent Browser')
def cent_browser(c):
    c.circle(16, 16, 13, 'Y')
    c.bevel(['Y'])
    c.ring(16, 16, 8.5, 5.5, '3')
    c.rect(18, 12, 26, 20, 'Y')
    c.rect(15, 5, 16, 27, '3')
    c.outline()


# ================================================================ office & reading

@icon('cajviewer', ['com.cnki.cajviewer', 'cajviewer-appimage', 'cajviewer-bin', 'CAJViewer', 'cnki-cajviewer'],
      'office', 'CAJViewer')
def cajviewer(c):
    doc(c, 'R', 'r')
    c.text(8, 11, 'CAJ', 'W', font=3, gap=2) if False else c.text(9, 12, 'CAJ', 'W', font=3)
    c.hline(9, 22, 20, 'r'); c.hline(9, 19, 23, 'r')
    c.outline()


@icon('yozo-office', ['yozo', 'yozooffice', 'yozo-office-bin', 'com.yozo.office', 'yozo-office-writer'], 'office',
      'Yozo Office')
def yozo(c):
    doc(c, 'C', 'c')
    c.text(10, 11, 'Y', 'W', font=5, scale=2, gap=0) if False else g(c, 10, 11, """
        ##....##
        .##..##.
        ..####..
        ...##...
        ...##...
        ...##...
    """, 'W')
    c.hline(9, 22, 22, 'c')
    c.outline()


@icon('mindmaster', ['MindMaster', 'mindmaster-bin', 'com.edrawsoft.mindmaster', 'edraw-mindmaster'], 'office',
      'MindMaster')
def mindmaster(c):
    c.rrect(11, 12, 20, 19, 'M', 2)
    for (x, y) in ((3, 4), (3, 22), (22, 4), (22, 22)):
        c.rrect(x, y, x + 6, y + 5, 'm', 1)
    c.line(9, 9, 12, 13, 'M', 2); c.line(9, 22, 12, 18, 'M', 2)
    c.line(22, 9, 19, 13, 'M', 2); c.line(22, 22, 19, 18, 'M', 2)
    c.bevel(['M', 'm'])
    c.outline()


@icon('edrawmax', ['edraw-max', 'EdrawMax', 'com.edrawsoft.edrawmax', 'edrawmax-bin'], 'office', 'EdrawMax')
def edrawmax(c):
    c.rrect(3, 3, 14, 14, 'R', 2)
    c.circle(22.5, 8.5, 6, 'O')
    c.poly([(3, 28), (9, 17), (15, 28)], 'Y')
    c.rect(17, 17, 28, 27, 'B')
    c.bevel(['R', 'O', 'B'])
    c.outline()


@icon('wiznote', ['cn.wiz.wiznote', 'WizNote', 'wiznote-bin', 'wiznotex'], 'office', 'WizNote')
def wiznote(c):
    c.rrect(4, 3, 26, 28, 'B', 2)
    c.bevel(['B'])
    c.rect(4, 3, 7, 28, '6')
    g(c, 10, 10, """
        #...#...#
        #...#...#
        #..#.#..#
        .#.#.#.#.
        .##...##.
        .#.....#.
    """, 'W')
    c.hline(10, 22, 21, 'b')
    c.outline()


@icon('powerword', ['kingsoft-powerword', 'com.kingsoft.powerword', 'iciba', 'powerword-bin'], 'office',
      'Kingsoft PowerWord')
def powerword(c):
    c.poly([(3, 6), (15, 8), (15, 27), (3, 25)], 'B')
    c.poly([(17, 8), (29, 6), (29, 25), (17, 27)], 'B')
    c.rect(15, 8, 16, 27, '6')
    c.bevel(['B'])
    c.text(6, 13, 'A', 'W', font=5)
    c.text(20, 13, 'Z', 'W', font=5)
    c.outline()


@icon('spark-store', ['com.spark-app.store', 'spark-store-bin', 'spark-store-console', 'spark-store-git',
                      'spark-app-store'], 'system', 'Spark Store')
def spark_store(c):
    # a spark star in a shopping basket
    _star4(c, 16, 12, 10, 'Y')
    c.bevel(['Y'], dark=False)
    c.poly([(3, 17), (29, 17), (25, 28), (7, 28)], 'R')
    c.bevel(['R'])
    for x in (10, 16, 22):
        c.vline(x, 19, 26, '1')
    c.outline()


@icon('uengine', ['com.uniontech.uengine', 'uengine-runtime', 'uengine-launcher', 'uos-uengine'], 'system',
      'UEngine')
def uengine(c):
    # green android head in deepin blue frame
    c.ellipse(16, 18, 11, 10, 'G')
    c.rect(4, 18, 27, 27, 'G')
    c.line(9, 6, 11, 10, 'G'); c.line(23, 6, 21, 10, 'G')
    c.bevel(['G'])
    c.rect(10, 14, 11, 15, 'W'); c.rect(20, 14, 21, 15, 'W')
    c.rect(4, 20, 27, 21, '4')
    c.text(13, 22, 'U', 'W', font=3) if False else g(c, 14, 22, "#.#\n#.#\n###", 'W')
    c.outline()
