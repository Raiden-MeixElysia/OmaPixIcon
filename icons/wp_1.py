"""Messengers, IRC, social networks and community sites."""
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


def bubble(c, col, x0=3, y0=4, x1=28, y1=23, r=4, tail='left'):
    c.rrect(x0, y0, x1, y1, col, r)
    if tail == 'left':
        c.poly([(x0 + 3, y1 - 1), (x0 + 10, y1 - 1), (x0 + 1, y1 + 6)], col)
    elif tail == 'right':
        c.poly([(x1 - 9, y1 - 1), (x1 - 2, y1 - 1), (x1, y1 + 6)], col)
    c.bevel([col])


def round_bubble(c, col, cx=16.5, cy=15, r=12, tail='left'):
    c.circle(cx, cy, r, col)
    if tail == 'left':
        c.poly([(5, 20), (11, 25), (3, 29)], col)
    else:
        c.poly([(28, 20), (22, 25), (30, 29)], col)
    c.bevel([col])


# ================================================================ private messengers

@icon('session-desktop', ['session', 'network.loki.Session', 'session-desktop-bin', 'Session'], 'chat', 'Session')
def session(c):
    disc(c, 'k')
    # two offset pill halves forming the Session "S"
    c.rrect(8, 7, 22, 14, 'G', 3)
    c.rrect(10, 18, 24, 25, 'G', 3)
    c.rect(9, 10, 20, 11, 'k')
    c.rect(12, 21, 23, 22, 'k')
    c.rect(8, 10, 11, 14, 'G'); c.rect(9, 10, 11, 11, 'k')
    c.rect(20, 18, 24, 22, 'G'); c.rect(20, 21, 23, 22, 'k')
    c.rect(9, 15, 23, 17, 'k')
    c.pixels([(9, 8), (10, 8)], 'g')
    c.outline()


@icon('simplex', ['chat.simplex.simplex', 'simplex-chat', 'simplex-chat-desktop', 'simplex-desktop'], 'chat',
      'SimpleX Chat')
def simplex(c):
    # two interlocking chevrons forming an X
    c.poly([(3, 6), (9, 3), (29, 23), (23, 29)], 'B')
    c.poly([(23, 3), (29, 9), (9, 29), (3, 23)], 'C')
    c.poly([(3, 6), (9, 3), (17, 11), (14, 14)], 'B')
    c.bevel(['B', 'C'])
    c.pixels([(7, 5), (8, 4)], 'W')
    c.outline()


@icon('threema', ['ch.threema.threema-desktop', 'threema-desktop', 'threema-work-desktop'], 'chat', 'Threema')
def threema(c):
    disc(c, 'k')
    c.ellipse(16, 13, 8, 6.5, 'W')
    c.poly([(10, 16), (13, 18), (9, 21)], 'W')
    c.shade_below(['W'], 'w')
    # padlock
    c.rect(13, 12, 18, 16, 'k')
    c.frame(14, 9, 17, 12, 'k'); c.rect(15, 10, 16, 11, 'W')
    for x in (11, 15, 19):
        c.rect(x, 23, x + 1, 24, 'G')
    c.outline()


@icon('wire-desktop', ['wire', 'com.wire.WireDesktop', 'wire-desktop-bin'], 'chat', 'Wire')
def wire(c):
    disc(c, 'k')
    g(c, 7, 9, """
        #.........#.........#
        #.........#.........#
        #........###........#
        #.......#...#.......#
        #.......#...#.......#
        #.......#...#.......#
        #.......#...#.......#
        #.......#...#.......#
        .#.....#.....#.....#.
        .##...##.....##...##.
        ..#####.......#####..
    """)
    c.replace('W', 'W')
    c.outline()


@icon('jami', ['net.jami.Jami', 'jami-gnome', 'jami-qt', 'jami-client-qt', 'jami-client-gnome'], 'chat', 'Jami')
def jami(c):
    c.poly([(16, 3), (27.5, 9.5), (27.5, 22.5), (16, 29), (4.5, 22.5), (4.5, 9.5)], 'B')
    c.bevel(['B'])
    c.poly([(16, 8), (22.5, 12), (22.5, 20), (16, 24), (9.5, 20), (9.5, 12)], 'C')
    c.poly([(16, 11), (19.5, 13.5), (19.5, 18.5), (16, 21), (12.5, 18.5), (12.5, 13.5)], '6')
    c.rect(15, 13, 16, 19, 'W')
    c.outline()


