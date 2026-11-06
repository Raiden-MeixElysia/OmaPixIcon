"""Developer tools, editors, terminals, VMs, notes/office and security apps."""
from pix import icon


# ====================================================================== editors

def _vscode(c, base, light, dark):
    # under-arm (bottom of panel up to the left), over-arm (top down to the left)
    c.poly([(23, 25), (19.5, 29), (3, 13.5), (6.5, 10)], dark)
    c.poly([(19.5, 3), (23, 7), (6.5, 22), (3, 18.5)], base)
    c.rect(3, 13, 5, 19, dark)
    c.poly([(19, 3), (22, 3), (28, 6), (28, 26), (22, 29), (19, 29)], base)
    c.bevel([base])
    c.vline(19, 6, 26, dark)
    c.pixels([(20, 5), (21, 5)], light)


@icon('code', ['com.visualstudio.code', 'visual-studio-code', 'vscode', 'code-oss',
               'com.visualstudio.code.oss', 'code-insiders', 'visual-studio-code-insiders',
               'com.visualstudio.code.insiders'], 'dev', 'Visual Studio Code')
def code(c):
    _vscode(c, 'B', 'b', '6')
    c.outline()


@icon('vscodium', ['com.vscodium.codium', 'codium', 'vscodium-bin', 'com.vscodium.codium-insiders',
                   'codium-insiders'], 'dev', 'VSCodium')
def vscodium(c):
    _vscode(c, 'C', 'c', '5')
    c.outline()


@icon('cursor', ['co.anysphere.cursor', 'cursor-ai', 'cursor-bin'], 'dev', 'Cursor')
def cursor(c):
    # isometric cube; a white arrow-facet cuts across the top
    c.poly([(16, 2.5), (28, 9), (28, 23), (16, 29.5), (4, 23), (4, 9)], 's')
    c.poly([(4, 9), (16, 16), (16, 29.5), (4, 23)], 'S')
    c.poly([(16, 2.5), (28, 9), (16, 16), (4, 9)], 'w')
    c.poly([(16, 16), (28, 9), (4, 9)], 'W')
    c.poly([(16, 16), (16, 29.5), (28, 9)], 'k')
    c.bevel(['S'], dark=False)
    c.outline()


@icon('zed', ['dev.zed.Zed', 'zed-editor', 'dev.zed.Zed-Preview', 'zed-preview', 'zeditor'], 'dev', 'Zed')
def zed(c):
    c.rect(4, 4, 27, 9, 'B')
    c.rect(4, 22, 27, 27, 'B')
    c.poly([(20, 9.5), (28, 9.5), (12, 22.5), (4, 22.5)], 'B')
    c.bevel(['B'])
    c.rect(4, 22, 9, 22, 'B')
    c.hline(5, 26, 5, 'b')
    c.outline()


@icon('sublime-text', ['com.sublimetext.three', 'sublime_text', 'sublime-text-3', 'sublime-text-4',
                       'sublime'], 'dev', 'Sublime Text')
def sublime(c):
    c.poly([(4, 10), (28, 16.5), (28, 23), (4, 16.5)], '2')
    c.poly([(4, 9.5), (28, 3), (28, 9.5), (4, 16)], 'O')
    c.poly([(4, 22.5), (28, 16), (28, 22.5), (4, 29)], 'O')
    c.bevel(['O'])
    c.outline()


# ------------------------------------------------------------ JetBrains family
# every product: black tile with its two-letter code + underscore, sitting on
# a product-coloured shard that pokes out from a different side each time.

def _jb(c, letters, shards, tile=(8, 8, 25, 25)):
    for pts, col in shards:
        c.poly(pts, col)
    c.bevel([col for _, col in shards])
    x0, y0, x1, y1 = tile
    c.rect(x0, y0, x1, y1, 'K')
    c.text(x0 + 3, y0 + 3, letters, 'W')
    c.rect(x0 + 3, y1 - 3, x0 + 8, y1 - 2, 'W')
    c.outline()


JB = 'dev'


@icon('jetbrains-idea', ['intellij-idea-ultimate-edition', 'intellij-idea-community-edition', 'idea',
                         'com.jetbrains.IntelliJ-IDEA-Community', 'com.jetbrains.IntelliJ-IDEA-Ultimate',
                         'intellij-idea', 'jetbrains-idea-ce', 'intellij-idea-ce', 'idea-ultimate',
                         'intellij-idea-ultimate'], JB, 'IntelliJ IDEA')
def idea(c):
    _jb(c, 'IJ', [([(3, 3), (18, 3), (8, 22), (3, 22)], 'M'),
                  ([(28, 10), (28, 28), (10, 28)], 'O')])


@icon('pycharm', ['pycharm-community', 'pycharm-professional', 'com.jetbrains.PyCharm-Community',
                  'com.jetbrains.PyCharm-Professional', 'jetbrains-pycharm', 'jetbrains-pycharm-ce',
                  'pycharm-ce', 'pycharm-community-edition', 'pycharm-professional-edition'], JB, 'PyCharm')
def pycharm(c):
    _jb(c, 'PC', [([(3, 12), (12, 3), (20, 3), (3, 26)], 'G'),
                  ([(15, 3), (28, 3), (28, 20)], 'Y')])


