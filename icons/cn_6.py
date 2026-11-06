from pix import icon
"""Chinese & Asian software VI: more AI, input methods, network tools, maker apps."""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cn_lib import g, gc, disc, bubble, round_bubble, doc, cloud, tile, shield, hexagon, diamond, play, note, monitor  # noqa: E402


def _keycap(c, top='W', side='w'):
    c.rrect(3, 5, 28, 28, side, 3)
    c.rrect(5, 5, 26, 24, top, 3)
    c.bevel([top], dark=False)


def _laptop(c, col, screen):
    c.rrect(5, 5, 26, 21, col, 2)
    c.rect(7, 7, 24, 19, screen)
    c.rrect(3, 22, 28, 25, col, 1)
    c.bevel([col])
    c.hline(13, 18, 22, DARKS.get(col, 'k'))


DARKS = {'R': '1', 'C': '5', 'B': '6', 'S': 's', 'G': '4'}


# ================================================================ input methods

@icon('wetype', ['com.tencent.wetype', 'wechat-input', 'wetype-bin', 'fcitx5-wetype', 'wechat-ime'], 'system',
      'WeChat Input')
def wetype(c):
    _keycap(c, 'G', '4')
    c.ellipse(16, 13.5, 8, 6, 'W')
    c.poly([(11, 17), (15, 19), (10, 22)], 'W')
    c.rect(13, 12, 14, 13, 'G'); c.rect(18, 12, 19, 13, 'G')
    c.outline()


@icon('qqpinyin', ['fcitx-qqpinyin', 'qq-pinyin', 'com.tencent.qqpinyin', 'qqpinyin-bin'], 'system', 'QQ Pinyin')
def qqpinyin(c):
    _keycap(c)
    c.ring(15, 14, 6.5, 4, 'B')
    c.line(17, 16, 22, 21, 'B', 2)
    c.outline()


@icon('huayupy', ['fcitx5-huayupy', 'huayu-pinyin', 'com.huayupy.ime', 'fcitx-huayupy'], 'system', 'Huayu Pinyin')
def huayupy(c):
    _keycap(c)
    c.text(8, 11, 'HY', 'R', font=5, gap=3)
    c.outline()


@icon('wubi', ['fcitx-table-wubi', 'ibus-table-wubi', 'fcitx5-table-wubi', 'wubi86', 'rime-wubi',
               'org.fcitx.Fcitx5.Addon.Wubi'], 'system', 'Wubi')
def wubi(c):
    _keycap(c)
    g(c, 10, 8, """
        ###########
        ....#......
        ....#......
        .#######...
        ...#...#...
        ...#...#...
        ...#...#...
        ###########
    """, 'k')
    c.outline()


@icon('ibus-table-cangjie', ['cangjie', 'fcitx-table-cangjie', 'fcitx5-table-cangjie', 'ibus-cangjie',
                             'cangjie5'], 'system', 'Cangjie')
def cangjie(c):
    _keycap(c)
    c.text(8, 11, 'CJ', 'M', font=5, gap=3)
    c.outline()


@icon('gcin', ['gcin-setup', 'gcin-tools'], 'system', 'gcin')
def gcin(c):
    _keycap(c, 'W', 'w')
    c.circle(16, 14.5, 7, 'O')
    c.circle(16, 14.5, 4, 'W')
    c.rect(16, 13, 23, 16, 'W')
    c.rect(17, 14, 20, 15, 'O')
    c.outline()


@icon('hime', ['hime-setup', 'hime-input-method'], 'system', 'HIME')
def hime(c):
    _keycap(c, 'P', '9')
    g(c, 9, 9, """
        ..#.....#..
        .###...###.
        ###########
        #.#.#.#.#.#
        ###########
    """, 'Y')
    c.hline(9, 19, 19, '9') if False else None
    c.outline()


# ================================================================ AI apps

