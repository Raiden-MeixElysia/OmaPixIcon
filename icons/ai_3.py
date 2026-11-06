"""Terminal emulators, multiplexers, containers, Kubernetes and cloud/IaC tools."""
import math
from pix import icon

DEV = 'dev'
SYS = 'system'

PROMPT = """
    #....
    ##...
    .##..
    ##...
    #..##
"""


def _win(c, chrome='w', screen='k', x0=3, y0=4, x1=28, y1=27, bar=4, r=2):
    """Terminal window: chrome frame with a title bar and a dark screen."""
    c.rrect(x0, y0, x1, y1, chrome, r)
    c.bevel([chrome])
    c.rect(x0 + 2, y0 + bar + 1, x1 - 2, y1 - 2, screen)


def _prompt(c, x, y, col):
    c.sprite(x, y, PROMPT, {'#': col})


# ====================================================================== terminals

@icon('terminator', ['terminator-gtk3'], DEV, 'Terminator')
def terminator(c):
    _win(c, 'R')
    c.rect(5, 9, 26, 25, 'K')
    for x0, y0, x1, y1 in ((6, 10, 15, 16), (17, 10, 25, 16), (6, 18, 15, 24), (17, 18, 25, 24)):
        c.rect(x0, y0, x1, y1, 'k')
    _prompt(c, 7, 11, 'r')
    c.pixels([(18, 11), (19, 11), (20, 11)], 's')
    c.outline()


@icon('guake', ['guake-prefs', 'org.guake.Guake'], DEV, 'Guake')
def guake(c):
    # terminal dropping down from the top bar
    c.rect(3, 3, 28, 6, 'S')
    c.rrect(6, 6, 25, 22, 'k', 2)
    c.rect(6, 6, 25, 9, 'G')
    c.bevel(['S', 'G'])
    _prompt(c, 9, 12, 'G')
    c.poly([(12, 23), (20, 23), (16, 28)], 'G')
    c.outline()


@icon('org.kde.yakuake', ['yakuake'], DEV, 'Yakuake')
def yakuake(c):
    c.rect(3, 3, 28, 6, 'B')
    c.rrect(5, 6, 26, 25, 'k', 2)
    c.bevel(['B'])
    _prompt(c, 8, 10, 'W')
    c.rrect(11, 24, 20, 28, 'B', 2)
    c.hline(13, 18, 26, 'b')
    c.outline()


@icon('tilda', ['tilda-terminal'], DEV, 'Tilda')
def tilda(c):
    # a fat tilde
    for x in range(3, 29):
        y = 16 - 6 * math.sin((x - 3) / 25 * 2 * math.pi)
        c.rect(x, int(y) - 3, x, int(y) + 3, 'O')
    c.bevel(['O'])
    c.outline()


@icon('cool-retro-term', ['cool-retro-term-git', 'coolretroterm'], DEV, 'Cool Retro Term')
def cool_retro_term(c):
    # beige CRT with amber phosphor
    c.rrect(3, 3, 28, 24, 'n', 3)
    c.rect(9, 24, 22, 28, 'N')
    c.bevel(['n', 'N'])
    c.rrect(5, 5, 24, 20, 'k', 3)
    for y in range(6, 20, 2):
        c.hline(7, 22, y, 'K')
    _prompt(c, 8, 9, 'O')
    c.hline(14, 19, 13, 'O')
    c.pixels([(26, 18), (26, 20)], '2')
    c.outline()


@icon('com.raggesilver.BlackBox', ['blackbox-terminal', 'blackbox', 'black-box'], DEV, 'Black Box')
def blackbox(c):
    c.poly([(16, 2.5), (28, 9), (28, 23), (16, 29.5), (4, 23), (4, 9)], 'k')
    c.poly([(16, 2.5), (28, 9), (16, 15.5), (4, 9)], 's')
    c.poly([(16, 15.5), (28, 9), (28, 23), (16, 29.5)], 'K')
    c.sprite(7, 15, """
        W....
        .WW..
        ...W.
        .WW..
        W....
    """)
    c.outline()


