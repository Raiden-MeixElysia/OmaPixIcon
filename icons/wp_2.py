"""Google / Microsoft / Apple web apps, notes and whiteboards."""
from pix import icon


# ================================================================ helpers

def disc(c, col, r=13, cx=16, cy=16):
    c.circle(cx, cy, r, col)
    c.bevel([col])


def g(c, x, y, art, col='W'):
    c.sprite(x, y, art, {'#': col, '+': 'w'})


def ctext(c, s, col, cy=16, scale=2, font=5, cx=16):
    w = c.text_width(s, font, scale)
    h = (7 if font == 5 else 5) * scale
    c.text(int(round(cx - w / 2)), int(round(cy - h / 2)), s, col, font, scale)


def gdoc(c, col, lt):
    """Google-style page with a dog-eared corner."""
    c.poly([(5, 3), (20, 3), (27, 10), (27, 29), (5, 29)], col)
    c.bevel([col])
    c.poly([(19, 3), (27, 11), (19, 11)], lt)


def office(c, page, dark, letter):
    """Modern Office: a page with a letter tile overlapping its left side."""
    c.rrect(10, 3, 28, 28, page, 2)
    c.bevel([page])
    for y in (8, 13, 18, 23):
        c.hline(19, 25, y, dark)
    c.rect(3, 9, 18, 22, dark)
    c.bevel([dark])
    ctext(c, letter, 'W', 15.5, 2, 3, 10.5)


# ================================================================ Google

@icon('google-keep', ['google-keep-webapp', 'com.google.keep', 'keep.google.com', 'google-keep-desktop'], 'web',
      'Google Keep')
def google_keep(c):
    gdoc(c, 'Y', 'y')
    c.circle(16, 16, 4.5, 'W')
    c.rect(14, 20, 17, 22, 'W')
    c.hline(14, 17, 23, 'w')
    c.pixels([(14, 14), (15, 13)], 'y')
    c.outline()


@icon('google-tasks', ['google-tasks-webapp', 'com.google.tasks', 'tasks.google.com'], 'web', 'Google Tasks')
def google_tasks(c):
    disc(c, 'B')
    g(c, 8, 10, """
        ..............##
        .............###
        ............###.
        ##.........###..
        ###.......###...
        .###.....###....
        ..###...###.....
        ...###.###......
        ....#####.......
        .....###........
    """)
    c.outline()


@icon('google-translate', ['google-translate-webapp', 'com.google.translate', 'translate.google.com'], 'web',
      'Google Translate')
def google_translate(c):
    c.rrect(3, 3, 19, 21, 'B', 2)
    c.bevel(['B'])
    ctext(c, 'G', 'W', 12, 2, 3, 11)
    c.rrect(13, 11, 28, 28, 'w', 2)
    c.bevel(['w'])
    c.poly([(15, 21), (19, 21), (16, 25)], 'B')
    g(c, 16, 13, """
        ....#....
        #########
        .#.....#.
        ..#...#..
        ...#.#...
        ....#....
        ...#.#...
        .##...##.
    """, 'k')
    c.outline()


@icon('google-lens', ['google-lens-webapp', 'com.google.lens', 'lens.google.com'], 'web', 'Google Lens')
def google_lens(c):
    c.rrect(3, 3, 28, 28, 'W', 5)
    c.bevel(['W'])
    c.arc(16, 16, 11, 7.5, 180, 270, 'B')
    c.arc(16, 16, 11, 7.5, 270, 360, 'R')
    c.arc(16, 16, 11, 7.5, 90, 180, 'Y')
    c.rect(18, 18, 27, 27, 'W')
    c.circle(16, 16, 4, 'B')
    c.circle(23, 23, 3, 'G')
    c.outline()


@icon('google-play', ['google-play-webapp', 'com.google.play', 'play.google.com', 'google-play-store'], 'web',
      'Google Play')