@icon('baichuan', ['baixiaoying', 'baichuan-ai', 'com.baichuan.app'], 'ai', 'Baichuan')
def baichuan(c):
    disc(c, 'O', 13)
    for i, y in enumerate((10, 16, 22)):
        for x in range(7, 26):
            yy = y + round(1.6 * math.sin((x - 7) / 2.6 + i))
            c.px(x, yy, 'W'); c.px(x, yy + 1, 'W')
    c.outline()


@icon('tiangong', ['tiangong-ai', 'skywork', 'skywork-ai', 'com.kunlun.tiangong'], 'ai', 'Tiangong / Skywork')
def tiangong(c):
    disc(c, 'M', 13)
    g(c, 9, 9, """
        #############
        ......#......
        ......#......
        #############
        .....#.#.....
        ....#...#....
        ..##.....##..
        ##.........##
    """, 'W')
    c.outline()


@icon('xinghuo', ['iflytek-spark', 'spark-desk', 'xunfei-xinghuo', 'sparkdesk', 'com.iflytek.spark'], 'ai',
      'iFlytek Spark')
def xinghuo(c):
    # a flame
    c.poly([(16, 2.5), (24, 12), (26, 20), (22, 27), (16, 29.5), (10, 27), (6, 20), (8, 12), (11, 15)], 'R')
    c.bevel(['R'])
    c.poly([(16, 12), (21, 20), (19, 26), (16, 27.5), (13, 26), (11, 20)], 'O')
    c.poly([(16, 18), (18.5, 23), (16, 26), (13.5, 23)], 'Y')
    c.outline()


@icon('metaso', ['metaso-ai', 'mita', 'com.metaso.app'], 'ai', 'Metaso')
def metaso(c):
    # a pagoda (秘塔)
    c.rect(15, 3, 16, 4, 'Y')
    for i, (y, w) in enumerate(((5, 6), (11, 9), (17, 12))):
        c.poly([(16 - w - 1, y + 4), (16, y), (16 + w + 1, y + 4)], 'B')
        c.rect(16 - w + 3, y + 4, 15 + w - 3, y + 6, 'W' if i < 2 else 'W')
    c.rect(7, 22, 24, 27, 'W')
    c.rect(14, 24, 17, 27, 'B')
    c.bevel(['B', 'W'])
    c.outline()


@icon('coze', ['coze-desktop', 'com.coze.app', 'coze-studio', 'koozi'], 'ai', 'Coze')
def coze(c):
    c.rrect(3, 5, 28, 27, 'B', 6)
    c.rect(6, 3, 8, 6, 'B'); c.rect(23, 3, 25, 6, 'B')
    c.bevel(['B'])
    c.ellipse(11.5, 16, 3, 4, 'W'); c.ellipse(20.5, 16, 3, 4, 'W')
    c.rect(11, 16, 12, 17, 'K'); c.rect(20, 16, 21, 17, 'K')
    c.outline()


@icon('jimeng', ['jimeng-ai', 'dreamina', 'com.bytedance.jimeng', 'jimeng-desktop'], 'ai', 'Jimeng / Dreamina')
def jimeng(c):
    cloud(c, 'M', 2)
    c.bevel(['M'])
    for x, y in ((12, 18), (20, 20)):
        c.rect(x - 1, y, x + 1, y, 'W'); c.rect(x, y - 1, x, y + 1, 'W')
    c.circle(16, 6, 3, 'Y') if False else None
    c.outline()


@icon('kling', ['kling-ai', 'keling', 'com.kuaishou.kling'], 'ai', 'Kling AI')
def kling(c):
    c.poly([(4, 3), (22, 16), (4, 29)], 'G')
    c.poly([(12, 7), (28.5, 16), (12, 25)], 'C')
    c.bevel(['G', 'C'])
    c.poly([(12, 10), (18, 16), (12, 22)], '4')
    c.outline()