@icon('org.gnome.Ptyxis', ['ptyxis', 'org.gnome.Ptyxis.Devel', 'Ptyxis'], DEV, 'Ptyxis')
def ptyxis(c):
    c.rrect(3, 4, 28, 27, 'k', 5)
    c.bevel(['k'], dark=False)
    c.rect(3, 8, 28, 9, 'R')
    c.rect(3, 4, 28, 7, 's') if False else None
    _prompt(c, 8, 13, 'W')
    c.rect(4, 4, 27, 7, 'S')
    c.rrect(3, 4, 28, 7, 'S', 2) if False else None
    c.outline()


@icon('rio', ['rio-terminal', 'com.rioterm.Rio', 'rioterm'], DEV, 'Rio')
def rio(c):
    _win(c, 'M', 'K')
    for i, col in enumerate(['M', 'P', 'm']):
        for x in range(5, 27):
            y = 14 + i * 3 + int(2 * math.sin((x + i * 2) / 3.0))
            c.px(x, y, col)
    c.outline()


@icon('waveterm', ['dev.commandline.waveterm', 'wave', 'waveterm-bin', 'Wave'], DEV, 'Wave Terminal')
def waveterm(c):
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'], dark=False)
    for x in range(5, 28):
        y = 16 + 5 * math.sin((x - 5) / 22 * 2 * math.pi)
        c.rect(x, int(y) - 1, x, int(y) + 1, 'C')
    c.outline()


@icon('tabby', ['tabby-bin', 'tabby-terminal', 'org.tabby.Tabby', 'Tabby'], DEV, 'Tabby')
def tabby(c):
    # faceted chevron
    c.poly([(4, 3), (13, 3), (28, 16), (13, 29), (4, 29), (17, 16)], 'B')
    c.poly([(4, 3), (13, 3), (28, 16), (17, 16)], 'M')
    c.bevel(['B', 'M'])
    c.outline()


@icon('hyper', ['hyper-bin', 'co.zeit.hyper', 'Hyper', 'hyper-terminal'], DEV, 'Hyper')
def hyper(c):
    c.rrect(3, 3, 28, 28, 'K', 4)
    c.rrect(4, 4, 27, 27, 'k', 3)
    c.sprite(8, 10, """
        WW......
        .WW.....
        ..WW....
        ...WW...
        ..WW....
        .WW.....
        WW......
    """)
    c.rect(17, 20, 24, 22, 'P')
    c.outline()


@icon('org.contourterminal.Contour', ['contour', 'contour-terminal'], DEV, 'Contour')
def contour(c):
    # stacked offset windows
    c.rrect(10, 3, 28, 19, 'B', 2)
    c.rrect(3, 11, 21, 28, 'w', 2)
    c.bevel(['B', 'w'])
    c.rect(5, 15, 19, 26, 'k')
    _prompt(c, 7, 17, 'C')
    c.outline()


@icon('st', ['st-256color', 'simple-terminal', 'st-terminal', 'st-git'], DEV, 'st')
def st(c):
    c.rect(3, 6, 28, 25, 'K')
    c.rect(4, 7, 27, 24, 'k')
    c.text(7, 10, 'ST', 'W', scale=2) if False else None
    c.text(6, 9, 'S', 'W', scale=2)
    c.text(17, 9, 'T', 'W', scale=2)
    c.outline()


@icon('urxvt', ['rxvt-unicode', 'rxvt', 'urxvtc', 'urxvt-tabbed', 'rxvt-unicode-truecolor'], DEV, 'urxvt')
def urxvt(c):
    # boxy X11-era terminal with a scrollbar
    c.rect(3, 4, 28, 27, 'S')
    c.bevel(['S'])
    c.rect(5, 6, 22, 25, 'K')
    c.rect(24, 6, 26, 25, 's')
    c.rect(24, 9, 26, 14, 'w')
    c.text(6, 8, 'X', 'G', font=3)
    c.hline(10, 18, 12, 'G'); c.hline(6, 15, 16, 'G'); c.hline(6, 12, 20, 'G')
    c.outline()