@icon('webstorm', ['jetbrains-webstorm', 'com.jetbrains.WebStorm'], JB, 'WebStorm')
def webstorm(c):
    _jb(c, 'WS', [([(3, 3), (22, 3), (3, 20)], 'C'),
                  ([(28, 6), (28, 28), (14, 28)], 'B')], tile=(9, 9, 26, 26))


@icon('clion', ['jetbrains-clion', 'com.jetbrains.CLion'], JB, 'CLion')
def clion(c):
    _jb(c, 'CL', [([(3, 8), (16, 3), (28, 3), (28, 14)], 'G'),
                  ([(3, 8), (12, 28), (3, 28)], 'C')], tile=(9, 7, 26, 24))


@icon('goland', ['jetbrains-goland', 'com.jetbrains.GoLand'], JB, 'GoLand')
def goland(c):
    _jb(c, 'GO', [([(10, 3), (28, 3), (28, 22)], 'C'),
                  ([(3, 8), (16, 28), (3, 28)], 'M')], tile=(7, 9, 24, 26))


@icon('rider', ['jetbrains-rider', 'com.jetbrains.Rider'], JB, 'Rider')
def rider(c):
    _jb(c, 'RD', [([(3, 3), (14, 3), (3, 26)], 'R'),
                  ([(14, 3), (28, 3), (28, 26)], 'Y')], tile=(8, 9, 25, 26))


@icon('rustrover', ['jetbrains-rustrover', 'com.jetbrains.RustRover'], JB, 'RustRover')
def rustrover(c):
    _jb(c, 'RR', [([(3, 20), (3, 28), (24, 28)], 'O'),
                  ([(8, 3), (28, 3), (28, 24)], 'P')], tile=(8, 8, 25, 25))


@icon('jetbrains-toolbox', ['com.jetbrains.Toolbox', 'jetbrains-toolbox-app'], JB, 'JetBrains Toolbox')
def jb_toolbox(c):
    _jb(c, 'TB', [([(3, 3), (28, 3), (28, 10), (3, 10)], 'O'),
                  ([(3, 3), (10, 3), (10, 28), (3, 28)], 'M')], tile=(9, 9, 26, 26))


@icon('android-studio', ['com.google.AndroidStudio', 'androidstudio', 'android-studio-canary',
                         'android-studio-beta'], 'dev', 'Android Studio')
def android_studio(c):
    # droid head peeking over a drafting compass
    c.ellipse(16, 16, 11, 10, 'G')
    c.rect(0, 16, 31, 31, '.')
    c.line(9, 4, 11, 7, 'G')
    c.line(22, 4, 20, 7, 'G')
    c.bevel(['G'])
    c.rect(10, 11, 11, 12, 'K')
    c.rect(20, 11, 21, 12, 'K')
    # compass
    c.circle(16, 15.5, 3, 'S')
    c.px(15, 14, 'W')
    c.line(14, 17, 8, 28, 'w', 2)
    c.line(16, 17, 22, 28, 'S', 2)
    c.hline(10, 21, 22, 's')
    c.outline()


EMACS_E = """
....########.
..##########.
.###.........
###..#######.
###..#######.
.###.........
..##########.
....########.
"""


@icon('emacs', ['org.gnu.emacs', 'emacsclient', 'emacs-gtk', 'emacs-nox', 'emacs-wayland'], 'dev', 'Emacs')
def emacs(c):
    c.circle(16, 16, 13, 'M')
    c.bevel(['M'])
    c.circle(16, 16, 13, '7')
    c.circle(15.5, 15.5, 12, 'M')
    c.ellipse(11, 9, 4, 2, 'm')
    c.sprite(10, 12, EMACS_E, {'#': 'W'})
    c.outline()


@icon('org.kde.kate', ['kate', 'org.kde.kwrite', 'kwrite'], 'dev', 'Kate')
def kate(c):
    # Kate's woodpecker
    c.ellipse(15, 18, 9, 9, 'B')
    c.circle(13, 10, 6, 'B')
    c.poly([(17, 7), (28, 9.5), (18, 12)], 'Y')
    c.poly([(5, 22), (3, 29), (11, 26)], 'B')
    c.poly([(8, 5), (11, 2.5), (14, 4.5)], 'R')
    c.bevel(['B', 'Y'])
    c.circle(13, 9.5, 1.5, 'W')
    c.px(13, 9, 'K')
    c.ellipse(16, 20, 5, 5, 'b')
    c.outline()


def _page(c, x0=6, y0=3, x1=25, y1=28, fold=5, col='W'):
    c.rect(x0, y0, x1, y1, col)
    c.tri((x1 - fold + 1, y0), (x1 + 1, y0), (x1 + 1, y0 + fold), '.')
    for i in range(fold):
        c.hline(x1 - fold + 1, x1 - fold + 1 + i, y0 + i, 'w')
    c.vline(x1 - fold + 1, y0, y0 + fold - 1, 'S')
    c.hline(x1 - fold + 1, x1, y0 + fold - 1, 'S')


@icon('org.gnome.TextEditor', ['gnome-text-editor', 'accessories-text-editor', 'text-editor',
                               'org.gnome.TextEditor-symbolic'], 'dev', 'Text Editor')
