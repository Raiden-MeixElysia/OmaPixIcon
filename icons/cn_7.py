from pix import icon
"""Chinese & Asian software VII: Korean players, Cutefish / UOS extras, Chinese web services."""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cn_lib import g, gc, disc, bubble, round_bubble, doc, cloud, tile, shield, hexagon, diamond, play, note, monitor  # noqa: E402


# ================================================================ Korean media / office

@icon('potplayer', ['potplayermini64', 'daum-potplayer', 'potplayer-wine', 'PotPlayer'], 'media', 'PotPlayer')
def potplayer(c):
    c.poly([(5, 3), (28.5, 16), (5, 29)], 'Y')
    c.bevel(['Y'])
    c.poly([(9, 10), (20, 16), (9, 22)], '3')
    c.outline()


@icon('gom-player', ['gomplayer', 'gom', 'gom-player-wine', 'GOMPlayer'], 'media', 'GOM Player')
def gom_player(c):
    disc(c, 'G', 13)
    c.text(7, 14, 'GOM', 'W', font=3, gap=3)
    c.outline()


@icon('kmplayer', ['KMPlayer', 'kmplayer-wine', 'kmplayer64'], 'media', 'KMPlayer')
def kmplayer(c):
    disc(c, 'k', 13)
    c.bevel(['k'], dark=False)
    c.text(7, 12, 'KM', 'Y', font=5, gap=3)
    c.outline()


@icon('hancom-office', ['hoffice', 'hancom-office-hwp', 'hwp', 'hancomoffice', 'hancom-hword', 'hwpviewer'],
      'office', 'Hancom Office')
def hancom(c):
    doc(c, '6', 'b')
    c.text(9, 13, 'HWP', 'W', font=3, gap=1)
    c.hline(9, 22, 21, 'B'); c.hline(9, 18, 24, 'B')
    c.outline()


@icon('naverworks', ['line-works', 'lineworks', 'naver-works', 'com.navercorp.works'], 'chat', 'LINE WORKS')
def naverworks(c):
    round_bubble(c, 'G', 16, 14, 13, 11, 'right')
    c.bevel(['G'])
    g(c, 8, 10, """
        ##...##...##
        ##...##...##
        .##.####.##.
        .##.#..#.##.
        ..###..###..
        ..##....##..
    """, 'W')
    c.outline()


@icon('pcmanx', ['pcmanx-gtk2', 'pcmanx-gtk', 'pcman-bbs', 'ptt-client'], 'chat', 'PCManX')
def pcmanx(c):
    monitor(c, 'S', '6')
    c.text(9, 9, 'PTT', 'Y', font=3, gap=2)
    c.hline(7, 15, 17, 'b')
    c.outline()


# ================================================================ Cutefish / UOS

@icon('cutefish-filemanager', ['cutefish-file-manager', 'org.cutefish.filemanager', 'cutefish-files'], 'deepin',
      'Cutefish Files')
def cutefish_fm(c):
    c.rrect(3, 5, 14, 11, 'B', 2)
    c.rrect(3, 8, 28, 27, 'B', 3)
    c.rrect(3, 11, 28, 27, 'b', 3)
    c.bevel(['b'])
    c.circle(16, 19, 3, 'W')
    c.outline()


@icon('cutefish-settings', ['org.cutefish.settings', 'cutefish-system-settings'], 'deepin', 'Cutefish Settings')
def cutefish_settings(c):
    c.circle(16, 16, 9.5, 'S')
    for a in range(0, 360, 60):
        c.circle(16 + 10.5 * math.cos(math.radians(a)), 16 + 10.5 * math.sin(math.radians(a)), 3, 'S')
    c.bevel(['S'])
    c.circle(16, 16, 4.5, 'W')
    c.circle(16, 16, 2.5, 'B')
    c.outline()


@icon('cutefish-terminal', ['org.cutefish.terminal'], 'deepin', 'Cutefish Terminal')
def cutefish_terminal(c):
    c.rrect(3, 4, 28, 27, 'k', 5)
    c.bevel(['k'], dark=False)
    g(c, 8, 11, """
        #....
        .#...
        ..#..
        .#...
        #....
    """, 'W')
    c.rect(15, 18, 22, 19, 'b')
    c.outline()


@icon('uos-ai-assistant', ['uos-ai', 'deepin-ai-assistant', 'com.deepin.uos-ai', 'org.deepin.uosai'], 'deepin',
      'UOS AI')
def uos_ai(c):
    disc(c, 'B', 13)
    c.poly([(14, 6), (16, 13), (23, 15), (16, 17), (14, 24), (12, 17), (5, 15), (12, 13)], 'W')
    c.poly([(22, 5), (23, 8), (26, 9), (23, 10), (22, 13), (21, 10), (18, 9), (21, 8)], 'c')
    c.outline()