@icon('termius', ['termius-app', 'com.termius.Termius', 'Termius', 'termius-beta'], DEV, 'Termius')
def termius(c):
    c.rrect(3, 3, 28, 28, 'k', 5)
    c.bevel(['k'], dark=False)
    c.sprite(7, 8, """
        ##.......
        .##......
        ..##.....
        ...##....
        ..##.....
        .##......
        ##.......
    """, {'#': 'G'})
    c.rect(16, 19, 24, 21, 'G')
    c.outline()


@icon('org.xfce.terminal', ['xfce4-terminal', 'xfce-terminal'], DEV, 'Xfce Terminal')
def xfce_terminal(c):
    _win(c, 'w')
    _prompt(c, 7, 11, 'W')
    # xfce mouse
    c.ellipse(21, 20, 4, 3, 'B')
    c.px(25, 18, 'B')
    c.outline()


@icon('lxterminal', ['lxqt-terminal'], DEV, 'LXTerminal')
def lxterminal(c):
    _win(c, 'C')
    _prompt(c, 7, 11, 'c')
    c.hline(11, 20, 18, '5'); c.hline(7, 15, 21, '5')
    c.outline()


@icon('qterminal', ['qterminal_drop'], DEV, 'QTerminal')
def qterminal(c):
    _win(c, 'B')
    c.ring(14, 17, 5, 3, 'W')
    c.line(16, 19, 19, 22, 'W', 2)
    c.hline(21, 24, 22, 'W')
    c.outline()


@icon('mate-terminal', ['org.mate.terminal'], DEV, 'MATE Terminal')
def mate_terminal(c):
    _win(c, 'G')
    _prompt(c, 7, 11, 'g')
    c.rect(13, 15, 18, 16, 'g')
    c.outline()


@icon('terminology', ['enlightenment-terminology'], DEV, 'Terminology')
def terminology(c):
    # glowing round-cornered screen in a bezel
    c.rrect(3, 4, 28, 27, 'K', 4)
    c.rrect(4, 5, 27, 26, 'k', 3)
    c.rrect(6, 7, 25, 24, '6', 3)
    c.dither(7, 8, 24, 23, '6', 'k', only='6')
    _prompt(c, 9, 12, 'C')
    c.rect(14, 16, 18, 17, 'c')
    c.outline()


@icon('sakura', ['sakura-terminal'], DEV, 'Sakura')
def sakura(c):
    # five-petal cherry blossom
    for k in range(5):
        a = math.radians(k * 72 - 90)
        c.circle(16 + 7.5 * math.cos(a), 16.5 + 7.5 * math.sin(a), 5.5, 'p')
    c.bevel(['p'])
    c.circle(16, 16.5, 3.5, 'P')
    c.pixels([(16, 16), (15, 17), (17, 17)], 'Y')
    c.outline()


@icon('com.system76.CosmicTerm', ['cosmic-term', 'cosmic-terminal'], DEV, 'COSMIC Terminal')
def cosmic_term(c):
    _win(c, 'C', 'k', r=4)
    _prompt(c, 7, 11, 'C')
    c.circle(22, 20, 3, 'O')
    c.pixels([(21, 19)], 'o')
    c.outline()


@icon('deepin-terminal', ['com.deepin.terminal', 'deepin-terminal-gtk'], DEV, 'Deepin Terminal')
def deepin_terminal(c):
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'], dark=False)
    _prompt(c, 9, 13, 'C')
    c.rect(15, 16, 21, 17, 'C')
    c.outline()


