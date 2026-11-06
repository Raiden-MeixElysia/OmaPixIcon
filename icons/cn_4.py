from pix import icon
"""Chinese & Asian software IV: openKylin / UKUI, Japanese & Korean apps,
proxy clients and remote desktop.
Kylin family look: teal (C/5/c) + paper white, one accent at most."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cn_lib import g, gc, disc, bubble, round_bubble, doc, cloud, shield, hexagon, play, note, monitor  # noqa: E402


# ================================================================ openKylin / UKUI

@icon('peony', ['org.ukui.peony', 'peony-file-manager', 'kylin-file-manager', 'ukui-file-manager'], 'kylin',
      'Peony Files')
def peony(c):
    c.rrect(3, 6, 13, 10, '5', 1)
    c.rect(3, 8, 28, 26, '5')
    c.rect(6, 9, 25, 13, 'W')
    c.rect(3, 12, 28, 26, 'C')
    c.bevel(['C'])
    # peony flower badge
    for dx, dy in ((0, -3), (3, 0), (0, 3), (-3, 0)):
        c.circle(16 + dx, 19.5 + dy, 2.2, 'P')
    c.circle(16, 19.5, 1.5, 'Y')
    c.outline()


@icon('ukui-control-center', ['org.ukui.control-center', 'kylin-control-center', 'ukui-control-center-settings'],
      'kylin', 'UKUI Control Center')
def ukui_cc(c):
    c.rrect(3, 3, 28, 28, 'C', 4)
    c.bevel(['C'])
    for i, (y, k) in enumerate(((9, 18), (16, 10), (23, 21))):
        c.rect(7, y, 24, y, 'W')
        c.circle(k + .5, y + .5, 2.6, 'W')
        c.circle(k + .5, y + .5, 1.2, '5')
    c.outline()


@icon('kylin-software-center', ['kylin-app-store', 'openkylin-software-center', 'kylin-software-center-plugin',
                                'org.kylin.software-center'], 'kylin', 'Kylin Software Center')
def kylin_sc(c):
    c.ring(16, 10, 6, 4, '5')
    c.rect(9, 10, 22, 12, '.')
    c.vline(10, 9, 12, '5'); c.vline(21, 9, 12, '5')
    c.poly([(4, 11), (28, 11), (26, 28), (6, 28)], 'C')
    c.bevel(['C'])
    c.poly([(16, 14), (22, 20), (16, 26), (10, 20)], 'W')
    c.poly([(16, 17), (19, 20), (16, 23), (13, 20)], 'c')
    c.outline()


@icon('kylin-video', ['org.kylin.video', 'kylin-video-player'], 'kylin', 'Kylin Video')
def kylin_video(c):
    c.circle(16, 16, 13, 'C')
    c.bevel(['C'])
    c.circle(16, 16, 9, 'W')
    play(c, 13, 10, 13, 'C')
    c.outline()


@icon('kylin-music', ['org.kylin.music', 'kylin-music-player'], 'kylin', 'Kylin Music')
def kylin_music(c):
    c.circle(16, 16, 13, 'C')
    c.bevel(['C'])
    c.rect(11, 8, 12, 21, 'W'); c.rect(21, 6, 22, 19, 'W')
    c.line(11, 8, 22, 6, 'W', 2)
    c.ellipse(10, 21.5, 3, 2.5, 'W'); c.ellipse(20, 19.5, 3, 2.5, 'W')
    c.outline()


@icon('kylin-ipmsg', ['org.kylin.ipmsg', 'kylin-messages', 'kylin-chuanshu', 'kylin-ipmsg-server'], 'kylin',
      'Kylin Messages')
def kylin_ipmsg(c):
    # paper plane
    c.poly([(3, 15), (29, 4), (21, 28), (15, 19)], 'W')
    c.poly([(15, 19), (29, 4), (13, 26)], 'C')
    c.bevel(['W'])
    c.line(15, 19, 28, 5, '5')
    c.outline()


@icon('kylin-screenshot', ['org.kylin.screenshot', 'kylin-screen-capture'], 'kylin', 'Kylin Screenshot')
def kylin_screenshot(c):
    # scissors
    c.ring(9, 22, 5.5, 3, 'C'); c.ring(23, 22, 5.5, 3, 'C')
    c.bevel(['C'])
    c.line(11, 17, 21, 3, 'w', 2)
    c.line(20, 17, 10, 3, 'W', 2)
    c.rect(15, 10, 16, 11, '5')
    c.outline()


@icon('kylin-calculator', ['ukui-calculator', 'org.kylin.calculator'], 'kylin', 'Kylin Calculator')
def kylin_calculator(c):
    c.rrect(6, 3, 25, 28, 'C', 3)
    c.bevel(['C'])
    c.rect(9, 6, 22, 11, 'k')
    c.rect(17, 8, 20, 9, 'c')
    g(c, 9, 14, """
        ...#.....#.#.
        ..###.....#..
        ...#.....#.#.
        .............
        .............
        .###.....#...
        ..........###
        .........#...
        .............
        ..###...###..
    """, 'W')
    c.outline()


@icon('kylin-recorder', ['org.kylin.recorder', 'kylin-sound-recorder'], 'kylin', 'Kylin Recorder')
def kylin_recorder(c):
    disc(c, 'C', 13)
    for x, h in ((8, 4), (11, 10), (14, 14), (17, 8), (20, 12), (23, 6)):
        c.rect(x, 16 - h // 2, x + 1, 16 + h // 2, 'W')
    c.circle(25, 25, 3, 'R')
    c.outline()


@icon('kylin-weather', ['indicator-china-weather', 'org.kylin.weather', 'china-weather'], 'kylin', 'Kylin Weather')
def kylin_weather(c):
    c.circle(11, 11, 8, 'Y')
    c.bevel(['Y'])
    cloud(c, 'W', 3)
    c.rect(0, 29, 31, 31, '.')
    c.bevel(['W'])
    c.outline()


@icon('kylin-scanner', ['org.kylin.scanner', 'kylin-scan'], 'kylin', 'Kylin Scanner')
def kylin_scanner(c):
    c.rrect(3, 11, 28, 24, 'C', 2)
    c.bevel(['C'])
    c.rect(5, 6, 26, 11, 'W')
    c.hline(5, 26, 10, 'R')
    c.rect(5, 14, 26, 15, '5')
    c.rect(22, 19, 25, 20, 'W')
    c.outline()


@icon('kylin-printer', ['org.kylin.printer', 'kylin-print-manager'], 'kylin', 'Kylin Printer')
def kylin_printer(c):
    c.rect(9, 3, 22, 10, 'W')
    c.rrect(3, 9, 28, 22, 'C', 3)
    c.bevel(['C', 'W'])
    c.rect(24, 12, 25, 13, 'Y')
    c.rect(8, 18, 23, 28, 'W')
    c.hline(10, 21, 22, '5'); c.hline(10, 18, 25, '5')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('kylin-photo-viewer', ['org.kylin.photo-viewer', 'kylin-image-viewer'], 'kylin', 'Kylin Photo Viewer')
def kylin_photo_viewer(c):
    c.rrect(3, 5, 28, 26, 'C', 3)
    c.bevel(['C'])
    c.rect(6, 8, 25, 23, 'W')
    c.circle(20, 12, 2, 'Y')
    c.poly([(6, 23.5), (13, 14), (20, 23.5)], 'C')
    c.poly([(15, 23.5), (20, 18), (25.5, 23.5)], '5')
    c.outline()


@icon('kylin-notebook', ['ukui-notebook', 'org.kylin.notebook', 'kylin-notes'], 'kylin', 'Kylin Notes')
def kylin_notebook(c):
    c.rect(6, 4, 26, 28, 'W')
    c.rect(6, 4, 9, 28, 'C')
    c.bevel(['W', 'C'])
    for y in (10, 14, 18, 22):
        c.hline(12, 23, y, 'c')
    for y in (7, 12, 17, 22):
        c.rect(4, y, 6, y + 1, 'S')
    c.outline()


@icon('kylin-os-manager', ['kylin-assistant', 'org.kylin.os-manager', 'kylin-security-center',
                           'ksc-defender'], 'kylin', 'Kylin OS Manager')
def kylin_os_manager(c):
    shield(c, 'C', 5, 26, 3, 28)
    c.poly([(16, 8), (21, 13), (16, 23), (11, 13)], 'W')
    c.poly([(16, 11), (18.5, 13.5), (16, 19), (13.5, 13.5)], 'c')
    c.outline()


@icon('kylin-burner', ['org.kylin.burner', 'kylin-disc-burner'], 'kylin', 'Kylin Burner')
def kylin_burner(c):
    disc(c, 'w', 13)
    c.arc(16, 16, 12, 6, 200, 250, 'c')
    c.arc(16, 16, 12, 6, 20, 70, 'C')
    c.circle(16, 16, 4, 'C')
    c.circle(16, 16, 1.6, '.')
    c.poly([(22, 2.5), (29, 2.5), (25.5, 11)], 'O') if False else None
    c.outline()


@icon('kylin-camera', ['org.kylin.camera', 'kylin-webcam'], 'kylin', 'Kylin Camera')
def kylin_camera(c):
    c.rrect(10, 6, 19, 9, '5', 1)
    c.rrect(3, 8, 28, 26, 'C', 3)
    c.bevel(['C'])
    c.circle(16, 17, 7.5, 'W')
    c.circle(16, 17, 5, '5')
    c.circle(16, 17, 2.5, 'k')
    c.px(14, 15, 'c')
    c.outline()


@icon('ukui-clock', ['kylin-alarm-clock', 'org.ukui.clock', 'kylin-clock'], 'kylin', 'UKUI Clock')
def ukui_clock(c):
    c.circle(7, 7, 4, 'C'); c.circle(25, 7, 4, 'C')
    c.circle(16, 17, 11.5, 'C')
    c.bevel(['C'])
    c.circle(16, 17, 8.5, 'W')
    c.rect(15, 10, 16, 17, 'k')
    c.rect(16, 16, 21, 17, 'k')
    c.rect(9, 28, 11, 29, '5') if False else None
    c.outline()


@icon('ukui-system-monitor', ['kylin-system-monitor', 'org.ukui.system-monitor'], 'kylin', 'UKUI System Monitor')
def ukui_system_monitor(c):
    c.rrect(3, 4, 28, 27, 'C', 3)
    c.bevel(['C'])
    for i, h in enumerate((6, 11, 8, 15, 10)):
        c.rect(7 + i * 4, 23 - h, 9 + i * 4, 23, 'W')
    c.hline(6, 25, 24, '5')
    c.outline()


@icon('kylin-font-viewer', ['org.kylin.font-viewer', 'kylin-font-manager'], 'kylin', 'Kylin Font Viewer')
def kylin_font_viewer(c):
    c.rrect(3, 3, 28, 28, 'C', 4)
    c.bevel(['C'])
    c.text(6, 9, 'A', 'W', font=5, scale=2, gap=0)
    c.text(18, 15, 'A', 'c', font=5)
    c.outline()


@icon('kylin-connectivity', ['org.kylin.connectivity', 'kylin-mobile-assistant'], 'kylin', 'Kylin Connectivity')
def kylin_connectivity(c):
    c.rrect(3, 6, 22, 20, 'S', 1)
    c.rect(5, 8, 20, 18, 'C')
    c.rect(3, 21, 22, 22, 'w')
    c.rrect(20, 11, 28, 26, 'k', 2)
    c.rect(21, 13, 27, 23, 'c')
    c.bevel(['C', 'c'])
    c.outline()


@icon('ukui-search', ['org.ukui.search', 'kylin-search'], 'kylin', 'UKUI Search')
def ukui_search(c):
    c.circle(13, 13, 10, 'C')
    c.circle(13, 13, 6.5, 'W')
    c.bevel(['C'])
    c.line(20, 20, 25, 25, 'C', 3)
    c.px(10, 10, 'c'); c.px(11, 9, 'c')
    c.outline()


@icon('kylin-user-guide', ['org.kylin.user-guide', 'kylin-manual', 'ukui-user-guide'], 'kylin', 'Kylin User Guide')
def kylin_user_guide(c):
    c.rrect(5, 3, 26, 28, 'C', 1)
    c.bevel(['C'])
    c.rect(5, 25, 26, 28, 'W')
    c.hline(6, 26, 26, 'w')
    c.vline(8, 3, 24, '5')
    c.circle(17, 14, 5, 'W')
    c.circle(17, 14, 2.5, 'C')
    c.outline()


@icon('distributor-logo-openkylin', ['openkylin', 'openkylin-logo', 'start-here-openkylin'], 'kylin', 'openKylin')
def openkylin_logo(c):
    c.circle(16, 16, 13, 'B')
    c.arc(16, 16, 13, 0, 0, 180, 'G')
    c.bevel(['B', 'G'])
    c.circle(16, 16, 7, 'W')
    c.circle(16, 16, 4, 'C')
    c.outline()


# ================================================================ Japan & Korea

@icon('kakaotalk', ['com.kakao.talk', 'kakaotalk-wine', 'kakaotalk-bin', 'KakaoTalk', 'kakao'], 'chat',
      'KakaoTalk')
def kakaotalk(c):
    round_bubble(c, 'k', 16, 14, 13, 10.5, 'left')
    c.replace('k', 'Y')
    c.bevel(['Y'])
    c.text(7, 11, 'TALK', '8', font=3, gap=1)
    c.outline()


@icon('naver-whale', ['whale', 'naver-whale-stable', 'com.naver.whale', 'whale-browser', 'naver-whale-beta'],
      'web', 'Naver Whale')
def naver_whale(c):
    c.circle(16, 16, 13, 'b')
    c.bevel(['b'])
    c.ellipse(16, 20, 11, 6, 'B')
    c.poly([(5, 20), (5, 10), (9, 14), (13, 13), (9, 18)], 'B')
    c.ellipse(18, 22, 7, 3, 'W')
    c.rect(21, 17, 22, 18, 'K')
    c.ring(16, 16, 13, 12, '6') if False else None
    c.outline()


@icon('mozc', ['ibus-mozc', 'fcitx-mozc', 'fcitx5-mozc', 'org.fcitx.Fcitx5.Addon.Mozc', 'mozc-tool',
               'mozc-ut'], 'system', 'Mozc')
def mozc(c):
    c.rrect(3, 5, 28, 28, 'w', 3)
    c.rrect(5, 5, 26, 24, 'W', 3)
    c.bevel(['W'], dark=False)
    g(c, 9, 8, """
        ....#.....#..
        ############.
        ....#.....#..
        ...###...##..
        ..#.#.#.#.#..
        .#..#..#..#..
        ...##...##...
    """, 'R')
    c.outline()


@icon('mozc-dictionary-tool', ['mozc-dictionary', 'mozc-word-register', 'mozc-dict-tool'], 'system',
      'Mozc Dictionary Tool')
def mozc_dict(c):
    c.rrect(5, 3, 26, 28, 'R', 1)
    c.bevel(['R'])
    c.rect(5, 25, 26, 28, 'W')
    c.hline(6, 26, 26, 'w')
    c.vline(8, 3, 24, '1')
    g(c, 12, 9, """
        .#####..
        ...#....
        #######.
        ..#.#...
        .#..#.#.
        #....##.
    """, 'W')
    c.outline()


@icon('ibus-anthy', ['anthy', 'fcitx-anthy', 'fcitx5-anthy', 'org.fcitx.Fcitx5.Addon.Anthy', 'ibus-setup-anthy',
                     'anthy-unicode'], 'system', 'Anthy')
def anthy(c):
    c.rrect(3, 5, 28, 28, 'w', 3)
    c.rrect(5, 5, 26, 24, 'W', 3)
    c.bevel(['W'], dark=False)
    g(c, 10, 8, """
        ...#.......
        ########...
        ..#........
        ..#.####...
        .#.#....#..
        #..#.....#.
        #.##....#..
        .#..####...
    """, 'B')
    c.outline()


@icon('ibus-hangul', ['hangul', 'fcitx-hangul', 'fcitx5-hangul', 'org.fcitx.Fcitx5.Addon.Hangul', 'nimf',
                      'ibus-setup-hangul'], 'system', 'Hangul')
def hangul(c):
    c.rrect(3, 5, 28, 28, 'w', 3)
    c.rrect(5, 5, 26, 24, 'W', 3)
    c.bevel(['W'], dark=False)
    g(c, 8, 8, """
        ..#.....#..
        #####...#..
        .###....###
        #...#...#..
        .###....#..
        .........#.
        ..########.
    """, 'R')
    g(c, 10, 15, "", 'B') if False else None
    c.outline()


@icon('kime', ['kime-indicator', 'kime-window', 'org.kime'], 'system', 'kime')
def kime(c):
    disc(c, 'B', 13)
    c.text(8, 12, 'KI', 'W', font=5, gap=2)
    c.rect(22, 12, 23, 18, 'R')
    c.outline()


@icon('ibus-skk', ['skk', 'fcitx-skk', 'fcitx5-skk', 'org.fcitx.Fcitx5.Addon.SKK', 'libskk'], 'system', 'SKK')
def skk(c):
    c.rrect(3, 5, 28, 28, 'w', 3)
    c.rrect(5, 5, 26, 24, 'W', 3)
    c.bevel(['W'], dark=False)
    c.text(7, 11, 'SKK', 'G', font=5, gap=1) if False else c.text(8, 11, 'SKK', 'G', font=3, gap=2)
    c.text(8, 11, 'SKK', 'G', font=3, gap=2)
    c.hline(8, 22, 18, '4')
    c.outline()


@icon('papago', ['naver-papago', 'com.naver.labs.translator', 'papago-desktop'], 'utilities', 'Papago')
def papago(c):
    round_bubble(c, 'G', 14, 13, 11, 9.5, 'left')
    c.bevel(['G'])
    c.circle(22, 20, 7.5, 'B')
    c.bevel(['B'])
    c.text(10, 10, 'A', 'W', font=5)
    c.text(19, 17, 'P', 'W', font=5) if False else g(c, 19, 17, """
        #####
        ..#..
        .#.#.
        #...#
        .....
        #####
    """, 'W')
    c.outline()


@icon('chatwork', ['com.chatwork', 'chatwork-desktop'], 'chat', 'Chatwork')
def chatwork(c):
    # four-petal clover in Chatwork colours
    for (x, y, col) in ((10, 10, 'R'), (22, 10, 'G'), (10, 22, 'B'), (22, 22, 'Y')):
        c.circle(x, y, 6.5, col)
    c.circle(16, 16, 3, 'W')
    c.outline()


@icon('niconico', ['jp.nicovideo', 'nicovideo', 'niconico-desktop'], 'media', 'niconico')
def niconico(c):
    c.line(10, 3, 14, 8, 'k', 2); c.line(22, 3, 18, 8, 'k', 2)
    c.rrect(3, 8, 28, 27, 'k', 3)
    c.bevel(['k'], dark=False)
    c.rrect(6, 11, 25, 24, 'W', 2)
    c.text(10, 15, 'NI', 'k', font=5, gap=2) if False else None
    c.rect(10, 15, 11, 18, 'k'); c.rect(20, 15, 21, 18, 'k')
    c.hline(13, 18, 21, 'k')
    c.outline()


@icon('pixiv', ['net.pixiv', 'pixiv-desktop', 'pixiv-webapp'], 'media', 'pixiv')
def pixiv(c):
    disc(c, 'B', 13)
    c.ring(17, 14, 7, 3.5, 'W')
    c.rect(9, 9, 11, 24, 'W')
    c.outline()


# ================================================================ proxy clients

def _cat(c, col, face='W', eyes='k'):
    c.poly([(4, 3), (12, 9), (5, 14)], col)
    c.poly([(28, 3), (20, 9), (27, 14)], col)
    c.ellipse(16, 18, 13, 10.5, col)
    c.bevel([col])
    c.ellipse(16, 20, 9, 6.5, face)
    c.rect(11, 18, 12, 20, eyes); c.rect(20, 18, 21, 20, eyes)
    c.hline(15, 16, 22, 'p')


@icon('clash-verge', ['clash-verge-rev', 'io.github.clash-verge-rev', 'clash-verge-rev-bin', 'clash-verge-bin',
                      'clash-verge-rev-alpha', 'io.github.clash_verge_rev.clash_verge_rev', 'Clash Verge',
                      'clash-verge-rev-git', 'clash-verge-service'], 'network', 'Clash Verge Rev')
def clash_verge(c):
    _cat(c, 'B')
    c.outline()


@icon('clash-nyanpasu', ['clash-nyanpasu-bin', 'clash-nyanpasu-git', 'io.github.libnyanpasu.clash-nyanpasu',
                         'Clash Nyanpasu', 'nyanpasu'], 'network', 'Clash Nyanpasu')
def clash_nyanpasu(c):
    _cat(c, 'P', 'W', 'M')
    c.px(9, 23, 'p'); c.px(22, 23, 'p')
    c.outline()


@icon('clash-for-windows', ['cfw', 'clash-for-windows-bin', 'clash-for-windows-chinese', 'Clash for Windows'],
      'network', 'Clash for Windows')
def cfw(c):
    _cat(c, 'S', 'W', 'B')
    c.outline()


@icon('nekoray', ['nekoray-bin', 'nekobox', 'nekoray-git', 'throne', 'nekobox-bin', 'moe.matsuri.nekoray'],
      'network', 'NekoRay / Throne')
def nekoray(c):
    _cat(c, 'k', 'k', 'Y')
    c.bevel(['k'], dark=False)
    c.outline()


@icon('mihomo-party', ['mihomo-party-bin', 'mihomo-party-electron', 'clash-party', 'mihomo-party-git',
                       'io.github.mihomo-party', 'sparkle', 'sparkle-bin'], 'network', 'Mihomo Party')
def mihomo_party(c):
    # party hat with confetti
    c.poly([(16, 2.5), (26, 26), (6, 26)], 'M')
    c.bevel(['M'])
    for i, col in enumerate(['Y', 'C', 'Y']):
        y = 10 + i * 5
        c.hline(16 - (y - 2) * 10 // 24 + 1, 16 + (y - 2) * 10 // 24 - 1, y, col)
    c.rrect(4, 26, 28, 28, 'm', 1)
    c.circle(16, 3.5, 2, 'Y') if False else None
    c.outline()


@icon('flclash', ['FlClash', 'com.follow.clash', 'flclash-bin', 'flclash-git', 'com.follow.FlClash'], 'network',
      'FlClash')
def flclash(c):
    hexagon(c, 'C', 16, 16, 13.5)
    c.rect(11, 9, 13, 23, 'W')
    c.rect(11, 9, 21, 11, 'W')
    c.rect(11, 15, 19, 17, 'W')
    c.outline()


@icon('v2rayn', ['v2rayN', 'v2rayn-bin', 'v2rayn-git', 'com.github.2dust.v2rayN'], 'network', 'v2rayN')
def v2rayn(c):
    c.poly([(3, 4), (12, 4), (16, 15), (20, 4), (29, 4), (19.5, 28), (12.5, 28)], 'B')
    c.bevel(['B'])
    c.poly([(7, 6), (10, 6), (15, 20), (14, 23)], 'b')
    c.outline()


@icon('v2raya', ['v2raya-bin', 'v2raya-git', 'v2rayA', 'org.v2raya.v2raya'], 'network', 'v2rayA')
def v2raya(c):
    c.poly([(16, 2.5), (29, 28), (21, 28), (16, 17), (11, 28), (3, 28)], 'M')
    c.bevel(['M'])
    c.rect(10, 21, 22, 23, 'm') if False else None
    c.outline()


@icon('qv2ray', ['com.github.Qv2ray', 'qv2ray-bin', 'Qv2ray', 'qv2ray-dev-git'], 'network', 'Qv2ray')
def qv2ray(c):
    c.ring(15, 15, 12, 6.5, 'C')
    c.line(19, 19, 25, 25, 'C', 3)
    c.bevel(['C'])
    c.circle(15, 15, 3, 'B')
    c.outline()


@icon('hiddify', ['hiddify-next', 'app.hiddify.com', 'hiddify-bin', 'hiddify-app', 'Hiddify'], 'network',
      'Hiddify')
def hiddify(c):
    c.rrect(4, 3, 12, 28, 'B', 3)
    c.rrect(19, 3, 27, 28, 'C', 3)
    c.rect(11, 13, 20, 18, 'b')
    c.bevel(['B', 'C', 'b'])
    c.outline()


@icon('shadowsocks-qt5', ['ss-qt5', 'shadowsocks', 'org.shadowsocks.qt5', 'shadowsocks-electron'], 'network',
      'Shadowsocks')
def shadowsocks(c):
    c.poly([(3, 15), (29, 4), (21, 28), (15, 19)], 'w')
    c.poly([(15, 19), (29, 4), (13, 26)], 'S')
    c.bevel(['w'])
    c.line(15, 19, 28, 5, 's')
    c.outline()


@icon('easyconnect', ['EasyConnect', 'easyconnect-bin', 'sangfor-easyconnect', 'com.sangfor.easyconnect'],
      'network', 'EasyConnect')
def easyconnect(c):
    disc(c, 'B', 13)
    c.ring(12, 16, 5, 3, 'W')
    c.ring(20, 16, 5, 3, 'W')
    c.arc(12, 16, 5, 3, 300, 60, 'B')
    c.ring(20, 16, 5, 3, 'W')
    c.outline()


@icon('atrust', ['aTrust', 'sangfor-atrust', 'atrust-bin', 'com.sangfor.atrust'], 'network', 'aTrust')
def atrust(c):
    shield(c, 'G', 5, 26, 3, 28)
    c.text(11, 9, 'A', 'W', font=5, scale=2, gap=0) if False else c.text(13, 10, 'A', 'W', font=5)
    c.hline(10, 21, 19, 'g')
    c.outline()


@icon('todesk', ['todesk-bin', 'com.todesk.ToDesk', 'ToDesk', 'todesk-client'], 'network', 'ToDesk')
def todesk(c):
    monitor(c, 'B', 'b')
    c.sprite(12, 8, """
        K.......
        KK......
        KWK.....
        KWWK....
        KWWWK...
        KWWWWK..
        KWWKKK..
        KK.KWK..
    """)
    c.outline()


@icon('sunloginclient', ['sunlogin', 'sunloginclient-bin', 'com.oray.sunlogin', 'oray-sunlogin',
                         'com.oray.sunlogin.client', 'sunlogin-remote'], 'network', 'Sunlogin')
def sunlogin(c):
    import math
    for a in range(0, 360, 45):
        x = 16 + 10.5 * math.cos(math.radians(a))
        y = 16 + 10.5 * math.sin(math.radians(a))
        c.circle(x, y, 2.6, 'O')
    c.circle(16, 16, 9.5, 'O')
    c.bevel(['O'])
    c.circle(16, 16, 5.5, 'Y')
    c.circle(16, 16, 2.5, 'W')
    c.outline()