@icon('dde-grand-search', ['deepin-grand-search', 'com.deepin.grand-search', 'org.deepin.dde.grand.search'],
      'deepin', 'deepin Grand Search')
def dde_grand_search(c):
    c.circle(13, 13, 10, 'B')
    c.circle(13, 13, 6.5, 'W')
    c.bevel(['B'])
    c.line(20, 20, 25, 25, '6', 3)
    c.px(10, 10, 'b'); c.px(11, 9, 'b')
    c.outline()


@icon('deepin-pc-manager', ['com.deepin.pc-manager', 'org.deepin.pc.manager', 'deepin-system-manager'], 'deepin',
      'deepin PC Manager')
def deepin_pc_manager(c):
    # rocket (speed-up)
    c.poly([(16, 2.5), (21, 9), (21, 22), (11, 22), (11, 9)], 'W')
    c.poly([(11, 15), (5, 23), (11, 23)], 'B')
    c.poly([(21, 15), (27, 23), (21, 23)], 'B')
    c.bevel(['W', 'B'])
    c.circle(16, 12, 2.5, 'B')
    c.poly([(13, 23), (19, 23), (16, 29)], 'O')
    c.outline()


@icon('deepin-installer', ['com.deepin.installer', 'org.deepin.installer', 'uos-installer', 'deepin-os-installer'],
      'deepin', 'deepin Installer')
def deepin_installer(c):
    c.rrect(3, 17, 28, 28, 'w', 2)
    c.bevel(['w'])
    c.rect(22, 22, 25, 23, 'G')
    c.rect(13, 3, 18, 10, 'B')
    c.poly([(8, 10), (23.5, 10), (16, 18)], 'B')
    c.bevel(['B'])
    c.outline()


# ================================================================ Chinese web services

@icon('toutiao', ['jinritoutiao', 'com.ss.android.article.news', 'toutiao-desktop'], 'web', 'Toutiao')
def toutiao(c):
    c.rect(4, 4, 27, 28, 'W')
    c.rect(4, 4, 27, 10, 'R')
    c.bevel(['W', 'R'])
    c.rect(7, 13, 14, 19, 'S')
    for y in (13, 16, 19):
        c.hline(16, 24, y, 'S')
    c.hline(7, 24, 22, 'S'); c.hline(7, 20, 25, 'S')
    c.text(7, 5, 'NEWS', 'W', font=3, gap=1)
    c.outline()


@icon('xigua-video', ['xigua', 'com.ss.android.article.video', 'ixigua'], 'media', 'Xigua Video')
def xigua(c):
    # watermelon slice
    c.circle(16, 8, 13, 'G')
    c.circle(16, 8, 11.5, 'g')
    c.circle(16, 8, 10.5, 'R')
    c.rect(0, 0, 31, 8, '.')
    c.hline(5, 26, 9, 'r')
    for x, y in ((10, 12), (16, 14), (22, 12), (13, 16), (19, 16)):
        c.rect(x, y, x, y + 1, 'K')
    c.outline()


@icon('bcut', ['bcut-desktop', 'bijian', 'com.bilibili.bcut'], 'media', 'Bcut')
def bcut(c):
    c.ring(9, 22, 5.5, 3, 'P'); c.ring(23, 22, 5.5, 3, 'P')
    c.bevel(['P'])
    c.line(11, 17, 21, 3, 'C', 2)
    c.line(20, 17, 10, 3, 'c', 2)
    c.rect(15, 10, 16, 11, 'W')
    c.outline()


@icon('meitu', ['meitu-xiuxiu', 'com.mt.mtxx', 'meituxiuxiu', 'meitu-desktop'], 'graphics', 'Meitu')
def meitu(c):
    disc(c, 'P', 13)
    c.rect(8, 10, 10, 22, 'W'); c.rect(21, 10, 23, 22, 'W')
    c.line(10, 10, 15, 16, 'W', 2); c.line(21, 10, 16, 16, 'W', 2)
    c.px(24, 7, 'W'); c.px(23, 7, 'p'); c.px(25, 7, 'p'); c.px(24, 6, 'p'); c.px(24, 8, 'p')
    c.outline()


@icon('acfun', ['com.acfun', 'acfun-desktop', 'acfun-live'], 'media', 'AcFun')
def acfun(c):
    c.rrect(3, 8, 28, 27, 'R', 4)
    c.line(9, 3, 13, 8, 'R', 2); c.line(23, 3, 19, 8, 'R', 2)
    c.bevel(['R'])
    c.text(8, 14, 'AC', 'W', font=5, gap=3)
    c.outline()


@icon('csdn', ['csdn-webapp', 'net.csdn', 'csdn-desktop'], 'web', 'CSDN')
def csdn(c):
    disc(c, 'R', 13)
    c.arc(16, 16, 8.5, 5, 45, 315, 'W')
    c.outline()