@icon('termite', ['termite-terminal'], DEV, 'Termite')
def termite(c):
    # little bug
    c.ellipse(16, 21.5, 6, 6.5, 'N')
    c.circle(16, 12, 4, 'N')
    c.circle(16, 6.5, 3.5, 'O')
    c.bevel(['N', 'O'])
    for y in (16, 21, 25):
        c.line(10, y, 4, y - 3, 'k'); c.line(21, y, 27, y - 3, 'k')
    c.line(14, 4, 11, 3, 'k'); c.line(17, 4, 20, 3, 'k')
    c.outline()


@icon('tmux', ['tmux-terminal'], DEV, 'tmux')
def tmux(c):
    c.rect(3, 4, 28, 27, 'k')
    c.vline(15, 4, 23, 'S')
    c.hline(16, 28, 13, 'S')
    c.rect(3, 24, 28, 27, 'G')
    c.bevel(['G'])
    _prompt(c, 5, 7, 'w')
    c.text(5, 25, '0', 'k', font=3) if False else None
    c.rect(5, 25, 9, 26, '4')
    c.outline()


@icon('zellij', ['zellij-bin'], DEV, 'Zellij')
def zellij(c):
    # stacked orange/green panes
    c.rect(3, 3, 17, 17, 'O')
    c.rect(14, 14, 28, 28, 'G')
    c.rect(3, 19, 12, 28, 'Y')
    c.rect(19, 3, 28, 12, 'R')
    c.bevel(['O', 'G', 'Y', 'R'], dark=False)
    c.outline()


# ====================================================================== containers / k8s

@icon('io.podman_desktop.PodmanDesktop', ['podman-desktop', 'podman-desktop-bin', 'podman', 'PodmanDesktop'], DEV,
      'Podman Desktop')
def podman_desktop(c):
    # seal face
    c.ellipse(16, 16.5, 13, 11.5, 'M')
    c.bevel(['M'])
    c.circle(10.5, 13, 2.5, 'W'); c.circle(21.5, 13, 2.5, 'W')
    c.rect(10, 13, 11, 14, 'K'); c.rect(21, 13, 22, 14, 'K')
    c.ellipse(16, 20, 5, 3, 'm')
    c.rect(15, 18, 16, 19, 'K')
    for y in (19, 21):
        c.hline(6, 9, y, 'm'); c.hline(22, 25, y, 'm')
    c.outline()


@icon('rancher-desktop', ['io.rancherdesktop.app', 'rancher-desktop-bin', 'rancher'], DEV, 'Rancher Desktop')
def rancher_desktop(c):
    # bull head
    c.poly([(3, 4), (8, 11), (12, 9)], 'w')
    c.poly([(29, 4), (24, 11), (20, 9)], 'w')
    c.rrect(7, 8, 24, 22, 'B', 4)
    c.rrect(10, 18, 21, 28, 'B', 3)
    c.bevel(['B', 'w'])
    c.rect(11, 13, 12, 14, 'W'); c.rect(19, 13, 20, 14, 'W')
    c.rect(12, 23, 13, 24, '6'); c.rect(18, 23, 19, 24, '6')
    c.outline()


def _lens(c, col):
    c.circle(16, 16, 13, col)
    c.bevel([col])
    for k in range(6):
        a = math.radians(k * 60)
        b = math.radians(k * 60 + 60)
        c.line(16 + 4 * math.cos(a), 16 + 4 * math.sin(a), 16 + 11 * math.cos(b - .4), 16 + 11 * math.sin(b - .4),
               DARK_OF[col])
    c.circle(16, 16, 4, 'K')


DARK_OF = {'B': '6', 'C': '5', 'O': '2'}


@icon('lens', ['lens-desktop', 'lens-bin', 'dev.k8slens.Lens', 'Lens', 'lens-ide'], DEV, 'Lens')
def lens(c):
    _lens(c, 'B')
    c.outline()