def gnome_text_editor(c):
    _page(c)
    c.shade_below(['W'], 'w')
    for i, w in enumerate([12, 9, 13, 7, 11, 13]):
        c.hline(9, 9 + w, 7 + i * 3, 'S')
    c.hline(9, 14, 7, 'B')
    c.vline(19, 18, 23, 'B')
    c.outline()


@icon('gedit', ['org.gnome.gedit', 'org.gnome.Gedit'], 'dev', 'gedit')
def gedit(c):
    c.rect(4, 6, 23, 28, 'W')
    c.shade_below(['W'], 'w')
    c.rect(4, 6, 23, 8, 'G')
    c.hline(4, 23, 8, '4')
    for x in range(6, 23, 4):
        c.rect(x, 4, x, 7, 'S')
    for i, w in enumerate([12, 9, 13, 8]):
        c.hline(7, 7 + w, 12 + i * 3, 'S')
    # pencil
    c.line(26, 6, 14, 23, 'O', 2)
    c.line(27, 7, 15, 24, '2')
    c.pixels([(26, 5), (27, 5), (28, 6), (27, 6), (28, 7)], 'P')
    c.pixels([(13, 24), (14, 25), (13, 25)], 'n')
    c.px(12, 26, 'K')
    c.outline()


@icon('mousepad', ['org.xfce.mousepad', 'org.xfce.Mousepad'], 'dev', 'Mousepad')
def mousepad(c):
    _page(c, 4, 3, 22, 26)
    c.shade_below(['W'], 'w')
    for i, w in enumerate([10, 7, 11, 6]):
        c.hline(7, 7 + w, 7 + i * 3, 'S')
    # the mouse
    c.ellipse(21, 23, 7, 5, 'S')
    c.circle(16, 17, 3, 'S')
    c.circle(25, 17, 3, 'S')
    c.bevel(['S'])
    c.circle(16, 17, 1.5, 'P')
    c.circle(25, 17, 1.5, 'P')
    c.px(18, 22, 'K'); c.px(23, 22, 'K')
    c.rect(20, 24, 21, 24, 'P')
    c.outline()


@icon('helix', ['com.helix_editor.Helix', 'helix-editor'], 'dev', 'Helix')
def helix(c):
    # double helix: two thick sine strands that swap front/back at each crossing
    import math
    pts = {0: [], 1: []}
    for y in range(3, 29):
        t = (y - 3) / 26 * 2 * math.pi * 1.0 + math.pi / 2
        for k in (0, 1):
            x = 16 + 7.5 * math.sin(t + k * math.pi)
            pts[k].append((round(x - 2), y, math.cos(t + k * math.pi)))
    for y in range(5, 28, 4):  # rungs
        xs = [p[0] for k in (0, 1) for p in pts[k] if p[1] == y]
        c.hline(min(xs) + 2, max(xs) + 1, y, 'w')
    order = []
    for k in (0, 1):
        for x, y, z in pts[k]:
            order.append((z, k, x, y))
    for z, k, x, y in sorted(order):
        col = ('M', 'C')[k]
        c.hline(x, x + 3, y, col if z > 0 else DARKER[col])
    c.bevel(['M', 'C'], dark=False)
    c.outline()


DARKER = {'M': '7', 'C': '5'}


@icon('lapce', ['dev.lapce.lapce', 'lapce-nightly'], 'dev', 'Lapce')
def lapce(c):
    c.poly([(5, 3), (13, 3), (13, 20), (28, 20), (28, 29), (5, 29)], 'B')
    c.poly([(13, 8), (27, 3), (27, 14), (13, 18)], 'M')
    c.bevel(['B', 'M'])
    c.poly([(9, 7), (11, 7), (11, 24), (9, 26)], 'b')
    c.outline()


# ==================================================================== terminals

@icon('Alacritty', ['alacritty', 'org.alacritty.Alacritty', 'com.alacritty.Alacritty'], 'dev', 'Alacritty')
def alacritty(c):
    c.poly([(12, 3), (20, 3), (29.5, 29), (2.5, 29)], 'O')
    c.poly([(16, 3), (20, 3), (29.5, 29), (16, 29)], 'Y')
    c.bevel(['O', 'Y'])
    c.poly([(16, 11), (24, 29.5), (8, 29.5)], '.')
    c.poly([(16, 18), (20, 26), (12, 26)], '2')
    c.px(16, 5, 'y'); c.px(17, 5, 'y')
    c.outline()


@icon('com.mitchellh.ghostty', ['ghostty'], 'dev', 'Ghostty')
def ghostty(c):
    c.circle(16, 14, 11, 'B')
    c.rect(5, 14, 26, 25, 'B')
    for i, x in enumerate((5, 12, 19)):  # wavy hem
        c.rrect(x, 24, x + 7, 28, 'B', 1)
    c.rect(10, 25, 10, 28, '.'); c.rect(21, 25, 21, 28, '.')
    c.rect(11, 27, 11, 28, '.'); c.rect(20, 27, 20, 28, '.')
    c.rect(17, 27, 18, 28, '.'); c.rect(13, 27, 14, 28, '.')
    c.bevel(['B'])
    c.rrect(8, 10, 23, 21, 'K', 2)
    c.rrect(9, 11, 22, 20, 'k', 1)
    c.sprite(11, 13, """
        W....
        .W...
        ..W..
        .W...
        W..WWWW
    """)
    c.outline()