@icon('nextchat', ['chatgpt-next-web', 'nextchat-bin', 'NextChat', 'com.yida.chatgpt.next.web'], 'ai', 'NextChat')
def nextchat(c):
    bubble(c, 'k', 3, 4, 28, 23, 'right')
    c.bevel(['k'], dark=False)
    c.rect(9, 9, 11, 19, 'G'); c.rect(20, 9, 22, 19, 'G')
    c.line(11, 9, 20, 19, 'G', 2)
    c.outline()


@icon('deepchat', ['deepchat-bin', 'com.thinkinaixyz.deepchat', 'DeepChat', 'deepchat-appimage'], 'ai', 'DeepChat')
def deepchat(c):
    round_bubble(c, 'B', 16, 14, 13, 11, 'left')
    c.bevel(['B'])
    for x in (9, 15, 21):
        c.rect(x, 13, x + 2, 15, 'W')
    c.outline()


@icon('lingma', ['tongyi-lingma', 'com.alibaba.lingma', 'lingma-bin'], 'ai', 'Tongyi Lingma')
def lingma(c):
    diamond(c, 'M', 16, 16, 13.5)
    g(c, 9, 12, """
        ..#.......#..
        .#...#.....#.
        #...#.......#
        .#.#.......#.
        ..#.......#..
    """, 'W')
    c.outline()


@icon('comate', ['baidu-comate', 'com.baidu.comate', 'comate-bin'], 'ai', 'Baidu Comate')
def comate(c):
    c.ring(16, 16, 13, 7.5, 'B')
    c.rect(22, 13, 29, 19, '.')
    c.bevel(['B'])
    c.rect(14, 12, 15, 20, 'C'); c.rect(18, 12, 19, 20, 'C')
    c.outline()


# ================================================================ media & creative

@icon('xiaoyuzhoufm', ['xiaoyuzhou', 'com.xiaoyuzhou.app', 'xiaoyuzhou-fm'], 'media', 'Xiaoyuzhou FM')
def xiaoyuzhou(c):
    c.circle(16, 16, 9, 'M')
    c.bevel(['M'])
    c.ellipse(16, 17, 12.5, 4, 'Y')
    c.ellipse(16, 16, 10, 2, '.')
    c.circle(16, 16, 9, 'M') if False else None
    for y in range(7, 17):
        for x in range(32):
            if (x + .5 - 16) ** 2 + (y + .5 - 16) ** 2 <= 81:
                c.px(x, y, 'M')
    c.bevel(['M'])
    c.px(12, 10, 'W'); c.px(13, 9, 'm')
    c.outline()


@icon('qishui-music', ['soda-music', 'qishuimusic', 'com.bytedance.qishui', 'qishui'], 'media', 'Qishui Music')
def qishui(c):
    # a soda bottle with bubbles
    c.rect(13, 3, 18, 5, 'R')
    c.rect(13, 6, 18, 9, 'C')
    c.poly([(13, 9), (18, 9), (23, 15), (23, 28), (8, 28), (8, 15)], 'C')
    c.bevel(['C'])
    c.rect(8, 17, 23, 22, 'W')
    note(c, 13, 16, 'C', 7) if False else c.rect(14, 18, 17, 21, 'B')
    for x, y in ((11, 25), (14, 13), (19, 25)):
        c.px(x, y, 'c')
    c.outline()


@icon('migu-music', ['migu', 'com.migu.music', 'migumusic', 'migu-video'], 'media', 'Migu Music')
def migu(c):
    disc(c, 'P', 13)
    c.circle(16, 16, 9.5, 'M')
    note(c, 11, 9, 'W', 14)
    c.outline()


@icon('livehime', ['bilibili-livehime', 'com.bilibili.livehime', 'bili-live'], 'media', 'Bilibili Livehime')
def livehime(c):
    c.line(9, 3, 13, 8, 'P', 2)
    c.line(23, 3, 19, 8, 'P', 2)
    c.rrect(3, 8, 28, 27, 'P', 4)
    c.bevel(['P'])
    c.rrect(6, 11, 25, 24, 'W', 3)
    c.circle(11, 17.5, 2.5, 'R')
    c.text(15, 15, 'ON', '9', font=3, gap=1)
    c.outline()


