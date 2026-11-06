"""Omarchy's own apps and the default system set (reference style)."""
from pix import icon, Canvas

OMARCHY_MAZE = """
###########################
###########################
##...........##..........##
##...........##..........##
##..###########....####..##
##..###########....####..##
##..##...............##..##
##..##...............##..##
##..##...............##..##
##..##...............##..##
##..##...............##..##
##..##...............##..##
######...............##..##
######...............##..##
##..##...............##..##
##..##...............##..##
##..##...............##..##
##..##...............##..##
##..##...............##..##
##..##...............##..##
##..###################..##
##..###################..##
##...........##..........##
##...........##..........##
###############..##########
###############..##########
"""


@icon('omarchy', ['omarchy-logo', 'omarchy-menu', 'distributor-logo-omarchy'], 'omarchy', 'Omarchy')
def omarchy(c):
    rows = [r for r in OMARCHY_MAZE.strip().split('\n')]
    rows = [r[:8] + r[9:] for r in rows]  # 26 wide
    c.rect(2, 2, 29, 29, 'k')  # solid dark plate behind the maze
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch == '#':
                c.px(3 + x, 3 + y, 'A')
    c.bevel(['A'])
    # plate edge
    c.frame(2, 2, 29, 29, 'K')
    c.replace('k', 'K', (2, 2, 29, 29))
    c.replace('K', 'k', (5, 5, 26, 26))


@icon('youtube', ['youtube-webapp', 'com.google.youtube'], 'web', 'YouTube')
def youtube(c):
    c.rrect(3, 6, 28, 23, 'R', 3)
    c.rrect(8, 27, 23, 28, 'R', 1)
    c.bevel(['R'])
    c.vline(25, 9, 20, 'r')
    c.sprite(12, 10, """
        WW.....
        WWWW...
        WWWWWW.
        WWWWWWW
        WWWWWW.
        WWWW...
        WW.....
    """)
    c.sprite(13, 16, "w", None)
    c.outline()


@icon('org.gnome.Nautilus', ['nautilus', 'system-file-manager', 'file-manager', 'org.gnome.Nautilus-symbolic',
                             'files'], 'omarchy', 'Files')
def nautilus(c):
    # back flap + tab
    c.rrect(3, 7, 13, 11, 'O', 1)
    c.rect(3, 9, 28, 26, 'O')
    # paper peeking out
    c.rect(6, 10, 25, 14, 'W')
    c.hline(8, 23, 12, 'w')
    # front flap (slightly lower so it reads as a pocket)
    c.rect(3, 14, 28, 26, 'Y')
    c.bevel(['Y'])
    c.hline(3, 28, 14, 'y')
    c.rect(13, 19, 18, 20, '3')  # label slot
    c.outline()


@icon('foot', ['foot-server', 'footclient', 'utilities-terminal', 'terminal', 'org.gnome.Terminal',
               'org.gnome.Console', 'kgx', 'xterm'], 'omarchy', 'Terminal')
def foot(c):
    # chunky CRT with a stand
    c.rrect(3, 4, 28, 22, 'w', 2)
    c.bevel(['w'])
    c.rect(5, 6, 26, 19, 'K')
    c.rect(6, 7, 25, 18, 'k')
    c.sprite(8, 9, """
        G.....
        .G....
        ..G...
        .G....
        G...GGG
    """)
    c.px(6, 7, 's')
    c.rect(12, 23, 19, 24, 'S')
    c.rrect(7, 25, 24, 27, 'w', 1)
    c.shade_below(['w'], 'S')
    c.px(25, 20, 'G')  # power led
    c.outline()


@icon('nvim', ['neovim', 'nvim-qt', 'vim', 'gvim', 'org.vim.Vim', 'neovide'], 'dev', 'Neovim')
def nvim(c):
    # the two leaning prisms of the Neovim "N"
    c.poly([(4, 8), (11, 3), (11, 29), (4, 24)], 'C')
    c.poly([(21, 3), (28, 8), (28, 24), (21, 29)], 'G')
    c.poly([(11, 3), (14, 3), (22, 29), (19, 29)], 'g')
    c.bevel(['C', 'G'])
    c.outline()


@icon('btop', ['btop++', 'htop', 'top'], 'system', 'btop')
def btop(c):
    c.rrect(3, 4, 28, 27, 'k', 2)
    c.rect(3, 4, 28, 7, 'S')
    c.px(5, 5, 'R'); c.px(7, 5, 'Y'); c.px(9, 5, 'G')
    c.hline(5, 26, 7, 'K')
    # history graph
    pts = [(5, 22), (8, 19), (11, 21), (14, 14), (17, 17), (20, 11), (23, 15), (26, 10)]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        c.line(x0, y0, x1, y1, 'C')
    for x in range(5, 27):
        for y in range(9, 26):
            if c.get(x, y) == 'C':
                for yy in range(y + 1, 26):
                    if c.get(x, yy) == 'k':
                        c.px(x, yy, '5' if (x + yy) % 2 else 'k')
    # meter bars
    for i, (w, col) in enumerate([(14, 'G'), (9, 'Y'), (17, 'R')]):
        pass
    c.outline()