@icon('briar-desktop', ['org.briarproject.Briar', 'briar', 'briar-desktop-bin'], 'chat', 'Briar')
def briar(c):
    disc(c, 'G')
    for x in (11, 18):
        c.rrect(x, 6, x + 3, 26, 'W', 1)
    for y in (11, 18):
        c.rrect(6, y, 26, y + 3, 'W', 1)
    c.shade_below(['W'], 'w')
    c.outline()


@icon('deltachat-desktop', ['chat.delta.desktop', 'deltachat', 'delta-chat', 'deltachat-desktop-bin'], 'chat',
      'Delta Chat')
def deltachat(c):
    round_bubble(c, '6')
    c.tri((16.5, 7), (24.5, 21), (8.5, 21), 'W')
    c.tri((16.5, 12), (20.5, 19), (12.5, 19), '6')
    c.outline()


@icon('org.gajim.Gajim', ['gajim'], 'chat', 'Gajim')
def gajim(c):
    bubble(c, 'C', 3, 3, 24, 18)
    c.rrect(11, 12, 28, 25, 'O', 4)
    c.poly([(20, 24), (26, 24), (27, 29)], 'O')
    c.bevel(['O'])
    for x in (15, 19, 23):
        c.rect(x, 18, x + 1, 19, 'W')
    c.outline()


@icon('pidgin', ['im.pidgin.Pidgin', 'pidgin-im'], 'chat', 'Pidgin')
def pidgin(c):
    # a plump pigeon walking right
    c.ellipse(14, 18, 11, 8, 'M')
    c.circle(22.5, 9.5, 5, 'M')
    c.poly([(4, 15), (8, 17), (5, 22)], 'M')
    c.bevel(['M'])
    c.ellipse(13, 18, 6.5, 4, '7')
    c.ellipse(12.5, 17, 5.5, 2.5, 'm')
    c.poly([(26.5, 9), (28.5, 10.5), (26.5, 12)], 'Y')
    c.rect(23, 8, 24, 9, 'K')
    c.vline(12, 26, 28, 'O'); c.vline(17, 26, 28, 'O')
    c.outline()


@icon('hexchat', ['io.github.Hexchat', 'xchat'], 'chat', 'HexChat')
def hexchat(c):
    c.poly([(9, 3.5), (23, 3.5), (29.5, 16), (23, 28.5), (9, 28.5), (2.5, 16)], 'M')
    c.bevel(['M'])
    c.poly([(11, 8), (21, 8), (25, 16), (21, 24), (11, 24), (7, 16)], '7')
    c.rrect(10, 11, 22, 19, 'W', 2)
    c.poly([(12, 18), (16, 18), (11, 22)], 'W')
    c.hline(13, 19, 14, 'w'); c.hline(13, 17, 16, 'w')
    c.outline()


@icon('org.gnome.Polari', ['polari'], 'chat', 'Polari')
def polari(c):
    bubble(c, 'B', 3, 4, 28, 23)
    g(c, 7, 7, """
        ......#.........
        .....###........
        ......#.......#.
        .............###
        ..#............#
        .###..#.........
        ..#..###....#...
        ......#....###..
        ............#...
    """, 'Y')
    c.line(9, 12, 13, 13, 'b'); c.line(14, 14, 18, 14, 'b'); c.line(19, 14, 21, 10, 'b')
    c.outline()


@icon('halloy', ['org.squidowl.halloy'], 'chat', 'Halloy')
def halloy(c):
    bubble(c, 'k', 3, 4, 28, 23)
    ctext(c, 'H', 'C', 13.5)
    c.rect(22, 18, 24, 19, 'C')
    c.outline()


@icon('org.kde.konversation', ['konversation'], 'chat', 'Konversation')
def konversation(c):
    bubble(c, 'b', 3, 3, 22, 17)
    c.rrect(9, 11, 28, 25, 'B', 4)
    c.poly([(21, 24), (26, 24), (28, 29)], 'B')
    c.bevel(['B'])
    for x in (13, 17, 21):
        c.rect(x, 17, x + 1, 18, 'W')
    c.outline()