@icon('dev.k8slens.OpenLens', ['openlens', 'openlens-bin', 'OpenLens'], DEV, 'OpenLens')
def openlens(c):
    _lens(c, 'C')
    c.outline()


@icon('app.freelens.Freelens', ['freelens', 'freelens-bin', 'Freelens'], DEV, 'Freelens')
def freelens(c):
    _lens(c, 'O')
    c.outline()


@icon('k9s', ['k9s-bin', 'k9s-git'], DEV, 'k9s')
def k9s(c):
    # dog head with floppy ears
    c.rrect(7, 5, 24, 24, 'n', 6)
    c.rrect(3, 5, 9, 19, 'N', 3)
    c.rrect(22, 5, 28, 19, 'N', 3)
    c.ellipse(16, 22, 6, 5, 'W')
    c.bevel(['n', 'N'])
    c.rect(11, 12, 12, 14, 'K'); c.rect(19, 12, 20, 14, 'K')
    c.rect(14, 19, 17, 21, 'K')
    c.rect(15, 24, 16, 28, 'R')
    c.outline()


@icon('portainer', ['portainer-desktop', 'io.portainer.Portainer'], DEV, 'Portainer')
def portainer(c):
    # crane lifting containers
    c.rect(8, 3, 10, 28, 'C')
    c.rect(3, 6, 28, 8, 'C')
    c.vline(23, 9, 14, 'k')
    c.rect(18, 15, 28, 21, 'B')
    c.rect(13, 22, 28, 28, 'B')
    c.bevel(['C', 'B'])
    for x in (21, 24):
        c.vline(x, 16, 20, '6')
    for x in (16, 19, 22, 25):
        c.vline(x, 23, 27, '6')
    c.outline()


@icon('com.github.marhkb.Pods', ['pods', 'Pods'], DEV, 'Pods')
def pods(c):
    # pea pod
    c.poly([(3, 20), (8, 12), (18, 6), (28, 4), (25, 13), (17, 22), (6, 26)], 'G')
    c.bevel(['G'])
    for x, y in ((9, 18), (14, 14), (19, 10)):
        c.circle(x + .5, y + .5, 3, 'g')
        c.px(x - 1, y - 1, 'W')
    c.outline()


@icon('kubernetes', ['kubectl', 'k8s', 'kubernetes-dashboard', 'kube'], DEV, 'Kubernetes')
def kubernetes(c):
    pts = [(16 + 13.5 * math.cos(math.radians(-90 + k * 360 / 7)), 16 + 13.5 * math.sin(math.radians(-90 + k * 360 / 7)))
           for k in range(7)]
    c.poly(pts, 'B')
    c.bevel(['B'])
    c.ring(16, 16.5, 7, 5, 'W')
    for k in range(7):
        a = math.radians(-90 + k * 360 / 7)
        c.line(16 + 2 * math.cos(a), 16.5 + 2 * math.sin(a), 16 + 9.5 * math.cos(a), 16.5 + 9.5 * math.sin(a), 'W')
    c.circle(16, 16.5, 2, 'W')
    c.outline()


@icon('helm', ['helm-bin', 'helm-chart'], DEV, 'Helm')
def helm(c):
    # ship's wheel
    for k in range(8):
        a = math.radians(k * 45)
        c.line(16 + 3 * math.cos(a), 16 + 3 * math.sin(a), 16 + 11.6 * math.cos(a), 16 + 11.6 * math.sin(a), 'B', 2)
    c.ring(16, 16, 10.5, 7.5, 'B')
    c.circle(16, 16, 3.5, 'B')
    c.bevel(['B'])
    c.outline()


@icon('io.kinvolk.Headlamp', ['headlamp', 'Headlamp', 'headlamp-bin'], DEV, 'Headlamp')
def headlamp(c):
    c.poly([(3, 10), (16, 15), (16, 18), (3, 23)], 'Y')
    c.rrect(14, 7, 28, 26, 'B', 3)
    c.bevel(['B', 'Y'])
    c.circle(21, 16.5, 4.5, 'y')
    c.circle(21, 16.5, 2.5, 'W')
    c.outline()


