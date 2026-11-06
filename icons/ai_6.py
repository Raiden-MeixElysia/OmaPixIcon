"""More dev tooling: TUIs, GNOME design tools, VMs, gamedev, science/maths, TeX, ML utilities."""
import math
from pix import icon

DEV = 'dev'
SCI = 'office'


def _tui(c, chrome='S', screen='k'):
    c.rrect(3, 5, 28, 26, chrome, 2)
    c.bevel([chrome])
    c.rect(5, 9, 26, 24, screen)
    c.pixels([(5, 7), (7, 7), (9, 7)], 'W')


def _page(c, x0=6, y0=3, x1=25, y1=28, fold=5, col='W'):
    c.rect(x0, y0, x1, y1, col)
    c.tri((x1 - fold + 1, y0), (x1 + 1, y0), (x1 + 1, y0 + fold), '.')
    for i in range(fold):
        c.hline(x1 - fold + 1, x1 - fold + 1 + i, y0 + i, 'w')
    c.vline(x1 - fold + 1, y0, y0 + fold - 1, 'S')
    c.hline(x1 - fold + 1, x1, y0 + fold - 1, 'S')


# ====================================================================== terminal tools

@icon('gh', ['github-cli', 'gh-cli'], DEV, 'GitHub CLI')
def gh(c):
    _tui(c, 'k', 'K')
    c.bevel(['k'], dark=False)
    c.text(9, 13, 'GH', 'W')
    c.hline(9, 20, 21, 's')
    c.outline()


@icon('aichat', ['aichat-bin'], DEV, 'AIChat')
def aichat(c):
    _tui(c, 'C')
    c.rrect(7, 11, 20, 17, 'C', 2)
    c.poly([(9, 16), (13, 16), (8, 20)], 'C')
    c.text(9, 12, 'AI', 'k', font=3)
    c.hline(14, 23, 21, 'c')
    c.outline()


@icon('tgpt', ['tgpt-bin'], DEV, 'tgpt')
def tgpt(c):
    _tui(c, 'G')
    c.text(7, 12, 'GPT', 'G', font=3)
    c.rect(7, 19, 9, 21, 'g')
    c.outline()


@icon('posting', ['posting-tui'], DEV, 'Posting')
def posting(c):
    # postcard with a stamp
    c.rect(3, 6, 28, 25, 'W')
    c.bevel(['W'])
    c.rect(20, 8, 26, 15, 'O')
    c.dither(20, 8, 26, 15, 'O', 'o')
    c.vline(16, 9, 22, 'S')
    for y in (17, 20, 23):
        c.hline(19, 26, y - 1, 'S')
    for y in (10, 13, 16):
        c.hline(5, 13, y, 'B')
    c.outline()


@icon('harlequin', ['harlequin-sql'], DEV, 'Harlequin')
def harlequin(c):
    c.poly([(16, 2), (29, 16), (16, 30), (3, 16)], 'Y')
    for (x, y), col in (((16, 9), 'R'), ((9.5, 16), 'B'), ((22.5, 16), 'B'), ((16, 23), 'R')):
        c.poly([(x, y - 6.5), (x + 6.5, y), (x, y + 6.5), (x - 6.5, y)], col)
    c.bevel(['Y', 'R', 'B'], dark=False)
    c.poly([(16, 2), (29, 16), (16, 30), (3, 16)], 'K') if False else None
    c.outline()


@icon('lazysql', ['lazysql-bin'], DEV, 'lazysql')
def lazysql(c):
    c.rect(4, 9, 21, 24, 'G')
    c.ellipse(12.5, 24.5, 9, 3, 'G')
    c.bevel(['G'])
    c.ellipse(12.5, 9, 9, 3, 'g')
    c.hline(5, 20, 16, '4')
    c.text(22, 3, 'Z', 'W', font=3)
    c.text(25, 9, 'Z', 'w', font=3)
    c.outline()


