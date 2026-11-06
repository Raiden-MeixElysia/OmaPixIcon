"""IDEs, code editors, more JetBrains products and git clients."""
import math
from pix import icon

DEV = 'dev'


# ------------------------------------------------------------ JetBrains (same recipe as dev.py)
def _jb(c, letters, shards, tile=(8, 8, 25, 25)):
    for pts, col in shards:
        c.poly(pts, col)
    c.bevel([col for _, col in shards])
    x0, y0, x1, y1 = tile
    c.rect(x0, y0, x1, y1, 'K')
    c.text(x0 + 3, y0 + 3, letters, 'W')
    c.rect(x0 + 3, y1 - 3, x0 + 8, y1 - 2, 'W')
    c.outline()


@icon('datagrip', ['jetbrains-datagrip', 'com.jetbrains.DataGrip', 'datagrip-jre'], DEV, 'DataGrip')
def datagrip(c):
    _jb(c, 'DG', [([(3, 3), (20, 3), (3, 18)], 'G'),
                  ([(28, 8), (28, 28), (12, 28)], 'M')])


@icon('phpstorm', ['jetbrains-phpstorm', 'com.jetbrains.PhpStorm', 'phpstorm-jre'], DEV, 'PhpStorm')
def phpstorm(c):
    _jb(c, 'PS', [([(3, 10), (14, 3), (3, 26)], 'M'),
                  ([(12, 3), (28, 3), (28, 20)], 'P')], tile=(9, 9, 26, 26))


@icon('rubymine', ['jetbrains-rubymine', 'com.jetbrains.RubyMine', 'rubymine-jre'], DEV, 'RubyMine')
def rubymine(c):
    _jb(c, 'RM', [([(3, 3), (24, 3), (3, 16)], 'R'),
                  ([(3, 14), (16, 28), (3, 28)], 'M')], tile=(9, 7, 26, 24))


@icon('dataspell', ['jetbrains-dataspell', 'com.jetbrains.DataSpell'], DEV, 'DataSpell')
def dataspell(c):
    _jb(c, 'DS', [([(3, 3), (18, 3), (3, 22)], 'C'),
                  ([(28, 3), (28, 24), (14, 3)], 'G')], tile=(7, 9, 24, 26))


@icon('jetbrains-fleet', ['fleet', 'com.jetbrains.Fleet', 'jetbrains-fleet-bin'], DEV, 'Fleet')
def fleet(c):
    _jb(c, 'FL', [([(3, 3), (14, 3), (3, 20)], 'Y'),
                  ([(28, 12), (28, 28), (6, 28)], 'M')])


@icon('jetbrains-aqua', ['aqua', 'com.jetbrains.Aqua'], DEV, 'Aqua')
def aqua(c):
    _jb(c, 'QA', [([(3, 16), (16, 3), (26, 3), (3, 26)], 'C'),
                  ([(28, 14), (28, 28), (16, 28)], 'G')], tile=(9, 7, 26, 24))


@icon('writerside', ['jetbrains-writerside', 'com.jetbrains.Writerside'], DEV, 'Writerside')
def writerside(c):
    _jb(c, 'WR', [([(3, 3), (22, 3), (3, 14)], 'B'),
                  ([(3, 12), (12, 28), (3, 28)], 'M')], tile=(9, 9, 26, 26))


@icon('jetbrains-gateway', ['gateway', 'com.jetbrains.Gateway'], DEV, 'JetBrains Gateway')
def jb_gateway(c):
    _jb(c, 'GW', [([(10, 3), (28, 3), (28, 18)], 'B'),
                  ([(3, 12), (20, 28), (3, 28)], 'C')], tile=(7, 8, 24, 25))


# ====================================================================== classic IDEs

@icon('eclipse', ['org.eclipse.Java', 'eclipse-java', 'eclipse-cpp', 'eclipse-jee', 'org.eclipse.Eclipse',
                  'eclipse-ide', 'eclipse-php', 'eclipse-bin'], DEV, 'Eclipse')
