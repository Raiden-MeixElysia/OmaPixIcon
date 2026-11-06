"""Browsers, mail, chat, cloud and web apps."""
from pix import icon


# ================================================================ helpers

def _rot90(c, n=1):
    """Rotate the canvas 90 degrees clockwise n times (about the grid centre)."""
    for _ in range(n % 4):
        c.g = [[c.g[c.n - 1 - x][y] for x in range(c.n)] for y in range(c.n)]
    return c


def _envelope(c, x0, y0, x1, y1, body, fold, r=1):
    """Front of an envelope with a V flap drawn in `fold`."""
    c.rrect(x0, y0, x1, y1, body, r)
    c.bevel([body])
    mx = (x0 + x1) / 2
    depth = (y1 - y0) * 0.6
    c.line(x0 + 1, y0 + 1, int(mx), int(y0 + depth), fold)
    c.line(x1 - 1, y0 + 1, int(mx + .5), int(y0 + depth), fold)


def _fox_globe(c, globe, globe_lt, globe_dk, fox, fox_lt, fox_dk, tip):
    """Firefox-style: a fox curling round a globe, ear poking out top-left."""
    c.ellipse(16, 17, 13, 12, fox)
    # tail tip licking up the right side
    c.arc(16, 17, 13, 6, 280, 10, tip)
    c.circle(17.5, 16, 8.5, globe_dk)
    c.circle(16.5, 15, 7.5, globe)
    # head / snout reaching over the top-left of the globe
    c.poly([(3.5, 14), (6, 8), (11, 5), (19, 5), (16, 7.5), (12, 10), (9, 15)], fox)
    # ear
    c.poly([(5, 11), (5, 3), (11, 7)], fox)
    c.px(15, 6, fox); c.px(16, 6, fox)
    c.bevel([fox, tip])
    c.pixels([(6, 5), (6, 6), (7, 6)], fox_dk)
    # body shade low-left, close to the globe
    c.arc(17.5, 16, 10.5, 8.5, 80, 170, fox_dk)
    c.pixels([(15, 9), (14, 10), (13, 11)], globe_lt)
    c.outline()


# ================================================================ browsers

@icon('firefox', ['org.mozilla.firefox', 'firefox-esr', 'firefox-bin', 'firefox-nightly',
                  'firefox-beta', 'org.mozilla.firefox_nightly', 'mozilla-firefox'], 'web', 'Firefox')
def firefox(c):
    _fox_globe(c, 'M', 'm', '7', 'O', 'o', '2', 'Y')


@icon('firefox-developer-edition', ['firefox-developer', 'firefoxdeveloperedition',
                                    'org.mozilla.firefox.developer', 'firefox-devedition'],
      'web', 'Firefox Developer Edition')
def firefox_dev(c):
    _fox_globe(c, '7', 'm', 'k', 'B', 'b', '6', 'C')