def google_play(c):
    c.poly([(5, 3), (28, 16), (5, 29)], 'G')
    c.poly([(5, 3), (17, 16), (5, 29)], 'C')
    c.poly([(17, 16), (28, 16), (22, 12.6)], 'Y')
    c.poly([(17, 16), (28, 16), (22, 19.4)], 'R')
    c.poly([(5, 3), (17, 16), (22, 12.6)], 'G')
    c.poly([(5, 29), (17, 16), (22, 19.4)], 'R')
    c.poly([(22, 12.6), (28, 16), (22, 19.4), (17, 16)], 'Y')
    c.bevel(['G', 'C', 'Y', 'R'])
    c.outline()


@icon('google-classroom', ['google-classroom-webapp', 'com.google.classroom', 'classroom.google.com'], 'web',
      'Google Classroom')
def google_classroom(c):
    c.rect(3, 5, 28, 26, 'Y')
    c.rect(5, 7, 26, 24, 'G')
    c.bevel(['G'])
    c.circle(16, 12.5, 2.5, 'W'); c.ellipse(16, 19, 5, 3, 'W'); c.rect(10, 19, 22, 21, 'G')
    c.circle(10, 14, 2, 'g'); c.ellipse(10, 19.5, 3.5, 2, 'g')
    c.circle(22, 14, 2, 'g'); c.ellipse(22, 19.5, 3.5, 2, 'g')
    c.rect(5, 20, 26, 21, 'G')
    c.circle(16, 12.5, 2.5, 'W'); c.ellipse(16, 18.5, 4.5, 2.5, 'W'); c.rect(10, 19, 22, 21, 'G')
    c.rect(18, 22, 23, 23, 'W')
    c.outline()


@icon('google-one', ['google-one-webapp', 'com.google.one', 'one.google.com'], 'web', 'Google One')
def google_one(c):
    c.poly([(8, 9), (17, 3), (22, 3), (22, 29), (15, 29), (15, 11), (8, 15)], 'B')
    c.poly([(15, 18), (22, 18), (22, 29), (15, 29)], 'G')
    c.poly([(8, 9), (14, 5.5), (15, 11), (8, 15)], 'R')
    c.poly([(14, 5.5), (17, 3), (22, 3), (22, 9), (15, 9)], 'Y')
    c.bevel(['B', 'G', 'R', 'Y'], light=False)
    c.outline()


@icon('google-analytics', ['google-analytics-webapp', 'analytics.google.com'], 'web', 'Google Analytics')
def google_analytics(c):
    c.rrect(20, 3, 27, 28, 'O', 3)
    c.rrect(12, 12, 19, 28, 'Y', 3)
    c.bevel(['O', 'Y'])
    c.circle(8.5, 24.5, 4, '2')
    c.bevel(['2'])
    c.outline()


@icon('google-search-console', ['search-console', 'search.google.com'], 'web', 'Google Search Console')
def google_search_console(c):
    c.rrect(3, 4, 25, 22, 'w', 2)
    c.bevel(['w'])
    c.rect(6, 7, 22, 9, 'S')
    c.rect(7, 13, 9, 19, 'B'); c.rect(11, 15, 13, 19, 'G'); c.rect(15, 12, 17, 19, 'Y')
    c.ring(20, 20, 6, 3.5, 'k')
    c.line(24, 24, 27, 27, 'k', 2)
    c.circle(20, 20, 3.5, 'c')
    c.outline()


@icon('google-fit', ['google-fit-webapp', 'com.google.fit', 'fit.google.com'], 'web', 'Google Fit')
def google_fit(c):
    c.circle(10, 11, 7, 'R')
    c.circle(22, 11, 7, 'B')
    c.poly([(3.5, 13), (16, 26), (16, 15)], 'Y')
    c.poly([(28.5, 13), (16, 26), (16, 15)], 'G')
    c.rect(4, 11, 15, 14, 'R'); c.rect(17, 11, 28, 14, 'B')
    c.poly([(3.5, 14), (16, 27), (16, 17)], 'Y')
    c.poly([(28.5, 14), (16, 27), (16, 17)], 'G')
    c.ellipse(16, 15, 4, 4, '.')
    c.bevel(['R', 'B', 'Y', 'G'], light=False)
    c.outline()