@icon('juejin', ['juejin-webapp', 'cn.juejin', 'xitu-juejin'], 'web', 'Juejin')
def juejin(c):
    c.poly([(16, 3), (21, 7), (16, 11), (11, 7)], 'B')
    c.poly([(16, 14), (25, 7), (29, 10), (16, 20), (3, 10), (7, 7)], 'B')
    c.poly([(16, 23), (25.5, 16), (29.5, 19), (16, 29), (2.5, 19), (6.5, 16)], 'B')
    c.bevel(['B'])
    c.outline()


@icon('gitee', ['gitee-webapp', 'com.gitee', 'gitee-desktop', 'gitee-go'], 'dev', 'Gitee')
def gitee(c):
    disc(c, 'R', 13)
    c.rrect(8, 8, 23, 23, 'W', 3)
    c.rect(11, 11, 23, 13, 'R')
    c.rect(11, 14, 13, 20, 'R')
    c.rect(14, 18, 20, 20, 'R')
    c.rect(16, 15, 20, 17, 'W')
    c.rect(18, 15, 20, 20, 'R')
    c.outline()


@icon('v2ex', ['v2ex-webapp', 'com.v2ex', 'v2ex-desktop'], 'web', 'V2EX')
def v2ex(c):
    disc(c, 'k', 13)
    c.bevel(['k'], dark=False)
    c.text(7, 12, 'V2', 'W', font=5, gap=3)
    c.outline()


@icon('hupu', ['com.hupu.games', 'hupu-desktop', 'hupu-webapp'], 'web', 'Hupu')
def hupu(c):
    # basketball
    c.circle(16, 16, 13, 'O')
    c.bevel(['O'])
    c.vline(16, 3, 28, '2'); c.hline(3, 28, 16, '2')
    c.arc(4, 16, 10, 9, 300, 60, '2')
    c.arc(28, 16, 10, 9, 120, 240, '2')
    c.outline()


@icon('dianping', ['com.dianping.v1', 'dazhong-dianping', 'dianping-desktop'], 'web', 'Dianping')
def dianping(c):
    round_bubble(c, 'O', 16, 14, 13, 11)
    c.bevel(['O'])
    c.poly([(16, 6), (18.5, 11.5), (24, 12), (20, 16), (21, 22), (16, 19), (11, 22), (12, 16), (8, 12), (13.5, 11.5)],
           'W')
    c.outline()


@icon('eleme', ['ele.me', 'me.ele', 'eleme-desktop'], 'web', 'Ele.me')
def eleme(c):
    round_bubble(c, 'B', 16, 15, 13, 11.5)
    c.bevel(['B'])
    c.ring(16, 15, 7, 4.5, 'W')
    c.rect(10, 14, 22, 15, 'W')
    c.rect(18, 16, 23, 19, 'B')
    c.outline()


@icon('ctrip', ['trip.com', 'ctrip.android.view', 'xiecheng', 'ctrip-desktop'], 'web', 'Ctrip')
def ctrip(c):
    # leaping dolphin
    c.poly([(3, 22), (8, 12), (16, 7), (24, 8), (29, 4), (27, 11), (24, 13), (20, 14), (16, 18), (12, 24), (6, 25)],
           'B')
    c.poly([(14, 8), (16, 3), (19, 7.5)], 'B')
    c.poly([(3, 22), (2.5, 28), (8, 25)], 'B')
    c.bevel(['B'])
    c.line(7, 21, 15, 13, 'b')
    c.px(22, 10, 'K')
    c.outline()


@icon('didi', ['com.sdu.didi.psnger', 'didi-chuxing', 'didi-desktop'], 'web', 'DiDi')
def didi(c):
    c.poly([(5, 3), (15, 3), (24, 7), (28, 16), (24, 25), (15, 29), (5, 29)], 'O')
    c.bevel(['O'])
    c.poly([(11, 9), (15, 9), (20, 12), (22, 16), (20, 20), (15, 23), (11, 23)], 'W')
    c.poly([(11, 13), (15, 13), (17, 16), (15, 19), (11, 19)], 'O')
    c.outline()


@icon('china-railway-12306', ['12306', 'com.MobileTicket', 'railway-12306', 'cn.12306'], 'web', 'China Railway 12306')
def railway12306(c):
    disc(c, 'B', 13)
    c.rrect(10, 7, 21, 21, 'W', 3)
    c.rect(12, 9, 19, 13, 'B')
    c.rect(11, 17, 12, 18, 'R'); c.rect(19, 17, 20, 18, 'R')
    c.line(11, 22, 8, 26, 'W'); c.line(20, 22, 23, 26, 'W')
    c.outline()