def eclipse(c):
    c.circle(16, 16, 13, '6')
    c.circle(19, 16, 11, 'B')
    c.bevel(['6'])
    for y in (12, 16, 20):
        c.rect(6, y - 1, 29, y, 'W')
    c.replace('W', 'w', (20, 0, 31, 31))
    c.circle(18, 16, 10, 'B') if False else None
    c.rect(26, 10, 30, 22, '.')
    c.rect(29, 0, 31, 31, '.')
    c.outline()


@icon('netbeans', ['apache-netbeans', 'org.apache.netbeans', 'netbeans-ide', 'apache-netbeans-bin'], DEV,
      'NetBeans')
def netbeans(c):
    # iso cube, blue faces with orange core edge
    c.poly([(16, 2.5), (28, 9), (28, 23), (16, 29.5), (4, 23), (4, 9)], 'B')
    c.poly([(16, 2.5), (28, 9), (16, 15.5), (4, 9)], 'b')
    c.poly([(16, 15.5), (28, 9), (28, 23), (16, 29.5)], '6')
    c.line(16, 16, 16, 28, 'O')
    c.line(5, 9, 15, 15, 'O')
    c.line(17, 15, 27, 9, 'O')
    c.outline()


@icon('org.qt-project.qtcreator', ['qtcreator', 'QtProject-qtcreator', 'qt-creator', 'qtcreator-bin'], DEV,
      'Qt Creator')
def qtcreator(c):
    c.poly([(9, 4), (28, 4), (28, 21), (22, 27), (3, 27), (3, 10)], 'G')
    c.bevel(['G'])
    c.ring(12.5, 15.5, 5.5, 3, 'W')
    c.line(14, 18, 17, 21, 'W', 2)
    c.rect(20, 9, 21, 21, 'W')
    c.rect(18, 12, 23, 13, 'W')
    c.hline(21, 23, 21, 'W')
    c.outline()


@icon('org.kde.kdevelop', ['kdevelop', 'kdevelop-pg-qt'], DEV, 'KDevelop')
def kdevelop(c):
    # blue gear holding a code bracket
    for k in range(8):
        a = math.radians(k * 45)
        cx, cy = 16 + 11 * math.cos(a), 16 + 11 * math.sin(a)
        c.rect(int(cx) - 2, int(cy) - 2, int(cx) + 1, int(cy) + 1, 'B')
    c.circle(16, 16, 11, 'B')
    c.bevel(['B'])
    c.circle(16, 16, 7.5, 'W')
    c.sprite(11, 12, """
        ..k.....k..
        .k...k...k.
        k....k....k
        .k...k...k.
        ..k.....k..
    """)
    c.vline(16, 12, 20, 'k') if False else None
    c.outline()


@icon('org.geany.Geany', ['geany'], DEV, 'Geany')
def geany(c):
    # the genie lamp
    c.ellipse(15, 20, 10, 6, 'Y')
    c.poly([(23, 19), (28, 13), (28, 15), (25, 22)], 'Y')
    c.ring(6.5, 19, 3.5, 1.8, 'Y')
    c.rect(10, 26, 20, 27, 'O')
    c.rrect(12, 11, 18, 15, 'O', 1)
    c.circle(15, 10, 2, 'O')
    c.bevel(['Y', 'O'])
    c.poly([(26, 6), (28, 3), (30, 6), (28, 10)], 'O') if False else None
    c.outline()


@icon('bluefish', ['bluefish-editor', 'org.bluefish.Bluefish'], DEV, 'Bluefish')
def bluefish(c):
    c.ellipse(14, 16, 11, 8, 'B')
    c.poly([(22, 16), (29, 8), (29, 24)], 'B')
    c.poly([(9, 9), (17, 4), (18, 10)], 'b')
    c.bevel(['B'])
    c.circle(9, 14, 2, 'W'); c.px(8, 14, 'K')
    c.arc(14, 16, 6, 4.5, 300, 60, '6')
    c.hline(5, 9, 19, '6')
    c.outline()