@icon('google-news', ['google-news-webapp', 'com.google.news', 'news.google.com'], 'web', 'Google News')
def google_news(c):
    c.rrect(6, 3, 26, 14, 'G', 1)
    c.rrect(3, 6, 23, 16, 'R', 1)
    c.bevel(['G', 'R'])
    c.rrect(4, 10, 28, 28, 'B', 1)
    c.bevel(['B'])
    c.rect(8, 15, 15, 16, 'W'); c.rect(8, 19, 15, 20, 'W'); c.rect(8, 23, 15, 24, 'W')
    c.circle(21.5, 20.5, 3.5, 'W')
    c.outline()


@icon('youtube-studio', ['youtube-studio-webapp', 'studio.youtube.com', 'com.google.android.apps.youtube.creator'],
      'web', 'YouTube Studio')
def youtube_studio(c):
    # gear with a play button
    for a in range(0, 360, 45):
        import math
        x, y = 16 + 10.5 * math.cos(math.radians(a)), 16 + 10.5 * math.sin(math.radians(a))
        c.circle(x, y, 2.5, 'R')
    c.circle(16, 16, 10.5, 'R')
    c.bevel(['R'])
    c.sprite(13, 10, """
        WW.....
        WWWW...
        WWWWWW.
        WWWWWWW
        WWWWWW.
        WWWW...
        WW.....
    """)
    c.outline()


@icon('youtube-kids', ['youtube-kids-webapp', 'com.google.android.apps.youtube.kids', 'youtubekids.com'], 'web',
      'YouTube Kids')
def youtube_kids(c):
    c.poly([(3, 9), (26, 4), (29, 23), (6, 28)], 'R')
    c.bevel(['R'])
    c.poly([(13, 11), (21, 15), (14, 20)], 'W')
    c.outline()


@icon('google-chat', ['google-chat-webapp', 'com.google.chat', 'chat.google.com', 'google-chat-electron'], 'web',
      'Google Chat')
def google_chat(c):
    c.rrect(3, 4, 28, 22, 'G', 3)
    c.poly([(3, 18), (10, 22), (3, 28)], 'G')
    c.bevel(['G'])
    c.rrect(8, 9, 23, 17, 'W', 1)
    c.poly([(19, 11), (23, 9), (23, 17), (19, 15)], 'g')
    c.rect(9, 10, 18, 16, 'W')
    c.outline()


@icon('google-slides', ['google-slides-webapp', 'com.google.slides', 'slides.google.com'], 'web', 'Google Slides')
def google_slides(c):
    gdoc(c, 'Y', 'y')
    c.rect(9, 14, 22, 24, 'W')
    c.rect(11, 16, 20, 22, 'Y')
    c.outline()


@icon('google-forms', ['google-forms-webapp', 'com.google.forms', 'forms.google.com'], 'web', 'Google Forms')
def google_forms(c):
    gdoc(c, 'M', 'm')
    for y in (14, 18, 22):
        c.rect(9, y, 10, y + 1, 'W')
        c.rect(12, y, 22, y + 1, 'W')
    c.outline()


@icon('google-earth-pro', ['google-earth', 'google-earth-webapp', 'earth.google.com', 'com.google.EarthPro'],
      'web', 'Google Earth')
def google_earth(c):
    disc(c, 'B')
    c.poly([(8, 8), (14, 6), (16, 10), (12, 14), (13, 18), (9, 17), (6, 12)], 'G')
    c.poly([(18, 15), (24, 14), (26, 19), (22, 25), (18, 22)], 'G')
    c.poly([(19, 6), (23, 7), (21, 10)], 'G')
    c.bevel(['G'])
    c.arc(16, 16, 13, 11.5, 200, 260, 'b')
    c.outline()


# ================================================================ Microsoft

@icon('microsoft-word', ['ms-word', 'word', 'word-webapp', 'com.microsoft.Word', 'msword'], 'office',
      'Microsoft Word')
def ms_word(c):
    office(c, 'b', '6', 'W')
    c.outline()


@icon('microsoft-excel', ['ms-excel', 'excel', 'excel-webapp', 'com.microsoft.Excel'], 'office', 'Microsoft Excel')
def ms_excel(c):
    office(c, 'g', '4', 'X')
    c.outline()