@icon('distrobox', ['distrobox-assemble', 'distroshelf', 'com.ranfdev.DistroShelf'], DEV, 'Distrobox')
def distrobox(c):
    # open cardboard box with distro balls
    c.circle(11, 11, 4, 'B'); c.circle(19, 9, 4, 'G'); c.circle(15, 14, 3, 'R')
    c.rect(4, 14, 27, 28, 'n')
    c.poly([(4, 14), (9, 10), (12, 14)], 'N')
    c.poly([(27, 14), (23, 10), (20, 14)], 'N')
    c.bevel(['n', 'B', 'G', 'R'])
    c.rect(13, 14, 18, 19, 'N')
    c.outline()


@icon('io.github.dvlv.boxbuddyrs', ['boxbuddy', 'boxbuddyrs', 'BoxBuddy'], DEV, 'BoxBuddy')
def boxbuddy(c):
    c.rect(4, 9, 27, 27, 'n')
    c.poly([(4, 9), (9, 3), (12, 9)], 'N')
    c.poly([(27, 9), (22, 3), (19, 9)], 'N')
    c.bevel(['n', 'N'])
    c.rect(10, 15, 11, 17, 'K'); c.rect(20, 15, 21, 17, 'K')
    c.hline(13, 18, 21, '8'); c.px(12, 20, '8'); c.px(19, 20, '8')
    c.outline()


@icon('toolbox', ['org.containers.toolbox', 'toolbx'], DEV, 'Toolbx')
def toolbox(c):
    c.rrect(10, 4, 21, 9, 'S', 2)
    c.rect(12, 6, 19, 9, '.')
    c.rect(3, 9, 28, 27, 'R')
    c.bevel(['R', 'S'])
    c.rect(3, 15, 28, 16, '1')
    c.rect(13, 14, 18, 18, 'Y')
    c.outline()


@icon('incus', ['lxd', 'linuxcontainers', 'incus-ui'], DEV, 'Incus')
def incus(c):
    for (x, y), col in (((3, 15), 'O'), ((16, 15), 'O'), ((9.5, 3), 'o')):
        c.rect(int(x), y, int(x) + 12, y + 12, col)
    c.bevel(['O', 'o'])
    c.outline()


# ------------------------------------------------------------ HashiCorp family
@icon('terraform', ['terraform-bin', 'opentofu', 'tofu'], DEV, 'Terraform')
def terraform(c):
    for pts in ([(4, 3), (11, 7), (11, 15), (4, 11)], [(13, 8), (20, 12), (20, 20), (13, 16)],
                [(22, 12), (28, 8.5), (28, 16.5), (22, 20)], [(13, 18), (20, 22), (20, 29), (13, 25)]):
        c.poly(pts, 'M')
    c.bevel(['M'])
    c.outline()


@icon('vagrant', ['vagrant-bin'], DEV, 'Vagrant')
def vagrant(c):
    c.poly([(3, 4), (11, 4), (16, 19), (21, 4), (29, 4), (19, 28), (13, 28)], 'B')
    c.poly([(3, 4), (8, 4), (8, 8), (6, 11)], '6')
    c.poly([(29, 4), (24, 4), (24, 8), (26, 11)], '6')
    c.bevel(['B'])
    c.outline()


@icon('vault', ['hashicorp-vault', 'vault-bin'], DEV, 'Vault')
def vault(c):
    c.poly([(3, 5), (29, 5), (16, 29)], 'Y')
    c.bevel(['Y'])
    for x, y in ((12, 9), (15, 9), (18, 9), (15, 13), (18, 13), (15, 17)):
        c.rect(x, y, x + 1, y + 1, 'k')
    c.rect(12, 13, 13, 14, 'k')
    c.outline()