@icon('evcapture', ['ev-capture', 'ev-recorder', 'ieway-evcapture'], 'media', 'EV Capture')
def evcapture(c):
    c.rrect(3, 8, 21, 25, 'R', 3)
    c.poly([(21, 14), (29, 9), (29, 24), (21, 19)], 'R')
    c.bevel(['R'])
    c.circle(12, 16.5, 4.5, 'W')
    c.circle(12, 16.5, 2.2, 'R')
    c.outline()


@icon('openutau', ['OpenUtau', 'openutau-bin', 'com.stakira.openutau'], 'media', 'OpenUtau')
def openutau(c):
    # piano-roll notes with a mic
    c.rrect(3, 4, 28, 27, 'k', 2)
    c.bevel(['k'], dark=False)
    for x, y, w in ((6, 8, 6), (13, 12, 7), (20, 7, 5), (8, 18, 9), (19, 22, 6)):
        c.rect(x, y, x + w, y + 2, 'C')
    c.outline()


# ================================================================ maker & 3D printing

@icon('flashprint', ['FlashPrint', 'flashforge-flashprint', 'flashprint5', 'com.flashforge.flashprint'],
      'graphics', 'FlashPrint')
def flashprint(c):
    # filament spool
    c.circle(16, 16, 13, 'S')
    c.bevel(['S'])
    c.circle(16, 16, 10.5, 'O')
    for r in (8.5, 6):
        c.ring(16, 16, r, r - .8, '2')
    c.circle(16, 16, 4, 'S')
    c.circle(16, 16, 2, '.')
    c.outline()


@icon('elegoo-slicer', ['ElegooSlicer', 'elegooslicer', 'elegoo-slicer-bin', 'com.elegoo.slicer'], 'graphics',
      'Elegoo Slicer')
def elegoo(c):
    for i, col in enumerate(('6', 'B', 'b', 'B', 'b')):
        y = 23 - i * 4
        w = 12 - i
        c.poly([(16 - w, y), (16, y - 3), (16 + w, y), (16, y + 3)], col)
        c.rect(16 - w, y, 16 + w, y + 1, col)
    c.poly([(4, 23), (16, 26), (28, 23), (28, 25), (16, 28), (4, 25)], '6')
    c.outline()


@icon('snapmaker-luban', ['luban', 'snapmaker', 'Snapmaker Luban', 'snapmaker-luban-bin', 'snapmaker-orca'],
      'graphics', 'Snapmaker Luban')
def luban(c):
    # carpenter's square + hammer for Luban (鲁班)
    c.rect(4, 4, 8, 28, 'O'); c.rect(4, 24, 27, 28, 'O')
    c.bevel(['O'])
    for y in range(7, 23, 3):
        c.hline(7, 8, y, '2')
    c.rect(13, 5, 26, 10, 'S')
    c.rect(18, 11, 20, 21, 'N')
    c.bevel(['S'])
    c.outline()


# ================================================================ network tools

@icon('gui-for-clash', ['GUI.for.Clash', 'gui.for.clash', 'gui-for-clash-bin'], 'network', 'GUI.for.Clash')
def gui_for_clash(c):
    c.rrect(3, 4, 28, 27, 'W', 2)
    c.rrect(3, 4, 28, 8, 'B', 2)
    c.rect(3, 7, 28, 8, 'B')
    c.bevel(['W', 'B'])
    c.poly([(8, 12), (13, 15), (9, 18)], 'B'); c.poly([(23, 12), (18, 15), (22, 18)], 'B')
    c.ellipse(15.5, 19, 7, 5, 'B')
    c.rect(12, 18, 12, 19, 'W'); c.rect(18, 18, 18, 19, 'W')
    c.outline()