@icon('codeblocks', ['org.codeblocks.codeblocks', 'codeblocks-ide', 'Code::Blocks'], DEV, 'Code::Blocks')
def codeblocks(c):
    for (x, y), col in zip(((3, 3), (17, 3), (3, 17), (17, 17)), 'RGYB'):
        c.rect(x, y, x + 11, y + 11, col)
    c.bevel(list('RGB'), dark=False)
    c.outline()


@icon('lite-xl', ['com.lite_xl.LiteXL', 'lite', 'lite-xl-bin', 'litexl'], DEV, 'Lite XL')
def lite_xl(c):
    c.rrect(3, 3, 28, 28, 'k', 4)
    c.bevel(['k'], dark=False)
    c.rect(8, 7, 11, 24, 'W')
    c.rect(8, 21, 23, 24, 'W')
    c.poly([(15, 7), (24, 7), (24, 16)], 'O')
    c.outline()


@icon('pulsar', ['dev.pulsar_edit.Pulsar', 'pulsar-bin', 'pulsar-edit', 'Pulsar'], DEV, 'Pulsar')
def pulsar(c):
    c.ring(16, 16, 13, 11, 'M')
    c.ellipse(16, 16, 3, 13, 'M') if False else None
    c.poly([(16, 5), (18.5, 13.5), (27, 16), (18.5, 18.5), (16, 27), (13.5, 18.5), (5, 16), (13.5, 13.5)], 'm')
    c.bevel(['M'])
    c.circle(16, 16, 2.5, 'W')
    c.outline()


@icon('atom', ['atom-editor', 'io.atom.Atom', 'atom-bin', 'atom-editor-bin'], DEV, 'Atom')
def atom(c):
    for k in range(3):
        a = math.radians(k * 60)
        for y in range(32):
            for x in range(32):
                dx, dy = x + .5 - 16, y + .5 - 16
                u = dx * math.cos(a) + dy * math.sin(a)
                v = -dx * math.sin(a) + dy * math.cos(a)
                d = (u / 13.5) ** 2 + (v / 5) ** 2
                if 0.55 < d <= 1.0:
                    c.px(x, y, 'G')
    c.circle(16, 16, 3, 'g')
    c.outline()


@icon('kakoune', ['kak', 'kakoune-git'], DEV, 'Kakoune')
def kakoune(c):
    c.poly([(4, 3), (11, 3), (11, 12), (20, 3), (28, 3), (18, 15), (28, 28), (20, 28), (11, 18), (11, 28), (4, 28)],
           'Y')
    c.bevel(['Y'])
    c.outline()


@icon('micro', ['micro-editor', 'io.github.zyedidia.micro'], DEV, 'micro')
def micro(c):
    # mu glyph
    c.rect(4, 4, 9, 28, 'G')
    c.rect(4, 4, 9, 21, 'G')
    c.rrect(4, 15, 25, 22, 'G', 3)
    c.rect(20, 4, 25, 22, 'G')
    c.rect(24, 18, 28, 22, 'G')
    c.bevel(['G'])
    c.outline()


@icon('nano', ['gnu-nano', 'nano-editor'], DEV, 'GNU nano')
def nano(c):
    c.rrect(3, 4, 28, 27, 'k', 1)
    c.rect(3, 4, 28, 7, 'w')
    c.bevel(['w', 'k'], dark=False)
    for i, w in enumerate([14, 10, 16, 7]):
        c.hline(6, 6 + w, 10 + i * 2, 's')
    c.rect(4, 21, 27, 26, 'w')
    for x, ch in ((6, 'X'), (17, 'O')):
        c.sprite(x, 22, ".#.\n#.#", {'#': 'k'})
        c.text(x + 4, 22, ch, 'k', font=3)
    c.outline()