@icon('unionpay', ['yunshanfu', 'com.unionpay', 'cloudquickpass', 'union-pay'], 'web', 'UnionPay')
def unionpay(c):
    c.poly([(6, 5), (14, 5), (11, 27), (3, 27)], 'R')
    c.poly([(14, 5), (22, 5), (19, 27), (11, 27)], 'B')
    c.poly([(22, 5), (29, 5), (26, 27), (19, 27)], 'G')
    c.bevel(['R', 'B', 'G'])
    c.outline()


@icon('baidumap', ['baidu-map', 'com.baidu.BaiduMap', 'baidu-maps'], 'web', 'Baidu Maps')
def baidumap(c):
    c.circle(16, 12, 10, 'B')
    c.poly([(7, 16), (25, 16), (16, 29)], 'B')
    c.bevel(['B'])
    c.circle(16, 12, 4.5, 'W')
    c.circle(16, 12, 2, 'R')
    c.outline()


@icon('weread', ['com.tencent.weread', 'wechat-read', 'weixin-dushu', 'weread-desktop'], 'office', 'WeRead')
def weread(c):
    c.rect(6, 3, 25, 26, 'B')
    c.bevel(['B'])
    c.rect(6, 25, 25, 28, 'W')
    c.hline(7, 25, 27, 'w')
    c.rect(18, 3, 21, 12, 'W')
    c.px(19, 12, 'B'); c.px(20, 12, 'B') if False else c.px(19, 12, 'B')
    c.ellipse(13, 16, 4, 3.5, 'W') if False else None
    c.outline()


@icon('yangshipin', ['cctv', 'cctv-video', 'com.cctv.yangshipin', 'cntv'], 'media', 'CCTV Video')
def yangshipin(c):
    c.rrect(3, 5, 28, 23, 'R', 3)
    c.bevel(['R'])
    c.rect(11, 24, 20, 26, '1')
    c.rrect(7, 27, 24, 28, '1', 1)
    c.text(7, 12, 'CCTV', 'W', font=3, gap=1)
    c.outline()


@icon('dewu', ['poizon', 'com.shizhuang.duapp', 'dewu-desktop'], 'web', 'Dewu')
def dewu(c):
    # a sneaker
    c.poly([(3, 12), (11, 10), (16, 15), (24, 17), (28.5, 21), (28.5, 24), (3, 24)], 'k')
    c.bevel(['k'], dark=False)
    c.rect(3, 23, 28, 26, 'W')
    c.hline(3, 28, 26, 'w')
    c.line(9, 13, 14, 18, 'W') if False else None
    for x in (10, 12, 14):
        c.px(x, 15, 'W')
    c.line(18, 21, 27, 21, 'C')
    c.outline()


@icon('keep', ['com.gotokeep.keep', 'keep-fitness', 'keep-desktop'], 'utilities', 'Keep')
def keep(c):
    hexagon(c, '7', 16, 16, 13.5)
    c.rect(9, 8, 11, 23, 'W')
    c.line(12, 16, 20, 8, 'W', 3)
    c.line(13, 15, 21, 22, 'W', 3)
    c.outline()


@icon('mijia', ['mihome', 'xiaomi-home', 'com.xiaomi.smarthome', 'mi-home'], 'utilities', 'Mi Home')
def mijia(c):
    c.poly([(16, 2.5), (29.5, 14), (3, 14)], 'O')
    c.rect(6, 13, 25, 28, 'W')
    c.bevel(['W', 'O'])
    c.rect(13, 19, 18, 28, 'O')
    c.px(17, 23, '2')
    c.outline()


@icon('lanzou-cloud', ['lanzouyun', 'lanzou', 'lanzou-cloud-bin', 'com.lanzou.cloud'], 'web', 'Lanzou Cloud')
def lanzou(c):
    cloud(c, 'b', 1)
    c.bevel(['b'])
    c.rect(15, 15, 16, 23, 'W')
    c.poly([(11, 16), (20.5, 16), (16, 11)], 'W')
    c.outline()


@icon('tianyi-cloud', ['cloud189', 'ecloud', 'tianyiyunpan', 'com.cn21.ecloud'], 'web', 'Tianyi Cloud')
def tianyi(c):
    cloud(c, 'C', 1)
    c.bevel(['C'])
    c.text(10, 16, '189', 'W', font=3, gap=1)
    c.outline()


@icon('caiyun', ['mcloud', 'hecaiyun', 'com.chinamobile.mcloud', 'china-mobile-cloud'], 'web', 'China Mobile Cloud')
def caiyun(c):
    cloud(c, 'W', 0)
    c.bevel(['W'])
    for i, col in enumerate(('R', 'Y', 'G', 'B')):
        c.hline(8, 23, 18 + i, col) if False else None
    c.rect(8, 17, 23, 18, 'R')
    c.rect(8, 19, 23, 20, 'Y')
    c.rect(8, 21, 23, 22, 'B')
    c.outline()