@icon('gui-for-singbox', ['GUI.for.SingBox', 'gui.for.singbox', 'gui-for-singbox-bin'], 'network',
      'GUI.for.SingBox')
def gui_for_singbox(c):
    c.rrect(3, 4, 28, 27, 'W', 2)
    c.rrect(3, 4, 28, 8, 'G', 2)
    c.rect(3, 7, 28, 8, 'G')
    c.bevel(['W', 'G'])
    c.poly([(15.5, 11), (22, 14), (15.5, 17), (9, 14)], 'g')
    c.poly([(9, 14), (15.5, 17), (15.5, 24), (9, 21)], 'G')
    c.poly([(15.5, 17), (22, 14), (22, 21), (15.5, 24)], '4')
    c.outline()


@icon('karing', ['Karing', 'karing-bin', 'com.nebula.karing', 'karing-appimage'], 'network', 'Karing')
def karing(c):
    disc(c, 'O', 13)
    c.rect(9, 8, 11, 23, 'W')
    c.line(12, 16, 20, 8, 'W', 3)
    c.line(13, 15, 21, 22, 'W', 3)
    c.outline()


@icon('easytier', ['easytier-gui', 'EasyTier', 'easytier-bin', 'com.easytier.gui'], 'network', 'EasyTier')
def easytier(c):
    c.line(16, 7, 7, 23, 'G', 2); c.line(16, 7, 24, 23, 'G', 2); c.line(7, 24, 24, 24, 'G', 2)
    for x, y in ((16, 7), (7, 24), (25, 24)):
        c.circle(x, y, 4.5, 'G')
        c.circle(x, y, 2, 'W')
    c.bevel(['G'])
    c.outline()


@icon('frpc-desktop', ['frp', 'frpc', 'frpc-gui', 'frpc-desktop-bin', 'frp-desktop'], 'network', 'frpc Desktop')
def frpc_desktop(c):
    # an arched tunnel with a passing arrow
    c.rect(4, 15, 27, 28, 'S')
    c.circle(15.5, 15, 11.5, 'S')
    c.bevel(['S'])
    c.rect(9, 16, 22, 28, 'k')
    c.circle(15.5, 16, 6.5, 'k')
    c.poly([(9, 21), (17, 21), (17, 18), (22, 23), (17, 28), (17, 25), (9, 25)], 'B')
    c.outline()


@icon('sakurafrp', ['natfrp', 'sakura-frp', 'sakurafrp-launcher', 'com.natfrp.launcher'], 'network', 'SakuraFrp')
def sakurafrp(c):
    # cherry blossom
    for a in range(-90, 270, 72):
        x = 16 + 7.5 * math.cos(math.radians(a))
        y = 16.5 + 7.5 * math.sin(math.radians(a))
        c.circle(x, y, 6, 'P')
    c.bevel(['P'])
    for a in range(-90, 270, 72):
        x = 16 + 11 * math.cos(math.radians(a))
        y = 16.5 + 11 * math.sin(math.radians(a))
        c.px(x, y, '.')
    c.circle(16, 16.5, 3, 'p')
    c.circle(16, 16.5, 1.5, 'Y')
    c.outline()


@icon('pgyvpn', ['pgy-vpn', 'oray-pgyvpn', 'com.oray.pgyvpn', 'pgyvpn-bin'], 'network', 'PgyVPN')
def pgyvpn(c):
    # dandelion (蒲公英)
    c.line(16, 18, 15, 27, 'G', 2)
    c.poly([(15, 25), (8, 22), (10, 26)], 'G')
    c.circle(16, 11, 8, 'W')
    c.bevel(['W'])
    for a in range(0, 360, 45):
        c.line(16, 11, 16 + 5 * math.cos(math.radians(a)), 11 + 5 * math.sin(math.radians(a)), 'w')
    c.circle(16, 11, 1.5, 'Y')
    c.outline()