@icon('mpv', ['io.mpv.Mpv', 'mpv-symbolic'], 'media', 'mpv')
def mpv(c):
    c.circle(16, 16, 13, 'm')
    c.circle(16, 16, 11, 'M')
    c.circle(17, 17, 8, '7')
    c.sprite(13, 10, """
        WW....
        WWWW..
        WWWWWW
        WWWWWW
        WWWW..
        WW....
    """)
    c.sprite(14, 17, """
        ......
    """)
    c.bevel(['M'], dark=False)
    c.outline()


@icon('imv', ['image-viewer', 'multimedia-photo-viewer', 'swayimg'], 'media', 'Image Viewer')
def imv(c):
    c.rect(3, 4, 28, 27, 'W')
    c.rect(5, 6, 26, 21, 'c')
    c.circle(21, 10, 2.5, 'y')
    c.poly([(5, 21.5), (12, 12), (19, 21.5)], 'G')
    c.poly([(13, 21.5), (19, 15), (26.5, 21.5)], '4')
    c.poly([(9, 15), (12, 12), (15, 15)], 'W')
    c.hline(5, 26, 21, '4')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('hype', ['hype-presentation'], 'omarchy', 'Hype')
def hype(c):
    # presentation screen on a tripod with a big cursor
    c.rrect(3, 4, 28, 21, 'k', 1)
    c.rect(5, 6, 26, 19, 'W')
    c.hline(5, 26, 19, 'w')
    c.rect(7, 8, 14, 9, 'R')
    c.hline(7, 18, 12, 'S')
    c.hline(7, 15, 14, 'S')
    c.rect(15, 22, 16, 28, 'k')
    c.line(15, 22, 9, 28, 'k')
    c.line(16, 22, 22, 28, 'k')
    c.sprite(17, 9, """
        K.....
        KK....
        KWK...
        KWWK..
        KWWWK.
        KWWWWK
        KWWKKK
        KK.KWK
        ....K.
    """)
    c.outline()


@icon('monologue', [], 'omarchy', 'Monologue')
def monologue(c):
    c.circle(16, 16, 13, 'w')
    c.ring(16, 16, 13, 11.5, 'S')
    c.circle(16, 16, 10, 'R')
    c.bevel(['w'])
    c.circle(16, 16, 10, '1')
    c.circle(15, 15, 9, 'R')
    c.ellipse(13, 11, 4, 2, 'r')
    c.px(11, 10, 'W'); c.px(12, 10, 'W')
    c.outline()


@icon('gliff', [], 'omarchy', 'Gliff')
def gliff(c):
    # stacked cards: back cards peek out in violet
    c.rrect(7, 3, 24, 7, 'm', 1)
    c.rrect(5, 5, 26, 9, 'M', 1)
    c.rrect(3, 7, 28, 27, 'k', 1)
    c.bevel(['m', 'M'], dark=False)
    c.sprite(6, 11, """
        .#.#..
        ######
        .#.#..
        ######
        .#.#..
    """, {'#': 'b'})
    c.rect(14, 13, 25, 14, 'b')
    c.rect(6, 19, 21, 19, 's')
    c.rect(6, 22, 17, 22, 's')
    c.outline()


@icon('signed', [], 'omarchy', 'Signed')
def signed(c):
    c.rect(4, 6, 23, 28, 'Y')
    c.bevel(['Y'])
    c.hline(7, 18, 9, '3'); c.hline(7, 15, 12, '3')
    # signature squiggle
    c.pixels([(7, 22), (8, 21), (9, 20), (10, 19), (10, 20), (10, 21), (11, 22), (12, 21), (13, 20), (14, 21),
              (15, 22), (16, 21), (17, 20)], 'K')
    c.hline(7, 18, 25, 'K')
    # fountain pen
    c.line(27, 4, 17, 18, 'k', 2)
    c.line(28, 5, 18, 19, 'S')
    c.pixels([(18, 18), (17, 19), (17, 20)], 'w')
    c.outline()


@icon('omasnap', ['camera-photo', 'org.gnome.Snapshot', 'snapshot', 'cheese', 'org.gnome.Cheese',
                  'camera-app', 'accessories-camera'], 'omarchy', 'Omasnap')
def omasnap(c):
    c.rrect(9, 6, 18, 9, 's', 1)
    c.rrect(3, 8, 28, 26, 'S', 2)
    c.rect(3, 12, 28, 22, 'n')
    c.bevel(['S'])
    c.circle(16, 17, 8, 'k')
    c.circle(16, 17, 6, 'B')
    c.circle(16, 17, 3.5, '6')
    c.px(14, 15, 'b'); c.px(13, 16, 'b'); c.px(14, 14, 'W')
    c.rect(24, 10, 26, 11, 'W')
    c.outline()