@icon('quassel', ['quasselclient', 'quassel-client', 'quassel-monolithic', 'quassel-client-qt'], 'chat', 'Quassel IRC')
def quassel(c):
    disc(c, 'B', 12, 15, 15)
    c.poly([(20, 22), (24, 21), (29, 28), (24, 28)], 'B')
    c.bevel(['B'])
    c.ring(15, 15, 7.5, 4.5, 'W')
    c.line(17, 18, 21, 22, 'W', 2)
    c.outline()


@icon('weechat', ['weechat-curses', 'weechat-headless'], 'chat', 'WeeChat')
def weechat(c):
    c.poly([(3, 6), (8, 6), (12, 21), (15, 13), (17.5, 18), (13, 27), (10, 27)], 'B')
    c.poly([(17, 6), (21, 6), (23, 18), (25, 6), (29, 6), (25, 27), (21, 27), (17.5, 18), (15.5, 13)], 'G')
    c.bevel(['B', 'G'])
    c.outline()


@icon('rocketchat-desktop', ['chat.rocket.RocketChat', 'rocketchat', 'rocket.chat', 'rocket-chat'], 'chat',
      'Rocket.Chat')
def rocketchat(c):
    c.ellipse(16, 14, 13, 9.5, 'R')
    c.ellipse(8, 22, 4, 4.5, 'R')
    c.poly([(5, 21), (9, 23), (5, 29)], 'R')
    c.bevel(['R'])
    c.ellipse(16, 14, 9.5, 6, 'W')
    c.shade_below(['W'], 'w')
    for x in (11, 15, 19):
        c.rect(x, 13, x + 2, 15, 'R')
    c.outline()


@icon('viber', ['com.viber.Viber', 'viber-desktop', 'Viber'], 'chat', 'Viber')
def viber(c):
    c.rrect(3, 3, 28, 24, 'M', 6)
    c.poly([(8, 23), (13, 23), (8, 28)], 'M')
    c.bevel(['M'])
    g(c, 9, 8, """
        ##.........
        ###........
        ###........
        .##........
        .###.......
        ..###......
        ...####....
        ....#####..
        ......#####
        ........###
    """)
    c.arc(13, 13, 9.5, 8, 280, 360, 'W')
    c.arc(13, 13, 6.5, 5, 280, 360, 'W')
    c.outline()


@icon('facebook', ['facebook-webapp', 'com.facebook.Facebook', 'facebook.com'], 'social', 'Facebook')
def facebook(c):
    disc(c, 'B')
    g(c, 12, 6, """
        ....####
        ...#####
        ..###...
        ..###...
        ########
        ########
        ..###...
        ..###...
        ..###...
        ..###...
        ..###...
        ..###...
        ..###...
        ..###...
        ..###...
        ..###...
    """)
    c.outline()


@icon('bluesky', ['bluesky-webapp', 'bsky', 'xyz.bsky.app', 'bluesky-desktop'], 'social', 'Bluesky')
def bluesky(c):
    # the butterfly
    c.poly([(3, 5), (8, 5), (16, 14), (24, 5), (29, 5), (29, 12), (26, 17), (16, 17), (6, 17), (3, 12)], 'B')
    c.ellipse(9.5, 22, 6, 5.5, 'B')
    c.ellipse(22.5, 22, 6, 5.5, 'B')
    c.poly([(13, 17), (19, 17), (16, 24)], 'B')
    c.bevel(['B'])
    c.vline(16, 15, 22, '6')
    c.pixels([(4, 6), (5, 6), (4, 7)], 'W')
    c.outline()


@icon('threads', ['threads-webapp', 'threads.net', 'com.instagram.barcelona'], 'social', 'Threads')
def threads(c):
    disc(c, 'k')
    g(c, 8, 7, """
        ....######....
        ..###....###..
        .##........##.
        ##...####...##
        ##..##..##..##
        ##..##..##..##
        ##..##..#####.
        ##...####.##..
        .##...........
        ..###....##...
        ....#######...
    """)
    c.outline()


@icon('whalebird', ['social.whalebird.WhalebirdDesktop', 'whalebird-desktop', 'whalebird-bin'], 'social',
      'Whalebird')
