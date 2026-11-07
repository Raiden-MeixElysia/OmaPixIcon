"""Apps that ship with Omarchy (webapps, packages, system tools) and the
user's installed extras (Ely suite, LCMD, R, magpie...)."""
import math

from pix import icon


# ---------------------------------------------------------------- helpers
def fill_fn(c, fn, col):
    """Paint every pixel whose centre satisfies fn(x, y)."""
    for y in range(c.n):
        for x in range(c.n):
            if fn(x + .5, y + .5):
                c.px(x, y, col)


def rot_ellipse(c, cx, cy, rx, ry, ang, col, r_in=None):
    """Filled (or ring, if r_in=(rx_in, ry_in)) rotated ellipse."""
    a = math.radians(ang)
    ca, sa = math.cos(a), math.sin(a)

    def inside(x, y, rx_, ry_):
        dx, dy = x - cx, y - cy
        u, v = dx * ca + dy * sa, -dx * sa + dy * ca
        return (u / rx_) ** 2 + (v / ry_) ** 2 <= 1.0

    fill_fn(c, lambda x, y: inside(x, y, rx, ry) and not (r_in and inside(x, y, *r_in)), col)


# ================================================================ webapps
@icon('basecamp', ['basecamp-webapp', 'basecamp3'], 'web', 'Basecamp')
def basecamp(c):
    c.circle(16, 16, 13, 'Y')
    c.bevel(['Y'])
    # the "mountain smile": climbs to a summit, then sweeps into a grin
    pts = [(5, 19), (7, 17), (9, 15), (11, 13), (13, 13), (14, 14), (15, 16), (17, 18),
           (19, 20), (22, 20), (24, 19), (26, 16)]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        c.line(x0, y0, x1, y1, 'k', 2)
    c.outline()


@icon('hey', ['hey-webapp', 'hey-mail', 'com.hey.app'], 'web', 'HEY')
def hey(c):
    c.rrect(3, 4, 28, 22, 'M', 3)
    c.poly([(7, 21), (6, 28.5), (14, 21)], 'M')
    c.bevel(['M'])
    c.text(8, 10, 'HEY', 'W')
    c.hline(8, 24, 17, '7')
    c.outline()


@icon('whatsapp', ['whatsapp-webapp', 'com.whatsapp', 'whatsapp-for-linux', 'whatsapp-desktop',
                   'io.github.mimbrero.WhatsAppDesktop', 'zapzap', 'com.rtosta.zapzap'], 'web', 'WhatsApp')
def whatsapp(c):
    c.circle(17, 15, 12, 'G')
    c.poly([(7, 20), (3.5, 28.5), (12, 25)], 'G')
    c.bevel(['G'])
    c.sprite(11, 9, """
        .##.........
        ###.........
        ###.........
        ##..........
        ##..........
        ###.........
        .###....#...
        ..####.###..
        ...########.
        ....#######.
        ......####..
    """, {'#': 'W'})
    c.outline()


@icon('x', ['x-webapp', 'twitter', 'com.twitter', 'x-twitter'], 'web', 'X')
def x_twitter(c):
    c.poly([(4, 3), (11, 3), (28, 29), (21, 29)], 'W')
    c.line(26, 3, 18, 13, 'W', 2)
    c.line(13, 18, 5, 27, 'W', 2)
    c.poly([(7, 3), (8, 3), (25, 29), (24, 29)], 'k')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('zoom', ['zoom-webapp', 'Zoom', 'us.zoom.Zoom', 'zoom-videocam'], 'web', 'Zoom')