@icon('me.iepure.devtoolbox', ['devtoolbox', 'dev-toolbox', 'DevToolbox'], DEV, 'Dev Toolbox')
def devtoolbox(c):
    c.rrect(10, 4, 21, 9, 'S', 2)
    c.rect(12, 6, 19, 9, '.')
    c.rect(3, 9, 28, 27, 'B')
    c.bevel(['B', 'S'])
    c.sprite(7, 13, """
        ...#.......#...#...
        ..#.......#.....#..
        .#.......#.......#.
        #.......#.........#
        .#.....#.........#.
        ..#...#.........#..
        ...#.#.........#...
    """, {'#': 'W'})
    c.outline()


@icon('ipython', ['ipython3', 'jupyter-console'], DEV, 'IPython')
def ipython(c):
    _tui(c, 'B')
    c.sprite(7, 12, """
        ###.###...#.#..
        .#..#.#.#.#.#..
        .#..###....#...
        .#..#...#..#.##
        ###.#......#.##
    """, {'#': 'b'})
    c.outline()


@icon('jupyter-qtconsole', ['qtconsole', 'org.jupyter.qtconsole'], DEV, 'Jupyter QtConsole')
def qtconsole(c):
    _tui(c, 'O')
    c.sprite(7, 12, """
        #....
        .#...
        ..#..
        .#...
        #....
    """, {'#': 'o'})
    c.circle(20, 16, 4, 'O')
    c.circle(21, 14.5, 3, 'k')
    c.outline()


@icon('doxywizard', ['doxygen', 'doxygen-gui'], DEV, 'Doxygen')
def doxywizard(c):
    # wizard hat
    c.poly([(16, 2), (25, 22), (7, 22)], 'B')
    c.rrect(3, 21, 28, 26, 'B', 2)
    c.bevel(['B'])
    for x, y in ((15, 9), (18, 15), (12, 17)):
        c.px(x, y, 'Y'); c.px(x - 1, y, 'y'); c.px(x + 1, y, 'y'); c.px(x, y - 1, 'y'); c.px(x, y + 1, 'y')
    c.hline(6, 25, 22, '6')
    c.outline()


@icon('cutecom', ['cutecom-qt', 'moserial', 'org.gnome.moserial'], DEV, 'CuteCom')
def cutecom(c):
    # DB9 serial connector
    c.poly([(3, 8), (29, 8), (25, 24), (7, 24)], 'S')
    c.bevel(['S'])
    c.poly([(6, 11), (26, 11), (23, 21), (9, 21)], 'k')
    for i in range(5):
        c.rect(8 + i * 3, 13, 9 + i * 3, 14, 'Y')
    for i in range(4):
        c.rect(10 + i * 3, 17, 11 + i * 3, 18, 'Y')
    c.outline()


@icon('binaryninja', ['binary-ninja', 'binaryninja-free', 'binaryninja-demo'], DEV, 'Binary Ninja')
def binaryninja(c):
    # shuriken
    for k in range(4):
        a = math.radians(k * 90)
        b = a + math.radians(55)
        c.poly([(16, 16), (16 + 13.5 * math.cos(a), 16 + 13.5 * math.sin(a)), (16 + 8 * math.cos(b), 16 + 8 * math.sin(b))],
               'R')
    c.circle(16, 16, 7, 'R')
    c.bevel(['R'])
    c.circle(16, 16, 2, '.')
    c.outline()


@icon('org.radare.iaito', ['iaito', 'radare2', 'r2'], DEV, 'iaito')
def iaito(c):
    # katana
    c.line(6, 26, 26, 6, 'w', 2)
    c.line(7, 26, 27, 6, 'W')
    c.line(4, 28, 9, 23, 'k', 3)
    c.line(8, 20, 13, 25, 'Y', 2)
    c.outline()


# ====================================================================== GNOME design tools

# ====================================================================== VMs / android

@icon('quickgui', ['quickemu', 'quickgui-bin'], DEV, 'Quickgui')
def quickgui(c):
    c.rrect(3, 4, 28, 22, 'S', 2)
    c.rect(5, 6, 26, 20, 'B')
    c.rect(12, 23, 19, 24, 'S'); c.rect(8, 25, 23, 27, 'S')
    c.bevel(['S'])
    c.poly([(18, 7), (11, 14), (15, 14), (13, 19), (20, 12), (16, 12)], 'Y')
    c.outline()