def whalebird(c):
    c.ellipse(15, 18, 12, 8, 'B')
    c.poly([(24, 16), (28, 8), (29, 13), (27, 18)], 'B')
    c.poly([(25, 13), (28, 6), (24, 9)], 'B')
    c.bevel(['B'])
    c.ellipse(14, 22, 9, 3.5, 'c')
    c.rect(8, 15, 9, 16, 'K')
    # water spout
    c.vline(11, 5, 9, 'C'); c.pixels([(9, 4), (10, 5), (12, 5), (13, 4)], 'C')
    c.outline()


@icon('org.kde.tokodon', ['tokodon'], 'social', 'Tokodon')
def tokodon(c):
    # little mastodon: head, trunk, ears
    c.ellipse(16, 13, 10, 9, 'M')
    c.ellipse(6.5, 13, 3.5, 6, '7')
    c.ellipse(25.5, 13, 3.5, 6, '7')
    c.rrect(13, 17, 19, 28, 'M', 2)
    c.bevel(['M', '7'])
    c.rect(11, 11, 12, 12, 'K'); c.rect(20, 11, 21, 12, 'K')
    c.pixels([(9, 19), (10, 20), (22, 19), (21, 20)], 'W')
    c.outline()


@icon('pinterest', ['pinterest-webapp', 'com.pinterest', 'pinterest.com'], 'social', 'Pinterest')
def pinterest(c):
    disc(c, 'R')
    g(c, 10, 6, """
        ..#######..
        .#########.
        ###.....###
        ###.....###
        ###.....###
        ###.....###
        .####..###.
        ..########.
        ..#######..
        .###.......
        .###.......
        .##........
        ###........
        ##.........
    """)
    c.outline()


@icon('tiktok', ['douyin-desktop', 'com.bytedance.douyin', 'tiktok-webapp', 'com.zhiliaoapp.musically', 'douyin', 'tiktok.com'], 'social', 'TikTok')
def tiktok(c):
    def note(dx, dy, col):
        c.rect(13 + dx, 4 + dy, 16 + dx, 21 + dy, col)
        c.poly([(16 + dx, 4 + dy), (19 + dx, 7.5 + dy), (24 + dx, 8 + dy), (24 + dx, 12.5 + dy), (19 + dx, 11.5 + dy),
                (16 + dx, 9.5 + dy)], col)
        c.ring(10.5 + dx, 21 + dy, 6.5, 2.5, col)
    note(-1, -1, 'C')
    note(1, 1, 'R')
    note(0, 0, 'k')
    c.outline()


@icon('snapchat', ['snapchat-webapp', 'com.snapchat', 'snapchat.com'], 'social', 'Snapchat')
def snapchat(c):
    c.ellipse(16, 13, 9, 9, 'Y')
    c.poly([(7, 13), (25, 13), (26, 21), (29, 24), (24, 26), (20, 28), (16, 26), (12, 28), (8, 26), (3, 24),
            (6, 21)], 'Y')
    c.bevel(['Y'])
    c.rect(12, 11, 13, 13, 'K'); c.rect(19, 11, 20, 13, 'K')
    c.pixels([(10, 7), (11, 6)], 'W')
    c.outline()


@icon('tumblr', ['tumblr-webapp', 'tumblr.com'], 'social', 'Tumblr')
def tumblr(c):
    c.poly([(11, 3), (17, 3), (17, 9), (24, 9), (24, 15), (17, 15), (17, 21), (19, 23), (24, 22), (24, 28),
            (17, 29), (12, 27), (11, 22), (11, 15), (7, 15), (7, 10), (11, 8)], '6')
    c.bevel(['6'])
    c.outline()


@icon('medium', ['medium-webapp', 'medium.com'], 'social', 'Medium')
def medium(c):
    c.circle(10, 16, 7.5, 'k')
    c.ellipse(21, 16, 3.5, 7, 'k')
    c.ellipse(27, 16, 1.5, 6, 'k')
    c.bevel(['k'])
    c.outline()