@icon('microsoft-powerpoint', ['ms-powerpoint', 'powerpoint', 'powerpoint-webapp', 'com.microsoft.PowerPoint'],
      'office', 'Microsoft PowerPoint')
def ms_powerpoint(c):
    c.circle(19, 16, 10.5, 'O')
    c.arc(19, 16, 10.5, 0, 270, 360, 'o')
    c.bevel(['O'])
    c.rect(3, 9, 18, 22, '2')
    c.bevel(['2'])
    ctext(c, 'P', 'W', 15.5, 2, 3, 10.5)
    c.outline()


@icon('microsoft-onenote', ['ms-onenote', 'onenote', 'onenote-webapp', 'com.microsoft.OneNote', 'p3x-onenote'],
      'office', 'Microsoft OneNote')
def ms_onenote(c):
    office(c, 'm', '7', 'N')
    c.outline()


@icon('microsoft-outlook', ['outlook', 'ms-outlook', 'outlook-webapp', 'prospect-mail', 'com.microsoft.Outlook',
                            'outlook-for-linux'], 'mail', 'Outlook')
def ms_outlook(c):
    c.rrect(10, 9, 28, 27, 'B', 1)
    c.bevel(['B'])
    c.poly([(11, 10), (27, 10), (19, 17)], 'b')
    c.rect(13, 4, 26, 9, 'c')
    c.bevel(['c'])
    c.rect(3, 8, 17, 22, '6')
    c.bevel(['6'])
    c.ring(10, 15, 5, 2.5, 'W')
    c.outline()


@icon('microsoft-to-do', ['ms-todo', 'microsoft-todo', 'todo-webapp', 'com.microsoft.ToDo', 'kuro'], 'office',
      'Microsoft To Do')
def ms_todo(c):
    c.poly([(3, 15), (8, 10), (13, 15), (24, 4), (29, 9), (13, 25)], 'B')
    c.poly([(3, 15), (8, 10), (13, 15), (13, 25)], 'b')
    c.bevel(['B', 'b'])
    c.outline()


@icon('azure', ['microsoft-azure', 'azure-portal', 'portal.azure.com', 'azure-data-studio', 'azuredatastudio'],
      'web', 'Microsoft Azure')
def azure(c):
    c.poly([(11, 3), (19, 3), (10, 28), (3, 28)], '6')
    c.poly([(19, 3), (29, 28), (11, 28), (17, 23), (21, 23), (14, 17)], 'C')
    c.bevel(['6', 'C'])
    c.outline()


@icon('bing', ['microsoft-bing', 'bing-webapp', 'bing.com'], 'web', 'Bing')
def bing(c):
    c.poly([(6, 3), (12, 5), (12, 21), (20, 17), (16, 14), (14, 10), (27, 15), (27, 20), (12, 29), (6, 26)], 'C')
    c.bevel(['C'])
    c.outline()


@icon('clipchamp', ['microsoft-clipchamp', 'clipchamp-webapp', 'clipchamp.com'], 'media', 'Clipchamp')
def clipchamp(c):
    disc(c, 'M')
    c.arc(16, 16, 9, 5, 45, 315, 'W')
    c.poly([(14, 12), (21, 16), (14, 20)], 'W')
    c.outline()


@icon('microsoft-loop', ['loop-webapp', 'loop.microsoft.com'], 'office', 'Microsoft Loop')
def ms_loop(c):
    c.ellipse(11, 16, 8, 12, 'M')
    c.ellipse(21, 16, 8, 12, 'B')
    c.ellipse(16, 16, 3, 9, '7')
    c.bevel(['M', 'B'])
    c.ellipse(11, 16, 3.5, 7, 'k')
    c.ellipse(21, 16, 3.5, 7, 'k')
    c.outline()


@icon('microsoft-365', ['office365', 'office-365', 'microsoft-office', 'ms-office', 'm365', 'office-webapp',
                        'office.com'], 'office', 'Microsoft 365')