@icon('vmware-workstation', ['vmware', 'vmware-player', 'vmplayer', 'vmware-workstation-pro'], DEV,
      'VMware Workstation')
def vmware(c):
    for (x, y), col in (((3, 3), 'S'), ((10, 10), 'B'), ((17, 17), 'O')):
        c.rect(x, y, x + 11, y + 11, col)
        c.rect(x + 3, y + 3, x + 8, y + 8, '.') if col == 'S' else None
    c.rect(13, 13, 15, 15, 'B') if False else None
    c.bevel(['S', 'B', 'O'])
    c.rect(20, 20, 25, 25, '.')
    c.outline()


# ====================================================================== gamedev

@icon('gdevelop', ['GDevelop', 'gdevelop5', 'io.gdevelop.ide'], DEV, 'GDevelop')
def gdevelop(c):
    c.poly([(3, 12), (12, 3), (20, 3), (11, 12), (11, 20), (20, 20), (20, 16), (16, 16), (21, 11), (28, 11), (28, 21),
            (21, 28), (12, 28), (3, 20)], 'M')
    c.bevel(['M'])
    c.poly([(20, 3), (28, 3), (28, 11), (21, 11), (20, 11)], 'B')
    c.bevel(['B'])
    c.outline()


@icon('defold', ['defold-editor', 'Defold', 'com.defold.editor'], DEV, 'Defold')
def defold(c):
    c.poly([(16, 3), (28, 9.5), (28, 22.5), (16, 29), (4, 22.5), (4, 9.5)], 'O')
    c.bevel(['O'])
    c.poly([(16, 9), (22, 12.5), (22, 19.5), (16, 23), (10, 19.5), (10, 12.5)], 'W')
    c.poly([(16, 12), (19, 14), (19, 18), (16, 20), (13, 18), (13, 14)], 'O')
    c.outline()


@icon('sonic-pi', ['sonic-pi-bin', 'sonicpi', 'net.sonic_pi.SonicPi'], DEV, 'Sonic Pi')
def sonic_pi(c):
    c.circle(16, 16, 13, 'P')
    c.bevel(['P'])
    c.rect(7, 9, 25, 11, 'W')
    c.rect(11, 11, 13, 23, 'W')
    c.rect(19, 11, 21, 21, 'W')
    c.rect(21, 21, 23, 23, 'W')
    c.rect(9, 22, 11, 23, 'W')
    c.outline()


# ====================================================================== science / maths

@icon('paraview', ['ParaView', 'org.paraview.ParaView', 'paraview-bin'], SCI, 'ParaView')
def paraview(c):
    c.rect(3, 3, 14, 14, 'B')
    c.rect(17, 3, 28, 14, 'G')
    c.rect(3, 17, 14, 28, 'G')
    c.rect(17, 17, 28, 28, 'R') if False else None
    c.bevel(['B', 'G'])
    c.outline()


@icon('anaconda-navigator', ['anaconda', 'conda', 'miniconda', 'anaconda-navigator-bin'], DEV, 'Anaconda Navigator')
def anaconda(c):
    c.ring(16, 16, 13, 8, 'G')
    for k in range(10):
        a = math.radians(k * 36)
        c.line(16 + 8.5 * math.cos(a), 16 + 8.5 * math.sin(a), 16 + 12.5 * math.cos(a), 16 + 12.5 * math.sin(a), '4')
    c.bevel(['G'])
    c.circle(16, 16, 4, 'g')
    c.outline()


@icon('orange-canvas', ['orange3', 'orange', 'Orange'], SCI, 'Orange Data Mining')
def orange(c):
    c.circle(16, 17, 12, 'O')
    c.bevel(['O'])
    c.poly([(16, 6), (21, 3), (24, 5), (19, 7)], 'G')
    c.circle(11.5, 15, 2.5, 'W'); c.circle(20.5, 15, 2.5, 'W')
    c.rect(11, 15, 12, 16, 'K'); c.rect(20, 15, 21, 16, 'K')
    c.pixels([(9, 22), (22, 22), (12, 24), (20, 24)], 'o')
    c.outline()


# ------------------------------------------------------------ TeX
# ====================================================================== ML / AI utilities