@icon('kitty', ['net.kovidgoyal.kitty', 'kitty-terminal'], 'dev', 'kitty')
def kitty(c):
    c.rrect(3, 9, 28, 28, 'S', 4)
    c.poly([(3, 15), (3, 2.5), (13, 10)], 'S')
    c.poly([(28, 15), (28, 2.5), (18, 10)], 'S')
    c.bevel(['S'])
    c.poly([(5, 10), (5, 6), (9, 9.5)], 'P')
    c.poly([(26, 10), (26, 6), (22, 9.5)], 'P')
    c.rect(9, 15, 11, 18, 'Y'); c.rect(20, 15, 22, 18, 'Y')
    c.vline(10, 15, 18, 'K'); c.vline(21, 15, 18, 'K')
    c.rect(15, 20, 16, 21, 'P')
    c.pixels([(14, 23), (15, 22), (16, 22), (17, 23)], 's')
    c.outline()


@icon('org.wezfurlong.wezterm', ['wezterm', 'wezterm-gui'], 'dev', 'WezTerm')
def wezterm(c):
    c.rrect(3, 5, 28, 27, 'k', 2)
    c.rrect(3, 5, 28, 9, 'M', 2)
    c.rect(3, 8, 28, 9, 'M')
    c.bevel(['M'])
    c.hline(3, 28, 10, 'K')
    c.sprite(7, 13, """
        ##....##....##
        ##....##....##
        ##...####...##
        .##.##..##.##.
        .####....####.
        ..##......##..
    """, {'#': 'Y'})
    c.rect(20, 21, 24, 23, 'w')
    c.outline()


@icon('org.kde.konsole', ['konsole'], 'dev', 'Konsole')
def konsole(c):
    c.rrect(3, 4, 28, 27, 'w', 1)
    c.bevel(['w'])
    c.rect(3, 4, 28, 8, 'B')
    c.bevel(['B'])
    c.rect(5, 9, 26, 25, 'K')
    c.rect(6, 10, 25, 24, 'k')
    c.sprite(9, 13, """
        W.....
        WW....
        .WW...
        ..WW..
        .WW...
        WW....
        W..WWWWW
    """)
    c.outline()


@icon('warp', ['dev.warp.Warp', 'warp-terminal', 'warp-terminal-preview'], 'dev', 'Warp')
def warp(c):
    c.poly([(14, 3), (29, 3), (24.5, 20), (9.5, 20)], 'M')
    c.poly([(7.5, 12), (22.5, 12), (18, 29), (3, 29)], 'C')
    c.bevel(['M', 'C'])
    c.outline()


@icon('tilix', ['com.gexperts.Tilix'], 'dev', 'Tilix')
def tilix(c):
    c.rrect(3, 4, 28, 27, 'S', 1)
    c.bevel(['S'])
    c.rect(5, 6, 26, 25, 'K')
    for x0, y0, x1, y1 in ((6, 7, 15, 24), (17, 7, 25, 15), (17, 17, 25, 24)):
        c.rect(x0, y0, x1, y1, 'k')
    c.sprite(8, 9, "G.\n.G\nG.")
    c.hline(10, 12, 11, 'G')
    c.hline(19, 23, 10, 's'); c.hline(19, 21, 12, 's')
    c.hline(19, 22, 20, 's'); c.hline(19, 23, 22, 's')
    c.rect(8, 14, 9, 15, 'w')
    c.outline()


# ============================================================ git / api / db

@icon('gitkraken', ['com.axosoft.GitKraken', 'gitkraken-bin'], 'dev', 'GitKraken')
def gitkraken(c):
    c.ellipse(16, 12, 10, 9, 'C')
    c.rect(7, 12, 24, 18, 'C')
    for x in (6, 11, 16, 21):
        c.rect(x + 1, 18, x + 3, 25, 'C')
    c.px(7, 26, 'C'); c.px(6, 27, 'C')
    c.rect(11, 26, 12, 28, 'C')
    c.rect(19, 26, 20, 28, 'C')
    c.px(24, 26, 'C'); c.px(25, 27, 'C')
    c.bevel(['C'])
    c.rect(10, 11, 12, 13, 'W'); c.rect(19, 11, 21, 13, 'W')
    c.rect(11, 12, 12, 13, 'K'); c.rect(20, 12, 21, 13, 'K')
    c.pixels([(10, 7), (11, 6)], 'c')
    c.outline()


OCTOCAT = """
..#........#..
..##......##..
..##########..
.############.
.############.
.############.
.############.
..##########..
...########...
#...####......
.#..####......
..######......
....####......
"""


@icon('github-desktop', ['io.github.shiftey.Desktop', 'github-desktop-bin'],
      'dev', 'GitHub Desktop')
def github_desktop(c):
    c.circle(16, 16, 13, 'M')
    c.bevel(['M'])
    c.sprite(9, 9, OCTOCAT, {'#': 'W'})
    c.outline()