def ms365(c):
    c.poly([(9, 3), (20, 3), (28, 9), (28, 23), (20, 29), (9, 29), (4, 25), (4, 7)], 'R')
    c.poly([(16, 3), (20, 3), (28, 9), (28, 16), (16, 16)], 'O')
    c.poly([(16, 16), (28, 16), (28, 23), (20, 29), (16, 29)], 'M')
    c.poly([(4, 16), (16, 16), (16, 29), (9, 29), (4, 25)], 'B')
    c.bevel(['R', 'O', 'M', 'B'])
    c.rrect(11, 11, 21, 21, 'k', 1)
    c.outline()


# ================================================================ Apple

@icon('icloud', ['icloud-webapp', 'icloud.com', 'apple-icloud'], 'web', 'iCloud')
def icloud(c):
    c.ellipse(16, 21, 13, 6, 'W')
    c.circle(13.5, 15, 7, 'W')
    c.circle(21, 17, 5.5, 'W')
    c.circle(7.5, 19.5, 4, 'W')
    c.bevel(['W'])
    c.shade_below(['W'], 'w')
    c.arc(13.5, 15, 7, 5.5, 200, 280, 'c')
    c.outline()


@icon('apple-music', ['apple-music-webapp', 'music.apple.com', 'apple-music-electron'], 'media', 'Apple Music')
def apple_music(c):
    c.rect(12, 7, 14, 23, 'P'); c.rect(25, 4, 27, 20, 'P')
    c.poly([(12, 7), (27, 3), (27, 8), (12, 12)], 'P')
    c.ellipse(9, 23.5, 5, 4, 'P')
    c.ellipse(22, 20.5, 5, 4, 'P')
    c.bevel(['P'])
    c.outline()


@icon('apple-tv', ['apple-tv-webapp', 'tv.apple.com', 'appletv'], 'media', 'Apple TV')
def apple_tv(c):
    c.rrect(3, 5, 28, 23, 'k', 2)
    c.bevel(['k'])
    c.rect(11, 24, 20, 25, 's'); c.rect(8, 26, 23, 27, 's')
    ctext(c, 'TV', 'W', 14, 2, 3)
    c.outline()


# ================================================================ notes & knowledge bases

@icon('zoho', ['zoho-workplace', 'zoho-webapp', 'zoho.com', 'zoho-mail', 'com.zoho.mail', 'zoho-cliq'], 'office',
      'Zoho')
def zoho(c):
    for (x, y, col, ch) in ((3, 3, 'R', 'Z'), (17, 3, 'G', 'O'), (3, 17, 'B', 'H'), (17, 17, 'Y', 'O')):
        c.rrect(x, y, x + 11, y + 11, col, 1)
        ctext(c, ch, 'W', y + 6, 1, 5, x + 6)
    c.bevel(['R', 'G', 'B', 'Y'], light=False)
    c.outline()


@icon('craft', ['craft-docs', 'craft-webapp', 'craft.do'], 'office', 'Craft')
def craft(c):
    c.rrect(3, 3, 28, 28, 'k', 5)
    c.bevel(['k'])
    c.poly([(9, 8), (22, 8), (22, 13), (14, 13), (14, 19), (22, 19), (22, 24), (9, 24)], 'W')
    c.poly([(14, 13), (22, 13), (18, 16)], 'w')
    c.outline()


@icon('affine', ['pro.affine.app', 'affine-bin', 'affine-canary', 'AFFiNE', 'affine-desktop'], 'office', 'AFFiNE')
def affine(c):
    c.poly([(16, 3), (29, 28), (3, 28)], 'k')
    c.bevel(['k'])
    c.line(16, 9, 9, 23, 'W'); c.line(16, 9, 23, 23, 'W'); c.hline(9, 23, 23, 'W')
    c.line(16, 9, 16, 23, 'w'); c.line(12, 17, 20, 17, 'w')
    c.outline()