@icon('substack', ['substack-webapp', 'substack.com'], 'social', 'Substack')
def substack(c):
    c.rect(6, 3, 26, 5, 'O')
    c.rect(6, 8, 26, 10, 'O')
    c.poly([(6, 13), (27, 13), (27, 29), (16.5, 23), (6, 29)], 'O')
    c.bevel(['O'])
    c.outline()


@icon('quora', ['quora-webapp', 'quora.com'], 'social', 'Quora')
def quora(c):
    disc(c, 'R')
    c.ellipse(15.5, 15, 7, 8.5, 'W')
    c.ellipse(15.5, 15, 3.5, 5.5, 'R')
    c.line(15, 19, 22, 26, 'W', 3)
    c.px(14, 18, 'R'); c.px(14, 19, 'R')
    c.outline()


@icon('stack-overflow', ['stackoverflow', 'stack-overflow-webapp', 'stackoverflow.com'], 'web', 'Stack Overflow')
def stack_overflow(c):
    # tray
    c.rect(4, 16, 6, 27, 'S'); c.rect(24, 16, 26, 27, 'S'); c.rect(4, 25, 26, 27, 'S')
    c.bevel(['S'])
    # stacked bars fanning up
    c.rect(9, 21, 21, 22, 'O')
    c.poly([(9.5, 16.5), (21.5, 18), (21.2, 20), (9.2, 18.5)], 'O')
    c.poly([(10.5, 11), (22, 14.5), (21.5, 16.5), (10, 13)], 'O')
    c.poly([(13, 6), (23.5, 11), (22.5, 13), (12, 8)], 'O')
    c.poly([(17, 2.6), (25, 8.5), (23.5, 10), (15.5, 4)], 'O')
    c.outline()


@icon('product-hunt', ['producthunt', 'product-hunt-webapp', 'producthunt.com'], 'web', 'Product Hunt')
def product_hunt(c):
    disc(c, 'O')
    g(c, 11, 8, """
        #######..
        ########.
        ###...###
        ###...###
        ########.
        #######..
        ###......
        ###......
        ###......
    """)
    c.outline()


@icon('dev-to', ['devto', 'dev.to', 'dev-to-webapp', 'forem'], 'web', 'DEV Community')
def devto(c):
    c.rrect(3, 7, 28, 25, 'k', 2)
    c.bevel(['k'])
    g(c, 6, 11, """
        ###..####.#...#
        #.##.#....#...#
        #..#.#....#...#
        #..#.###..#...#
        #..#.#.....#.#.
        #.##.#.....#.#.
        ###..####...#..
    """)
    c.shift(0, 0)
    c.outline()


@icon('lemmy', ['lemmy-webapp', 'join-lemmy', 'lemmy.ml'], 'social', 'Lemmy')
def lemmy(c):
    # lemming face
    c.ellipse(16, 17, 12, 10, 'W')
    c.ellipse(6.5, 8, 3, 4, 'W')
    c.ellipse(25.5, 8, 3, 4, 'W')
    c.bevel(['W'])
    c.circle(11.5, 15.5, 2, 'K'); c.circle(20.5, 15.5, 2, 'K')
    c.px(11, 14, 'W'); c.px(20, 14, 'W')
    c.hline(14, 18, 21, 'S'); c.rect(15, 22, 17, 23, 'W'); c.vline(16, 22, 23, 'S')
    c.ellipse(6.5, 8.5, 1.5, 2, 'p'); c.ellipse(25.5, 8.5, 1.5, 2, 'p')
    c.outline()


@icon('discourse', ['discourse-webapp'], 'web', 'Discourse')
def discourse(c):
    round_bubble(c, 'k')
    c.arc(16.5, 15, 9, 6, 180, 270, 'Y')
    c.arc(16.5, 15, 9, 6, 270, 360, 'C')
    c.arc(16.5, 15, 9, 6, 0, 90, 'G')
    c.arc(16.5, 15, 9, 6, 90, 180, 'R')
    c.circle(16.5, 15, 6, 'W')
    c.outline()


# ================================================================ voice / video

@icon('jitsi-meet', ['org.jitsi.jitsi-meet', 'jitsi-meet-desktop', 'jitsi'], 'chat', 'Jitsi Meet')
def jitsi(c):
    disc(c, 'B')
    c.rrect(7, 11, 19, 21, 'W', 2)
    c.poly([(19, 15), (25, 11), (25, 21), (19, 17)], 'W')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('linphone', ['org.linphone.desktop', 'linphone-desktop'], 'chat', 'Linphone')