@icon('librewolf', ['io.gitlab.librewolf-community', 'librewolf-bin', 'LibreWolf'], 'web', 'LibreWolf')
def librewolf(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    # paw print
    c.ellipse(16, 20, 6, 5, 'W')
    c.ellipse(9.5, 13.5, 2, 2.5, 'W')
    c.ellipse(13.5, 9.5, 2, 2.5, 'W')
    c.ellipse(18.5, 9.5, 2, 2.5, 'W')
    c.ellipse(22.5, 13.5, 2, 2.5, 'W')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('zen-browser', ['app.zen_browser.zen', 'zen', 'zen-browser-bin', 'zen-twilight'], 'web', 'Zen Browser')
def zen(c):
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'])
    c.ring(16, 16, 10.5, 8.5, 'W')
    c.ring(16, 16, 6.5, 4.5, 'W')
    c.circle(16, 16, 2, 'W')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('brave-browser', ['com.brave.Browser', 'brave', 'brave-desktop', 'brave-browser-beta',
                        'brave-browser-nightly', 'brave-bin'], 'web', 'Brave')
def brave(c):
    c.poly([(3, 9), (8, 3), (12, 4.5), (16, 3), (20, 4.5), (24, 3), (29, 9), (27, 16),
            (24, 23), (16, 29), (8, 23), (5, 16)], 'O')
    c.bevel(['O'])
    # eyes
    c.sprite(7, 11, """
        WWW............WWW
        .WWWW........WWWW.
        ...WW........WW...
    """)
    # nose + muzzle
    c.poly([(11, 16), (21, 16), (16, 22)], 'W')
    c.hline(14, 18, 17, 'w')
    c.vline(16, 22, 24, 'W')
    c.hline(13, 19, 24, 'W')
    c.outline()


@icon('vivaldi', ['vivaldi-stable', 'vivaldi-snapshot', 'com.vivaldi.Vivaldi', 'vivaldi-bin'], 'web', 'Vivaldi')
def vivaldi(c):
    c.poly([(3, 9), (10, 6), (18.5, 21.5), (24, 6), (29, 7), (21, 28), (15, 28)], 'R')
    c.circle(7, 8, 4.5, 'R')
    c.circle(25.5, 8, 3.5, 'R')
    c.bevel(['R'])
    c.px(5, 6, 'W'); c.px(6, 5, 'W')
    c.outline()


@icon('opera', ['com.opera.Opera', 'opera-stable', 'opera-beta', 'opera-developer', 'opera-gx'], 'web', 'Opera')
def opera(c):
    c.ellipse(16, 16, 11, 13, 'R')
    c.ellipse(16, 16, 5, 9.5, '.')
    c.bevel(['R'])
    c.ellipse(16, 16, 6, 10.5, '1')
    c.ellipse(16, 16, 5, 9.5, '.')
    c.outline()


@icon('microsoft-edge', ['com.microsoft.Edge', 'microsoft-edge-stable', 'microsoft-edge-beta',
                         'microsoft-edge-dev', 'msedge'], 'web', 'Microsoft Edge')
def edge(c):
    # the Edge wave: dark-blue crest curling over a teal/green body
    c.circle(16, 16, 13, 'G')
    c.arc(16, 16, 13, 0, 165, 375, 'B')
    # the curl: a light tongue tucked under the crest
    c.ellipse(17.5, 19, 9, 5.5, 'C')
    c.ellipse(19, 18, 7, 3.5, 'c')
    # notch where the wave's lip breaks away on the right
    c.ellipse(28.5, 21.5, 4.5, 2.5, '.')
    c.bevel(['B', 'G', 'C'])
    c.pixels([(8, 7), (9, 6), (10, 6)], 'b')
    c.outline()


@icon('torbrowser', ['torbrowser-launcher', 'org.torproject.torbrowser-launcher', 'tor-browser',
                     'torbrowser-launcher-settings', 'org.torproject.TorBrowser'], 'web', 'Tor Browser')
def torbrowser(c):
    c.ellipse(16, 17.5, 11.5, 10.5, 'M')
    c.poly([(11, 10), (16, 4), (21, 10)], 'M')
    c.bevel(['M'])
    c.ellipse(16, 17.5, 8.5, 7.5, '7')
    c.ellipse(16, 17.5, 7.5, 6.5, 'M')
    c.ellipse(16, 17.5, 5, 4.5, '7')
    c.ellipse(16, 17.5, 4, 3.5, 'M')
    c.ellipse(16, 17.5, 1.5, 1.5, '7')
    c.vline(16, 6, 9, '7')
    # sprout
    c.poly([(16, 5), (10, 2), (13, 2), (17, 4)], 'G')
    c.poly([(16, 5), (20, 2), (23, 2.5), (18, 5)], 'g')
    c.pixels([(10, 9), (9, 10), (8, 11)], 'm')
    c.outline()


@icon('org.gnome.Epiphany', ['epiphany', 'epiphany-browser', 'org.gnome.Epiphany.Devel'], 'web', 'GNOME Web')
def epiphany(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.ellipse(16, 16, 6, 12.5, 'b')
    c.ellipse(16, 16, 5, 11.5, 'B')
    c.vline(15, 4, 28, 'b'); c.vline(16, 4, 28, 'b')
    c.hline(4, 27, 16, 'b')
    c.hline(6, 25, 10, 'b'); c.hline(6, 25, 22, 'b')
    c.circle(10, 10, 2, 'W')
    c.outline()


@icon('qutebrowser', ['org.qutebrowser.qutebrowser'], 'web', 'qutebrowser')
def qutebrowser(c):
    c.circle(15, 14.5, 12, 'B')
    c.bevel(['B'])
    c.ring(14.5, 15, 7, 4, 'W')
    c.rect(19, 9, 21, 27, 'W')
    c.rect(22, 26, 23, 27, 'W')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('floorp', ['one.ablaze.floorp', 'floorp-bin'], 'web', 'Floorp')
def floorp(c):
    c.circle(16, 16, 13, 'B')
    c.arc(16, 16, 13, 0, 200, 340, 'M')
    c.bevel(['B', 'M'])
    c.sprite(11, 7, """
        ...WWWW
        ..WWWWW
        ..WW...
        WWWWWW.
        WWWWWW.
        ..WW...
        ..WW...
        ..WW...
        ..WW...
        ..WW...
        ..WW...
        WWWWWW.
    """)
    c.outline()


@icon('mullvad-browser', ['mullvadbrowser', 'mullvad-browser-bin', 'net.mullvad.MullvadBrowser'], 'web',
      'Mullvad Browser')
def mullvad_browser(c):
    c.circle(16, 16, 13, '6')
    c.bevel(['6'], dark=False)
    c.ellipse(16, 16, 6, 12.5, 'B')
    c.ellipse(16, 16, 5, 11.5, '6')
    c.hline(4, 27, 11, 'B')
    c.vline(15, 4, 11, 'B'); c.vline(16, 4, 11, 'B')
    # the Mullvad mole popping up over the horizon
    c.ellipse(16, 23, 8, 7, 'Y')
    for y in range(32):
        for x in range(32):
            if c.get(x, y) == 'Y' and ((x + .5 - 16) ** 2 + (y + .5 - 16) ** 2) > 169:
                c.px(x, y, '.')
    c.bevel(['Y'], dark=False)
    c.ellipse(16, 22.5, 3, 2, 'y')
    c.rect(15, 21, 16, 22, 'P')
    c.rect(15, 24, 16, 25, 'W')
    c.rect(11, 19, 11, 20, 'K'); c.rect(20, 19, 20, 20, 'K')
    c.outline()


@icon('falkon', ['org.kde.falkon'], 'web', 'Falkon')
def falkon(c):
    c.circle(15, 14, 11, 'B')
    c.poly([(5, 20), (13, 29), (20, 29), (21, 22)], 'B')
    c.poly([(24, 9), (29, 12), (28, 18), (24, 16)], 'Y')
    c.bevel(['B', 'Y'])
    c.ellipse(15, 18, 6, 6, 'W')
    c.poly([(19, 11), (23, 11), (21, 19), (18, 17)], '6')
    c.circle(20.5, 11, 2, 'K')
    c.px(20, 10, 'W')
    c.outline()


@icon('waterfox', ['net.waterfox.waterfox', 'waterfox-g', 'waterfox-bin', 'waterfox-current'], 'web',
      'Waterfox')
def waterfox(c):
    c.poly([(3, 2), (11, 8), (21, 8), (29, 2), (28, 14), (16, 29), (4, 14)], 'B')
    c.bevel(['B'])
    c.poly([(5, 5), (9, 9), (6, 12)], '6')
    c.poly([(27, 5), (23, 9), (26, 12)], '6')
    c.poly([(5, 15), (16, 18), (27, 15), (16, 28)], 'c')
    c.rect(10, 13, 11, 14, 'K'); c.rect(21, 13, 22, 14, 'K')
    c.rect(15, 24, 17, 25, 'K')
    c.outline()


# ================================================================ mail

def _bird_mail(c, bird, bird_lt, bird_dk, tip):
    """Thunderbird-style: a bird wrapping its wings round a letter."""
    c.ellipse(16, 17, 13, 12, bird)
    c.arc(16, 17, 13, 6, 280, 10, tip)
    c.rrect(10, 12, 25, 23, 'W', 1)
    c.hline(10, 25, 23, 'w')
    c.line(11, 13, 17, 18, 'S'); c.line(24, 13, 18, 18, 'S')
    # head with crest feathers over the top-left
    c.poly([(3.5, 14), (6, 8), (11, 5), (19, 5), (16, 8), (12, 10.5), (9, 15)], bird)
    c.poly([(5, 11), (3, 3), (11, 6)], bird)
    c.bevel([bird, tip])
    c.arc(17, 17, 11, 9, 80, 170, bird_dk)
    c.px(9, 9, 'K')
    c.outline()


@icon('thunderbird', ['org.mozilla.Thunderbird', 'net.thunderbird.Thunderbird', 'org.mozilla.thunderbird',
                      'thunderbird-esr', 'thunderbird-bin', 'mozilla-thunderbird', 'thunderbird-beta'],
      'chat', 'Thunderbird')
def thunderbird(c):
    _bird_mail(c, 'B', 'b', '6', 'C')


@icon('betterbird', ['eu.betterbird.Betterbird', 'betterbird-bin'], 'chat', 'Betterbird')
def betterbird(c):
    _bird_mail(c, 'G', 'g', '4', 'Y')


@icon('org.gnome.Evolution', ['evolution', 'evolution-mail', 'evolution-calendar'], 'chat', 'Evolution')
def evolution(c):
    # calendar card behind, envelope in front
    c.rrect(13, 3, 28, 19, 'W', 1)
    c.rect(13, 3, 28, 7, 'R')
    c.rrect(13, 3, 28, 7, 'R', 1)
    c.bevel(['R'])
    c.sprite(16, 9, """
        #.#.#.#.#
        .........
        #.#.#.#.#
    """, {'#': 'S'})
    c.rrect(3, 12, 22, 27, 'Y', 1)
    c.bevel(['Y'])
    c.line(4, 13, 12, 20, '3'); c.line(21, 13, 13, 20, '3')
    c.outline()


@icon('org.gnome.Geary', ['geary'], 'chat', 'Geary')
def geary(c):
    # envelope with its flap open, letter peeking out
    c.poly([(3, 12), (16, 2.5), (29, 12)], '6')
    c.rect(7, 6, 25, 16, 'W')
    c.hline(10, 22, 9, 'S'); c.hline(10, 19, 12, 'S')
    c.rrect(3, 12, 28, 28, 'B', 1)
    c.bevel(['B'])
    c.poly([(3.5, 12.5), (16, 22), (28.5, 12.5), (28.5, 13.5), (16, 23.5), (3.5, 13.5)], 'b')
    c.outline()


@icon('mailspring', ['com.getmailspring.Mailspring', 'Mailspring'], 'chat', 'Mailspring')
def mailspring(c):
    # envelope whose fold springs up into an "M"
    c.rrect(3, 7, 28, 25, 'C', 2)
    c.bevel(['C'])
    c.sprite(6, 10, """
        WW..............WW
        WWW............WWW
        WWWW..........WWWW
        WW.WW........WW.WW
        WW..WW......WW..WW
        WW...WW....WW...WW
        WW....WW..WW....WW
        WW.....WWWW.....WW
        WW......WW......WW
        WW..............WW
        WW..............WW
    """)
    c.shade_below(['W'], 'w')
    c.outline()


@icon('proton-mail', ['ch.protonmail.protonmail-bridge', 'proton-mail-bin', 'protonmail',
                      'me.proton.Mail', 'proton-mail-desktop', 'protonmail-desktop'], 'chat', 'Proton Mail')
def proton_mail(c):
    c.rrect(3, 7, 28, 25, 'M', 2)
    c.bevel(['M'])
    c.poly([(3, 9), (16, 19), (29, 9), (29, 12), (16, 22), (3, 12)], 'm')
    c.poly([(3, 12), (16, 22), (3, 26)], '7')
    c.poly([(3, 11), (16, 21), (16, 22), (3, 12)], 'm')
    c.outline()


@icon('gmail', ['gmail-webapp', 'com.google.mail', 'google-gmail', 'mail.google.com'], 'chat', 'Gmail')
def gmail(c):
    c.rect(3, 7, 28, 25, 'W')
    c.hline(4, 27, 25, 'w')
    # the coloured M: blue / green legs, red fold, yellow corner
    c.rect(3, 9, 7, 25, 'B')
    c.rect(24, 9, 28, 25, 'G')
    c.poly([(3, 7), (8, 7), (16, 14), (24, 7), (29, 7), (29, 11), (16, 21), (3, 11)], 'R')
    c.poly([(24, 7), (29, 7), (29, 11), (24, 15)], 'Y')
    c.poly([(3, 7), (8, 7), (8, 15), (3, 11)], '1')
    c.bevel(['B', 'G'])
    c.px(3, 7, '.'); c.px(28, 7, '.')
    c.outline()


@icon('fastmail', ['com.fastmail.Fastmail', 'fastmail-desktop'], 'chat', 'Fastmail')
def fastmail(c):
    _envelope(c, 9, 7, 28, 25, 'B', '6', 2)
    c.poly([(10, 8), (18.5, 17), (27, 8)], 'O')
    c.bevel(['O'], dark=False)
    # speed streaks
    c.rect(4, 11, 7, 12, 'b')
    c.rect(5, 15, 7, 16, 'b')
    c.rect(3, 19, 7, 20, 'b')
    c.outline()


# ================================================================ chat

@icon('telegram', ['org.telegram.desktop', 'telegram-desktop', 'telegramdesktop', 'Telegram',
                   'telegram-desktop-bin', 'io.github.kotatogram', 'kotatogram'], 'chat', 'Telegram')
def telegram(c):
    c.circle(16, 16, 13, 'C')
    c.bevel(['C'])
    c.sprite(7, 9, """
        ..............WW.
        ...........WWWWW.
        ........WWWWWWWW.
        .....WWWWWW.WWWW.
        ..WWWWWWW..WWWW..
        WWWWWWW...WWWWW..
        ..WWWW...WWWWWW..
        ....WW.wWWWWWWW..
        .....w..WWWWWWW..
        .....w...WWWWW...
        ...........WW....
    """)
    c.outline()


@icon('slack', ['com.slack.Slack', 'slack-desktop', 'Slack', 'slack-electron'], 'chat', 'Slack')
def slack(c):
    # draw the top-left piece, rotate, repeat: TL cyan, TR green, BR yellow, BL red
    for col in ['C', 'R', 'Y', 'G']:
        c.rrect(3, 9, 14, 14, col, 2)
        c.rrect(9, 3, 14, 7, col, 2)
        _rot90(c, 1)
    c.bevel(['C', 'G', 'Y', 'R'], dark=False)
    c.outline()


@icon('element', ['im.riot.Riot', 'element-desktop', 'io.element.Element', 'riot', 'riot-desktop',
                  'element-desktop-nightly'], 'chat', 'Element')
def element(c):
    c.circle(16, 16, 13, 'G')
    c.bevel(['G'])
    for _ in range(4):
        c.arc(14, 18, 8, 5, 180, 268, 'W')
        _rot90(c, 1)
    c.outline()


@icon('teams', ['teams-for-linux', 'com.github.IsmaelMartinez.teams_for_linux', 'microsoft-teams',
                'teams-insiders', 'com.microsoft.Teams'], 'chat', 'Microsoft Teams')
def teams(c):
    c.circle(23.5, 7.5, 3.5, 'm')
    c.rrect(18, 12, 28, 25, 'm', 3)
    c.circle(15, 6, 3.5, 'M')
    c.rrect(9, 11, 23, 27, 'M', 3)
    c.bevel(['m', 'M'])
    c.rrect(3, 9, 18, 24, '7', 1)
    c.bevel(['7'], dark=False)
    c.sprite(6, 12, """
        WWWWWWWWWW
        WWWWWWWWWW
        ....WW....
        ....WW....
        ....WW....
        ....WW....
        ....WW....
        ....WW....
    """)
    c.outline()


@icon('skype', ['com.skype.Client', 'skypeforlinux', 'skype-desktop'], 'chat', 'Skype')
def skype(c):
    c.circle(16, 16, 12, 'C')
    c.circle(8.5, 8.5, 5.5, 'C')
    c.circle(23.5, 23.5, 5.5, 'C')
    c.bevel(['C'])
    c.sprite(10, 8, """
        ..WWWWWW..
        .WWWWWWWW.
        WWW....WW.
        WWW.......
        .WWWWWW...
        ..WWWWWWW.
        .......WWW
        .WW....WWW
        .WWWWWWWW.
        ..WWWWWW..
    """)
    c.shade_below(['W'], 'w')
    c.outline()


@icon('zulip', ['org.zulip.Zulip', 'zulip-desktop'], 'chat', 'Zulip')
def zulip(c):
    c.circle(16, 16, 13, 'C')
    c.ellipse(16, 16, 13, 13, 'C')
    for y in range(3, 16):
        for x in range(32):
            if c.get(x, y) == 'C':
                c.px(x, y, 'G')
    c.bevel(['C', 'G'])
    c.sprite(8, 8, """
        WWWWWWWWWWWWWWW.
        WWWWWWWWWWWWWW..
        .........WWWW...
        ........WWWW....
        .......WWWW.....
        ......WWWW......
        .....WWWW.......
        ....WWWW........
        ...WWWWWWWWWWWWW
        ..WWWWWWWWWWWWWW
    """)
    c.shade_below(['W'], 'w')
    c.outline()


@icon('mattermost', ['com.mattermost.Desktop', 'mattermost-desktop', 'Mattermost'], 'chat', 'Mattermost')
def mattermost(c):
    c.ring(16, 16, 13, 9, 'B')
    c.arc(16, 16, 14, 8, 285, 330, '.')
    c.circle(15.5, 17, 7, 'B')
    c.poly([(16, 10), (21.5, 4.5), (22.5, 15)], 'B')
    c.bevel(['B'])
    c.outline()


@icon('fractal', ['org.gnome.Fractal', 'org.gnome.Fractal.Devel'], 'chat', 'Fractal')
def fractal(c):
    c.rrect(3, 4, 28, 23, 'B', 4)
    c.poly([(8, 22), (8, 29), (15, 22)], 'B')
    c.bevel(['B'])
    # Sierpinski triangle
    c.sprite(8, 7, """
        .......WW.......
        ......WWWW......
        .....WW..WW.....
        ....WWWWWWWW....
        ...WW......WW...
        ..WWWW....WWWW..
        .WW..WW..WW..WW.
        WWWWWWWWWWWWWWWW
    """)
    c.outline()


@icon('dino', ['im.dino.Dino', 'dino-im'], 'chat', 'Dino')
def dino(c):
    # friendly dino head in a speech-bubble pose
    c.sprite(3, 3, """
        ...........#########......
        .........#############....
        ........################..
        ........#################.
        ........#################.
        ........##################
        ........##################
        ........##################
        ........#################.
        ........#########.........
        ........########..........
        ........##########........
        .......#######............
        ......########............
        .....#########............
        ....##########............
        ...###########............
        ..############............
        ..############............
        .#############............
        .##############...........
        ##############............
        #############.............
        ##########................
        ########..................
        #######...................
    """, {'#': 'G'})
    c.bevel(['G'])
    c.rect(15, 5, 16, 6, 'K')
    c.px(15, 5, 'W')
    c.hline(16, 23, 11, '4')
    c.pixels([(22, 7), (24, 7)], '4')
    c.sprite(16, 12, "W.W.W", None)
    c.outline()


@icon('vesktop', ['dev.vencord.Vesktop', 'vesktop-bin', 'vencord', 'vencord-desktop'], 'chat', 'Vesktop')
def vesktop(c):
    # a pink chat blob with a big V
    c.ellipse(16, 15, 13, 11.5, 'P')
    c.poly([(19, 22), (26, 29), (24, 21)], 'P')
    c.bevel(['P'])
    c.sprite(7, 8, """
        WWW............WWW
        .WWW..........WWW.
        .WWW..........WWW.
        ..WWW........WWW..
        ...WWW......WWW...
        ...WWW......WWW...
        ....WWW....WWW....
        .....WWW..WWW.....
        .....WWWWWWWW.....
        ......WWWWWW......
        .......WWWW.......
    """)
    c.shade_below(['W'], 'p')
    c.outline()


@icon('webcord', ['io.github.spacingbat3.webcord', 'webcord-bin'], 'chat', 'WebCord')
def webcord(c):
    # a globe on a cord
    c.circle(14, 14, 11, 'C')
    c.bevel(['C'])
    c.ellipse(14, 14, 5, 10.5, 'c')
    c.ellipse(14, 14, 4, 9.5, 'C')
    c.hline(4, 24, 14, 'c')
    c.vline(13, 4, 24, 'c')
    # cord and plug
    c.line(21, 22, 24, 25, 'k', 2)
    c.rrect(23, 24, 28, 28, 'S', 1)
    c.outline()


@icon('caprine', ['com.sindresorhus.Caprine', 'messenger', 'facebook-messenger', 'caprine-bin',
                  'com.facebook.Messenger'], 'chat', 'Caprine')
def caprine(c):
    c.ellipse(16, 15, 13, 12, 'B')
    c.poly([(5, 21), (5, 29), (12, 25)], 'B')
    for y in range(32):
        for x in range(32):
            if c.get(x, y) == 'B' and x - y > 2:
                c.px(x, y, 'M')
    c.bevel(['B', 'M'])
    c.sprite(6, 10, """
        ........WW..........
        .......WWWW......WW.
        ......WWWWWW....WWW.
        .....WWWWWWWW..WWW..
        ....WWW....WWWWWW...
        ...WWW......WWWW....
        ..WWW...............
        .WW.................
    """)
    c.outline()


@icon('ferdium', ['org.ferdium.Ferdium', 'ferdium-bin', 'ferdi', 'com.getferdi.Ferdi', 'franz',
                  'com.meetfranz.Franz'], 'chat', 'Ferdium')
def ferdium(c):
    # a stack of chat bubbles from different services
    c.rrect(9, 3, 28, 15, 'C', 3)
    c.poly([(23, 14), (27, 19), (19, 14)], 'C')
    c.rrect(3, 11, 22, 24, 'M', 3)
    c.poly([(7, 23), (5, 29), (12, 23)], 'M')
    c.bevel(['C', 'M'])
    c.sprite(7, 15, """
        WWWWWWWWWWW
        ...........
        WWWWWWW....
    """)
    c.outline()


@icon('beeper', ['com.automattic.beeper.desktop', 'beeper-desktop', 'Beeper', 'beepertexts'], 'chat', 'Beeper')
def beeper(c):
    # a chunky pager
    c.rrect(3, 7, 28, 26, 'M', 3)
    c.rect(22, 4, 25, 7, '7')
    c.bevel(['M'])
    c.rect(6, 10, 25, 17, 'K')
    c.rect(7, 11, 24, 16, 'g')
    c.text(8, 12, 'HI', '4', font=3)
    c.pixels([(19, 13), (20, 13), (21, 13), (22, 13), (19, 15), (20, 15)], '4')
    c.rrect(6, 20, 10, 23, 'm', 1)
    c.rrect(13, 20, 18, 23, 'm', 1)
    c.rrect(21, 20, 25, 23, 'm', 1)
    c.shade_below(['m'], '7')
    c.outline()


@icon('nheko', ['io.github.NhekoReborn.Nheko', 'nheko-git'], 'chat', 'Nheko')
def nheko(c):
    # cat head
    c.ellipse(16, 18, 13, 10, 'B')
    c.poly([(3.5, 15), (4, 3), (13, 9)], 'B')
    c.poly([(28.5, 15), (28, 3), (19, 9)], 'B')
    c.bevel(['B'])
    c.poly([(5.5, 11), (6, 6), (10, 9)], 'b')
    c.poly([(26.5, 11), (26, 6), (22, 9)], 'b')
    c.ellipse(16, 22.5, 7, 5, 'W')
    c.rect(10, 15, 11, 18, 'K'); c.rect(20, 15, 21, 18, 'K')
    c.px(10, 15, 'W'); c.px(20, 15, 'W')
    c.rect(15, 20, 16, 21, 'P')
    c.pixels([(14, 23), (15, 22), (16, 22), (17, 23)], 'S')
    c.outline()


@icon('tuba', ['dev.geopjr.Tuba', 'mastodon', 'org.joinmastodon.Mastodon', 'tootle',
               'com.github.bleakgrey.tootle'], 'chat', 'Tuba')
def tuba(c):
    # a brass tuba, bell up
    c.ellipse(15, 5.5, 10, 3.5, 'Y')
    c.poly([(5, 5), (25, 5), (18, 12), (12, 12)], 'Y')
    c.rect(12, 11, 18, 24, 'Y')
    c.ellipse(15, 24, 6, 4.5, 'Y')
    c.ring(21, 19, 7.5, 4.5, 'Y')
    c.bevel(['Y'])
    c.ellipse(15, 5, 8, 2, '3')
    c.ellipse(15, 5.5, 7, 1.5, '8')
    # valves
    for x in (19, 22, 25):
        c.rect(x, 9, x + 1, 12, 'w')
        c.hline(x, x + 1, 8, 'W')
    # lead pipe + mouthpiece
    c.rect(7, 16, 11, 17, 'y')
    c.rect(5, 14, 6, 17, 'S')
    c.outline()


@icon('revolt', ['chat.revolt.RevoltDesktop', 'revolt-desktop', 'revolt-desktop-bin', 'stoat'], 'chat', 'Revolt')
def revolt(c):
    c.rrect(3, 4, 28, 23, 'R', 4)
    c.poly([(21, 22), (25, 29), (14, 22)], 'R')
    c.bevel(['R'])
    c.sprite(10, 8, """
        WWWWWWWWW..
        WWWWWWWWWW.
        WWW.....WWW
        WWW.....WWW
        WWWWWWWWWW.
        WWWWWWWWW..
        WWW...WWW..
        WWW....WWW.
        WWW.....WWW
    """)
    c.shade_below(['W'], 'w')
    c.outline()


# ================================================================ google & productivity

@icon('google-calendar', ['google-calendar-webapp', 'com.google.calendar', 'calendar.google.com'], 'web',
      'Google Calendar')
def google_calendar(c):
    c.rect(3, 5, 28, 28, 'W')
    c.rect(3, 5, 28, 10, 'B')
    c.bevel(['B'], dark=False)
    c.hline(4, 27, 28, 'w')
    c.vline(28, 10, 28, 'w')
    c.sprite(6, 13, """
        BBBBBBB....BBBB.
        BBBBBBBB..BBBBB.
        .....BBB....BBB.
        .....BBB....BBB.
        ...BBBB.....BBB.
        ...BBBBB....BBB.
        ......BBB...BBB.
        ......BBB...BBB.
        BBBBBBBBB...BBB.
        BBBBBBB....BBBBB
    """)
    c.pixels([(9, 3), (9, 4), (22, 3), (22, 4)], 'S')
    c.outline()


@icon('google-drive', ['google-drive-webapp', 'com.google.drive', 'drive.google.com', 'insync'], 'web',
      'Google Drive')
def google_drive(c):
    c.poly([(11, 4), (20, 4), (8.5, 25), (3, 20)], 'G')
    c.poly([(12, 4), (20, 4), (29, 20), (21, 20)], 'Y')
    c.poly([(9, 20), (29, 20), (24, 27), (4, 27)], 'B')
    c.bevel(['G', 'Y', 'B'], dark=False)
    c.outline()


@icon('google-docs', ['google-docs-webapp', 'com.google.docs', 'docs.google.com'], 'web', 'Google Docs')
def google_docs(c):
    c.poly([(5, 3), (20, 3), (27, 10), (27, 29), (5, 29)], 'B')
    c.bevel(['B'])
    c.poly([(19, 3), (27, 11), (19, 11)], 'b')
    for y, w in ((14, 13), (17, 13), (20, 13), (23, 9)):
        c.rect(9, y, 9 + w - 1, y + 1, 'W')
    c.outline()


@icon('google-sheets', ['google-sheets-webapp', 'com.google.sheets', 'sheets.google.com'], 'web',
      'Google Sheets')
def google_sheets(c):
    c.poly([(5, 3), (20, 3), (27, 10), (27, 29), (5, 29)], 'G')
    c.bevel(['G'])
    c.poly([(19, 3), (27, 11), (19, 11)], 'g')
    c.rect(9, 13, 22, 25, 'W')
    c.rect(10, 16, 14, 18, 'G'); c.rect(16, 16, 21, 18, 'G')
    c.rect(10, 20, 14, 21, 'G'); c.rect(16, 20, 21, 21, 'G')
    c.rect(10, 23, 14, 24, 'G'); c.rect(16, 23, 21, 24, 'G')
    c.outline()


@icon('google-meet', ['google-meet-webapp', 'com.google.meet', 'meet.google.com'], 'web', 'Google Meet')
def google_meet(c):
    c.rrect(3, 7, 21, 25, 'G', 1)
    c.poly([(3, 7), (21.5, 7), (21.5, 12), (3, 12)], 'Y')
    c.rect(3, 12, 7, 25, 'B')
    c.rect(3, 7, 7, 11, 'R')
    c.px(3, 7, '.')
    c.poly([(21, 13), (29, 7.5), (29, 24.5), (21, 19)], '4')
    c.bevel(['G', 'Y', 'B', '4'], dark=False)
    c.outline()


@icon('notion', ['notion-app', 'notion-app-enhanced', 'notion-desktop', 'com.notion.Notion', 'notion-app-electron',
                 'notion-snap-reborn'], 'web', 'Notion')
def notion(c):
    c.poly([(3, 6), (22, 3), (29, 8), (29, 27), (9, 29), (3, 24)], 'W')
    c.shade_below(['W'], 'w')
    c.sprite(9, 9, """
        KKKKK.....KKKK
        .KKKK......KK.
        .KKKKK.....KK.
        .KK.KKK....KK.
        .KK..KKK...KK.
        .KK...KKK..KK.
        .KK....KKK.KK.
        .KK.....KKKKK.
        .KK......KKKK.
        KKKK......KKK.
    """, {'K': 'k'})
    c.outline()


@icon('linear', ['linear-app', 'linear-desktop', 'linear-linux', 'app.linear.Linear'], 'web', 'Linear')
def linear(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    for y in range(32):
        for x in range(32):
            d = y - x
            if c.get(x, y) != '.' and d in (4, 5, 10, 11, 16, 17):
                c.px(x, y, '.')
    c.outline()


@icon('trello', ['trello-desktop', 'com.atlassian.Trello', 'trello-webapp'], 'web', 'Trello')
def trello(c):
    c.rrect(3, 3, 28, 28, 'B', 3)
    c.bevel(['B'])
    c.rrect(7, 7, 14, 24, 'W', 1)
    c.rrect(18, 7, 25, 17, 'W', 1)
    c.shade_below(['W'], 'w')
    c.outline()


@icon('gitlab', ['gitlab-webapp', 'com.gitlab.GitLab', 'gitlab-desktop', 'glab'], 'web', 'GitLab')
def gitlab(c):
    c.poly([(3, 14), (7, 3), (11, 14), (21, 14), (25, 3), (29, 14), (28, 19), (16, 28.5), (4, 19)], 'O')
    c.poly([(11, 14), (21, 14), (16, 28.5)], 'R')
    c.poly([(3.5, 15), (10.5, 15), (4.5, 19)], 'Y')
    c.poly([(28.5, 15), (21.5, 15), (27.5, 19)], 'Y')
    c.bevel(['O'], dark=False)
    c.outline()



# ================================================================ AI

@icon('claude', ['claude-desktop', 'com.anthropic.claude', 'claude-desktop-bin', 'claude-ai', 'claude-code',
                 'io.github.aaddrick.claude-desktop'], 'web', 'Claude')
def claude(c):
    import math
    # the Claude spark: uneven rays bursting from a solid core
    rays = [(0, 13), (32, 11), (62, 13), (95, 11.5), (125, 13), (152, 11), (184, 13),
            (212, 11.5), (243, 13), (272, 12), (302, 13), (332, 11)]
    for a, ln in rays:
        r = math.radians(a)
        dx, dy = math.cos(r), math.sin(r)
        px_, py_ = -dy, dx
        w0, w1 = 2.2, 1.1
        c.poly([(16 + px_ * w0, 16 + py_ * w0), (16 + dx * ln + px_ * w1, 16 + dy * ln + py_ * w1),
                (16 + dx * ln - px_ * w1, 16 + dy * ln - py_ * w1), (16 - px_ * w0, 16 - py_ * w0)], 'O')
    c.circle(16, 16, 4.5, 'O')
    c.bevel(['O'])
    c.outline()


@icon('gemini', ['google-gemini', 'gemini-webapp', 'gemini-desktop', 'com.google.gemini'], 'web', 'Gemini')
def gemini(c):
    # four-point sparkle with concave sides, blue fading to violet
    for y in range(32):
        for x in range(32):
            dx, dy = abs(x + .5 - 16) / 16.5, abs(y + .5 - 16) / 16.5
            if dx ** .6 + dy ** .6 <= 1:
                c.px(x, y, 'B' if x + y < 31 else 'M')
    c.bevel(['B', 'M'])
    c.pixels([(15, 9), (15, 10), (14, 12)], 'W')
    c.outline()


@icon('perplexity', ['perplexity-ai', 'perplexity-webapp', 'ai.perplexity.Perplexity'], 'web', 'Perplexity')
def perplexity(c):
    # the geometric book/asterisk mark, teal strokes on a dark body
    c.poly([(4, 3), (16, 10), (28, 3), (28, 11), (29, 11), (29, 20), (26, 20), (26, 28), (16, 21.5),
            (6, 28), (6, 20), (3, 20), (3, 11), (4, 11)], 'k')
    C = 'C'
    c.line(5, 5, 15, 11, C); c.line(26, 5, 16, 11, C)
    c.vline(5, 5, 11, C); c.vline(26, 5, 11, C)
    c.hline(4, 27, 11, C); c.hline(4, 27, 19, C)
    c.vline(4, 11, 19, C); c.vline(27, 11, 19, C)
    c.vline(15, 4, 27, C); c.vline(16, 4, 27, C)
    c.vline(7, 19, 26, C); c.vline(24, 19, 26, C)
    c.line(7, 26, 15, 20, C); c.line(24, 26, 16, 20, C)
    c.outline()


@icon('deepseek', ['deepseek-harness', 'deepseek-chat', 'deepseek-harness-desktop', 'deepseek-desktop', 'deepseek-webapp', 'com.deepseek.chat'], 'web', 'DeepSeek')
def deepseek(c):
    # the DeepSeek whale, tail flicked up
    c.ellipse(13, 18, 10.5, 8, 'B')
    c.poly([(18, 13), (25, 9), (27, 4), (29, 7), (28, 13), (23, 21)], 'B')
    c.poly([(26, 6), (23, 3), (27, 3.5)], 'B')
    c.bevel(['B'])
    c.ellipse(11, 22.5, 7, 3.5, 'b')
    c.ellipse(11, 21, 7, 2.5, 'B')
    c.rect(7, 16, 8, 17, 'W')
    c.outline()


@icon('copilot', ['microsoft-copilot', 'copilot-desktop', 'copilot-webapp', 'com.microsoft.Copilot'], 'web',
      'Copilot')
def copilot(c):
    # two interlocking ribbon halves split by an S-shaped seam
    c.rrect(3, 4, 28, 27, 'C', 6)
    for y in range(32):
        for x in range(32):
            if c.get(x, y) != '.':
                seam = 16 + 5 * __import__('math').sin((x - 3) / 25 * 6.283)
                if y > seam + 1:
                    c.px(x, y, 'M' if x > 9 else 'O')
                elif y >= seam:
                    c.px(x, y, '.')
                elif x > 21:
                    c.px(x, y, 'G')
    c.bevel(['C', 'M', 'O', 'G'], dark=False)
    c.outline()



# ================================================================ cloud & VPN

def _cloud(c, col, dy=0):
    c.circle(10, 19 + dy, 6.5, col)
    c.circle(17, 13 + dy, 8.5, col)
    c.circle(23.5, 18 + dy, 6, col)
    c.rrect(4, 18 + dy, 28, 25 + dy, col, 3)


@icon('nextcloud', ['com.nextcloud.desktopclient.nextcloud', 'Nextcloud', 'nextcloud-client',
                    'nextcloud-desktop'], 'web', 'Nextcloud')
def nextcloud(c):
    _cloud(c, 'B', 1)
    c.bevel(['B'])
    c.ring(16, 18, 5, 2.5, 'W')
    c.ring(8, 19, 3, 1.2, 'W')
    c.ring(24, 19, 3, 1.2, 'W')
    c.outline()


@icon('syncthing', ['syncthing-gtk', 'syncthingtray', 'me.kozec.syncthingtk', 'syncthing-ui',
                    'io.github.martchus.syncthingtray', 'com.github.zocker_160.SyncThingy'], 'web', 'Syncthing')
def syncthing(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.ring(16, 16, 9.5, 8, 'W')
    c.arc(16, 16, 9.5, 8, 200, 240, 'B')
    nodes = [(23, 9), (24, 22), (8, 14)]
    hub = (15, 17)
    for x, y in nodes:
        c.line(hub[0], hub[1], x, y, 'W')
    for x, y in nodes + [hub]:
        c.circle(x + .5, y + .5, 2.2, 'W')
    c.outline()


@icon('onedrive', ['com.microsoft.OneDrive', 'onedrive-gui', 'onedrivegui', 'io.github.bpozdena.OneDriveGUI',
                   'microsoft-onedrive', 'abraunegg-onedrive'], 'web', 'OneDrive')
def onedrive(c):
    c.circle(12, 13, 7, '6')
    c.circle(6.5, 17, 4, '6')
    c.rrect(3, 14, 16, 20, '6', 3)
    c.bevel(['6'], dark=False)
    c.circle(19, 15, 7.5, 'B')
    c.circle(12.5, 21, 4.5, 'B')
    c.circle(25, 20.5, 4, 'B')
    c.rrect(9, 20, 28, 25, 'B', 2)
    c.bevel(['B'])
    c.outline()


@icon('proton-vpn', ['protonvpn-app', 'proton-vpn-gtk-app', 'protonvpn', 'com.protonvpn.www', 'proton-vpn-gtk',
                     'protonvpn-gui', 'proton-vpn-app'], 'web', 'Proton VPN')
def proton_vpn(c):
    c.poly([(3, 4), (29, 4), (16, 28.5)], 'M')
    c.bevel(['M'])
    c.poly([(9, 8), (23, 8), (16, 21)], 'G')
    c.poly([(9, 8), (16, 8), (14, 14)], 'g')
    c.outline()


@icon('mullvad-vpn', ['net.mullvad.MullvadVPN', 'mullvad-vpn-bin', 'mullvad', 'mullvad-gui'], 'web', 'Mullvad VPN')
def mullvad_vpn(c):
    # mole face on a shield
    c.poly([(4, 4), (16, 2.5), (28, 4), (28, 15), (24, 23), (16, 29), (8, 23), (4, 15)], '6')
    c.bevel(['6'], dark=False)
    c.ellipse(16, 15.5, 9.5, 9, 'Y')
    c.bevel(['Y'], dark=False)
    c.ellipse(16, 19.5, 4, 3, 'y')
    c.rect(15, 17, 16, 18, 'P')
    c.rect(15, 21, 16, 22, 'W')
    c.rect(11, 13, 11, 14, 'K'); c.rect(20, 13, 20, 14, 'K')
    c.pixels([(10, 23), (12, 24), (14, 24), (17, 24), (19, 24), (21, 23)], '3')
    c.outline()


# ================================================================ social & streaming

@icon('reddit', ['reddit-webapp', 'com.reddit.Reddit', 'reddit-desktop', 'giara', 'org.gabmus.giara'], 'web',
      'Reddit')
def reddit(c):
    c.circle(15.5, 17, 12, 'O')
    c.bevel(['O'])
    # Snoo
    c.ellipse(15.5, 20, 8.5, 5.5, 'W')
    c.circle(7.5, 16.5, 2, 'W'); c.circle(23.5, 16.5, 2, 'W')
    c.line(16, 14, 18, 7, 'W')
    c.line(18, 7, 23, 8, 'W')
    c.circle(25, 7, 2.5, 'W')
    c.circle(25, 7, 2.5, 'W')
    c.rect(11, 18, 12, 19, 'R'); c.rect(19, 18, 20, 19, 'R')
    c.pixels([(12, 22), (13, 23), (14, 23), (15, 23), (16, 23), (17, 23), (18, 22)], 'S')
    c.outline()


@icon('twitch', ['twitch-webapp', 'com.twitch.Twitch', 'gnome-twitch', 'com.vinszent.GnomeTwitch', 'streamlink-twitch-gui'],
      'web', 'Twitch')
def twitch(c):
    c.poly([(7, 3), (28, 3), (28, 18), (21, 25), (16, 25), (11, 29), (11, 25), (5, 25), (5, 8)], 'M')
    c.bevel(['M'])
    c.poly([(9, 6), (25, 6), (25, 17), (20, 22), (9, 22)], 'W')
    c.rect(14, 10, 15, 16, 'M'); c.rect(20, 10, 21, 16, 'M')
    c.outline()


@icon('netflix', ['netflix-webapp', 'com.netflix.Netflix', 'netflix-desktop'], 'web', 'Netflix')
def netflix(c):
    c.rect(7, 3, 12, 28, '1')
    c.rect(20, 3, 25, 28, '1')
    c.poly([(7, 3), (13, 3), (25.5, 28.5), (19.5, 28.5)], 'R')
    c.bevel(['R'], dark=False)
    c.outline()


@icon('instagram', ['instagram-webapp', 'com.instagram.Instagram', 'instagram-desktop'], 'web', 'Instagram')
def instagram(c):
    c.rrect(3, 3, 28, 28, 'M', 6)
    for y in range(32):
        for x in range(32):
            if c.get(x, y) == 'M':
                d = y - x
                c.px(x, y, 'Y' if d > 14 else 'O' if d > 3 else 'R' if d > -9 else 'M')
    c.rrect(6, 6, 25, 25, 'W', 4)
    c.rrect(8, 8, 23, 23, '.', 3)
    c.ring(16, 16, 5.5, 3.5, 'W')
    c.circle(20.5, 11.5, 1, 'W')
    for y in range(32):
        for x in range(32):
            if c.get(x, y) == '.' and 8 <= x <= 23 and 8 <= y <= 23:
                d = y - x
                c.px(x, y, 'Y' if d > 14 else 'O' if d > 3 else 'R' if d > -9 else 'M')
    c.outline()


@icon('linkedin', ['linkedin-webapp', 'com.linkedin.LinkedIn', 'linkedin-desktop'], 'web', 'LinkedIn')
def linkedin(c):
    c.rrect(3, 3, 28, 28, 'B', 3)
    c.bevel(['B'])
    c.rect(7, 13, 10, 24, 'W')
    c.rect(7, 7, 10, 10, 'W')
    c.sprite(13, 13, """
        WWWW.WWWWW..
        WWWWWWWWWWW.
        WWWW....WWWW
        WWWW....WWWW
        WWWW....WWWW
        WWWW....WWWW
        WWWW....WWWW
        WWWW....WWWW
        WWWW....WWWW
        WWWW....WWWW
        WWWW....WWWW
        WWWW....WWWW
    """)
    c.shade_below(['W'], 'w')
    c.outline()


@icon('wikipedia', ['wikipedia-webapp', 'org.wikipedia.Wikipedia', 'wike', 'com.github.hugolabe.Wike'], 'web',
      'Wikipedia')
def wikipedia(c):
    c.circle(16, 16, 13, 'w')
    c.bevel(['w'])
    # missing puzzle piece at the top
    c.rect(15, 2, 21, 6, '.')
    c.circle(18, 7.5, 1.8, '.')
    # seams
    c.line(4, 12, 15, 9, 'S'); c.line(15, 9, 27, 13, 'S')
    c.line(4, 21, 16, 19, 'S'); c.line(16, 19, 27, 22, 'S')
    c.line(10, 5, 9, 26, 'S'); c.line(22, 8, 23, 27, 'S')
    c.line(15, 9, 16, 28, 'S')
    # glyphs on the pieces
    c.sprite(5, 14, "s.s\n.s.", None)
    c.sprite(12, 12, "ss\n.s", None)
    c.sprite(18, 14, "s.s\ns.s", None)
    c.sprite(12, 23, "ss\ns.", None)
    c.sprite(19, 23, "s.s\n.s.", None)
    c.outline()


@icon('hacker-news', ['hackernews', 'hn', 'hacker-news-webapp', 'com.ycombinator.news', 'harbour-hn',
                      'io.github.lainsce.Hackgregator'], 'web', 'Hacker News')
def hacker_news(c):
    c.rect(3, 3, 28, 28, 'O')
    c.bevel(['O'])
    c.sprite(8, 7, """
        WWW........WWW
        .WWW......WWW.
        ..WWW....WWW..
        ...WWW..WWW...
        ....WWWWWW....
        .....WWWW.....
        ......WW......
        ......WW......
        ......WW......
        ......WW......
        ......WW......
        ......WW......
        ......WW......
        ......WW......
    """)
    c.outline()