@icon('appflowy', ['io.appflowy.AppFlowy', 'appflowy-bin', 'AppFlowy'], 'office', 'AppFlowy')
def appflowy(c):
    c.ellipse(11, 10, 7, 6.5, 'M')
    c.ellipse(22, 11, 6.5, 7, 'C')
    c.ellipse(10, 21, 6.5, 7, 'Y')
    c.ellipse(21, 22, 7, 6.5, 'P')
    c.bevel(['M', 'C', 'Y', 'P'], light=False)
    c.circle(16, 16, 2.5, 'W')
    c.outline()


@icon('siyuan', ['siyuan-note', 'org.b3log.siyuan', 'siyuan-bin', 'siyuan-appimage', 'SiYuan'], 'office',
      'SiYuan')
def siyuan(c):
    c.rrect(3, 3, 28, 28, 'R', 4)
    c.bevel(['R'])
    c.poly([(8, 9), (14, 6), (14, 23), (8, 26)], 'W')
    c.poly([(16, 9), (24, 5), (24, 21), (16, 25)], 'W')
    c.poly([(14, 6), (16, 9), (16, 25), (14, 23)], 'w')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('trilium', ['trilium-notes', 'com.github.zadam.trilium', 'trilium-bin', 'trilium-desktop', 'trilium-next',
                  'triliumnext', 'TriliumNext', 'trilium-next-desktop', 'com.triliumnext.notes'], 'office',
      'Trilium Notes')
def trilium(c):
    # three-petal trillium flower
    c.ellipse(16, 9.5, 5.5, 7, 'W')
    c.ellipse(9.5, 20.5, 6, 5.5, 'W')
    c.ellipse(22.5, 20.5, 6, 5.5, 'W')
    c.bevel(['W'])
    c.poly([(16, 15), (6, 9), (11, 15)], 'G')
    c.poly([(16, 15), (26, 9), (21, 15)], 'G')
    c.poly([(14, 19), (18, 19), (16, 28)], 'G')
    c.bevel(['G'])
    c.circle(16, 16, 2.5, 'Y')
    c.outline()


@icon('notesnook', ['com.notesnook.Notesnook', 'notesnook-bin', 'Notesnook'], 'office', 'Notesnook')
def notesnook(c):
    c.rrect(5, 3, 26, 28, 'k', 2)
    c.bevel(['k'])
    c.rect(5, 3, 7, 28, 'K')
    g(c, 11, 9, """
        #.####.
        ##....#
        #.....#
        #.....#
        #.....#
        #.....#
        #.....#
        #.....#
        #.....#
    """)
    c.rect(11, 21, 21, 22, 'G')
    c.outline()


@icon('simplenote', ['com.simplenote.Simplenote', 'simplenote-electron', 'simplenote-bin'], 'office', 'Simplenote')
def simplenote(c):
    disc(c, 'B')
    c.arc(13.5, 12, 6, 3, 90, 330, 'W')
    c.arc(18.5, 20, 6, 3, 270, 150, 'W')
    c.outline()


@icon('memos', ['usememos', 'memos-desktop', 'memos-webapp'], 'office', 'Memos')
def memos(c):
    c.poly([(4, 4), (28, 4), (28, 21), (21, 28), (4, 28)], 'Y')
    c.bevel(['Y'])
    c.poly([(21, 21), (28, 21), (21, 28)], '3')
    c.rect(10, 11, 11, 13, 'K'); c.rect(20, 11, 21, 13, 'K')
    c.arc(16, 15, 6, 4.5, 30, 150, 'K')
    c.outline()


@icon('outline', ['outline-wiki', 'getoutline', 'outline-webapp'], 'office', 'Outline')
def outline_app(c):
    c.rrect(3, 3, 28, 28, 'k', 4)
    c.bevel(['k'])
    c.rrect(9, 7, 22, 18, 'W', 1); c.rrect(11, 9, 20, 16, 'k', 0)
    c.rrect(9, 14, 22, 25, 'W', 1); c.rect(11, 16, 20, 23, 'w')
    c.outline()


@icon('workflowy', ['workflowy-desktop', 'com.workflowy.desktop', 'workflowy-webapp'], 'office', 'WorkFlowy')
def workflowy(c):
    disc(c, 'k')
    c.circle(16, 16, 7, 's')
    c.circle(16, 16, 4, 'W')
    c.outline()