def linphone(c):
    disc(c, 'O')
    g(c, 8, 8, """
        ###...........
        ####..........
        ####..........
        .###..........
        .####.........
        ..####........
        ...#####......
        ....######..##
        ......########
        ........######
        ..........###.
    """)
    c.outline()


@icon('org.kde.kmail2', ['kmail', 'kmail2', 'org.kde.kmail'], 'mail', 'KMail')
def kmail(c):
    c.rrect(3, 7, 28, 25, 'b', 1)
    c.bevel(['b'])
    c.poly([(4, 8), (27, 8), (16, 18)], 'B')
    c.line(4, 24, 13, 15, '6'); c.line(27, 24, 18, 15, '6')
    c.outline()


@icon('org.kde.neochat', ['neochat'], 'chat', 'NeoChat')
def neochat(c):
    round_bubble(c, 'C', tail='right')
    g(c, 10, 8, """
        ..##..##..
        ..##..##..
        ##########
        ##########
        .##..##...
        .##..##...
        ##########
        ##########
        ##..##....
        ##..##....
    """)
    c.outline()


@icon('in.cinny.Cinny', ['cinny', 'cinny-desktop'], 'chat', 'Cinny')
def cinny(c):
    round_bubble(c, 'G')
    c.circle(16.5, 15, 6.5, 'W')
    c.circle(19, 13.5, 5, 'G')
    c.outline()


@icon('sm.puri.Chatty', ['chatty'], 'chat', 'Chatty')
def chatty(c):
    bubble(c, 'G', 3, 4, 28, 22)
    for x in (9, 15, 21):
        c.rect(x, 12, x + 2, 14, 'W')
    c.outline()


@icon('de.schmidhuberj.Flare', ['flare'], 'chat', 'Flare')
def flare(c):
    round_bubble(c, 'B')
    c.poly([(16.5, 5), (21, 13), (19, 13), (22, 21), (16.5, 25), (11, 21), (14, 13), (12, 13)], 'O')
    c.poly([(16.5, 13), (19, 20), (16.5, 23), (14, 20)], 'Y')
    c.outline()


# ================================================================ China / Asia

@icon('wechat', ['wechat-universal', 'wechat-universal-bwrap', 'com.qq.weixin.deepin', 'deepin-wine-wechat', 'wechat-uos-qt', 'wechat-uos-bwrap', 'weixin', 'com.tencent.WeChat', 'wechat-uos', 'wechat-bin', 'wechat-appimage', 'electronic-wechat',
                 'com.qq.weixin', 'weixin'], 'chat', 'WeChat')
def wechat(c):
    c.ellipse(12.5, 12, 9.5, 8.5, 'G')
    c.poly([(5, 16), (9, 19), (4.5, 22)], 'G')
    c.bevel(['G'])
    c.ellipse(20, 19.5, 8, 7.5, 'W')
    c.poly([(24, 24), (27.5, 28.5), (21, 26)], 'W')
    c.bevel(['W'])
    c.rect(8, 9, 9, 10, 'K'); c.rect(14, 9, 15, 10, 'K')
    c.rect(17, 17, 18, 18, 'G'); c.rect(23, 17, 24, 18, 'G')
    c.outline()


@icon('qq', ['com.qq.im', 'com.qq.im.deepin', 'deepin-wine-qq', 'qqnt', 'com.qq.QQ', 'linuxqq', 'linuxqq-nt-bwrap', 'qq-nt', 'tencent-qq'], 'chat', 'QQ')
def qq(c):
    # the penguin
    c.ellipse(16, 18, 9.5, 10, 'k')
    c.ellipse(16, 11, 7.5, 7, 'k')
    c.ellipse(5.5, 20, 2.5, 5, 'k'); c.ellipse(26.5, 20, 2.5, 5, 'k')
    c.bevel(['k'])
    c.ellipse(16, 20, 6.5, 7.5, 'W')
    c.ellipse(13, 9, 2, 2.5, 'W'); c.ellipse(19, 9, 2, 2.5, 'W')
    c.rect(13, 9, 13, 10, 'K'); c.rect(19, 9, 19, 10, 'K')
    c.ellipse(16, 13, 3.5, 1.5, 'Y')
    c.rect(8, 15, 24, 16, 'R'); c.rect(20, 17, 22, 21, 'R')
    c.ellipse(11, 27, 4, 1.5, 'Y'); c.ellipse(21, 27, 4, 1.5, 'Y')
    c.outline()