@icon('witsy', ['witsy-bin', 'Witsy', 'com.nabocorp.witsy'], DEV, 'Witsy')
def witsy(c):
    # light bulb with a sparkle
    c.circle(15, 12, 9, 'Y')
    c.rect(11, 18, 19, 22, 'Y')
    c.bevel(['Y'])
    c.rect(11, 23, 19, 26, 'S'); c.hline(11, 19, 24, 's')
    c.rect(13, 27, 17, 28, 's')
    c.poly([(26, 2), (27, 5), (30, 6), (27, 7), (26, 10), (25, 7), (22, 6), (25, 5)], 'W') if False else None
    c.pixels([(11, 8), (10, 9), (10, 10)], 'y')
    c.outline()


@icon('amazon-q', ['amazon-q-developer', 'q-developer', 'amazonq', 'amazon-q-cli'], DEV, 'Amazon Q')
def amazon_q(c):
    pts = [(16 + 13.5 * math.cos(math.radians(a)), 16 + 13.5 * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
    c.poly(pts, 'M')
    c.bevel(['M'])
    c.ring(15, 15, 7, 4, 'W')
    c.line(17, 17, 21, 21, 'W', 2)
    c.outline()


@icon('llamafile', ['llamafile-bin', 'llama-cpp', 'llama.cpp', 'llama-server'], DEV, 'llamafile')
def llamafile(c):
    _page(c, 5, 3, 26, 28)
    c.shade_below(['W'], 'w')
    # llama silhouette
    c.rect(17, 9, 19, 17, 'N')
    c.rect(19, 9, 21, 11, 'N')
    c.rect(9, 16, 19, 21, 'N')
    for x in (9, 12, 15, 18):
        c.rect(x, 21, x + 1, 25, 'N')
    c.px(20, 8, 'N')
    c.outline()


@icon('netron', ['netron-bin', 'Netron'], DEV, 'Netron')
def netron(c):
    # neural net graph
    layers = [(6, (9, 16, 23)), (16, (6, 12, 19, 26)), (26, (12, 20))]
    for (xa, ya), (xb, yb) in zip(layers, layers[1:]):
        for y0 in ya:
            for y1 in yb:
                c.line(xa, y0, xb, y1, 's')
    for x, ys in layers:
        for y in ys:
            c.circle(x + .5, y + .5, 2.5, 'C')
    c.outline()


@icon('tensorboard', ['tensorboard-bin', 'tensorflow'], DEV, 'TensorBoard')
def tensorboard(c):
    c.poly([(16, 3), (28, 9), (28, 15), (19, 11), (19, 29), (13, 26), (13, 11), (4, 15), (4, 9)], 'O')
    c.poly([(16, 3), (28, 9), (28, 15), (16, 9)], 'o')
    c.bevel(['O'])
    c.outline()


# ====================================================================== more AI CLIs / image tools

@icon('oterm', ['oterm-bin'], DEV, 'oterm')
def oterm(c):
    c.rrect(8, 2, 11, 8, 'W', 1); c.rrect(20, 2, 23, 8, 'W', 1)
    c.rrect(3, 7, 28, 27, 'W', 3)
    c.bevel(['W'])
    c.rect(5, 11, 26, 25, 'k')
    c.sprite(7, 14, """
        #....
        .#...
        ..#..
        .#...
        #..##
    """, {'#': 'W'})
    c.outline()


@icon('open-interpreter', ['interpreter', 'openinterpreter', 'open-interpreter-bin'], DEV, 'Open Interpreter')
def open_interpreter(c):
    c.circle(16, 16, 13, 'W')
    c.bevel(['W'])
    c.circle(16, 16, 8, 'k')
    c.circle(16, 16, 4, 'W')
    c.outline()


@icon('shell-gpt', ['sgpt', 'shellgpt'], DEV, 'ShellGPT')
def shell_gpt(c):
    # scallop shell
    c.ellipse(16, 18, 13, 11, 'o')
    c.rect(2, 20, 30, 31, '.')
    c.rrect(11, 20, 20, 26, 'O', 2)
    c.bevel(['o', 'O'])
    for k in range(7):
        a = math.radians(195 + k * 25)
        c.line(16, 19, 16 + 11 * math.cos(a), 19 + 11 * math.sin(a), '2')
    c.outline()


@icon('mods', ['charm-mods', 'mods-bin'], DEV, 'mods')
def mods(c):
    _tui(c, 'M')
    c.poly([(16, 10), (18, 15), (23, 17), (18, 19), (16, 24), (14, 19), (9, 17), (14, 15)], 'P')
    c.px(16, 16, 'p'); c.px(16, 17, 'W')
    c.outline()


@icon('swarmui', ['SwarmUI', 'swarm-ui', 'stableswarmui'], DEV, 'SwarmUI')
def swarmui(c):
    # honeycomb cluster
    for cx, cy in ((10, 9.5), (22, 9.5), (16, 16.5), (10, 23.5), (22, 23.5)):
        pts = [(cx + 6.5 * math.cos(math.radians(a)), cy + 6.5 * math.sin(math.radians(a))) for a in range(0, 360, 60)]
        c.poly(pts, 'Y' if (cx, cy) != (16, 16.5) else 'O')
    c.bevel(['Y', 'O'])
    c.outline()


@icon('sdnext', ['sd-next', 'automatic', 'vladmandic-sdnext'], DEV, 'SD.Next')
def sdnext(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.poly([(9, 9), (16, 16), (9, 23)], 'W')
    c.poly([(16, 9), (23, 16), (16, 23)], 'W')
    c.outline()


@icon('ramalama', ['RamaLama', 'ramalama-bin'], DEV, 'RamaLama')
def ramalama(c):
    # llama ears poking out of a container
    c.rrect(9, 3, 12, 9, 'W', 1); c.rrect(19, 3, 22, 9, 'W', 1)
    c.rect(3, 8, 28, 28, 'M')
    c.bevel(['M', 'W'])
    for x in (7, 11, 15, 19, 23):
        c.vline(x, 11, 25, '7')
    c.rect(11, 13, 20, 20, 'W')
    c.rect(13, 15, 13, 16, 'K'); c.rect(18, 15, 18, 16, 'K')
    c.outline()


@icon('kohya_ss', ['kohya-ss', 'kohya'], DEV, 'Kohya SS')
def kohya(c):
    # dumbbell: model training
    c.line(6, 16, 25, 16, 'S', 1)
    c.rect(8, 15, 23, 17, 'S')
    for x in (3, 23):
        c.rrect(x, 8, x + 5, 24, 'k', 1)
    c.rrect(7, 10, 9, 22, 's', 0); c.rrect(22, 10, 24, 22, 's', 0)
    c.bevel(['k', 'S'], dark=False)
    c.outline()


# ====================================================================== infra

@icon('kind', ['kind-bin', 'kubernetes-kind'], DEV, 'kind')
def kind(c):
    # container ship with a helm wheel
    c.rect(8, 9, 13, 15, 'O'); c.rect(14, 9, 19, 15, 'G'); c.rect(14, 4, 19, 8, 'R')
    c.poly([(3, 16), (29, 16), (25, 25), (7, 25)], 'B')
    c.bevel(['B', 'O', 'G', 'R'], dark=False)
    c.ring(22, 10, 4.5, 2.5, 'W')
    for x in range(3, 29):
        if x % 4 < 2:
            c.px(x, 27, 'b')
    c.outline()


@icon('minikube', ['minikube-bin'], DEV, 'minikube')
def minikube(c):
    c.poly([(16, 2.5), (28, 9), (28, 23), (16, 29.5), (4, 23), (4, 9)], 'B')
    c.poly([(16, 2.5), (28, 9), (16, 15.5), (4, 9)], 'b')
    c.poly([(16, 15.5), (28, 9), (28, 23), (16, 29.5)], '6')
    c.ring(10, 19.5, 4, 2, 'W')
    c.px(10, 19, 'W')
    c.outline()


@icon('argocd', ['argo-cd', 'argo', 'argocd-bin'], DEV, 'Argo CD')
def argocd(c):
    # octopus
    c.ellipse(16, 11.5, 10, 8.5, 'O')
    for x in (6, 11, 16, 21, 26):
        c.rrect(x - 2, 15, x + 1, 28, 'O', 1)
    c.bevel(['O'])
    c.rect(11, 9, 13, 12, 'W'); c.rect(19, 9, 21, 12, 'W')
    c.rect(12, 10, 13, 11, 'K'); c.rect(20, 10, 21, 11, 'K')
    c.outline()


@icon('prometheus', ['prometheus-bin', 'prometheus-server'], DEV, 'Prometheus')
def prometheus(c):
    c.circle(16, 16, 13, 'O')
    c.bevel(['O'])
    c.poly([(16, 6), (21, 13), (20, 18), (16, 20), (12, 18), (11, 13), (14, 15)], 'W')
    c.rect(10, 21, 22, 22, 'W')
    c.rect(12, 24, 20, 25, 'W')
    c.outline()


@icon('grafana', ['grafana-bin', 'grafana-server'], DEV, 'Grafana')
def grafana(c):
    for k in range(10):
        a = math.radians(k * 36)
        x, y = 16 + 11.5 * math.cos(a), 16 + 11.5 * math.sin(a)
        c.rect(int(x) - 1, int(y) - 1, int(x) + 1, int(y) + 1, 'O')
    c.circle(16, 16, 11, 'O')
    c.bevel(['O'])
    c.arc(16, 16, 7, 4.5, 20, 300, 'W')
    c.rect(16, 14, 23, 16, 'W')
    c.outline()


@icon('jenkins', ['jenkins-lts', 'jenkins-bin'], DEV, 'Jenkins')
def jenkins(c):
    # butler head
    c.ellipse(16, 15, 10, 11, 'p')
    c.ellipse(16, 8, 10, 5, 'S')
    c.rect(6, 8, 26, 12, 'S') if False else None
    c.bevel(['p', 'S'])
    c.rect(11, 13, 12, 14, 'K'); c.rect(20, 13, 21, 14, 'K')
    c.hline(13, 19, 20, '9')
    c.poly([(9, 24), (15, 26), (9, 29)], 'R') if False else None
    c.poly([(9, 24), (16, 26.5), (9, 29), ], 'R')
    c.poly([(23, 24), (16, 26.5), (23, 29)], 'R')
    c.outline()


@icon('duckdb', ['duckdb-bin', 'duckdb-cli', 'DuckDB'], DEV, 'DuckDB')
def duckdb(c):
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'], dark=False)
    c.circle(13, 16, 6.5, 'Y')
    c.rrect(21, 13, 26, 19, 'Y', 1)
    c.outline()


@icon('neo4j-desktop', ['neo4j', 'Neo4j Desktop', 'neo4j-desktop-bin', 'com.neo4j.desktop'], DEV, 'Neo4j Desktop')
def neo4j(c):
    c.line(10, 10, 22, 12, 'S', 2); c.line(10, 10, 13, 23, 'S', 2); c.line(22, 12, 13, 23, 'S', 2)
    c.circle(9.5, 9.5, 6, 'B')
    c.circle(23, 12.5, 4.5, 'C')
    c.circle(13.5, 23.5, 5, 'b')
    c.bevel(['B', 'C', 'b'])
    c.outline()


# ====================================================================== editors / terminals

@icon('scite', ['SciTE', 'org.scintilla.SciTE'], DEV, 'SciTE')
def scite(c):
    _page(c)
    c.shade_below(['W'], 'w')
    for i, w in enumerate([12, 8, 13, 6, 10, 12]):
        c.hline(9, 9 + w, 9 + i * 3, 'B' if i in (0, 3) else 'S')
    c.poly([(22, 15), (23.5, 19), (27.5, 20.5), (23.5, 22), (22, 26), (20.5, 22), (16.5, 20.5), (20.5, 19)], 'Y')
    c.outline()


@icon('textadept', ['textadept-gtk', 'textadept-curses', 'Textadept'], DEV, 'Textadept')
def textadept(c):
    c.rrect(3, 3, 28, 28, '6', 3)
    c.bevel(['6'], dark=False)
    c.text(6, 9, 'T', 'W', scale=2)
    c.text(17, 15, 'A', 'O')
    c.outline()


@icon('spacemacs', ['spacemacs-bin'], DEV, 'Spacemacs')
def spacemacs(c):
    c.ellipse(16, 16, 13, 4.5, 'm')
    c.circle(16, 16, 9, 'M')
    c.bevel(['M'])
    c.ellipse(16, 18, 13, 3, 'm')
    c.rect(4, 12, 28, 17, '.') if False else None
    c.circle(16, 16, 9, 'M') if False else None
    c.sprite(13, 10, """
        ##...
        ..#..
        ..#..
        .#.#.
        .#.#.
        #...#
    """, {'#': 'W'})
    c.outline()


def _term_letter(c, chrome, txt, col):
    c.rrect(3, 5, 28, 26, chrome, 2)
    c.bevel([chrome])
    c.rect(5, 9, 26, 24, 'k')
    c.pixels([(5, 7), (7, 7), (9, 7)], 'W')
    c.text(8, 12, txt, col)


@icon('roxterm', ['roxterm-gtk'], DEV, 'ROXTerm')
def roxterm(c):
    _term_letter(c, 'R', 'R', 'r')
    c.rect(15, 17, 20, 18, 'r')
    c.outline()


@icon('extraterm', ['com.extraterm.extratermqt', 'extraterm-bin', 'extratermqt'], DEV, 'Extraterm')
def extraterm(c):
    _term_letter(c, 'G', 'E', 'g')
    c.circle(21, 16, 3, 'g')
    c.rect(21, 16, 21, 16, 'k')
    c.outline()


@icon('mlterm', ['mlterm-fb'], DEV, 'mlterm')
def mlterm(c):
    _term_letter(c, 'Y', 'ML', 'y')
    c.outline()


@icon('zutty', ['zutty-terminal'], DEV, 'Zutty')
def zutty(c):
    _term_letter(c, 'O', 'Z', 'o')
    c.rect(15, 17, 20, 18, 'o')
    c.outline()


@icon('tig', ['tig-git'], DEV, 'tig')
def tig(c):
    # tiger face
    c.poly([(5, 10), (6, 3), (12, 7)], 'O'); c.poly([(27, 10), (26, 3), (20, 7)], 'O')
    c.circle(16, 17, 12, 'O')
    c.bevel(['O'])
    for x in (11, 15, 19):
        c.vline(x + 1, 6, 9, 'K')
    c.line(4, 14, 8, 16, 'K'); c.line(28, 14, 24, 16, 'K')
    c.line(4, 20, 8, 20, 'K'); c.line(28, 20, 24, 20, 'K')
    c.rect(11, 14, 12, 15, 'K'); c.rect(20, 14, 21, 15, 'K')
    c.ellipse(16, 22, 5, 4, 'W')
    c.rect(15, 19, 16, 20, 'K')
    c.outline()


# ====================================================================== git / API / debug

@icon('gitfiend', ['GitFiend', 'gitfiend-bin'], DEV, 'GitFiend')
def gitfiend(c):
    c.poly([(5, 10), (4, 3), (12, 7)], 'R'); c.poly([(27, 10), (28, 3), (20, 7)], 'R')
    c.circle(16, 17, 12, 'M')
    c.bevel(['M', 'R'])
    c.line(9, 13, 13, 15, 'W', 2); c.line(23, 13, 19, 15, 'W', 2)
    c.arc(16, 19, 6, 4, 20, 160, 'W')
    c.outline()


@icon('restfox', ['Restfox', 'restfox-bin'], DEV, 'Restfox')
def restfox(c):
    # fox head
    c.poly([(3, 3), (12, 9), (7, 15)], 'O'); c.poly([(29, 3), (20, 9), (25, 15)], 'O')
    c.poly([(4, 10), (28, 10), (16, 29)], 'O')
    c.bevel(['O'])
    c.poly([(5, 13), (14, 19), (16, 29)], 'W')
    c.poly([(27, 13), (18, 19), (16, 29)], 'W')
    c.rect(10, 14, 11, 15, 'K'); c.rect(20, 14, 21, 15, 'K')
    c.rect(15, 26, 16, 27, 'K')
    c.outline()


@icon('kreya', ['Kreya', 'kreya-bin', 'com.kreya.Kreya'], DEV, 'Kreya')
def kreya(c):
    c.circle(16, 16, 13, 'C')
    c.bevel(['C'])
    c.rect(9, 8, 12, 24, 'W')
    c.poly([(12, 15), (19, 8), (23, 8), (15, 16), (23, 24), (19, 24), (12, 17)], 'W')
    c.outline()


@icon('altair', ['com.altairgraphql.Altair', 'altair-graphql', 'altair-bin', 'graphql'], DEV, 'Altair GraphQL')
def altair(c):
    pts = [(16 + 13.5 * math.cos(math.radians(a)), 16 + 13.5 * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
    c.poly(pts, 'P')
    c.bevel(['P'])
    tri = [(16 + 8 * math.cos(math.radians(a)), 16 + 8 * math.sin(math.radians(a))) for a in (-90, 30, 150)]
    for (xa, ya), (xb, yb) in zip(tri, tri[1:] + tri[:1]):
        c.line(xa, ya, xb, yb, 'W')
    for x, y in tri:
        c.circle(x, y, 2, 'W')
    c.outline()


@icon('soapui', ['SoapUI', 'soapui-bin', 'soapui-os'], DEV, 'SoapUI')
def soapui(c):
    # soap bubbles
    c.circle(12, 18, 10, 'G')
    c.circle(22.5, 9.5, 5.5, 'g')
    c.circle(24, 22, 4, 'G')
    c.bevel(['G', 'g'])
    c.ring(10, 16, 5, 3.5, 'W') if False else None
    c.pixels([(7, 13), (8, 12), (9, 12), (21, 6), (22, 6)], 'W')
    c.outline()


@icon('jmeter', ['apache-jmeter', 'JMeter', 'jmeter-bin'], DEV, 'Apache JMeter')
def jmeter(c):
    # apache feather
    c.poly([(28, 3), (20, 6), (12, 14), (6, 24), (8, 26), (18, 18), (25, 10)], 'R')
    c.poly([(28, 3), (20, 6), (16, 10), (25, 8)], 'Y')
    c.poly([(16, 10), (25, 8), (21, 14), (13, 14)], 'O')
    c.poly([(9, 20), (16, 19), (8, 26), (6, 24)], 'M')
    c.line(26, 5, 4, 28, '1')
    c.outline()


@icon('renderdoc', ['qrenderdoc', 'RenderDoc', 'renderdoc-bin'], DEV, 'RenderDoc')
def renderdoc(c):
    c.rrect(3, 5, 28, 26, 'k', 2)
    c.bevel(['k'], dark=False)
    c.poly([(16, 8), (25, 23), (7, 23)], 'G')
    c.poly([(16, 8), (25, 23), (16, 23)], '4')
    for y in range(9, 24, 2):
        c.hline(5, 26, y, 'k') if False else None
    c.rect(5, 7, 26, 7, 'G') if False else None
    c.outline()


@icon('tracy', ['tracy-profiler', 'tracy-bin', 'tracy-capture'], DEV, 'Tracy Profiler')
def tracy(c):
    c.rect(3, 4, 28, 27, 'k')
    c.bevel(['k'], dark=False)
    for y, segs in ((6, [(5, 26, 'B')]), (11, [(5, 14, 'G'), (16, 25, 'G')]), (16, [(6, 10, 'Y'), (17, 22, 'Y')]),
                    (21, [(7, 8, 'R'), (18, 20, 'R')])):
        for x0, x1, col in segs:
            c.rect(x0, y, x1, y + 3, col)
    c.outline()


@icon('seergdb', ['seer', 'seer-gdb', 'Seer'], DEV, 'Seer')
def seer(c):
    # crystal ball on a stand
    c.circle(16, 13, 10.5, 'M')
    c.bevel(['M'])
    c.circle(12.5, 9.5, 2.5, 'm')
    c.px(11, 8, 'W')
    c.poly([(9, 22), (23, 22), (26, 28), (6, 28)], 'N')
    c.bevel(['N'])
    c.outline()
