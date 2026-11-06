from pix import icon
"""Chinese & Asian software II: music, video, social, shopping."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cn_lib import g, gc, disc, bubble, round_bubble, tile, play, note  # noqa: E402


ZHI = """
.#.....######
.####..#....#
#.#....#....#
..#....#....#
######.#....#
..#....#....#
.#.#...#....#
.#..#..######
#....#.......
"""
ZHI_ = """
.....#.....
.....#.....
###########
.....#.....
.#########.
..#.....#..
...#...#...
....#.#....
...##.##...
###.....###
"""
DOU = """
###########
...........
.#########.
.#.......#.
.#########.
...........
..#.....#..
...#...#...
###########
"""
MEI = """
..#.....#..
...#...#...
###########
.....#.....
.#########.
.....#.....
###########
.....#.....
...##.##...
.##.....##.
#.........#
"""
TAO = """
#...#........
.#..########.
...#.......#.
#.#..#.#.#.#.
.#...#####.#.
.....#.#.#.#.
.#...#####.#.
.#...#.#.#.#.
#....#####.#.
#..........#.
#........###.
"""


# ================================================================ music

@icon('netease-cloud-music', ['com.netease.CloudMusic', 'netease-cloud-music-bin', 'neteasecloudmusic',
                              'netease-cloud-music-gtk', 'com.gitee.gmg137.NeteaseCloudMusicGtk4',
                              'netease-cloud-music-gtk4', 'ncm', 'netease-music', 'cloudmusic',
                              'netease-cloud-music-appimage'], 'media', 'NetEase Cloud Music')
def netease_cloud_music(c):
    disc(c, 'R', 13)
    # the NetEase note swirl: open ring with a rising stem
    c.arc(15.5, 18, 6.5, 4, 120, 20, 'W')
    c.rect(17, 8, 18, 17, 'W')
    c.line(18, 8, 22, 9, 'W', 2)
    c.px(9, 15, 'W'); c.px(9, 16, 'W')
    c.outline()


@icon('yesplaymusic', ['yesplaymusic-bin', 'com.github.qier222.YesPlayMusic', 'YesPlayMusic', 'r3play',
                       'yesplaymusic-appimage', 'yesplaymusicosd'], 'media', 'YesPlayMusic')
def yesplaymusic(c):
    disc(c, 'k', 13)
    for r in (11, 8.5):
        c.ring(16, 16, r, r - .8, 's')
    c.circle(16, 16, 5.5, 'R')
    c.circle(16, 16, 1.5, 'K')
    c.arc(16, 16, 12, 10, 200, 250, 'S')
    c.outline()


@icon('qqmusic', ['qqmusic-bin', 'com.qq.QQMusic', 'tencent-qqmusic', 'com.tencent.qqmusic', 'qq-music',
                  'QQMusic', 'qqmusic-appimage'], 'media', 'QQ Music')
def qqmusic(c):
    disc(c, 'Y', 13)
    c.circle(16, 16, 10, 'G')
    c.bevel(['G'], dark=False)
    note(c, 11, 9, 'W', 13)
    c.outline()


@icon('kugou', ['kugoumusic', 'com.kugou.music', 'kugou-music', 'kugou-bin', 'com.kugou.kugoumusic'], 'media',
      'Kugou')
def kugou(c):
    disc(c, 'B', 13)
    c.ring(16, 16, 10, 8.5, 'W')
    c.rect(11, 9, 13, 23, 'W')
    c.line(14, 16, 20, 9, 'W', 2)
    c.line(14, 15, 21, 22, 'W', 2)
    c.outline()


@icon('kuwo', ['kuwomusic', 'kwmusic', 'com.kuwo.music', 'kuwo-music', 'kuwo-bin'], 'media', 'Kuwo Music')
def kuwo(c):
    disc(c, 'O', 13)
    c.arc(16, 17, 8, 6, 180, 360, 'W')
    c.rect(8, 17, 9, 19, 'W'); c.rect(23, 17, 24, 19, 'W')
    c.rrect(7, 17, 11, 23, 'W', 1); c.rrect(21, 17, 25, 23, 'W', 1)
    c.outline()


@icon('ximalaya', ['com.ximalaya', 'ximalaya-desktop', 'ximalaya-bin', 'xmly'], 'media', 'Ximalaya')
def ximalaya(c):
    disc(c, 'R', 13)
    for x, h in ((8, 4), (11, 8), (14, 12), (17, 8), (20, 12), (23, 5)):
        c.rect(x, 16 - h // 2, x + 1, 16 + h // 2, 'W')
    c.outline()


@icon('lx-music-desktop', ['lx-music', 'cn.toside.music.desktop', 'lx-music-desktop-bin', 'lxmusic',
                           'lx-music-appimage'], 'media', 'LX Music')
def lx_music(c):
    disc(c, 'G', 13)
    c.text(7, 12, 'LX', 'W', font=5, gap=3)
    c.outline()


@icon('musicfree', ['MusicFree', 'musicfree-desktop', 'musicfree-bin', 'fun.upup.musicfree'], 'media',
      'MusicFree')
def musicfree(c):
    # a cassette tape
    c.rrect(3, 6, 28, 26, 'O', 2)
    c.bevel(['O'])
    c.rect(6, 9, 25, 18, 'W')
    c.circle(11, 13.5, 2.5, 'k'); c.circle(21, 13.5, 2.5, 'k')
    c.rect(13, 12, 18, 15, 's')
    c.poly([(8, 26), (10, 21), (22, 21), (24, 26)], '2')
    c.outline()


@icon('listen1', ['listen1-desktop', 'com.listen1.Listen1', 'listen1-bin', 'listen1-appimage', 'Listen1'], 'media',
      'Listen 1')
def listen1(c):
    # headphones with a "1"
    c.arc(16, 17, 12.5, 10, 180, 360, 'B')
    c.rrect(4, 17, 9, 28, 'B', 2); c.rrect(22, 17, 27, 28, 'B', 2)
    c.bevel(['B'])
    c.rect(6, 19, 7, 26, '6'); c.rect(24, 19, 25, 26, '6')
    g(c, 14, 16, """
        .##
        ###
        .##
        .##
        .##
        .##
        ###
    """, 'b')
    c.outline()


@icon('splayer', ['SPlayer', 'splayer-bin', 'splayer-appimage', 'com.imsyy.splayer'], 'media', 'SPlayer')
def splayer(c):
    disc(c, 'P', 13)
    c.circle(16, 16, 8, 'W')
    play(c, 14, 11, 11, 'P')
    c.outline()


@icon('feeluown', ['FeelUOwn', 'feeluown-git', 'io.github.feeluown'], 'media', 'FeelUOwn')
def feeluown(c):
    round_bubble(c, 'N', 16, 14, 12.5, 11, 'left')
    c.bevel(['N'])
    note(c, 11, 7, 'W', 13)
    c.outline()


# ================================================================ video & social

@icon('bilibili', ['io.github.msojocs.bilibili', 'bilibili-bin', 'bilibili-desktop', 'com.bilibili.app', 'bili',
                   'bilibili-electron', 'tv.danmaku.bili', 'Bilibili'], 'media', 'Bilibili')
def bilibili(c):
    # the little TV with antennae and >< eyes
    c.line(9, 3, 13, 8, 'C', 2)
    c.line(23, 3, 19, 8, 'C', 2)
    c.rrect(3, 8, 28, 27, 'C', 4)
    c.bevel(['C'])
    c.rrect(6, 11, 25, 24, 'W', 3)
    g(c, 9, 15, """
        ##.......##
        ..##...##..
        ##.......##
    """, '5')
    g(c, 12, 20, "#.#.#.#", '5')
    c.outline()


@icon('kuaishou', ['com.smile.gifmaker', 'kwai', 'kuaishou-desktop', 'kuaishou-bin'], 'media', 'Kuaishou')
def kuaishou(c):
    # the camcorder made of two reels and a body
    c.circle(10, 9, 5.5, 'O'); c.circle(20, 9, 5, 'O')
    c.rrect(4, 14, 22, 27, 'O', 2)
    c.poly([(22, 18), (29, 14), (29, 27), (22, 23)], 'O')
    c.bevel(['O'])
    c.circle(10, 9, 2.5, 'W'); c.circle(20, 9, 2, 'W')
    play(c, 11, 17, 7, 'W')
    c.outline()


@icon('xiaohongshu', ['rednote', 'xhs', 'com.xingin.xhs', 'xiaohongshu-desktop', 'xiaohongshu-bin'], 'media',
      'Xiaohongshu')
def xiaohongshu(c):
    tile(c, 'R', 6)
    c.text(7, 12, 'RED', 'W', font=5, gap=1) if False else c.text(6, 13, 'RED', 'W', font=5, gap=1)
    c.outline()


@icon('weibo', ['com.sina.weibo', 'sina-weibo', 'weibo-desktop', 'weibo-bin', 'Weibo'], 'media', 'Weibo')
def weibo(c):
    # the Weibo eye with its orange antenna arcs
    c.ellipse(14, 20, 11.5, 8, 'R')
    c.bevel(['R'])
    c.ellipse(13, 21, 7, 5, 'W')
    c.ellipse(12, 22, 3, 2.5, 'K')
    c.px(13, 21, 'W')
    c.arc(21, 10, 8, 6, 270, 360, 'O')
    c.arc(21, 10, 4, 2.2, 270, 360, 'O')
    c.outline()


@icon('zhihu', ['com.zhihu', 'zhihu-desktop', 'zhihu-bin', 'Zhihu'], 'media', 'Zhihu')
def zhihu(c):
    tile(c, 'B', 6)
    g(c, 9, 11, ZHI, 'W')
    c.outline()


@icon('douban', ['com.douban', 'douban-desktop', 'douban-fm', 'Douban'], 'media', 'Douban')
def douban(c):
    tile(c, 'G', 6)
    g(c, 10, 11, DOU, 'W')
    c.outline()


def _paw(c, col, cx=16, cy=16):
    c.ellipse(cx, cy + 6, 8, 6.5, col)
    c.ellipse(cx - 10, cy - 1, 3.5, 4.5, col)
    c.ellipse(cx + 10, cy - 1, 3.5, 4.5, col)
    c.ellipse(cx - 4.5, cy - 8, 3.5, 4.5, col)
    c.ellipse(cx + 4.5, cy - 8, 3.5, 4.5, col)


@icon('baidu', ['baidu-webapp', 'com.baidu.search', 'baidu-search', 'Baidu'], 'web', 'Baidu')
def baidu(c):
    _paw(c, 'B', 16, 15)
    c.bevel(['B'])
    c.ellipse(16, 22, 4, 3, 'W')
    c.outline()


@icon('tieba', ['baidu-tieba', 'com.baidu.tieba', 'tieba-desktop'], 'media', 'Baidu Tieba')
def tieba(c):
    bubble(c, 'B', 3, 3, 28, 23)
    c.bevel(['B'])
    for x, y in ((10, 10), (14, 8), (18, 8), (22, 10)):
        c.rect(x - 1, y - 1, x, y, 'W')
    c.ellipse(16, 16.5, 4.5, 3.5, 'W')
    c.outline()


# ================================================================ shopping & life

@icon('taobao-desktop', ['taobao', 'com.taobao.taobao', 'taobao-bin', 'Taobao', 'com.taobao.TaobaoDesktop'], 'web', 'Taobao')
def taobao(c):
    tile(c, 'O', 6)
    g(c, 9, 10, TAO, 'W')
    c.outline()


@icon('alipay', ['com.eg.android.AlipayGphone', 'alipay-desktop', 'zhifubao', 'Alipay'], 'web', 'Alipay')
def alipay(c):
    tile(c, 'B', 6)
    g(c, 10, 10, ZHI_, 'W')
    c.outline()


@icon('jd', ['jingdong', 'com.jd.app', 'jd-desktop', 'com.jingdong.app.mall', 'JD'], 'web', 'JD.com')
def jd(c):
    # Joy the JD dog: white head, red ears
    c.poly([(4, 4), (11, 8), (6, 15)], 'R')
    c.poly([(28, 4), (21, 8), (26, 15)], 'R')
    c.ellipse(16, 17, 11, 10.5, 'W')
    c.bevel(['W', 'R'])
    c.rect(10, 14, 11, 16, 'K'); c.rect(20, 14, 21, 16, 'K')
    c.ellipse(16, 21, 3, 2, 'K')
    c.hline(14, 17, 25, 'R')
    c.outline()


@icon('meituan', ['com.sankuai.meituan', 'meituan-desktop', 'Meituan'], 'web', 'Meituan')
def meituan(c):
    tile(c, 'Y', 6)
    g(c, 10, 10, MEI, 'k')
    c.outline()


@icon('pinduoduo', ['pdd', 'com.xunmeng.pinduoduo', 'pinduoduo-desktop', 'Pinduoduo'], 'web', 'Pinduoduo')
def pinduoduo(c):
    # red shopping bag with a white heart
    c.ring(16, 10, 6.5, 3.5, '1')
    c.rect(4, 10, 27, 28, 'R')
    c.rect(9, 7, 11, 12, 'R') if False else None
    c.bevel(['R'])
    g(c, 10, 14, """
        .##..##.
        ########
        ########
        .######.
        ..####..
        ...##...
    """, 'W', ) if False else gc(c, """
        .###.###.
        #########
        #########
        .#######.
        ..#####..
        ...###...
        ....#....
    """, 'W', 16, 19)
    c.outline()


@icon('xianyu', ['goofish', 'com.taobao.idlefish', 'xianyu-desktop', 'Xianyu'], 'web', 'Xianyu')
def xianyu(c):
    # a salted fish (咸鱼)
    c.ellipse(14, 16, 11, 7.5, 'Y')
    c.poly([(23, 16), (29.5, 9), (28, 16), (29.5, 23)], 'Y')
    c.bevel(['Y'])
    c.rect(8, 14, 9, 15, 'K')
    c.arc(14, 16, 5, 3.8, 300, 60, '3')
    c.poly([(12, 9), (17, 6), (18, 9)], '3')
    c.outline()


@icon('amap', ['autonavi', 'com.autonavi.minimap', 'gaode', 'amap-desktop', 'Amap'], 'web', 'Amap')
def amap(c):
    # navigation arrow, half shaded
    c.poly([(16, 2.5), (28, 29), (16, 22), (4, 29)], 'B')
    c.bevel(['B'])
    c.poly([(16, 6), (16, 22), (25.5, 27)], 'c')
    c.outline()


# ================================================================ streaming video

@icon('iqiyi', ['com.qiyi.video', 'iqiyi-desktop', 'aiqiyi', 'iqiyi-bin', 'iQIYI', 'iq.com'], 'media', 'iQIYI')
def iqiyi(c):
    c.rrect(3, 6, 28, 24, 'G', 3)
    c.bevel(['G'])
    c.rect(11, 25, 20, 27, '4')
    c.text(8, 12, 'IQ', 'W', font=5, gap=3)
    c.px(15, 18, '4')
    c.outline()


@icon('youku', ['com.youku', 'youku-desktop', 'youku-bin', 'com.youku.phone', 'Youku'], 'media', 'Youku')
def youku(c):
    c.circle(13, 16, 10.5, 'b')
    c.arc(13, 16, 10.5, 7.5, 90, 270, 'M')
    c.poly([(11, 4), (28.5, 16), (11, 28)], 'B')
    c.bevel(['B', 'b', 'M'])
    c.poly([(14, 11), (21, 16), (14, 21)], 'W')
    c.outline()


@icon('tencent-video', ['txvideo', 'com.tencent.qqlive', 'qqlive', 'tenvideo', 'tencent-video-bin', 'v.qq.com',
                        'TencentVideo'], 'media', 'Tencent Video')
def tencent_video(c):
    c.poly([(4, 3), (28, 16), (4, 29)], 'B')
    c.poly([(9, 7), (26, 16), (9, 25)], 'G')
    c.poly([(9, 10), (22, 16), (9, 22)], 'O')
    c.bevel(['B'])
    c.poly([(12, 13), (17, 16), (12, 19)], 'W')
    c.outline()


@icon('mangotv', ['mgtv', 'mango-tv', 'com.hunantv.imgo.activity', 'mangotv-desktop', 'MangoTV'], 'media',
      'Mango TV')
def mangotv(c):
    # an orange mango with a play mark
    c.ellipse(15, 17, 11, 11.5, 'O')
    c.ellipse(19, 15, 9, 10, 'O')
    c.bevel(['O'])
    c.poly([(16, 6), (22, 3), (25, 6), (19, 8)], 'G')
    c.px(22, 4, 'g')
    play(c, 12, 12, 11, 'W')
    c.outline()


@icon('huya', ['com.duowan.kiwi', 'huya-desktop', 'huya-bin', 'Huya'], 'media', 'Huya')
def huya(c):
    # tiger head
    c.circle(7, 7, 4, 'O'); c.circle(25, 7, 4, 'O')
    c.ellipse(16, 17, 13, 11, 'O')
    c.bevel(['O'])
    c.circle(7, 7, 2, 'W'); c.circle(25, 7, 2, 'W')
    for x in (12, 15, 18):
        c.vline(x + 1, 7, 10, 'K')
    c.ellipse(16, 22, 6.5, 4.5, 'W')
    c.rect(9, 15, 10, 16, 'K'); c.rect(21, 15, 22, 16, 'K')
    c.rect(15, 19, 16, 20, 'K')
    c.rect(4, 16, 6, 16, 'K'); c.rect(25, 16, 27, 16, 'K')
    c.outline()


@icon('douyu', ['com.douyu', 'douyu-desktop', 'douyu-bin', 'Douyu'], 'media', 'Douyu')
def douyu(c):
    # the orange Douyu shark-fish, mouth open
    c.ellipse(15, 17, 12, 10, 'O')
    c.poly([(9, 7), (14, 2.5), (17, 8)], 'O')
    c.bevel(['O'])
    c.poly([(16, 20), (28.5, 15), (28.5, 25)], '.')
    c.rect(9, 13, 11, 15, 'W'); c.px(10, 14, 'K')
    c.ellipse(13, 23, 6, 3, 'y')
    c.outline()


@icon('jianying', ['jianyingpro', 'com.lemon.lvpro', 'jianying-pro', 'Jianying'], 'media', 'Jianying')
def jianying(c):
    # clapperboard
    c.rect(4, 13, 27, 27, 'k')
    c.bevel(['k'], dark=False)
    c.poly([(3, 9), (26, 3), (27.5, 8), (4.5, 14)], 'W')
    for i in range(3):
        x = 8 + i * 7
        c.poly([(x, 7.5 - i * 1.8), (x + 3, 6.7 - i * 1.8), (x + 5, 12 - i * 1.8), (x + 2, 12.8 - i * 1.8)], 'k')
    c.hline(7, 24, 18, 'W'); c.hline(7, 18, 22, 'S')
    c.outline()