def zoom(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.rrect(6, 11, 18, 21, 'W', 2)
    c.poly([(20, 14), (26, 10), (26, 22), (20, 18)], 'W')
    c.hline(8, 16, 21, 'w')
    c.outline()


DISCORD = """
....####..........####....
...#######......#######...
..######################..
..######################..
.########################.
.########################.
.########################.
##########################
##########################
##########################
##########################
##########################
##########################
##########################
.########################.
.########################.
..######################..
..#####.##########.#####..
...####............####...
....##..............##....
"""


@icon('omarchy-discord', ['discord', 'com.discordapp.Discord', 'discord-canary', 'discord-ptb',
                          'discord-webapp'], 'web', 'Discord')
def discord(c):
    c.sprite(3, 6, DISCORD, {'#': 'B'})
    c.bevel(['B'])
    c.ellipse(11, 16.5, 2.5, 3, 'W')
    c.ellipse(21, 16.5, 2.5, 3, 'W')
    c.outline()


@icon('docker', ['docker-desktop', 'docker-webapp', 'com.docker.docker'], 'dev', 'Docker')
def docker(c):
    # Moby: hull with a curled tail, containers stacked on the back
    c.ellipse(15, 16, 12, 10, 'B')
    c.rect(0, 0, 31, 16, '.')
    c.poly([(22, 17), (26, 12), (29, 11), (28, 14), (27, 17)], 'B')
    c.bevel(['B'])
    c.px(8, 20, 'W')
    for i in range(5):
        c.rect(4 + i * 4, 12, 6 + i * 4, 14, 'C')
    for i in range(3):
        c.rect(8 + i * 4, 8, 10 + i * 4, 10, 'C')
    c.rect(16, 4, 18, 6, 'C')
    c.bevel(['C'], dark=False)
    c.outline()


def _chrome(c, top, right, left, hub):
    c.circle(16, 16, 13, top)
    c.arc(16, 16, 13, 0, 330, 90, right)
    c.arc(16, 16, 13, 0, 90, 210, left)
    c.bevel([top, right, left])
    c.circle(16, 16, 6.5, 'W')
    c.circle(16, 16, 4.5, hub)
    c.px(14, 13, 'b' if hub == 'B' else 'W')


@icon('google-chrome', ['google-chrome-stable', 'com.google.Chrome', 'google-chrome-beta',
                        'google-chrome-unstable', 'chrome'], 'web', 'Google Chrome')
def chrome(c):
    _chrome(c, 'R', 'Y', 'G', 'B')
    c.outline()


@icon('chromium', ['chromium-browser', 'org.chromium.Chromium', 'chromium-freeworld'], 'web', 'Chromium')
def chromium(c):
    c.circle(16, 16, 13, 'b')
    c.arc(16, 16, 13, 0, 330, 90, 'B')
    c.arc(16, 16, 13, 0, 90, 210, '6')
    c.circle(16, 16, 6.5, 'W')
    c.circle(16, 16, 4.5, 'B')
    c.px(14, 13, 'b')
    c.outline()


@icon('google-contacts', ['google-contacts-webapp'], 'web', 'Google Contacts')
def google_contacts(c):
    c.rrect(5, 3, 28, 28, 'B', 2)
    c.bevel(['B'])
    c.rect(5, 4, 7, 27, '6')
    c.circle(18, 12, 4, 'W')
    c.ellipse(18, 24, 7, 5, 'W')
    c.hline(11, 25, 24, 'B')
    c.rect(11, 25, 25, 27, 'B')
    c.hline(11, 25, 27, '6')
    for y in (8, 15, 22):
        c.rect(3, y, 5, y + 1, 'S')
        c.px(3, y, 'w')
    c.outline()


@icon('google-maps', ['google-maps-webapp'], 'web', 'Google Maps')
def google_maps(c):
    c.poly([(3, 14), (11, 12), (11, 27), (3, 29)], 'G')
    c.poly([(11, 12), (20, 14), (20, 29), (11, 27)], 'Y')
    c.poly([(20, 14), (29, 12), (29, 27), (20, 29)], 'B')
    c.bevel(['G', 'Y', 'B'], light=False)
    # pin
    c.circle(19, 9, 6.5, 'R')
    c.poly([(13.5, 11), (24.5, 11), (19, 23)], 'R')
    c.bevel(['R'])
    c.circle(19, 9, 2.5, '1')
    c.px(16, 5, 'r')
    c.outline()


@icon('google-messages', ['google-messages-webapp', 'messages'], 'web', 'Google Messages')
def google_messages(c):
    c.rrect(3, 4, 28, 23, 'B', 4)
    c.poly([(19, 22), (27, 29), (25, 22)], 'B')
    c.bevel(['B'])
    c.rect(8, 9, 23, 10, 'W')
    c.rect(8, 13, 23, 14, 'W')
    c.rect(8, 17, 17, 18, 'W')
    c.outline()


@icon('google-photos', ['google-photos-webapp'], 'web', 'Google Photos')
def google_photos(c):
    cx, cy, r = 16, 16, 6.5
    petals = [  # (centre dx, dy, half-plane test, colour)
        (-r, 0, lambda x, y: y <= cy, 'R'),
        (0, -r, lambda x, y: x >= cx, 'Y'),
        (r, 0, lambda x, y: y >= cy, 'G'),
        (0, r, lambda x, y: x <= cx, 'B'),
    ]
    for dx, dy, half, col in petals:
        fill_fn(c, lambda x, y: (x - cx - dx) ** 2 + (y - cy - dy) ** 2 <= r * r and half(x, y), col)
    c.bevel(['R', 'Y', 'G', 'B'], dark=False)
    c.outline()


@icon('chatgpt', ['chatgpt-webapp', 'openai', 'com.openai.chatgpt'], 'web', 'ChatGPT')
def chatgpt(c):
    # the OpenAI blossom: a thick ring cut by six slanted seams round a hex hole
    for k in range(6):
        a = math.radians(k * 60 + 30)
        c.circle(16 + 8 * math.cos(a), 16 + 8 * math.sin(a), 5.2, 'W')
    c.circle(16, 16, 9, 'W')
    c.circle(16, 16, 4.2, '.')
    # each link: a curved seam from a hex corner sweeping round to the next lobe
    for k in range(6):
        pts = []
        for t in range(0, 11):
            r = 4.2 + t * 0.85
            a = math.radians(k * 60 + t * 6.5)
            pts.append((int(16 + r * math.cos(a)), int(16 + r * math.sin(a))))
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            c.line(x0, y0, x1, y1, 'S')
    c.bevel(['W'], light=False)
    c.outline()


@icon('battle-net', ['battle.net', 'battlenet', 'battle-net-webapp', 'net.battle'], 'web', 'Battle.net')
def battle_net(c):
    c.circle(16, 16, 9, 'B')
    c.bevel(['B'])
    c.circle(13, 13, 3, 'b')
    c.px(12, 12, 'W')
    rot_ellipse(c, 16, 16, 14, 5.5, -30, 'C', (11.5, 3.5))
    # tuck the orbit behind the planet on its far side
    fill_fn(c, lambda x, y: (x - 16) ** 2 + (y - 16) ** 2 <= 81 and y < 16 + (x - 16) * -0.58 - 0.5
            and c.get(int(x), int(y)) == 'C', 'B')
    c.outline()


@icon('retro-gaming', ['retro-gaming-webapp'], 'web', 'Retro Gaming')
def retro_gaming(c):
    c.circle(10.5, 16, 7.5, 'w')
    c.circle(21.5, 16, 7.5, 'w')
    c.rect(10, 9, 22, 22, 'w')
    c.bevel(['w'])
    c.rect(8, 15, 12, 16, 'k')
    c.rect(9, 13, 10, 18, 'k')
    for x, y, col in ((22, 12, 'G'), (19, 15, 'B'), (25, 15, 'R'), (22, 18, 'Y')):
        c.rect(x - 1, y - 1, x, y, col)
    c.pixels([(14, 17), (15, 16), (17, 17), (18, 16)], 's')
    c.outline()


@icon('windows', ['windows-webapp', 'microsoft-windows', 'winboat', 'windows-vm'], 'web', 'Windows')
def windows(c):
    for x0 in (3, 17):
        for y0 in (3, 17):
            c.rect(x0, y0, x0 + 11, y0 + 11, 'B')
    c.bevel(['B'])
    c.outline()


@icon('github', ['github-webapp', 'github-mark'], 'dev', 'GitHub')
def github(c):
    c.circle(16, 16, 13, 'k')
    c.sprite(9, 7, """
        .#..........#.
        .##........##.
        .############.
        ##############
        ##############
        ##############
        ##############
        ##############
        .############.
        ..##########..
        ....######....
        ....######....
        ....######....
        ....######....
        ....######....
        ....######....
        ....######....
        ....######....
        ....######....
        ....######....
        ....######....
        ....######....
    """, {'#': 'W'})
    c.line(12, 22, 8, 18, 'W')
    c.line(13, 22, 9, 18, 'W')
    c.line(12, 23, 8, 19, 'W')
    c.ring(16, 16, 13.5, 12.5, 'k')
    c.rect(0, 29, 31, 31, '.')
    c.ring(16, 16, 13, 12, 'k')
    c.px(10, 10, 's')
    c.outline()


FIG_LEFT = """
..######
.#######
########
########
########
########
.#######
..######
"""
FIG_RIGHT = """
######..
#######.
########
########
########
########
#######.
######..
"""
FIG_BALL = """
..####..
.######.
########
########
########
########
.######.
..####..
"""
FIG_DROP = """
..######
.#######
########
########
########
########
.######.
..####..
"""


@icon('figma', ['figma-linux', 'io.github.Figma_Linux.figma_linux', 'figma-webapp'], 'web', 'Figma')
def figma(c):
    c.sprite(8, 3, FIG_LEFT, {'#': 'R'})
    c.sprite(16, 3, FIG_RIGHT, {'#': 'O'})
    c.sprite(8, 11, FIG_LEFT, {'#': 'M'})
    c.sprite(16, 11, FIG_BALL, {'#': 'C'})
    c.sprite(8, 19, FIG_DROP, {'#': 'G'})
    c.bevel(['R', 'O', 'M', 'C', 'G'], dark=False)
    c.outline()


# ================================================================ system-shipped
@icon('disk-usage', [],
      'omarchy', 'Disk Usage')
def disk_usage(c):
    c.circle(16, 16, 13, 'B')
    c.arc(16, 16, 13, 0, 270, 20, 'Y')
    c.arc(16, 16, 13, 0, 20, 110, 'R')
    c.arc(16, 16, 13, 0, 110, 160, 'G')
    c.bevel(['B', 'Y', 'R', 'G'], dark=False)
    c.ring(16, 16, 8.5, 6, 'k')
    c.circle(16, 16, 6, '.')
    c.outline()


@icon('disktree', ['disk-tree'], 'omarchy', 'DiskTree')
def disktree(c):
    c.rect(3, 4, 28, 27, 'k')
    c.rect(4, 5, 14, 26, 'G')
    c.rect(16, 5, 27, 14, 'B')
    c.rect(16, 16, 21, 26, 'Y')
    c.rect(23, 16, 27, 20, 'R')
    c.rect(23, 22, 27, 26, 'M')
    c.bevel(['G', 'B', 'Y', 'R', 'M'], dark=False, edge=('.', 'K', 'k'))
    c.outline()


@icon('fcitx', ['fcitx5', 'org.fcitx.Fcitx5', 'fcitx5-configtool', 'fcitx-configtool',
                'org.fcitx.fcitx5-qt6-gui-wrapper', 'org.fcitx.fcitx5-qt5-gui-wrapper'], 'omarchy', 'Fcitx')
def fcitx(c):
    c.rrect(3, 4, 28, 28, 'S', 3)
    c.rrect(5, 5, 26, 23, 'w', 2)
    c.bevel(['w'], dark=False)
    c.hline(6, 25, 24, 's')
    c.sprite(9, 8, """
        .....##......
        ......##.....
        #############
        #############
        ..##.....##..
        ...##...##...
        ....##.##....
        .....###.....
        ....##.##....
        ..###...###..
        ###.......###
    """, {'#': 'k'})
    c.outline()


@icon('hwloc', ['lstopo', 'hwloc-ls'], 'omarchy', 'Hardware Topology')
def hwloc(c):
    for i in range(6):
        p = 7 + i * 4
        c.vline(p, 3, 28, 'S'); c.hline(3, 28, p, 'S')
    c.rrect(6, 6, 25, 25, 'k', 1)
    c.rect(8, 8, 23, 23, 's')
    for x0 in (9, 17):
        for y0 in (9, 17):
            c.rect(x0, y0, x0 + 5, y0 + 5, 'G')
    c.bevel(['G'], edge=('.', 'K', 's'))
    c.outline()


@icon('CMakeSetup', ['cmake-gui', 'cmake'], 'omarchy', 'CMake')
def cmake(c):
    P = (18, 21)
    c.poly([(16, 2), (3, 28.5), P], 'B')
    c.poly([(16, 2), (29, 28.5), P], 'R')
    c.poly([(3, 28.5), (29, 28.5), P], 'G')
    c.bevel(['B', 'R', 'G'], dark=False)
    c.line(16, 4, 18, 20, '1')
    c.outline()


@icon('LimineSnapperSync', ['limine-snapper-restore', 'limine-snapper-sync'], 'omarchy', 'Limine Snapper')
def limine_snapper(c):
    c.circle(17, 16, 12, 'C')
    c.circle(17, 16, 9, 'W')
    c.bevel(['C'])
    c.arc(17, 16, 12.5, 0, 145, 196, '.')
    # arrowhead on the open end, pointing back round the dial
    c.poly([(2.5, 12), (12.5, 12), (7.5, 18.5)], 'C')
    c.hline(4, 11, 12, 'c')
    c.vline(17, 10, 16, 'k')
    c.hline(17, 21, 16, 'k')
    c.px(17, 16, 'R')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('applications-system', ['uuctl', 'applications-utilities'], 'omarchy', 'System Tools')
def applications_system(c):
    def gear(x, y):
        dx, dy = x - 16, y - 16
        r = math.hypot(dx, dy)
        a = (math.degrees(math.atan2(dy, dx)) + 22.5) % 45
        return r <= 9.5 or (r <= 13 and 12 < a < 33)
    fill_fn(c, gear, 'S')
    c.bevel(['S'])
    c.ring(16, 16, 6, 4, 's')
    c.circle(16, 16, 4, '.')
    c.outline()


@icon('application-x-executable', ['application-default-icon', 'exec', 'application-x-sharedlib',
                                   'gnome-panel-launcher', 'unknown'], 'omarchy', 'Application')
def application_x_executable(c):
    c.rrect(3, 5, 28, 27, 'W', 1)
    c.rect(3, 5, 28, 9, 'B')
    c.bevel(['B'], dark=False)
    c.pixels([(23, 7), (25, 7)], 'W')
    c.circle(10.5, 15.5, 3, 'R')
    c.rect(14, 13, 18, 17, 'G')
    c.poly([(19.5, 18), (24.5, 18), (22, 13)], 'Y')
    c.hline(7, 24, 21, 'S'); c.hline(7, 18, 24, 'S')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('qv4l2', ['v4l2', 'webcamoid', 'io.github.webcamoid.Webcamoid', 'camera-web'], 'omarchy', 'Qt V4L2 test bench')
def qv4l2(c):
    c.circle(16, 12.5, 9.5, 'w')
    c.bevel(['w'])
    c.circle(16, 12.5, 6, 'k')
    c.circle(16, 12.5, 4, 'B')
    c.circle(16, 12.5, 2, '6')
    c.px(14, 10, 'W')
    c.px(22, 7, 'R')
    c.rect(14, 22, 17, 24, 'S')
    c.rrect(6, 25, 25, 28, 'w', 1)
    c.shade_below(['w'], 'S')
    c.outline()


@icon('qvidcap', ['video-capture'], 'omarchy', 'Qt Video Capture')
def qvidcap(c):
    c.line(15, 9, 9, 3, 'S'); c.line(17, 9, 23, 3, 'S')
    c.rrect(3, 9, 28, 28, 'N', 2)
    c.bevel(['N'])
    c.rect(5, 11, 24, 26, 'k')
    for i, col in enumerate('WYCGMR'):
        c.rect(6 + i * 3, 12, 8 + i * 3, 21, col)
    for i, col in enumerate('RkMkCk'):
        c.rect(6 + i * 3, 23, 8 + i * 3, 25, col)
    c.px(26, 13, 'k'); c.px(26, 16, 'k'); c.px(26, 25, 'G')
    c.outline()


MAGPIE = """
...................kkk....
.................kkkkkkk..
................kkkkkWkkk.
................kkkkkkkkss
...............kkkkkkkk...
..............kkkkkkkk....
.............kkkkkkkWW....
...........WWWkkkkWWWWW...
.........BBWWWWkkWWWWWW...
.......BBBBBWWkkWWWWWWW...
.....bBBBBBBBkkWWWWWWW....
...bBBBBBBBBBkWWWWWWW.....
.bBBBB666BBBkkkkkkk.......
BBBB66...kkkkkkk..........
BB6.........s..s..........
............s..s..........
...........ss.ss..........
"""


@icon('magpie', ['magpie-agent'], 'omarchy', 'Magpie')
def magpie(c):
    c.sprite(3, 8, MAGPIE)
    c.outline()


@icon('org.quickshell', ['quickshell', 'qs'], 'omarchy', 'Quickshell')
def quickshell(c):
    def gear(x, y):
        dx, dy = x - 15, y - 15
        r = math.hypot(dx, dy)
        a = (math.degrees(math.atan2(dy, dx)) + 22.5) % 45
        return r <= 9.5 or (r <= 12.5 and 13 < a < 32)
    fill_fn(c, gear, 'G')
    c.poly([(18, 19), (22, 16), (29, 26), (26, 29)], 'G')
    c.bevel(['G'])
    c.circle(15, 15, 5, '.')
    c.outline()


@icon('org.gnome.Evince', ['evince', 'org.gnome.Papers', 'papers'], 'office', 'Document Viewer')
def evince(c):
    c.rect(7, 3, 25, 23, 'w')
    c.rect(4, 6, 22, 27, 'W')
    c.shade_below(['W'], 'w')
    c.rect(7, 9, 15, 10, 'R')
    for y in (13, 16, 19):
        c.hline(7, 19, y, 'S')
    c.ring(20, 20, 6, 4, 'k')
    c.circle(20, 20, 4, 'c')
    c.px(18, 18, 'W')
    c.line(24, 24, 27, 27, 'N', 2)
    c.outline()


@icon('org.gnome.DiskUtility', ['gnome-disks', 'gnome-disk-utility'], 'omarchy', 'Disks')
def disk_utility(c):
    c.rrect(4, 3, 27, 28, 'S', 2)
    c.bevel(['S'])
    c.circle(15, 14, 9, 'w')
    c.circle(15, 14, 8, 'W')
    c.ring(15, 14, 6, 5, 'w')
    c.circle(15, 14, 2, 's')
    c.line(24, 8, 18, 18, 'k', 2)
    c.px(24, 7, 'R')
    for x, y in ((6, 5), (25, 5), (6, 26), (25, 26)):
        c.px(x, y, 's')
    c.rect(8, 25, 20, 26, 'k')
    c.px(22, 25, 'G')
    c.outline()


@icon('printer', ['cups', 'org.cups.cupsd', 'system-config-printer', 'printer-network', 'printer-local', 'print-manager',
                  'org.kde.print-manager'], 'omarchy', 'Printer')
def printer(c):
    c.rect(9, 3, 22, 11, 'W')
    c.rrect(3, 10, 28, 23, 'w', 2)
    c.bevel(['w'])
    c.rect(7, 18, 24, 19, 'k')
    c.px(25, 13, 'G')
    c.rect(9, 20, 22, 28, 'W')
    c.hline(11, 20, 23, 'S'); c.hline(11, 17, 25, 'S')
    c.shade_below(['W'], 'w')
    c.outline()


def _tui(c):
    c.rrect(3, 4, 28, 27, 'k', 2)
    c.rect(3, 4, 28, 7, 'S')
    c.px(5, 5, 'R'); c.px(7, 5, 'Y'); c.px(9, 5, 'G')
    c.hline(5, 26, 7, 'K')


@icon('lazygit', ['lazygit-tui'], 'dev', 'lazygit')
def lazygit(c):
    _tui(c)
    c.vline(8, 10, 24, 'O')
    c.line(8, 13, 13, 17, 'G'); c.vline(13, 17, 21, 'G'); c.line(13, 21, 8, 24, 'G')
    for x, y, col in ((8, 11, 'O'), (8, 24, 'O'), (13, 18, 'G')):
        c.rect(x - 1, y - 1, x + 1, y + 1, col)
    c.px(12, 17, 'g')
    c.hline(17, 25, 10, 'w'); c.hline(17, 23, 14, 's'); c.hline(17, 25, 18, 's'); c.hline(17, 22, 23, 's')
    c.outline()


@icon('lazydocker', ['lazydocker-tui'], 'dev', 'lazydocker')
def lazydocker(c):
    _tui(c)
    for row, n in ((0, 1), (1, 2), (2, 3)):
        for i in range(n):
            x = 16 - n * 2 + i * 4
            c.rect(x, 11 + row * 4, x + 2, 13 + row * 4, 'C')
            c.px(x, 11 + row * 4, 'c')
    c.hline(5, 26, 23, 'B'); c.hline(6, 25, 24, '6')
    c.outline()


@icon('superwhisper', ['superwhisper-bin', 'com.superwhisper.app', 'audio-input-microphone'],
      'omarchy', 'Superwhisper')
def superwhisper(c):
    c.arc(16, 13, 10, 8, 0, 180, 'S')
    c.rrect(11, 3, 20, 19, 'M', 4)
    c.bevel(['M'])
    for y in (7, 10, 13):
        c.hline(13, 18, y, '7')
    c.rect(15, 23, 16, 25, 'S')
    c.rrect(9, 26, 22, 28, 'S', 1)
    c.shade_below(['S'], 's')
    c.pixels([(3, 10), (3, 11), (3, 12), (28, 10), (28, 11), (28, 12)], 'm')
    c.outline()


# ================================================================ Ely office suite
def _ely(c, col):
    """Shared Ely motif: a coloured sheet with a paper-white dog-ear."""
    c.rect(5, 3, 26, 28, col)
    for i in range(7):
        c.hline(20 + i, 26, 3 + i, '.')
    c.bevel([col])
    c.poly([(20, 3), (20, 9.5), (26.5, 9.5)], 'W')
    c.hline(20, 26, 9, 'w')
    c.vline(19, 3, 9, {'B': '6', 'C': '5', 'Y': '3', 'R': '1', 'O': '2', 'G': '4', 'M': '7'}[col])


@icon('ely-doc', ['ely-docs', 'ely-writer'], 'omarchy', 'Ely Doc')
def ely_doc(c):
    _ely(c, 'B')
    c.rect(9, 8, 16, 9, 'W')
    for y, x1 in ((13, 22), (16, 22), (19, 22), (22, 17)):
        c.rect(9, y, x1, y + 1, 'W')
    c.outline()


@icon('ely-mail', [], 'omarchy', 'Ely Mail')
def ely_mail(c):
    _ely(c, 'C')
    c.rect(8, 13, 23, 24, 'W')
    c.line(8, 13, 15, 19, '5'); c.line(23, 13, 16, 19, '5')
    c.hline(8, 23, 24, 'w')
    c.outline()


@icon('ely-mark', ['ely-markdown'], 'omarchy', 'Ely Mark')
def ely_mark(c):
    _ely(c, 'Y')
    c.sprite(8, 12, """
        ##....##......
        ###..###...##.
        ########...##.
        ##.##.##...##.
        ##....##.######
        ##....##..####.
        ##....##...##..
    """, {'#': 'k'})
    c.rect(8, 22, 22, 23, '3')
    c.outline()


@icon('ely-pdf', [], 'omarchy', 'Ely PDF')
def ely_pdf(c):
    _ely(c, 'R')
    c.rect(8, 12, 23, 24, 'W')
    c.poly([(8.5, 24), (13, 17), (17.5, 24)], '1')
    c.poly([(14, 24), (18.5, 19), (23.5, 24)], 'R')
    c.rect(19, 14, 20, 15, 'Y')
    c.outline()


@icon('ely-show', ['ely-slides'], 'omarchy', 'Ely Show')
def ely_show(c):
    _ely(c, 'O')
    c.rect(8, 12, 23, 22, 'W')
    c.rect(10, 18, 11, 20, '2'); c.rect(13, 16, 14, 20, '2'); c.rect(16, 14, 17, 20, 'O')
    c.circle(20.5, 15.5, 1.6, '2')
    c.line(13, 23, 11, 25, 'W'); c.line(18, 23, 20, 25, 'W')
    c.outline()


@icon('ely-table', ['ely-sheet', 'ely-sheets'], 'omarchy', 'Ely Table')
def ely_table(c):
    _ely(c, 'G')
    c.rect(8, 12, 23, 24, 'W')
    for y in (15, 18, 21):
        c.hline(8, 23, y, '4')
    c.vline(13, 12, 24, '4')
    c.rect(8, 12, 23, 14, 'g')
    c.outline()


@icon('ely-tree', [], 'omarchy', 'Ely Tree')
def ely_tree(c):
    _ely(c, 'M')
    c.rect(10, 12, 11, 24, 'W')
    for i in range(6):
        c.rect(12 + i, 19 - i, 13 + i, 20 - i, 'W')
    for x, y in ((10, 11), (10, 23), (18, 12)):
        c.rrect(x - 1, y - 1, x + 2, y + 2, 'W', 1)
        c.rect(x, y, x + 1, y + 1, '7')
    c.outline()


# ================================================================ other installed apps
@icon('r', ['R', 'rstudio', 'r-base', 'org.r-project.R'], 'dev', 'R')
def r_lang(c):
    c.ellipse(15, 13, 13, 10, 'S')
    c.ellipse(17, 14, 9, 6, '.')
    c.bevel(['S'], edge=('.',))
    c.sprite(11, 9, """
        ###########....
        ############...
        ####.....####..
        ####......###..
        ####......###..
        ####.....####..
        ############...
        ###########....
        ####...####....
        ####....####...
        ####....####...
        ####.....####..
        ####.....####..
        ####......####.
        ####......####.
        ####.......####
        ####.......####
        ####.......####
        ####.......####
    """, {'#': 'B'})
    c.bevel(['B'], dark=False)
    c.outline()


@icon('lzc-client', ['lzc-client-desktop', 'lcmd', 'lazycat'], 'system', 'LCMD')
def lzc_client(c):
    # chunky "L" + a "C" that grows a fox ear
    c.rect(3, 5, 8, 28, 'B')
    c.rect(3, 23, 13, 28, 'B')
    c.bevel(['B'])
    c.circle(21, 17, 8, 'O')
    c.circle(21, 17, 4, '.')
    c.poly([(21, 17), (30, 13), (30, 21)], '.')
    c.poly([(15, 12), (17, 3), (22, 10)], 'O')
    c.bevel(['O'])
    c.outline()


# ================================================================ Omarchy package apps
@icon('obsidian', ['md.obsidian.Obsidian', 'obsidian-bin'], 'office', 'Obsidian')
def obsidian(c):
    c.poly([(13, 3), (23, 7.5), (27, 21), (19, 29), (8, 25.5), (5, 14)], 'M')
    c.poly([(13, 3), (16, 15), (8, 25.5), (5, 14)], 'm')
    c.poly([(16, 15), (27, 21), (19, 29)], '7')
    c.line(13, 4, 15, 14, 'W')
    c.outline()


def _lo(c, col, dark):
    """LibreOffice family: paper sheet with a coloured fold."""
    c.rect(5, 3, 26, 28, 'W')
    for i in range(7):
        c.hline(20 + i, 26, 3 + i, '.')
    c.shade_below(['W'], 'w')
    c.vline(26, 10, 27, 'w')
    c.poly([(20, 3), (20, 9.5), (26.5, 9.5)], col)
    c.vline(19, 3, 9, dark)
    c.hline(20, 26, 9, dark)


@icon('libreoffice-startcenter', ['libreoffice-main', 'org.libreoffice.LibreOffice', 'libreoffice',
                                  'libreoffice-fresh', 'libreoffice-still'], 'office', 'LibreOffice')
def lo_start(c):
    _lo(c, 'S', 's')
    for (x, y), col in zip(((8, 13), (16, 13), (8, 20), (16, 20)), 'BGOM'):
        c.rect(x, y, x + 6, y + 5, col)
    c.outline()


@icon('libreoffice-writer', ['org.libreoffice.LibreOffice.Writer', 'libreoffice-fresh-writer',
                             'libreoffice-still-writer'], 'office', 'LibreOffice Writer')
def lo_writer(c):
    _lo(c, 'B', '6')
    c.rect(8, 7, 15, 8, 'B')
    for y, x1 in ((12, 22), (15, 22), (18, 22), (21, 22), (24, 16)):
        c.hline(8, x1, y, 'b')
        c.hline(8, x1, y + 1, 'B')
    c.outline()


@icon('libreoffice-calc', ['org.libreoffice.LibreOffice.Calc', 'libreoffice-fresh-calc',
                           'libreoffice-still-calc'], 'office', 'LibreOffice Calc')
def lo_calc(c):
    _lo(c, 'G', '4')
    c.rect(8, 12, 23, 25, 'G')
    c.rect(8, 12, 23, 14, '4')
    for y in (15, 18, 21):
        c.hline(8, 23, y, 'g')
    for x in (13, 18):
        c.vline(x, 15, 25, 'W')
    c.outline()


@icon('libreoffice-impress', ['org.libreoffice.LibreOffice.Impress', 'libreoffice-fresh-impress',
                              'libreoffice-still-impress'], 'office', 'LibreOffice Impress')
def lo_impress(c):
    _lo(c, 'O', '2')
    c.rect(8, 12, 23, 23, 'O')
    c.circle(13, 17.5, 3.5, 'W')
    c.arc(13, 17.5, 3.5, 0, 270, 360, 'Y')
    c.hline(18, 21, 15, 'W'); c.hline(18, 21, 18, 'W'); c.hline(18, 20, 21, 'W')
    c.hline(8, 23, 25, '2')
    c.outline()


@icon('libreoffice-draw', ['org.libreoffice.LibreOffice.Draw', 'libreoffice-fresh-draw',
                           'libreoffice-still-draw'], 'office', 'LibreOffice Draw')
def lo_draw(c):
    _lo(c, 'Y', '3')
    c.circle(13, 16, 5, 'Y')
    c.bevel(['Y'], light=False, edge=('W', 'w'))
    c.poly([(14, 25.5), (19, 15), (24, 25.5)], 'O')
    c.outline()


@icon('libreoffice-base', ['org.libreoffice.LibreOffice.Base', 'libreoffice-fresh-base',
                           'libreoffice-still-base'], 'office', 'LibreOffice Base')
def lo_base(c):
    _lo(c, 'M', '7')
    c.rect(9, 14, 22, 24, 'M')
    c.ellipse(16, 25, 7, 2, 'M')
    c.ellipse(16, 14, 7, 2.5, 'm')
    for y in (18, 21):
        c.hline(9, 22, y, '7')
    c.outline()


@icon('libreoffice-math', ['org.libreoffice.LibreOffice.Math', 'libreoffice-fresh-math',
                           'libreoffice-still-math'], 'office', 'LibreOffice Math')
def lo_math(c):
    _lo(c, 'R', '1')
    c.sprite(8, 12, """
        ......########
        ......#.......
        ......#.......
        .....#..#...#.
        ##...#...#.#..
        .#...#....#...
        ..#.#....#.#..
        ..#.#...#...#.
        ...#..........
    """, {'#': 'R'})
    c.hline(8, 22, 24, '1')
    c.outline()


@icon('localsend', ['localsend_app', 'org.localsend.localsend_app', 'localsend-bin'], 'system', 'LocalSend')
def localsend(c):
    c.circle(16, 16, 13, 'C')
    c.bevel(['C'])
    c.sprite(8, 8, """
        ......##........
        .....####.......
        ....######......
        ...########.....
        ......##........
        ......##..##....
        ......##..##....
        ..........##....
        ..........##....
        .....########...
        ......######....
        .......####.....
        ........##......
    """, {'#': 'W'})
    c.sprite(8, 8, """
        ......##........
    """, {'#': 'W'})
    c.outline()


@icon('pinta', ['com.github.PintaProject.Pinta', 'pinta-bin'], 'media', 'Pinta')
def pinta(c):
    # a canvas with a fresh stroke, and the brush that made it
    c.rect(3, 7, 21, 28, 'W')
    c.shade_below(['W'], 'w')
    c.vline(21, 7, 27, 'w')
    c.line(6, 24, 10, 20, 'B', 2); c.line(10, 20, 14, 21, 'B', 2); c.line(14, 21, 18, 17, 'B', 2)
    c.line(27, 3, 21, 9, 'N', 2)
    c.line(28, 4, 22, 10, '8')
    c.rect(18, 11, 21, 14, 'S')
    c.px(18, 11, 'w')
    c.poly([(17, 13.5), (20.5, 17), (15, 20)], 'B')
    c.px(16, 18, 'b')
    c.outline()


@icon('aether', ['aether-theme', 'omarchy-aether'], 'omarchy', 'Aether')
def aether(c):
    c.ellipse(16, 16, 13, 11, 'A')
    c.circle(25, 21, 4, '.')
    c.bevel(['A'])
    c.circle(19, 20, 2, '.')
    for x, y, col in ((9, 11, 'R'), (14, 8, 'Y'), (20, 9, 'G'), (24, 13, 'B'), (9, 18, 'W')):
        c.rect(x - 1, y - 1, x + 1, y + 1, col)
    c.outline()


@icon('cliamp', ['cliamp-player'], 'omarchy', 'cliamp')
def cliamp(c):
    c.rrect(3, 7, 26, 27, 'S', 1)
    c.bevel(['S'])
    c.rect(5, 9, 24, 10, 'O')
    c.rect(5, 12, 24, 22, 'k')
    for i, h in enumerate((5, 8, 6, 9, 4, 7, 3, 6, 5)):
        x = 6 + i * 2
        c.vline(x, 22 - h, 21, 'G')
        c.px(x, 22 - h, 'Y')
    for i in range(4):
        c.rect(5 + i * 5, 24, 7 + i * 5, 25, 's')
    c.poly([(23, 2), (29, 2), (26, 8), (29, 8), (21, 17), (23, 10), (20, 10)], 'Y')
    c.outline()


@icon('omacalc', ['omarchy-calculator'], 'omarchy', 'Omacalc')
def omacalc(c):
    c.rrect(6, 3, 25, 28, 'A', 2)
    c.bevel(['A'])
    c.rect(8, 5, 23, 10, 'k')
    c.text(13, 6, '42', 'G', font=3)
    for j in range(4):
        for i in range(4):
            x, y = 8 + i * 4, 13 + j * 4
            col = 'k' if i == 3 else 'W'
            c.rect(x, y, x + 2, y + 2, col)
            c.px(x + 2, y + 2, 's' if col == 'k' else 'w')
    c.outline()


@icon('omacut', ['omarchy-video-editor'], 'omarchy', 'Omacut')
def omacut(c):
    c.rect(4, 13, 27, 28, 'k')
    c.rect(4, 13, 27, 16, 'W')
    for i in range(4):
        c.poly([(5 + i * 6, 13), (8 + i * 6, 13), (6 + i * 6, 16.5), (3 + i * 6, 16.5)], 'k')
    c.hline(6, 18, 20, 's'); c.hline(6, 14, 23, 's'); c.rect(21, 20, 25, 25, 'A')
    # clapper stick, open
    c.poly([(3, 9), (25, 3), (26.5, 7), (4.5, 13)], 'W')
    for i in range(4):
        x = 7 + i * 5
        c.poly([(x, 7.5 - i * 1.3), (x + 3, 6.7 - i * 1.3), (x + 4, 10.2 - i * 1.3), (x + 1, 11 - i * 1.3)], 'A')
    c.rect(3, 12, 5, 14, 'S')
    c.outline()


@icon('omawrite', ['omarchy-write'], 'omarchy', 'Omawrite')
def omawrite(c):
    c.rect(9, 3, 22, 14, 'W')
    for y in (6, 8, 10):
        c.hline(11, 20, y, 'S')
    c.rrect(3, 12, 28, 15, 'k', 1)
    c.poly([(6, 16), (26, 16), (28.5, 28.5), (3.5, 28.5)], 'A')
    c.bevel(['A'])
    for j, (x0, n) in enumerate(((7, 8), (6, 9))):
        for i in range(n):
            c.px(x0 + i * 2 + j, 20 + j * 3, 'W')
    c.hline(11, 20, 26, 'W')
    c.outline()


@icon('moonlight', ['com.moonlight_stream.Moonlight', 'moonlight-qt'], 'media', 'Moonlight')
def moonlight(c):
    c.circle(16, 16, 13, 'Y')
    c.circle(22, 12, 10, '.')
    c.bevel(['Y'])
    c.pixels([(23, 23), (8, 20)], '3')
    c.rect(6, 12, 7, 13, '3')
    c.sprite(20, 4, """
        ..#..
        .###.
        #####
        .###.
        ..#..
    """, {'#': 'W'})
    c.outline()


@icon('typora', ['io.typora.Typora', 'typora-bin'], 'office', 'Typora')
def typora(c):
    c.rect(5, 3, 26, 28, 'W')
    c.shade_below(['W'], 'w')
    c.vline(26, 3, 27, 'w')
    c.rect(8, 7, 23, 10, 'k')
    c.rect(14, 7, 17, 24, 'k')
    c.rect(12, 23, 19, 24, 'k')
    c.pixels([(8, 11), (23, 11)], 'k')
    c.vline(21, 18, 24, 'B')
    c.outline()


@icon('spotify', ['spotify-client', 'com.spotify.Client', 'spotify-launcher', 'spotify-adblock'],
      'media', 'Spotify')
def spotify(c):
    c.circle(16, 16, 13, 'G')
    c.bevel(['G'])
    for cy, ro, ri, a0, a1 in ((27, 15, 12.5, 222, 318), (28.5, 11.5, 9.5, 228, 312), (30, 8.5, 6.8, 235, 305)):
        fill_fn(c, lambda x, y, cy=cy, ro=ro, ri=ri, a0=a0, a1=a1:
                ri < math.hypot(x - 16, y - cy) <= ro
                and a0 <= math.degrees(math.atan2(y - cy, x - 16)) % 360 <= a1
                and c.get(int(x), int(y)) in 'Ggr4', 'k')
    c.outline()


@icon('signal-desktop', ['signal', 'org.signal.Signal', 'signal-desktop-beta'], 'web', 'Signal')
def signal(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])

    def dashes(x, y):
        d = math.hypot(x - 16, y - 16)
        a = (math.degrees(math.atan2(y - 16, x - 16)) + 360) % 30
        return 9.4 < d <= 11 and 8 < a < 24
    fill_fn(c, dashes, 'W')
    c.circle(16, 16, 6.5, 'W')
    c.poly([(11, 18), (9, 23.5), (15, 21.5)], 'W')
    c.outline()