@icon('meld', ['org.gnome.meld', 'org.gnome.Meld'], 'dev', 'Meld')
def meld(c):
    c.rect(3, 4, 13, 28, 'W')
    c.rect(18, 4, 28, 28, 'W')
    c.shade_below(['W'], 'w')
    for y in (7, 10, 22, 25):
        c.hline(5, 11, y, 'S'); c.hline(20, 26, y, 'S')
    c.rect(5, 13, 11, 19, 'G')
    c.rect(20, 14, 26, 18, 'B')
    c.poly([(12, 13), (21, 14), (21, 19), (12, 20)], 'g')
    c.bevel(['G', 'B'], light=False)
    c.outline()


@icon('postman', ['com.getpostman.Postman', 'postman-bin', 'postman-agent'], 'dev', 'Postman')
def postman(c):
    c.circle(16, 16, 13, 'O')
    c.bevel(['O'])
    c.sprite(7, 7, """
        ............###
        ..........#####
        .........#####.
        ........#####..
        ...#...#####...
        ....#######....
        .....#####.....
        ....#######....
        ...##.###......
        ..#....#.......
        .#.............
    """, {'#': 'W'})
    c.pixels([(18, 10), (19, 10), (19, 9)], 'O')
    c.outline()


@icon('insomnia', ['rest.insomnia.Insomnia', 'insomnia-bin'], 'dev', 'Insomnia')
def insomnia(c):
    c.circle(16, 16, 13, 'M')
    c.bevel(['M'])
    c.circle(16, 16, 8.5, 'W')
    c.circle(18.5, 13.5, 5.5, 'M')
    c.outline()


@icon('bruno', ['com.usebruno.Bruno', 'bruno-bin'], 'dev', 'Bruno')
def bruno(c):
    c.ellipse(16, 16, 9, 11, 'O')
    c.poly([(8, 5), (3, 11), (4, 22), (9, 17)], 'N')
    c.poly([(24, 5), (29, 11), (28, 22), (23, 17)], 'N')
    c.bevel(['O', 'N'])
    c.ellipse(16, 22, 6, 5, 'W')
    c.rect(14, 18, 17, 19, 'K'); c.hline(15, 16, 20, 'K')
    c.rect(11, 12, 12, 13, 'K'); c.rect(19, 12, 20, 13, 'K')
    c.pixels([(15, 24), (16, 24)], 'P')
    c.outline()


@icon('dbeaver', ['io.dbeaver.DBeaverCommunity', 'dbeaver-ce', 'dbeaver-ee', 'io.dbeaver.DBeaverEnterprise'],
      'dev', 'DBeaver')
def dbeaver(c):
    c.circle(8, 7, 3.5, 'N'); c.circle(24, 7, 3.5, 'N')
    c.ellipse(16, 16, 12, 12, 'N')
    c.bevel(['N'])
    c.circle(8, 7, 1.5, '8'); c.circle(24, 7, 1.5, '8')
    c.ellipse(16, 21, 6, 4, 'n')
    c.rect(14, 18, 17, 19, 'K')
    c.rect(14, 22, 17, 26, 'W'); c.vline(15, 22, 26, 'W'); c.vline(16, 22, 26, 'w')
    c.rect(10, 12, 11, 13, 'K'); c.rect(20, 12, 21, 13, 'K')
    c.px(10, 12, 'W'); c.px(20, 12, 'W')
    c.outline()


@icon('beekeeper-studio', ['io.beekeeperstudio.Studio', 'beekeeper-studio-bin'], 'dev', 'Beekeeper Studio')
def beekeeper(c):
    c.ellipse(12, 9, 5, 6, 'c'); c.ellipse(19, 8, 5, 6, 'c')
    c.ellipse(17, 19, 11, 7, 'Y')
    c.circle(8, 18, 4.5, 'K')
    c.bevel(['Y', 'c'])
    for x in (12, 13, 18, 19, 24):
        c.vline(x, 12, 26, 'K')
    c.replace('K', 'Y', (24, 0, 24, 31))
    c.px(28, 19, 'K')
    c.px(7, 17, 'W')
    c.outline()


@icon('mongodb-compass', ['com.mongodb.Compass', 'mongodb-compass-bin', 'mongodb-compass-isolated'],
      'dev', 'MongoDB Compass')
def mongodb_compass(c):
    c.poly([(16, 3.5), (22, 9), (23, 16), (19, 23), (16.5, 25), (15.5, 25), (13, 23), (9, 16), (10, 9)], 'G')
    c.bevel(['G'])
    c.vline(16, 6, 24, '4')
    c.rect(15, 25, 16, 28, 'n')
    c.outline()


@icon('pgadmin4', ['org.pgadmin.pgadmin4', 'pgadmin', 'pgadmin3', 'pgAdmin4'], 'dev', 'pgAdmin')
def pgadmin(c):
    # PostgreSQL elephant
    c.ellipse(19, 14, 9, 10, 'B')
    c.ellipse(11, 12, 7, 8, 'B')
    c.line(6, 15, 5, 24, 'B', 3)
    c.rect(5, 25, 9, 27, 'B')
    c.bevel(['B'])
    c.ellipse(21, 14, 5, 7, '6')
    c.rect(10, 9, 11, 10, 'K'); c.px(10, 9, 'W')
    c.line(10, 18, 14, 20, 'W'); c.px(14, 19, 'W')
    c.outline()