@icon('org.spyder_ide.spyder', ['spyder', 'spyder3', 'spyder-ide'], DEV, 'Spyder')
def spyder(c):
    # spider web wheel
    c.circle(16, 16, 13, 'R')
    c.bevel(['R'])
    c.ring(16, 16, 9, 8, '1')
    c.ring(16, 16, 5, 4, '1')
    for k in range(8):
        a = math.radians(k * 45 + 22)
        c.line(16, 16, 16 + 12 * math.cos(a), 16 + 12 * math.sin(a), '1')
    c.circle(16, 16, 2.5, 'k')
    c.outline()


@icon('org.thonny.Thonny', ['thonny', 'Thonny'], DEV, 'Thonny')
def thonny(c):
    # friendly blue egg with the Th monogram
    c.ellipse(16, 16, 12, 13, 'B')
    c.bevel(['B'])
    c.rect(8, 9, 16, 11, 'Y')
    c.rect(11, 9, 13, 23, 'Y')
    c.rect(17, 9, 19, 23, 'W')
    c.rrect(17, 14, 24, 17, 'W', 1)
    c.rect(22, 15, 24, 23, 'W')
    c.outline()


@icon('positron', ['positron-bin', 'com.posit.Positron', 'positron-ide'], DEV, 'Positron')
def positron(c):
    c.circle(16, 16, 13, 'B')
    c.circle(16, 16, 9, 'C')
    c.bevel(['B', 'C'])
    c.rect(14, 9, 17, 22, 'W')
    c.rect(9, 14, 22, 17, 'W')
    c.outline()


@icon('jupyterlab', ['jupyterlab-desktop', 'jlab', 'jupyter', 'jupyter-notebook', 'jupyter-lab', 'jupyterlab-app',
                     'org.jupyter.JupyterLab'], DEV, 'JupyterLab')
def jupyterlab(c):
    # two orange moons + three planets
    c.arc(16, 35.5, 27.5, 24.5, 242, 298, 'O')
    c.arc(16, -3.5, 27.5, 24.5, 62, 118, 'O')
    c.bevel(['O'])
    c.circle(25.5, 6, 2.5, 'S')
    c.circle(6.5, 26, 2.5, 'S')
    c.circle(6.5, 6.5, 1.5, 's')
    c.outline()


# ------------------------------------------------------------ notepad-style editors
def _pad(c, band, glyph=None):
    c.rect(5, 5, 26, 28, 'W')
    c.shade_below(['W'], 'w')
    c.rect(5, 4, 26, 8, band)
    c.bevel([band])
    for x in range(8, 25, 4):
        c.rect(x, 3, x, 6, 'S')
    for i, w in enumerate([14, 10, 16, 8, 12]):
        c.hline(8, 8 + w, 12 + i * 3, 'S')


@icon('notepadqq', ['notepadqq-bin', 'com.notepadqq.Notepadqq'], DEV, 'Notepadqq')
def notepadqq(c):
    _pad(c, 'M')
    c.text(16, 18, 'QQ', 'M', font=3)
    c.outline()


@icon('com.github.dail8859.NotepadNext', ['NotepadNext', 'notepadnext', 'notepad-next'], DEV, 'Notepad Next')
def notepadnext(c):
    _pad(c, 'G')
    c.circle(22, 22, 6, 'G')
    c.bevel(['G'])
    c.sprite(20, 19, """
        W...
        WW..
        WWW.
        WW..
        W...
    """)
    c.outline()


@icon('org.x.editor', ['xed', 'xed-editor'], DEV, 'Xed')
def xed(c):
    _pad(c, 'g')
    c.line(26, 10, 16, 25, 'G', 2)
    c.pixels([(15, 26), (16, 27), (15, 27)], 'k')
    c.outline()


@icon('org.mate.pluma', ['pluma', 'mate-text-editor'], DEV, 'Pluma')
def pluma(c):
    _pad(c, 'C')
    # quill feather
    c.poly([(28, 6), (23, 9), (18, 20), (21, 20), (27, 11)], 'W')
    c.line(28, 6, 15, 26, 's')
    c.outline()