@icon('dingtalk', ['dingtalk-electron', 'com.dingtalk.DingTalk', 'com.alibabainc.dingtalk', 'dingtalk-bin', 'com.alibaba.dingtalk'], 'chat', 'DingTalk')
def dingtalk(c):
    round_bubble(c, 'B')
    g(c, 7, 7, """
        ##..............
        .######.........
        ..##########....
        ...###########..
        ....###########.
        .....##########.
        ..........####..
        .......######...
        ..........###...
        .........###....
        ........###.....
        ........##......
        .......#........
    """)
    c.outline()


@icon('bytedance-feishu', ['lark-bin', 'com.larksuite.Lark', 'bytedance-lark', 'com.ss.lark', 'feishu-electron', 'lark-global', 'larksuite', 'feishu', 'lark', 'bytedance-feishu-stable', 'com.bytedance.feishu', 'feishu-bin',
                           'larksuite'], 'chat', 'Feishu / Lark')
def feishu(c):
    # the swooping Lark bird: cyan wing, blue body, teal tail
    c.poly([(5, 5), (17, 5), (22, 14), (15, 17)], 'C')
    c.poly([(3, 14), (11, 18), (19, 21), (28, 12), (24, 23), (16, 27), (8, 25)], 'B')
    c.poly([(19, 16), (29, 10), (25, 19)], '6')
    c.bevel(['C', 'B', '6'])
    c.outline()


@icon('wemeet', ['voov-meeting', 'tencent-meeting', 'wemeet-bin', 'com.tencent.wemeet', 'wemeetapp'], 'chat', 'Tencent Meeting')
def wemeet(c):
    c.ring(10.5, 16, 8, 3.5, 'B')
    c.ring(21.5, 16, 8, 3.5, 'C')
    c.arc(10.5, 16, 8, 3.5, 300, 60, 'B')
    c.bevel(['B', 'C'])
    c.outline()


@icon('line', ['line-webapp', 'jp.naver.line', 'line-desktop'], 'chat', 'LINE')
def line_app(c):
    c.ellipse(16, 14, 13, 10.5, 'G')
    c.poly([(16, 23), (21, 23), (13, 29)], 'G')
    c.bevel(['G'])
    g(c, 6, 11, """
        #...#.#...#.####
        #...#.##..#.#...
        #...#.#.#.#.###.
        #...#.#..##.#...
        ###.#.#...#.####
    """)
    c.outline()


@icon('webex', ['cisco-webex', 'webex-bin', 'com.cisco.webex', 'Webex'], 'chat', 'Webex')
def webex(c):
    disc(c, 'k')
    c.arc(16, 16, 10, 6, 150, 330, 'C')
    c.arc(16, 16, 10, 6, 330, 150, 'G')
    c.circle(16, 16, 3, 'W')
    c.outline()


@icon('protonmail-bridge', ['proton-mail-bridge'], 'mail', 'Proton Mail Bridge')
def proton_bridge(c):
    c.rrect(3, 9, 28, 26, 'M', 1)
    c.bevel(['M'])
    c.poly([(4, 10), (27, 10), (16, 19)], 'm')
    c.line(4, 25, 13, 17, '7'); c.line(27, 25, 18, 17, '7')
    c.arc(16, 9, 8, 6, 180, 360, 'S')
    c.rect(7, 7, 9, 9, 'S'); c.rect(23, 7, 25, 9, 'S')
    c.bevel(['S'])
    c.outline()


@icon('claws-mail', ['org.claws_mail.Claws-Mail', 'claws'], 'mail', 'Claws Mail')
def claws(c):
    c.rrect(3, 11, 25, 27, 'W', 1)
    c.bevel(['W'])
    c.line(4, 12, 14, 20, 'S'); c.line(24, 12, 14, 20, 'S')
    # the claw
    c.poly([(19, 3), (29, 7), (28, 16), (25, 12), (22, 10)], 'R')
    c.poly([(16, 6), (20, 8), (22, 14), (18, 11)], 'R')
    c.bevel(['R'])
    c.outline()