@icon('consul', ['hashicorp-consul', 'consul-bin'], DEV, 'Consul')
def consul(c):
    c.arc(16, 16, 13, 7.5, 50, 310, 'P')
    c.bevel(['P'])
    c.circle(16, 16, 3, 'P')
    for x, y in ((23, 11), (26, 15), (23, 19), (26, 21), (26, 9)):
        c.rect(x, y, x + 1, y + 1, 'P')
    c.outline()


@icon('nomad', ['hashicorp-nomad', 'nomad-bin'], DEV, 'Nomad')
def nomad(c):
    pts = [(16 + 13.5 * math.cos(math.radians(a)), 16 + 13.5 * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
    c.poly(pts, 'G')
    c.bevel(['G'])
    c.poly([(10, 11), (13, 9.5), (19, 16), (19, 10), (22, 8.5), (22, 21), (19, 22.5), (13, 16), (13, 22), (10, 23.5)],
           'W')
    c.outline()


@icon('packer', ['hashicorp-packer', 'packer-bin'], DEV, 'Packer')
def packer(c):
    c.poly([(6, 3), (13, 7), (13, 29), (6, 25)], 'B')
    c.poly([(15, 8), (23, 12), (26, 15), (26, 21), (22, 24), (15, 20)], 'b')
    c.bevel(['B'])
    c.rect(15, 14, 21, 17, '6')
    c.outline()


@icon('pulumi', ['pulumi-bin'], DEV, 'Pulumi')
def pulumi(c):
    for (x, y), col in (((9, 7), 'M'), ((21, 7), 'P'), ((15, 16), 'm'), ((9, 25), 'P'), ((21, 25), 'M')):
        c.ellipse(x + .5, y + .5, 5.5, 3.5, col)
    c.bevel(['M', 'P'])
    c.outline()


@icon('ansible', ['ansible-core', 'ansible-navigator', 'ansible-bin'], DEV, 'Ansible')
def ansible(c):
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'], dark=False)
    c.poly([(14.5, 6), (17.5, 6), (24, 23), (21, 23), (16, 10), (11, 23), (8, 23)], 'W')
    c.poly([(13, 17), (16, 15), (23, 21)], 'W')
    c.outline()


# ------------------------------------------------------------ cloud CLIs / consoles
@icon('aws-cli', ['aws', 'awscli', 'aws-cli-v2', 'amazon-web-services', 'aws-vpn-client'], DEV, 'AWS')
def aws(c):
    c.rrect(3, 5, 28, 21, 'k', 3)
    c.bevel(['k'], dark=False)
    c.text(5, 8, 'AWS', 'W', font=3, gap=1) if False else None
    c.sprite(6, 8, """
        .#..#...#.###
        #.#.#...#.#..
        ###.#.#.#.###
        #.#.#.#.#...#
        #.#..#.#..###
    """, {'#': 'W'})
    # the smile arrow
    c.arc(16, 6, 15, 12.5, 50, 130, 'O')
    c.poly([(23, 23), (28, 21), (27, 26)], 'O')
    c.outline()


@icon('google-cloud-sdk', ['gcloud', 'google-cloud-cli', 'google-cloud-console'], DEV, 'Google Cloud')
def gcloud(c):
    c.circle(11, 18, 7, 'G')
    c.circle(18, 13, 9, 'R')
    c.circle(23.5, 19, 5.5, 'Y')
    c.rrect(5, 18, 28, 26, 'B', 3)
    c.bevel(['R', 'B'])
    c.rrect(10, 14, 22, 22, 'W', 3)
    c.outline()


@icon('azure-cli', ['az', 'azure-data-cli'], DEV, 'Azure')
def azure(c):
    c.poly([(12, 3), (19, 3), (11, 27), (3, 27)], 'B')
    c.poly([(19, 3), (29, 27), (13, 27), (22, 21), (17, 13)], 'b')
    c.bevel(['B'])
    c.outline()