@icon('featherpad', ['org.featherpad.FeatherPad', 'FeatherPad'], DEV, 'FeatherPad')
def featherpad(c):
    c.poly([(26, 3), (16, 8), (7, 20), (6, 26), (12, 25), (23, 15), (29, 5)], 'C')
    c.bevel(['C'])
    c.line(26, 5, 4, 28, '5')
    c.pixels([(18, 12), (14, 17), (11, 20)], 'c')
    c.outline()


@icon('me.mitya57.ReText', ['retext', 'ReText'], DEV, 'ReText')
def retext(c):
    _pad(c, 'B')
    c.rect(14, 16, 25, 25, 'B')
    c.text(16, 18, 'MD', 'W', font=3) if False else None
    c.sprite(15, 18, """
        W...W.WW.
        WW.WW.W.W
        W.W.W.W.W
        W...W.WW.
    """)
    c.outline()


@icon('cudatext', ['cudatext-qt5', 'cudatext-gtk2', 'cudatext-qt6', 'CudaText'], DEV, 'CudaText')
def cudatext(c):
    # cheetah-spotted paw-shaped C
    c.arc(16, 16, 13, 7, 40, 320, 'Y')
    c.bevel(['Y'])
    for x, y in ((9, 8), (6, 15), (9, 22), (16, 25), (15, 5), (21, 26)):
        c.rect(x, y, x + 1, y + 1, '8')
    c.outline()


@icon('codelite', ['codelite-bin', 'org.codelite.CodeLite'], DEV, 'CodeLite')
def codelite(c):
    c.poly([(16, 3), (28, 16), (16, 29), (4, 16)], 'B')
    c.bevel(['B'])
    c.text(11, 13, 'CL', 'W', font=3)
    c.rect(11, 13, 23, 13, 'B') if False else None
    c.outline()


@icon('brackets', ['io.brackets.Brackets', 'brackets-bin', 'brackets-editor'], DEV, 'Brackets')
def brackets(c):
    c.rrect(3, 3, 28, 28, 'B', 3)
    c.bevel(['B'])
    c.rect(8, 7, 13, 9, 'W'); c.rect(8, 7, 10, 24, 'W'); c.rect(8, 22, 13, 24, 'W')
    c.rect(18, 7, 23, 9, 'W'); c.rect(21, 7, 23, 24, 'W'); c.rect(18, 22, 23, 24, 'W')
    c.outline()


# ====================================================================== git clients

def _branch(c, col, node='W', link='W'):
    """Classic three-node git branch glyph."""
    c.line(11, 9, 11, 23, link, 2)
    c.line(21, 10, 12, 20, link, 2)
    for x, y in ((11, 8), (21, 9), (11, 23)):
        c.circle(x + 1, y + 1, 3, node)


@icon('git', ['git-gui', 'gitk', 'git-scm', 'git-cola-git'], DEV, 'Git')
def git(c):
    c.poly([(16, 2.5), (29.5, 16), (16, 29.5), (2.5, 16)], 'O')
    c.bevel(['O'])
    c.line(10, 11, 18, 19, 'W', 2)
    c.line(14, 7, 14, 23, 'W', 2) if False else None
    c.line(11, 8, 11, 23, 'W', 2)
    c.line(11, 11, 20, 19, 'W', 2)
    c.circle(12, 23, 2.5, 'W')
    c.circle(21, 20, 2.5, 'W')
    c.outline()


@icon('org.gnome.gitg', ['gitg'], DEV, 'gitg')
def gitg(c):
    c.circle(16, 16, 13, 'O')
    c.bevel(['O'])
    _branch(c, 'O')
    c.outline()


@icon('gitahead', ['io.github.gitahead.GitAhead', 'GitAhead', 'gitahead-bin'], DEV, 'GitAhead')
def gitahead(c):
    # upward arrow made from a branch
    c.poly([(16, 3), (28, 14), (21, 14), (21, 29), (11, 29), (11, 14), (4, 14)], 'B')
    c.bevel(['B'])
    c.circle(16, 21, 2.5, 'W')
    c.circle(16, 12, 2.5, 'W')
    c.vline(15, 13, 20, 'W')
    c.outline()