# ================================================================ VMs / net

@icon('virtualbox', ['VirtualBox', 'org.virtualbox.VirtualBox', 'virtualbox-qt', 'virtualbox-ose'],
      'dev', 'VirtualBox')
def virtualbox(c):
    c.poly([(16, 2.5), (28, 9), (28, 23), (16, 29.5), (4, 23), (4, 9)], '6')
    c.poly([(4, 9), (16, 16), (16, 29.5), (4, 23)], 'B')
    c.poly([(16, 2.5), (28, 9), (16, 16), (4, 9)], 'b')
    c.bevel(['B'], dark=False)
    # white "V" on the front face
    c.line(7, 15, 10, 24, 'W', 2); c.line(13, 18, 11, 24, 'W', 2)
    c.pixels([(16, 6), (17, 6)], 'W')
    c.outline()


@icon('virt-manager', ['org.virt_manager.virt-manager', 'virt-manager-symbolic', 'virtual-machine-manager'],
      'dev', 'Virtual Machine Manager')
def virt_manager(c):
    c.rrect(3, 3, 20, 16, 'S', 1)
    c.rect(5, 5, 18, 14, 'k')
    c.rrect(10, 9, 28, 23, 'w', 1)
    c.bevel(['w', 'S'])
    c.rect(12, 11, 26, 21, 'B')
    c.bevel(['B'], light=False)
    c.pixels([(13, 12), (14, 12), (13, 13)], 'b')
    c.rect(17, 24, 21, 25, 'S')
    c.rrect(14, 26, 24, 28, 'w', 1)
    c.shade_below(['w'], 'S')
    c.outline()


@icon('org.gnome.Boxes', ['gnome-boxes', 'org.gnome.Boxes-symbolic'], 'dev', 'Boxes')
def gnome_boxes(c):
    c.rect(5, 13, 26, 28, 'N')
    c.poly([(5, 13), (2.5, 7), (12, 7), (14, 13)], 'n')
    c.poly([(27, 13), (29.5, 7), (20, 7), (18, 13)], 'n')
    c.rect(6, 12, 25, 13, '8')
    c.bevel(['N'])
    c.rect(12, 3, 20, 11, 'B')
    c.bevel(['B'])
    c.rect(13, 4, 19, 9, 'c')
    c.rect(6, 13, 25, 13, '8')
    c.rect(12, 18, 19, 19, 'n')
    c.outline()


@icon('qemu', ['qemu-system', 'qemu-system-x86_64', 'org.qemu.qemu'], 'dev', 'QEMU')
def qemu(c):
    c.ring(15, 15, 12, 6.5, 'O')
    c.poly([(17, 19), (22, 19), (29, 27), (29, 29), (24, 29)], 'O')
    c.bevel(['O'])
    c.ring(15, 15, 7.5, 6.5, '2')
    c.outline()