@icon('org.kde.kontact', ['kontact'], 'mail', 'Kontact')
def kontact(c):
    c.rrect(3, 5, 22, 27, 'B', 1)
    c.bevel(['B'])
    c.circle(12.5, 12, 3.5, 'W'); c.ellipse(12.5, 21, 6, 3.5, 'W'); c.rect(6, 21, 19, 24, 'B')
    c.rect(6, 21, 19, 23, 'B'); c.ellipse(12.5, 21.5, 6, 3, 'W'); c.rect(6, 22, 19, 24, 'B')
    c.rrect(17, 14, 28, 24, 'Y', 1)
    c.bevel(['Y'])
    c.line(18, 15, 22, 19, '3'); c.line(27, 15, 23, 19, '3')
    c.outline()


# ================================================================ alternative Discord / Telegram / WhatsApp clients

def paper_plane(c, col='W', dx=0, dy=0):
    c.sprite(7 + dx, 9 + dy, """
        ..............##.
        ...........#####.
        ........########.
        .....######.####.
        ..#######..####..
        #######...#####..
        ..####...######..
        ....##.+#######..
        .....+..#######..
        .....+...#####...
        ...........##....
    """, {'#': col, '+': 'w'})


@icon('legcord', ['app.legcord.Legcord', 'legcord-bin', 'armcord', 'xyz.armcord.ArmCord', 'armcord-bin',
                  'ArmCord'], 'chat', 'Legcord')
def legcord(c):
    round_bubble(c, 'B')
    # power plug
    c.rect(12, 7, 13, 11, 'W'); c.rect(19, 7, 20, 11, 'W')
    c.rrect(10, 11, 22, 19, 'W', 2)
    c.rect(15, 19, 17, 24, 'W')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('so.libdb.dissent', ['dissent', 'gtkcord4', 'xyz.diamondb.gtkcord4'], 'chat', 'Dissent')
def dissent(c):
    round_bubble(c, 'M', tail='right')
    g(c, 11, 8, """
        #######..
        ########.
        ##....###
        ##.....##
        ##.....##
        ##.....##
        ##....###
        ########.
        #######..
    """)
    c.outline()


@icon('app.drey.PaperPlane', ['paper-plane', 'paperplane'], 'chat', 'Paper Plane')
def paperplane(c):
    c.poly([(3, 15), (29, 4), (21, 28), (15, 19)], 'W')
    c.poly([(15, 19), (29, 4), (18, 27)], 'w')
    c.poly([(15, 19), (17, 27), (20, 23)], 'S')
    c.bevel(['W'])
    c.line(15, 19, 28, 5, 'C')
    c.outline()


@icon('io.github.tdesktop_x64.TDesktop', ['64gram', '64gram-desktop', '64gram-desktop-bin'], 'chat', '64Gram')
def gram64(c):
    disc(c, 'B')
    paper_plane(c)
    c.rrect(16, 19, 28, 28, 'O', 1)
    c.text(18, 21, '64', 'W', 3, 1)
    c.outline()


@icon('com.ayugram.desktop', ['ayugram', 'ayugram-desktop', 'ayugram-desktop-bin'], 'chat', 'AyuGram')
def ayugram(c):
    disc(c, 'k')
    paper_plane(c)
    c.replace('w', 'S')
    c.pixels([(8, 7), (9, 6), (10, 6)], 'm')
    c.outline()


@icon('io.github.materialgram.materialgram', ['materialgram', 'materialgram-bin'], 'chat', 'materialgram')
def materialgram(c):
    c.rrect(3, 3, 28, 28, 'G', 6)
    c.bevel(['G'])
    paper_plane(c)
    c.outline()


@icon('com.ktechpit.whatsie', ['whatsie'], 'chat', 'Whatsie')
def whatsie(c):
    round_bubble(c, 'g')
    c.ring(16.5, 15, 8, 5.5, 'W')
    c.circle(16.5, 15, 2.5, 'G')
    c.outline()