@icon('sourcegit', ['SourceGit', 'sourcegit-bin', 'com.sourcegit.SourceGit'], DEV, 'SourceGit')
def sourcegit(c):
    c.rrect(3, 3, 28, 28, 'R', 4)
    c.bevel(['R'])
    _branch(c, 'R')
    c.outline()


@icon('sublime-merge', ['sublime_merge', 'com.sublimemerge.App', 'sublime-merge-dev'], DEV, 'Sublime Merge')
def sublime_merge(c):
    c.poly([(4, 10), (28, 16.5), (28, 23), (4, 16.5)], '5')
    c.poly([(4, 9.5), (28, 3), (28, 9.5), (4, 16)], 'C')
    c.poly([(4, 22.5), (28, 16), (28, 22.5), (4, 29)], 'C')
    c.bevel(['C'])
    c.outline()


@icon('git-cola', ['com.github.git_cola.git-cola', 'cola', 'git-dag', 'git-cola-dag'], DEV, 'Git Cola')
def git_cola(c):
    # cola can
    c.rrect(8, 3, 23, 28, 'R', 2)
    c.rect(9, 3, 22, 5, 'S')
    c.rect(9, 26, 22, 28, 'S')
    c.bevel(['R', 'S'])
    c.rect(8, 12, 23, 18, 'W')
    c.hline(10, 21, 15, 'R')
    c.outline()


@icon('gitbutler', ['gitbutler-tauri', 'com.gitbutler.app', 'GitButler', 'gitbutler-bin', 'git-butler'], DEV,
      'GitButler')
def gitbutler(c):
    # bow tie
    c.poly([(3, 7), (14, 13), (14, 19), (3, 25)], 'k')
    c.poly([(29, 7), (18, 13), (18, 19), (29, 25)], 'k')
    c.rrect(13, 11, 19, 21, 'S', 1)
    c.bevel(['k', 'S'], dark=False)
    c.outline()


@icon('smartgit', ['com.syntevo.SmartGit', 'smartgit-bin', 'SmartGit'], DEV, 'SmartGit')
def smartgit(c):
    # owl-ish head made of branch nodes
    c.rrect(4, 6, 27, 28, 'B', 6)
    c.poly([(4, 10), (6, 3), (11, 7)], 'B')
    c.poly([(27, 10), (25, 3), (20, 7)], 'B')
    c.bevel(['B'])
    c.circle(11, 15, 4, 'W'); c.circle(21, 15, 4, 'W')
    c.rect(10, 14, 11, 15, 'K'); c.rect(20, 14, 21, 15, 'K')
    c.poly([(14, 19), (18, 19), (16, 23)], 'Y')
    c.outline()


@icon('com.jetpackduba.Gitnuro', ['gitnuro', 'Gitnuro', 'gitnuro-bin'], DEV, 'Gitnuro')
def gitnuro(c):
    c.circle(16, 16, 13, 'M')
    c.bevel(['M'])
    _branch(c, 'M')
    c.outline()


@icon('com.github.Murmele.Gittyup', ['gittyup', 'Gittyup'], DEV, 'Gittyup')
def gittyup(c):
    c.poly([(16, 2), (29, 16), (16, 29), (3, 16)], 'G')
    c.bevel(['G'])
    c.poly([(16, 8), (22, 15), (18, 15), (18, 22), (14, 22), (14, 15), (10, 15)], 'W')
    c.outline()


@icon('gitui', ['gitui-bin'], DEV, 'gitui')
def gitui(c):
    c.rrect(3, 5, 28, 26, 'k', 1)
    c.bevel(['k'], dark=False)
    c.rect(5, 7, 13, 24, 's')
    c.rect(15, 7, 26, 15, 's')
    c.rect(15, 17, 26, 24, 's')
    for y in (9, 12, 15, 18):
        c.hline(6, 11, y, 'G')
    c.hline(16, 22, 9, 'O'); c.hline(16, 24, 11, 'w')
    c.hline(16, 20, 19, 'R'); c.hline(16, 23, 21, 'G')
    c.outline()