@icon('wireshark', ['org.wireshark.Wireshark', 'wireshark-gtk', 'wireshark-qt'], 'dev', 'Wireshark')
def wireshark(c):
    c.poly([(7, 21), (19, 8), (25, 2.5), (22, 12), (25, 21)], 'B')
    c.bevel(['B'])
    for y, off in ((22, 0), (26, 2)):
        for x in range(3, 29):
            yy = y + (0 if ((x + off) // 4) % 2 == 0 else 1)
            c.rect(x, yy, x, yy + 1, 'C' if y == 22 else 'b')
    c.outline()


@icon('godot', ['org.godotengine.Godot', 'org.godotengine.Godot4', 'godot4', 'godot-engine', 'godot-mono',
                'org.godotengine.GodotSharp'], 'dev', 'Godot')
def godot(c):
    c.rrect(5, 6, 26, 26, 'B', 4)
    c.rrect(3, 4, 9, 11, 'B', 2); c.rrect(22, 4, 28, 11, 'B', 2)
    c.rrect(13, 3, 18, 7, 'B', 1)
    c.rect(3, 15, 28, 21, 'B')
    c.bevel(['B'])
    c.rect(6, 22, 25, 27, 'w')
    c.shade_below(['w'], 'S')
    c.rect(10, 22, 11, 25, 'B'); c.rect(20, 22, 21, 25, 'B')
    c.rect(15, 24, 16, 27, 'B')
    c.circle(10.5, 15.5, 4, 'W'); c.circle(21.5, 15.5, 4, 'W')
    c.circle(11, 16, 2, 's'); c.circle(21, 16, 2, 's')
    c.outline()


@icon('unityhub', ['com.unity.UnityHub', 'unity-hub', 'unity', 'unityhub-beta'], 'dev', 'Unity Hub')
def unityhub(c):
    hexa = [(16, 3), (28, 9.5), (28, 22.5), (16, 29), (4, 22.5), (4, 9.5)]
    c.poly(hexa, 'W')
    c.poly([(16, 5.5), (25.5, 10.5), (25.5, 21.5), (16, 26.5), (6.5, 21.5), (6.5, 10.5)], 'k')
    c.line(15, 16, 15, 27, 'W', 2)
    c.line(15, 16, 6, 11, 'W', 2)
    c.line(16, 16, 25, 11, 'W', 2)
    c.replace('W', 'w', (17, 17, 31, 31))
    c.outline()


@icon('arduino-ide', ['arduino', 'cc.arduino.IDE2', 'cc.arduino.arduinoide', 'arduino-ide-bin'],
      'dev', 'Arduino IDE')
def arduino(c):
    c.circle(9.5, 16, 6.5, 'C'); c.circle(22.5, 16, 6.5, 'C')
    c.bevel(['C'])
    c.circle(9.5, 16, 3.5, 'W'); c.circle(22.5, 16, 3.5, 'W')
    c.hline(8, 11, 15, '5'); c.hline(8, 11, 16, '5')
    c.rect(21, 14, 22, 17, '5'); c.rect(20, 15, 23, 16, '5')
    c.outline()


# ============================================================ notes / office

@icon('logseq', ['com.logseq.Logseq', 'logseq-desktop'], 'office', 'Logseq')
def logseq(c):
    c.circle(16, 16, 13, '5')
    c.bevel(['5'], dark=False)
    c.ellipse(13, 12, 7, 4, 'c')
    c.ellipse(20, 21, 5, 3, 'c')
    c.hline(9, 17, 15, 'C'); c.hline(17, 23, 23, 'C')
    c.outline()


@icon('joplin', ['net.cozic.joplin_desktop', 'joplin-desktop', '@joplinapp-desktop'], 'office', 'Joplin')
def joplin(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.sprite(11, 8, """
        .....###
        .....###
        .....###
        .....###
        .....###
        .....###
        ##...###
        ###.###.
        .#####..
    """, {'#': 'W'})
    c.rect(8, 8, 10, 10, 'b')
    c.outline()


@icon('anytype', ['io.anytype.anytype', 'anytype-bin'], 'office', 'Anytype')
def anytype(c):
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'])
    c.circle(14, 16, 6, 'W')
    c.circle(14, 16, 3, 'k')
    c.rect(19, 10, 22, 22, 'W')
    c.outline()


@icon('marktext', ['com.github.marktext.marktext', 'mark-text'], 'office', 'MarkText')
def marktext(c):
    _page(c)
    c.shade_below(['W'], 'w')
    c.sprite(8, 12, """
        #...#..###.
        ##.##..###.
        #.#.#..###.
        #...#.#####
        #...#..###.
        #...#...#..
    """, {'#': 'k'})
    c.hline(9, 22, 21, 'S'); c.hline(9, 18, 24, 'S')
    c.outline()


@icon('zettlr', ['com.zettlr.Zettlr', 'zettlr-bin'], 'office', 'Zettlr')
def zettlr(c):
    # slip-box cards
    c.poly([(9, 3), (28, 5), (26, 22), (7, 20)], 'g')
    c.rect(4, 9, 23, 28, 'G')
    c.bevel(['G'])
    c.text(9, 12, 'Z', 'W', scale=2)
    c.outline()


@icon('zotero', ['org.zotero.Zotero', 'zotero-bin'], 'office', 'Zotero')
def zotero(c):
    _page(c)
    c.shade_below(['W'], 'w')
    c.rect(9, 9, 21, 11, 'R')
    c.rect(9, 21, 22, 23, 'R')
    c.poly([(17, 11.5), (21.5, 11.5), (13.5, 21), (9, 21)], 'R')
    c.vline(9, 8, 12, 'R'); c.vline(22, 20, 24, 'R')
    c.bevel(['R'], light=False)
    c.outline()


@icon('calibre', ['calibre-gui', 'com.calibre_ebook.calibre', 'calibre-ebook-viewer', 'calibre-viewer'],
      'office', 'calibre')
def calibre(c):
    books = [(3, 7, 'R'), (8, 4, 'B'), (13, 9, 'G')]
    for x, top, col in books:
        c.rect(x, top, x + 4, 28, col)
    c.poly([(18, 10), (22, 8), (29, 27), (25, 29)], 'R')
    c.bevel(['R', 'B', 'G'], light=False)
    for x, top, col in books:
        c.vline(x, top, 27, LIGHT2[col])
    for x, top, col in books:
        c.hline(x + 1, x + 3, top + 3, 'W'); c.hline(x + 1, x + 3, 24, 'W')
    c.line(21, 13, 22, 12, 'W'); c.line(26, 25, 27, 24, 'W')
    c.outline()


@icon('org.kde.okular', ['okular'], 'office', 'Okular')
def okular(c):
    c.ellipse(16, 16, 13, 7.5, 'W')
    c.circle(16, 16, 6.5, 'B')
    c.bevel(['W'])
    c.circle(16, 16, 6.5, '6')
    c.circle(15.5, 15.5, 5.5, 'B')
    c.circle(16, 16, 2.5, 'K')
    c.px(14, 13, 'W'); c.px(13, 14, 'b')
    c.outline()


@icon('onlyoffice-desktopeditors', ['org.onlyoffice.desktopeditors', 'onlyoffice', 'onlyoffice-desktop',
                                    'ONLYOFFICE'], 'office', 'ONLYOFFICE')
def onlyoffice(c):
    for y, col in ((17, 'R'), (11, 'G'), (4, 'B')):
        c.poly([(3, y + 6), (16, y), (29, y + 6), (16, y + 12)], DARKER2[col])
        c.poly([(3, y + 5), (16, y - 1), (29, y + 5), (16, y + 11)], col)
        c.bevel([col], dark=False)
    c.outline()


LIGHT2 = {'R': 'r', 'B': 'b', 'G': 'g'}
DARKER2 = {'R': '1', 'G': '4', 'B': '6'}


@icon('wps-office', ['wps-office2019-kprometheus', 'com.wps.Office', 'wps-office-kprometheus', 'wps',
                     'wps-office-wps', 'wps-office2019-wpsmain'], 'office', 'WPS Office')
def wps(c):
    c.poly([(3, 4), (9, 4), (12, 18), (14, 11), (18, 11), (20, 18), (23, 4), (29, 4),
            (24, 28), (18.5, 28), (16, 19), (13.5, 28), (8, 28)], 'R')
    c.bevel(['R'])
    c.outline()


@icon('standard-notes', ['org.standardnotes.standardnotes', 'standardnotes', 'standard-notes-bin'],
      'office', 'Standard Notes')
def standard_notes(c):
    c.rrect(3, 3, 28, 28, 'B', 5)
    c.bevel(['B'])
    c.rrect(9, 9, 22, 22, '.', 2)
    c.outline()
    c.replace('B', 'b', (9, 8, 22, 8)); c.replace('B', 'b', (8, 9, 8, 22))


@icon('todoist', ['com.todoist.Todoist', 'todoist-appimage', 'todoist-electron'], 'office', 'Todoist')
def todoist(c):
    for i, y in enumerate((4, 11, 18)):
        c.poly([(4, y + 2.5), (16, y - 1), (28, y + 2.5), (28, y + 7), (16, y + 10.5), (4, y + 7)], 'R')
        c.bevel(['R'])
        c.line(9, y + 4, 12, y + 6, 'W'); c.line(13, y + 5, 22, y + 1, 'W')
    c.outline()


@icon('ticktick', ['dida365', 'dida', 'com.ticktick.task', 'com.ticktick.TickTick', 'ticktick-bin'], 'office', 'TickTick')
def ticktick(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.line(9, 16, 13, 20, 'W', 3)
    c.line(13, 20, 22, 10, 'W', 3)
    c.outline()


@icon('xmind', ['net.xmind.XMind', 'xmind-zen', 'xmind-2020', 'xmind8'], 'office', 'XMind')
def xmind(c):
    for (x, y), col in (((5, 5), 'Y'), ((24, 5), 'G'), ((5, 24), 'B'), ((24, 24), 'M')):
        c.line(16, 16, x, y, 'S', 2)
    for (x, y), col in (((3, 3), 'Y'), ((22, 3), 'G'), ((3, 22), 'B'), ((22, 22), 'M')):
        c.rrect(x, y, x + 6, y + 6, col, 1)
    c.rrect(10, 11, 21, 20, 'R', 2)
    c.bevel(['R'])
    c.hline(13, 18, 15, 'W')
    c.outline()


# ================================================================== security

@icon('bitwarden', ['com.bitwarden.desktop', 'bitwarden-desktop', 'bitwarden-bin'], 'security', 'Bitwarden')
def bitwarden(c):
    shield = [(4, 3), (28, 3), (28, 16), (24, 23), (16, 29.5), (8, 23), (4, 16)]
    c.poly(shield, 'B')
    c.bevel(['B'])
    c.poly([(8, 7), (24, 7), (24, 16), (21.5, 21), (16, 25.5), (10.5, 21), (8, 16)], 'W')
    c.poly([(16, 9), (22, 9), (22, 16), (20, 19.5), (16, 23)], 'B')
    c.outline()


@icon('keepassxc', ['org.keepassxc.KeePassXC', 'keepassxc-bin'],
      'security', 'KeePassXC')
def keepassxc(c):
    c.ring(16, 12, 9, 5.5, 'S')
    c.rect(0, 12, 31, 31, '.')
    c.bevel(['S'])
    c.rrect(5, 13, 26, 28, 'G', 2)
    c.bevel(['G'])
    c.circle(16, 19, 2.5, 'K')
    c.rect(15, 20, 16, 24, 'K')
    c.outline()


@icon('proton-pass', ['me.proton.Pass', 'proton-pass-bin', 'protonpass'], 'security', 'Proton Pass')
def proton_pass(c):
    c.circle(12, 12, 9, 'M')
    c.line(16, 16, 24, 24, 'M', 4)
    c.rect(21, 25, 23, 28, 'M'); c.rect(25, 21, 28, 23, 'M')
    c.bevel(['M'])
    c.circle(11, 11, 3, '.')
    c.outline()


@icon('authenticator', ['com.belmoussaoud.Authenticator', 'gnome-authenticator'], 'security', 'Authenticator')
def authenticator(c):
    c.circle(16, 16, 13, 'w')
    c.bevel(['w'])
    c.arc(16, 16, 11, 8, -90, 180, 'C')
    c.arc(16, 16, 11, 8, 180, 270, 'S')
    c.circle(16, 16, 8, 'W')
    c.text(12, 13, '42', 'k', font=3)
    c.text(12, 13, '42', 'k', font=3)
    c.outline()