@icon('uu-remote', ['uuyc', 'netease-uu-remote', 'com.netease.uuremote', 'uu-remote-bin'], 'network',
      'UU Remote')
def uu_remote(c):
    c.rrect(3, 3, 19, 15, 'G', 2)
    c.rect(5, 5, 17, 13, 'k')
    c.rrect(12, 13, 28, 25, 'G', 2)
    c.rect(14, 15, 26, 23, 'k')
    c.rect(18, 26, 22, 28, '4')
    c.bevel(['G'])
    c.poly([(7, 7), (11, 9), (7, 11)], 'g')
    c.poly([(18, 17), (22, 19), (18, 21)], 'g')
    c.outline()


@icon('gameviewer', ['netease-gameviewer', 'GameViewer', 'com.netease.gameviewer'], 'network', 'GameViewer')
def gameviewer(c):
    monitor(c, 'C', 'k')
    c.rrect(9, 10, 22, 16, 'W', 2)
    c.rect(11, 12, 13, 12, 'k'); c.rect(12, 11, 12, 13, 'k')
    c.px(19, 12, 'R'); c.px(20, 14, 'B')
    c.outline()


# ================================================================ vendor tools

@icon('lenovo-pc-manager', ['lenovo-pcmanager', 'lenovo-vantage', 'com.lenovo.pcmanager', 'lenovo-legion-zone'],
      'system', 'Lenovo PC Manager')
def lenovo_pc_manager(c):
    _laptop(c, 'R', 'W')
    c.text(10, 10, 'L', 'R', font=5)
    c.hline(16, 21, 16, 'R')
    c.outline()


@icon('honor-pc-manager', ['honor-pcmanager', 'com.hihonor.pcmanager', 'honor-manager'], 'system',
      'Honor PC Manager')
def honor_pc_manager(c):
    _laptop(c, 'C', 'k')
    c.text(13, 10, 'H', 'c', font=5)
    c.outline()


# ================================================================ office

@icon('shimo', ['shimo-desktop', 'shimo-docs', 'com.shimo.app', 'shimo-bin'], 'office', 'Shimo Docs')
def shimo(c):
    # a graphite pencil (石墨)
    c.poly([(4, 28), (6, 21), (22, 5), (27, 10), (11, 26)], 'k')
    c.poly([(22, 5), (25, 2.5), (29.5, 7), (27, 10)], 'R')
    c.poly([(4, 28), (6, 21), (11, 26)], 'n')
    c.poly([(4, 28), (5, 25), (7, 27)], 'K')
    c.line(8, 22, 23, 7, 's')
    c.outline()


@icon('kdocs', ['kingsoft-docs', 'kdocs-desktop', 'jinshan-docs', 'com.kingsoft.kdocs'], 'office',
      'Kingsoft Docs')
def kdocs(c):
    cloud(c, 'B', 1)
    c.bevel(['B'])
    c.rect(11, 13, 20, 23, 'W')
    c.hline(13, 18, 16, 'b'); c.hline(13, 18, 18, 'b'); c.hline(13, 16, 20, 'b')
    c.outline()


@icon('qqgame', ['qq-game', 'com.tencent.qqgame', 'qqgame-bin'], 'games', 'QQ Game')
def qqgame(c):
    # joystick
    c.circle(16, 8, 5.5, 'R')
    c.bevel(['R'])
    c.rect(15, 13, 17, 20, 'S')
    c.rrect(4, 19, 27, 28, 'B', 3)
    c.bevel(['B'])
    c.rect(21, 21, 23, 22, 'Y')
    c.outline()


@icon('tencent-start', ['start-cloud-game', 'com.tencent.start', 'tencent-start-bin'], 'games',
      'START Cloud Gaming')
def tencent_start(c):
    cloud(c, 'G', 1)
    c.bevel(['G'])
    play(c, 14, 13, 11, 'W')
    c.outline()
