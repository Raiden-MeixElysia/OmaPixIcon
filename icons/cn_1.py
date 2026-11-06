from pix import icon
"""Chinese & Asian software I: messaging, office, cloud drives."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cn_lib import g, gc, disc, bubble, round_bubble, doc, cloud, tile, shield, play  # noqa: E402


# ================================================================ Tencent messaging

def _wechat_pair(c, big, small, eye_big='K', eye_small='K'):
    c.ellipse(12.5, 13, 9.5, 8.5, big)
    c.poly([(6, 18), (11, 20), (5, 24)], big)
    c.bevel([big])
    c.ellipse(21, 19.5, 7.5, 7, 'K')
    c.ellipse(21, 19.5, 6.5, 6, small)
    c.poly([(23, 24), (27, 23), (27.5, 28)], small)
    c.px(26, 24, small)
    c.bevel([small], light=False)
    for x in (8, 15):
        c.rect(x, 10, x + 1, 11, eye_big)
    for x in (18, 23):
        c.px(x, 17, eye_small)


@icon('wecom', ['wxwork', 'wework', 'com.qq.weixin.work.deepin', 'deepin-wine-wxwork', 'com.tencent.wework',
                'com.tencent.WeCom', 'wecom-bin', 'wechat-work', 'qiyeweixin', 'wxwork-bin'], 'chat', 'WeCom')
def wecom(c):
    _wechat_pair(c, 'B', 'W', 'W', 'B')
    # the four-colour pinwheel of WeCom
    c.rect(20, 18, 21, 19, 'Y'); c.rect(22, 18, 23, 19, 'R')
    c.rect(20, 20, 21, 21, 'G'); c.rect(22, 20, 23, 21, 'b')
    c.px(18, 17, 'w'); c.px(23, 17, 'w')
    c.outline()


def _penguin(c, body, belly, beak, scarf=None, shade=None):
    shade = shade or 'k'
    c.ellipse(16, 10.5, 8, 7, body)          # head
    c.ellipse(16, 19, 10, 9, body)           # body
    c.poly([(6.5, 17), (3, 23), (7, 22)], body)   # flippers
    c.poly([(25.5, 17), (29, 23), (25, 22)], body)
    c.bevel([body])
    c.ellipse(16, 20.5, 7, 7, belly)
    c.ellipse(13, 9.5, 2, 2.5, 'W'); c.ellipse(19, 9.5, 2, 2.5, 'W')
    c.px(13, 10, 'K'); c.px(18, 10, 'K')
    c.rect(13, 13, 18, 14, beak); c.hline(14, 17, 15, beak)
    c.hline(13, 18, 14, '2' if beak == 'O' else '3')
    if scarf:
        c.rect(8, 16, 23, 17, scarf)
        c.rect(19, 18, 21, 21, scarf)
        c.hline(8, 23, 17, '1')
    c.ellipse(11, 27.5, 4, 1.5, beak); c.ellipse(21, 27.5, 4, 1.5, beak)
    c.bevel([belly], light=False)


@icon('tim', ['com.qq.office.deepin', 'deepin-wine-tim', 'com.qq.tim', 'tencent-tim', 'TIM', 'com.tencent.tim'],
      'chat', 'TIM')
def tim(c):
    _penguin(c, 'B', 'W', 'C')
    c.replace('3', '5')
    c.outline()


# ================================================================ WPS family

def _wps_doc(c, col, glyph):
    doc(c, col, 'w')
    gc(c, glyph, 'W', 16, 17)


@icon('wps-office2019-wpsmain-writer', ['wps-office-wpsmain', 'wps-writer', 'wps-office2023-wpsmain',
                                        'wps-office-writer', 'com.wps.Office.writer'], 'office', 'WPS Writer')
def wps_writer(c):
    _wps_doc(c, 'B', """
        #...#...#
        #...#...#
        #..#.#..#
        #..#.#..#
        .#.#.#.#.
        .##...##.
        .#.....#.
    """)
    c.hline(9, 22, 25, 'b')
    c.outline()


@icon('wps-office2019-etmain', ['wps-office-etmain', 'wps-office-et', 'wps-et', 'wps-office2023-etmain',
                                'wps-spreadsheets', 'com.wps.Office.et'], 'office', 'WPS Spreadsheets')
def wps_et(c):
    _wps_doc(c, 'G', """
        .#####.
        #.....#
        #......
        .#####.
        ......#
        #.....#
        .#####.
    """)
    c.hline(9, 22, 25, 'g')
    c.outline()


@icon('wps-office2019-wppmain', ['wps-office-wppmain', 'wps-office-wpp', 'wps-wpp', 'wps-office2023-wppmain',
                                 'wps-presentation', 'com.wps.Office.wpp'], 'office', 'WPS Presentation')
def wps_wpp(c):
    _wps_doc(c, 'O', """
        ######.
        #.....#
        #.....#
        ######.
        #......
        #......
        #......
    """)
    c.hline(9, 22, 25, 'o')
    c.outline()


@icon('wps-office2019-pdfmain', ['wps-office-pdfmain', 'wps-office-pdf', 'wps-pdf', 'wps-office2023-pdfmain',
                                 'com.wps.Office.pdf'], 'office', 'WPS PDF')
def wps_pdf(c):
    doc(c, 'R', 'w')
    c.text(8, 14, 'PDF', 'W', font=3)
    c.hline(9, 22, 21, 'r')
    c.hline(9, 18, 24, 'r')
    c.outline()


# ================================================================ dictionaries & notes

@icon('youdao-dict', ['youdaodict', 'com.youdao.dict', 'youdao-dictionary', 'netease-youdao-dict', 'YoudaoDict',
                      'youdaodict-bin', 'com.youdao.YoudaoDict'], 'office', 'Youdao Dictionary')
def youdao_dict(c):
    # red open book with the Youdao "Y"
    c.poly([(3, 6), (15, 8), (15, 27), (3, 25)], 'R')
    c.poly([(17, 8), (29, 6), (29, 25), (17, 27)], 'R')
    c.rect(15, 8, 16, 27, '1')
    c.bevel(['R'])
    g(c, 6, 12, """
        #...#
        .#.#.
        ..#..
        ..#..
        ..#..
    """, 'W')
    c.hline(19, 26, 13, 'r'); c.hline(19, 26, 16, 'r'); c.hline(19, 24, 19, 'r')
    c.outline()


@icon('youdao-note', ['youdaonote', 'ynote', 'com.youdao.note', 'youdao-note-electron', 'youdaonote-bin',
                      'YoudaoNote', 'youdao-note-bin'], 'office', 'Youdao Note')
def youdao_note(c):
    # spiral notepad in Youdao blue with a pen stroke
    c.rect(5, 5, 25, 28, 'B')
    c.bevel(['B'])
    c.rect(8, 8, 22, 25, 'W')
    c.shade_below(['W'], 'w')
    for x in (8, 12, 16, 20):
        c.rect(x, 3, x + 1, 6, 'S')
    c.hline(10, 20, 13, 'b'); c.hline(10, 20, 17, 'b'); c.hline(10, 16, 21, 'b')
    c.line(27, 12, 20, 23, 'R', 2)
    c.px(20, 24, 'K')
    c.outline()


# ================================================================ cloud drives & downloaders

@icon('baidunetdisk', ['baidunetdisk-bin', 'com.baidu.NetDisk', 'baidu-netdisk', 'baidunetdisk-electron',
                       'baidupan', 'com.baidu.netdisk', 'baidunetdisk-uos', 'BaiduNetdisk'], 'web', 'Baidu Netdisk')
def baidunetdisk(c):
    cloud(c, 'B', 1)
    c.bevel(['B'])
    # the two-tone ribbon "S" loop
    c.ring(12.5, 19.5, 4.5, 2, 'W')
    c.ring(20.5, 19.5, 4.5, 2, 'c')
    c.rect(12, 17, 13, 17, 'W')
    c.outline()


@icon('aliyundrive', ['alipan', 'com.alibaba.aliyundrive', 'aliyunpan', 'aliyundrive-desktop', 'alipan-desktop',
                      'aliyundrive-bin', 'adrive', 'alipan-bin', 'com.alicloud.alipan'], 'web', 'Alipan')
def aliyundrive(c):
    # purple-to-orange disc with the white circular arrow
    c.circle(16, 16, 13, 'M')
    for y in range(32):
        for x in range(32):
            if c.get(x, y) == 'M' and (31 - x) + y > 38:
                c.px(x, y, 'O')
    c.bevel(['M', 'O'])
    c.arc(16, 16, 8, 4.5, 330, 250, 'W')
    c.poly([(16, 5), (22, 9.5), (16, 14)], 'W')
    c.outline()


@icon('quark', ['quark-cloud-drive', 'quark-netdisk', 'quarkpan', 'com.quark.browser', 'quark-browser',
                'com.quark.cloud', 'quark-bin', 'Quark'], 'web', 'Quark')
def quark(c):
    # the Quark "Q" bubble: indigo ring with the tail swirl
    c.circle(15, 15, 12, '6')
    c.circle(15, 15, 11, 'B')
    c.poly([(19, 21), (25, 19), (29, 28), (22, 28)], 'B')
    c.bevel(['B'])
    c.circle(14, 14, 5.5, 'W')
    c.circle(15, 15, 3, 'B')
    c.poly([(16, 16), (20, 16), (24, 24), (20, 24)], 'W')
    c.outline()


@icon('115pc', ['115', '115-browser', '115br', 'com.115.pc', '115-desktop', 'com.115.browser'], 'web', '115')
def p115(c):
    disc(c, 'B', 13)
    c.text(5, 11, '115', 'W', font=5, gap=1)
    c.outline()


@icon('xunlei', ['com.xunlei.download', 'xunlei-bin', 'thunder-xunlei', 'deepin-wine-thunderspeed',
                 'com.xunlei.thunder', 'thunder-speed', 'xunlei-download', 'Thunder', 'com.xunlei.Thunder'],
      'web', 'Xunlei Thunder')
def xunlei(c):
    # the blue Thunder bird / bolt
    c.poly([(10, 3), (26, 3), (21, 11), (27, 11), (11, 29), (14, 17), (6, 17)], 'B')
    c.bevel(['B'])
    c.poly([(12, 5), (19, 5), (16, 10), (13, 10)], 'b')
    c.outline()


# ================================================================ office extras

def _envelope(c, col, flap='W', x0=3, y0=7, x1=28, y1=25):
    c.rect(x0, y0, x1, y1, col)
    c.bevel([col])
    c.line(x0 + 1, y0 + 1, (x0 + x1) // 2, y0 + 10, flap)
    c.line(x1 - 1, y0 + 1, (x0 + x1 + 1) // 2, y0 + 10, flap)


@icon('tencent-docs', ['com.tencent.docs', 'txdocs', 'tencent-docs-bin', 'docs.qq.com'], 'office', 'Tencent Docs')
def tencent_docs(c):
    doc(c, 'B', 'b')
    c.rect(10, 12, 21, 13, 'W')
    c.rect(10, 17, 21, 18, 'W')
    c.rect(10, 22, 17, 23, 'W')
    c.outline()


@icon('qqmail', ['com.tencent.qqmail', 'qq-mail', 'qqmail-bin', 'com.qq.mail'], 'office', 'QQ Mail')
def qqmail(c):
    _envelope(c, 'B')
    c.rect(22, 18, 27, 23, 'Y')
    c.rect(23, 19, 26, 22, 'R')
    c.outline()


@icon('foxmail', ['com.tencent.foxmail', 'foxmail-bin', 'deepin-wine-foxmail', 'com.foxmail.deepin',
                  'Foxmail'], 'office', 'Foxmail')
def foxmail(c):
    # envelope with fox ears
    c.poly([(4, 10), (6, 3), (12, 9)], 'O')
    c.poly([(20, 9), (26, 3), (28, 10)], 'O')
    _envelope(c, 'O', 'W', 3, 9, 28, 27)
    c.px(6, 6, '2'); c.px(25, 6, '2')
    c.outline()


@icon('netease-mailmaster', ['mailmaster', 'com.netease.mailmaster', 'mail163', 'netease-mail',
                             'mailmaster-bin'], 'office', 'NetEase MailMaster')
def mailmaster(c):
    _envelope(c, 'R', 'W', 3, 7, 28, 25)
    c.rect(4, 22, 27, 24, '1')
    c.outline()


@icon('yuque', ['com.yuque.app', 'yuque-desktop', 'yuque-bin', 'Yuque'], 'office', 'Yuque')
def yuque(c):
    # Yuque's green bird
    c.ellipse(15, 18, 11.5, 9, 'G')
    c.ellipse(20, 10, 6.5, 6.5, 'G')
    c.poly([(25, 8), (29.5, 10), (25, 12)], 'Y')
    c.poly([(3.5, 14), (3, 26), (10, 23)], 'G')
    c.bevel(['G'])
    c.poly([(8, 15), (19, 18), (12, 23)], '4')
    c.rect(21, 8, 22, 9, 'K')
    c.outline()


@icon('yinxiangbiji', ['yinxiang', 'com.yinxiang.biji', 'evernote-china', 'yinxiang-bin'], 'office',
      'Yinxiang Biji')
def yinxiang(c):
    # green elephant head
    c.ellipse(17, 13, 10, 9.5, 'G')
    c.ellipse(8, 14, 5, 7, 'G')
    c.rect(15, 18, 21, 27, 'G')
    c.ellipse(18, 27, 3.5, 2, 'G')
    c.bevel(['G'])
    c.ellipse(8, 14, 3, 5, '4')
    c.rect(19, 10, 20, 11, 'K')
    c.poly([(22, 17), (27, 19), (22, 21)], 'W')
    c.outline()


@icon('nutstore', ['jianguoyun', 'com.nutstore', 'nutstore-bin', 'nutstore-experimental', 'Nutstore'], 'web',
      'Nutstore')
def nutstore(c):
    # an acorn
    c.ellipse(16, 18.5, 9, 10, 'B')
    c.bevel(['B'])
    c.rrect(4, 7, 27, 13, 'N', 3)
    c.bevel(['N'])
    c.rect(15, 3, 16, 6, '8')
    c.dither(6, 9, 25, 11, '8', 'N', only='N')
    c.px(11, 17, 'b'); c.px(11, 18, 'b'); c.px(12, 16, 'W')
    c.outline()


# ================================================================ input methods

def _keycap(c, col='w', top='W'):
    c.rrect(3, 5, 28, 28, col, 3)
    c.rrect(5, 5, 26, 24, top, 3)
    c.bevel([top], dark=False)


@icon('sogoupinyin', ['sogou-pinyin', 'fcitx-sogoupinyin', 'sogouimebs', 'com.sogou.ime', 'sogoupinyin-bin',
                      'sogou', 'fcitx5-sogou', 'fcitx-sogouimebs'], 'system', 'Sogou Pinyin')
def sogou(c):
    disc(c, 'O', 13)
    c.text(11, 9, 'S', 'W', font=5, scale=2, gap=0)
    c.outline()


@icon('fcitx-baidupinyin', ['baidu-pinyin', 'com.baidu.fcitx-baidupinyin', 'baidupinyin', 'fcitx5-baidupinyin',
                            'baidu-input'], 'system', 'Baidu Pinyin')
def baidupinyin(c):
    _keycap(c)
    _paw(c, 'B', 16, 15)
    c.outline()


def _paw(c, col, cx=16, cy=16, s=1):
    c.ellipse(cx, cy + 4, 6 * s, 4.5 * s, col)
    c.ellipse(cx - 7 * s, cy - 1, 2.5 * s, 3 * s, col)
    c.ellipse(cx + 7 * s, cy - 1, 2.5 * s, 3 * s, col)
    c.ellipse(cx - 3 * s, cy - 6 * s, 2.5 * s, 3 * s, col)
    c.ellipse(cx + 3 * s, cy - 6 * s, 2.5 * s, 3 * s, col)


@icon('iflyime', ['com.iflytek.iflyime', 'iflytek-ime', 'xunfei-input', 'iflyime-bin', 'fcitx-iflyime'],
      'system', 'iFlytek Input')
def iflyime(c):
    disc(c, 'B', 13)
    c.rrect(13, 7, 18, 18, 'W', 2)
    c.arc(15.5, 15, 7, 5.5, 0, 180, 'W')
    c.rect(15, 21, 16, 24, 'W')
    c.hline(12, 19, 24, 'W')
    c.outline()


@icon('rime', ['fcitx-rime', 'fcitx5-rime', 'ibus-rime', 'org.fcitx.Fcitx5.Addon.Rime', 'rime-ice', 'squirrel',
               'weasel'], 'system', 'Rime')
def rime(c):
    # an ink stone disc with the 中 (Zhongzhou rhyme)
    disc(c, 'k', 13)
    c.ring(16, 16, 11, 10, 's')
    g(c, 10, 8, """
        .....##.....
        .....##.....
        ############
        ##...##...##
        ##...##...##
        ############
        .....##.....
        .....##.....
        .....##.....
    """, 'W')
    c.outline()


@icon('ibus-libpinyin', ['ibus-pinyin', 'libpinyin', 'ibus-setup-libpinyin', 'fcitx-pinyin', 'fcitx5-pinyin',
                         'org.fcitx.Fcitx5.Addon.Pinyin'], 'system', 'Pinyin')
def ibus_pinyin(c):
    _keycap(c)
    c.text(8, 9, 'PY', 'B', font=5, gap=2)
    c.hline(8, 23, 19, 'b')
    c.outline()


@icon('ibus-chewing', ['chewing', 'fcitx-chewing', 'fcitx5-chewing', 'org.fcitx.Fcitx5.Addon.Chewing',
                       'libchewing'], 'system', 'Chewing')
def ibus_chewing(c):
    _keycap(c)
    g(c, 11, 8, """
        .#........
        .#........
        .########.
        .#......#.
        ........#.
        .......#..
        ......#...
        .....#....
        ....#.....
    """, 'G')
    c.outline()


# ================================================================ desktop tools

@icon('utools', ['utools-bin', 'uTools', 'com.utools.app', 'utools-appimage'], 'utilities', 'uTools')
def utools(c):
    # the chunky "u" magnet
    c.rrect(4, 4, 27, 28, 'B', 6)
    c.rrect(11, 3, 20, 20, '.', 3)
    c.rect(11, 3, 20, 12, '.')
    c.bevel(['B'])
    c.rect(4, 4, 10, 7, 'M')
    c.rect(21, 4, 27, 7, 'M')
    c.outline()


@icon('snipaste', ['Snipaste', 'com.snipaste.Snipaste', 'snipaste-bin', 'snipaste-appimage'], 'utilities',
      'Snipaste')
def snipaste(c):
    # crop corners over a teal snip
    c.rect(8, 8, 23, 23, 'C')
    c.bevel(['C'])
    c.poly([(8, 23.5), (14, 15), (19, 23.5)], '5')
    c.rect(3, 3, 13, 5, 'k'); c.rect(3, 3, 5, 13, 'k')
    c.rect(18, 26, 28, 28, 'k'); c.rect(26, 18, 28, 28, 'k')
    c.rect(18, 3, 20, 5, 'k'); c.rect(3, 18, 5, 20, 'k')
    c.circle(20, 12, 2, 'W')
    c.outline()


@icon('pixpin', ['PixPin', 'pixpin-bin', 'com.pixpin.PixPin'], 'utilities', 'PixPin')
def pixpin(c):
    # a push-pin
    c.rrect(9, 3, 22, 7, 'B', 1)
    c.rect(11, 8, 20, 15, 'B')
    c.rrect(6, 15, 25, 18, 'B', 1)
    c.bevel(['B'])
    c.rect(15, 19, 16, 27, 'S')
    c.vline(15, 19, 27, 'w')
    c.outline()


@icon('picgo', ['PicGo', 'picgo-appimage', 'picgo-bin', 'com.github.Molunerfinn.PicGo', 'picgo-electron'],
      'utilities', 'PicGo')
def picgo(c):
    c.rect(3, 9, 24, 28, 'W')
    c.rect(5, 11, 22, 24, 'c')
    c.circle(10, 15, 2, 'y')
    c.poly([(5, 24.5), (12, 17), (19, 24.5)], 'B')
    c.shade_below(['W'], 'w')
    # upload arrow badge
    c.circle(23, 9, 6.5, 'B')
    c.poly([(23, 4), (27.5, 9), (18.5, 9)], 'W')
    c.rect(22, 9, 23, 12, 'W')
    c.outline()


@icon('umi-ocr', ['Umi-OCR', 'umi-ocr-bin', 'umiocr'], 'utilities', 'Umi-OCR')
def umi_ocr(c):
    c.rect(4, 3, 22, 26, 'W')
    c.shade_below(['W'], 'w')
    c.text(6, 6, 'OCR', 'k', font=3)
    c.hline(6, 19, 13, 'S'); c.hline(6, 16, 16, 'S')
    c.ring(20, 20, 6.5, 4, 'k')
    c.circle(20, 20, 4, 'c')
    c.line(24, 24, 27, 27, 'k', 2)
    c.px(18, 18, 'W')
    c.outline()


@icon('pot', ['pot-desktop', 'com.pot-app.desktop', 'pot-translation', 'pot-bin', 'pot-desktop-bin'], 'utilities',
      'Pot')
def pot(c):
    # a cooking pot (Pot translator)
    c.rrect(6, 11, 25, 27, 'P', 3)
    c.rect(3, 13, 5, 15, 'P'); c.rect(26, 13, 28, 15, 'P')
    c.bevel(['P'])
    c.rrect(4, 8, 27, 10, 'p', 1)
    c.rrect(13, 5, 18, 7, '9', 1)
    c.rect(9, 17, 10, 18, 'K'); c.rect(21, 17, 22, 18, 'K')
    c.hline(14, 17, 21, '9')
    c.outline()


@icon('eudic', ['com.eusoft.eudic', 'frhelper', 'eudic-bin', 'Eudic', 'eusoft-eudic'], 'office', 'Eudic')
def eudic(c):
    disc(c, 'R', 13)
    c.text(7, 12, 'EU', 'W', font=5, gap=3)
    c.outline()


@icon('baidu-translate', ['baidufanyi', 'com.baidu.translate', 'baidu-fanyi', 'baidu-translate-bin'], 'utilities',
      'Baidu Translate')
def baidu_translate(c):
    bubble(c, 'B', 3, 4, 28, 23)
    g(c, 7, 8, """
        .###......
        #...#.....
        #####.....
        #...#.....
        #...#.....
    """, 'W')
    g(c, 15, 11, """
        ...#....
        ########
        .#....#.
        ..#..#..
        ...##...
        .##..##.
        #......#
    """, 'c')
    c.outline()


# ================================================================ AI assistants

@icon('doubao', ['doubao-desktop', 'com.bytedance.doubao', 'doubao-bin', 'Doubao', 'com.doubao.app'], 'ai',
      'Doubao')
def doubao(c):
    # the round Doubao head: hair cap, two buns, smile
    c.circle(8, 6, 3.5, '6'); c.circle(24, 6, 3.5, '6')
    c.circle(16, 17, 12, 'B')
    c.bevel(['B', '6'])
    c.ellipse(16, 20, 9.5, 8, 'y')
    c.rect(11, 18, 12, 20, 'K'); c.rect(20, 18, 21, 20, 'K')
    c.hline(14, 18, 24, '2'); c.px(13, 23, '2'); c.px(19, 23, '2')
    c.px(9, 22, 'p'); c.px(23, 22, 'p')
    c.outline()


@icon('yuanbao', ['tencent-yuanbao', 'com.tencent.yuanbao', 'yuanbao-desktop', 'yuanbao-bin', 'Yuanbao'], 'ai',
      'Tencent Yuanbao')
def yuanbao(c):
    # an ingot (元宝) in Yuanbao green-teal
    c.ellipse(16, 13, 6, 6, 'G')
    c.poly([(3, 12), (9, 16), (23, 16), (29, 12), (26, 23), (16, 27), (6, 23)], 'C')
    c.bevel(['G', 'C'])
    c.hline(8, 23, 16, '5')
    c.px(14, 10, 'g'); c.px(13, 11, 'W')
    c.outline()


@icon('ernie-bot', ['wenxin', 'yiyan', 'wenxin-yiyan', 'ernie', 'com.baidu.yiyan', 'wenxiaoyan', 'ernie-desktop'],
      'ai', 'ERNIE Bot')
def ernie(c):
    # blue-violet rhombus with a white ripple
    c.poly([(16, 2.5), (29.5, 16), (16, 29.5), (2.5, 16)], 'B')
    c.poly([(16, 9), (23, 16), (16, 23)], 'M')
    c.bevel(['B', 'M'])
    c.arc(16, 16, 6, 4, 180, 359, 'W')
    c.arc(16, 16, 6, 4, 90, 180, 'W')
    c.outline()


@icon('chatglm', ['zhipu-qingyan', 'qingyan', 'chatglm-desktop', 'zhipuai', 'zhipu', 'com.zhipuai.chatglm'], 'ai',
      'ChatGLM / Qingyan')
def chatglm(c):
    round_bubble(c, 'B', 16, 14, 13, 10.5, 'right')
    c.bevel(['B'])
    c.text(6, 12, 'GLM', 'W', font=3, gap=2)
    c.outline()


@icon('hailuo', ['minimax', 'hailuo-ai', 'minimax-desktop', 'com.minimax.hailuo', 'minimax-agent'], 'ai',
      'MiniMax Hailuo')
def hailuo(c):
    # a conch shell (海螺)
    c.poly([(3, 20), (12, 5), (22, 3), (29, 10), (27, 22), (17, 29), (8, 28)], 'O')
    c.bevel(['O'])
    c.arc(18, 14, 8, 6.5, 200, 80, '2')
    c.arc(18, 14, 5, 3.5, 140, 20, '2')
    c.circle(18, 14, 2, 'o')
    c.poly([(3, 20), (8, 23), (6, 27)], 'p')
    c.outline()


@icon('stepfun', ['yuewen', 'stepfun-desktop', 'com.stepfun.yuewen', 'step-chat'], 'ai', 'StepFun')
def stepfun(c):
    # the climbing steps
    for i, col in enumerate(['G', 'C', 'B']):
        x0 = 4 + i * 8
        c.rect(x0, 21 - i * 8, x0 + 7, 28, col)
    c.bevel(['G', 'C', 'B'])
    c.outline()