@icon('roam-research', ['roam', 'roam-webapp', 'roamresearch.com'], 'office', 'Roam Research')
def roam(c):
    disc(c, 'k')
    import math
    for a in range(0, 360, 30):
        x0, y0 = 16 + 4 * math.cos(math.radians(a)), 16 + 4 * math.sin(math.radians(a))
        x1, y1 = 16 + 10 * math.cos(math.radians(a)), 16 + 10 * math.sin(math.radians(a))
        c.line(x0, y0, x1, y1, 'W')
    c.circle(16, 16, 2.5, 'W')
    c.outline()


@icon('miro', ['miro-webapp', 'miro.com', 'com.miro.Miro'], 'office', 'Miro')
def miro(c):
    c.rrect(3, 3, 28, 28, 'Y', 5)
    c.bevel(['Y'])
    for x in (8, 13, 18):
        c.poly([(x + 3, 7), (x + 6, 7), (x + 3, 25), (x, 25)], 'k')
    c.poly([(20, 7), (23, 7), (25, 25), (22, 25)], 'k')
    c.outline()


@icon('excalidraw', ['excalidraw-desktop', 'com.excalidraw.Excalidraw', 'excalidraw-webapp'], 'office',
      'Excalidraw')
def excalidraw(c):
    # scribbled box and a fat pencil
    c.rrect(3, 9, 22, 28, 'W', 1)
    c.bevel(['W'])
    c.frame(6, 12, 19, 25, 'M')
    c.line(7, 22, 18, 13, 'm')
    c.poly([(23, 3), (29, 9), (16, 22), (12, 23), (13, 19)], 'M')
    c.poly([(12, 23), (13, 19), (16, 22)], 'y')
    c.bevel(['M'])
    c.outline()


@icon('tldraw', ['tldraw-desktop', 'tldraw-webapp', 'tldraw.com'], 'office', 'tldraw')
def tldraw(c):
    c.rrect(3, 3, 28, 28, 'W', 5)
    c.bevel(['W'])
    c.circle(16, 12, 4.5, 'k')
    c.poly([(15, 15), (20, 13), (18, 21), (12, 26)], 'k')
    c.outline()


@icon('yed', ['com.yworks.yEd', 'yEd', 'yed-graph-editor'], 'office', 'yEd')
def yed(c):
    c.line(9, 9, 22, 9, 'k', 2); c.line(9, 9, 9, 22, 'k', 2); c.line(9, 9, 22, 22, 'k', 2)
    c.line(22, 9, 22, 22, 'k', 2)
    c.circle(9, 9, 6, 'Y'); c.circle(23, 9, 5, 'B'); c.circle(9, 23, 5, 'G'); c.circle(23, 23, 6, 'R')
    c.bevel(['Y', 'B', 'G', 'R'], light=False)
    c.outline()


# ================================================================ calendars / scheduling

@icon('notion-calendar', ['cron', 'cron-calendar', 'notion-calendar-webapp', 'calendar.notion.so'], 'office',
      'Notion Calendar')
def notion_calendar(c):
    c.rrect(3, 4, 28, 28, 'W', 3)
    c.bevel(['W'])
    c.rect(3, 4, 28, 10, 'k')
    c.rrect(3, 4, 28, 10, 'k', 3)
    c.rect(3, 8, 28, 10, 'k')
    ctext(c, '31', 'k', 19.5, 1, 5)
    c.outline()


@icon('cal-com', ['calcom', 'cal.com', 'cal-com-webapp'], 'office', 'Cal.com')
def calcom(c):
    c.rrect(3, 3, 28, 28, 'k', 4)
    c.bevel(['k'])
    g(c, 6, 13, """
        .##...##...#.....
        #....#..#..#.....
        #....####..#.....
        .##..#..#..###.#.
    """)
    c.outline()


@icon('calendly', ['calendly-webapp', 'calendly.com'], 'office', 'Calendly')
def calendly(c):
    disc(c, 'B')
    c.arc(16, 16, 9, 6, 50, 310, 'W')
    c.circle(22.5, 16, 2, 'c')
    c.outline()