@icon('1password', ['1password-beta', 'com.onepassword.OnePassword', 'onepassword'], 'system', '1Password')
def onepassword(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.ring(16, 16, 10, 9, '6')
    c.rrect(14, 8, 18, 24, 'W', 1)
    c.rect(12, 9, 13, 12, 'W')
    c.rect(14, 15, 15, 17, '6')
    c.outline()


@icon('obs', ['com.obsproject.Studio', 'obs-studio', 'obs-studio-browser'], 'media', 'OBS Studio')
def obs(c):
    c.circle(16, 16, 13, 'k')
    c.ring(16, 16, 13, 12, 's')
    for k in range(3):
        a = math.radians(-90 + k * 120)
        x, y = 16 + 6 * math.cos(a), 16 + 6 * math.sin(a)
        c.circle(x, y, 4, 'W')
        c.circle(x + 1.2, y + 1.2, 2.2, 'w')
        c.circle(x - .4, y - .4, 2.6, 'W')
        c.px(round(x - 2.5), round(y - 2.5), 'W')
    c.circle(16, 16, 1.5, 's')
    c.outline()


@icon('kdenlive', ['org.kde.kdenlive'], 'media', 'Kdenlive')
def kdenlive(c):
    c.circle(14, 14, 11, 'S')
    c.bevel(['S'])
    for k in range(5):
        a = math.radians(-90 + k * 72)
        c.circle(14 + 6 * math.cos(a), 14 + 6 * math.sin(a), 2.3, 'k')
    c.circle(14, 14, 1.5, 's')
    c.poly([(16, 15), (28.5, 21.5), (16, 28)], 'B')
    c.bevel(['B'], edge=('.', 'K', 'S', 's'))
    c.outline()


@icon('xournalpp', ['com.github.xournalpp.xournalpp', 'xournal', 'xournal++'], 'office', 'Xournal++')
def xournalpp(c):
    c.rect(4, 5, 24, 28, 'W')
    c.shade_below(['W'], 'w')
    c.vline(8, 7, 27, 'r')
    for y in (11, 15, 19, 23):
        c.hline(9, 23, y, 'b')
    for x in (7, 11, 15, 19, 23):
        c.vline(x - 1, 3, 6, 'S')
        c.px(x - 1, 3, 'w')
    c.line(28, 11, 16, 23, 'O', 2)
    c.pixels([(15, 24), (16, 25)], 'k')
    c.px(29, 10, 'R'); c.px(28, 10, 'R'); c.px(29, 11, 'R')
    c.outline()


@icon('dropbox', ['com.dropbox.Client', 'dropbox-client'], 'system', 'Dropbox')
def dropbox(c):
    def diamond(cx, cy):
        c.poly([(cx, cy - 5), (cx + 6.5, cy), (cx, cy + 5), (cx - 6.5, cy)], 'B')
    diamond(9.5, 8.5); diamond(22.5, 8.5)
    diamond(9.5, 18.5); diamond(22.5, 18.5)
    c.poly([(16, 21.5), (22.5, 25.5), (16, 29.5), (9.5, 25.5)], 'B')
    c.bevel(['B'], dark=False)
    c.outline()
