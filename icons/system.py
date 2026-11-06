from pix import icon

"""System tools & utilities: settings, disks, capture, accessories, archives,
hardware, network/transfer and alternative file managers."""

import math


# ------------------------------------------------------------------ helpers
def gear(c, cx, cy, r_out, r_body, teeth, col, hole=0, phase=0, tooth=0.5):
    """Toothed gear: body disc + square-ish teeth; optional transparent hole."""
    c.circle(cx, cy, r_body, col)
    step = 360 / teeth
    half = step * tooth / 2
    for i in range(teeth):
        a = phase + i * step
        c.arc(cx, cy, r_out, r_body - 1, a - half, a + half, col)
    if hole:
        c.circle(cx, cy, hole, '.')


def rows(art):
    ls = [l.strip() for l in art.strip('\n').split('\n')]
    return len(ls[0]), len(ls)


# ================================================================== settings
@icon('org.gnome.Settings', ['gnome-control-center', 'preferences-system', 'systemsettings',
                             'preferences-desktop', 'gnome-settings',
                             'xfce4-settings-manager', 'org.kde.systemsettings'], 'system', 'Settings')
def settings(c):
    gear(c, 14, 14, 12, 9, 8, 'S', phase=22.5, tooth=0.45)
    c.bevel(['S'])
    c.circle(14, 14, 5, 's')
    c.circle(14, 14, 3, '.')
    # wrench across the lower right, open jaw facing out
    c.line(14, 14, 22, 22, 'w', 3)
    c.circle(24.5, 24.5, 4.5, 'w')
    c.pixels([(x, y) for y in range(20, 32) for x in range(20, 32)
              if abs(x - y) <= 1 and x + y >= 50], '.')
    c.bevel(['w'], light=False)
    c.line(15, 14, 21, 20, 'W')
    c.circle(14, 14, 2.5, '.')
    c.outline()


@icon('nwg-look', ['nwg-look-gtk', 'preferences-desktop-theme', 'preferences-desktop-appearance',
                   'lxappearance', 'qt5ct', 'qt6ct', 'kvantummanager'], 'system', 'nwg-look')
def nwg_look(c):
    # painter's palette with paint blobs
    c.ellipse(16, 16, 13.5, 11, 'n')
    c.circle(21, 21, 3, '.')
    c.ellipse(28, 21.5, 3.5, 2.5, '.')
    c.bevel(['n'])
    for (x, y, col) in [(9, 10, 'R'), (15, 8, 'Y'), (21, 10, 'G'), (8, 17, 'B'), (13, 21, 'M')]:
        c.rect(x, y, x + 2, y + 2, col)
    c.outline()


@icon('nwg-displays', ['preferences-desktop-display', 'display', 'wdisplays', 'arandr',
                       'video-display', 'org.kde.kscreen'], 'system', 'nwg-displays')
def nwg_displays(c):
    # two monitors, arranged side by side & offset
    c.rect(13, 3, 28, 15, 'k')
    c.rect(14, 4, 27, 14, 'C')
    c.bevel(['C'])
    c.rect(3, 9, 20, 23, 'k')
    c.rect(4, 10, 19, 22, 'B')
    c.bevel(['B'])
    c.text(9, 13, '1', 'W', font=3)
    c.text(14 + 7, 6, '2', 'W', font=3)
    c.rect(10, 24, 13, 25, 's')
    c.rect(6, 26, 17, 27, 'S')
    c.hline(6, 17, 26, 'w')
    c.outline()


@icon('blueman', ['bluetooth', 'blueman-manager', 'preferences-system-bluetooth', 'blueman-device',
                  'bluetooth-active', 'org.blueman.Manager', 'blueberry', 'overskride',
                  'io.github.kaii_lb.Overskride'], 'system', 'Bluetooth')
def blueman(c):
    c.ellipse(16, 16, 10, 13.5, 'B')
    c.bevel(['B'])
    c.sprite(11, 9, """
        ....##.....
        ....###....
        ....####...
        #...##.##..
        ##..##..##.
        .##.##.##..
        ..######...
        ...####....
        ..######...
        .##.##.##..
        ##..##..##.
        #...##.##..
        ....####...
        ....###....
        ....##.....
    """, {'#': 'W'})
    c.outline()


@icon('nm-connection-editor', ['network-manager', 'preferences-system-network', 'network-wireless',
                               'nm-applet', 'network-wireless-signal-excellent', 'gnome-nettool',
                               'org.gnome.NetworkDisplays', 'iwgtk', 'impala'], 'system', 'Network')
def nm_editor(c):
    cx, cy = 16, 27
    c.arc(cx, cy, 15.5, 0, 210, 330, 'B')
    c.arc(cx, cy, 12, 10, 200, 340, 'k')
    c.arc(cx, cy, 7.5, 5.5, 200, 340, 'k')
    c.bevel(['B'], dark=False)
    c.outline()


@icon('org.gnome.tweaks', ['gnome-tweaks', 'gnome-tweak-tool', 'org.gnome.TweakTool',
                           'preferences-other'], 'system', 'Tweaks')
def tweaks(c):
    c.rrect(3, 3, 28, 14, 'G', 5)
    c.bevel(['G'])
    c.circle(22.5, 8.5, 4.5, 'W')
    c.arc(22.5, 8.5, 4.5, 3.5, 0, 140, 'w')
    c.rrect(3, 17, 28, 28, 'S', 5)
    c.bevel(['S'])
    c.circle(9.5, 22.5, 4.5, 'W')
    c.arc(9.5, 22.5, 4.5, 3.5, 0, 140, 'w')
    c.outline()


@icon('dconf-editor', ['ca.desrt.dconf-editor', 'dconf', 'gconf-editor'], 'system', 'dconf Editor')
def dconf(c):
    # settings key tree: root node branching into two leaves
    c.rect(15, 9, 16, 15, 's')
    c.rect(7, 14, 24, 15, 's')
    c.rect(7, 14, 8, 19, 's')
    c.rect(23, 14, 24, 19, 's')
    c.rrect(9, 3, 22, 10, 'O', 1)
    c.rrect(3, 19, 13, 27, 'B', 1)
    c.rrect(18, 19, 28, 27, 'G', 1)
    c.bevel(['O', 'B', 'G'])
    c.hline(12, 19, 6, '2'); c.hline(12, 16, 8, '2')
    c.hline(5, 10, 22, '6'); c.hline(5, 8, 24, '6')
    c.hline(20, 25, 22, '4'); c.hline(20, 23, 24, '4')
    c.outline()


@icon('com.mattjakeman.ExtensionManager', ['extension-manager', 'org.gnome.Extensions',
                                           'gnome-extensions', 'gnome-extensions-app'],
      'system', 'Extension Manager')
def extman(c):
    c.rect(3, 8, 23, 28, 'B')
    c.circle(13, 6.5, 3.5, 'B')
    c.circle(25.5, 18, 3.5, 'B')
    c.circle(3, 18, 3.5, '.')
    c.rect(0, 15, 2, 21, '.')
    c.bevel(['B'])
    c.outline()


@icon('com.github.tchx84.Flatseal', ['flatseal'], 'system', 'Flatseal')
def flatseal(c):
    # ribbons
    c.poly([(9, 17), (14, 19), (13, 28.5), (10.5, 26), (7, 28.5)], 'R')
    c.poly([(23, 17), (18, 19), (19, 28.5), (21.5, 26), (25, 28.5)], 'R')
    c.bevel(['R'])
    # scalloped wax seal
    c.circle(16, 13.5, 9, 'B')
    for i in range(12):
        a = math.radians(i * 30 + 15)
        c.circle(16 + 9.5 * math.cos(a), 13.5 + 9.5 * math.sin(a), 2.5, 'B')
    c.bevel(['B'])
    c.ring(16, 13, 7.5, 6.5, '6')
    c.sprite(11, 9, """
        .......##
        ......##.
        ##...##..
        .##.##...
        ..###....
        ...#.....
    """, {'#': 'W'})
    c.outline()


# ================================================================== disks / backup
@icon('gparted', ['GParted', 'partitionmanager', 'org.kde.partitionmanager'], 'system', 'GParted')
def gparted(c):
    c.rrect(3, 7, 28, 25, 'S', 1)
    c.bevel(['S'])
    # partition map bar
    c.rect(5, 9, 26, 17, 'K')
    c.rect(6, 10, 11, 16, 'M')
    c.rect(13, 10, 20, 16, 'G')
    c.rect(22, 10, 25, 16, 'Y')
    c.hline(6, 11, 10, 'm'); c.hline(13, 20, 10, 'g'); c.hline(22, 25, 10, 'y')
    c.rect(6, 20, 15, 21, 's')
    c.px(24, 21, 'G')
    c.outline()


@icon('org.gnome.baobab', ['baobab', 'disk-usage-analyzer', 'filelight', 'org.kde.filelight',
                           'qdirstat', 'k4dirstat'], 'system', 'Disk Usage')
def baobab(c):
    c.line(19, 19, 25, 25, 'N', 3)
    c.line(20, 19, 26, 25, 'n')
    c.circle(13, 13, 10.5, 'S')
    c.circle(13, 13, 9, 'W')
    c.arc(13, 13, 8, 3.5, 270, 30, 'R')
    c.arc(13, 13, 8, 3.5, 30, 140, 'B')
    c.arc(13, 13, 8, 3.5, 140, 220, 'G')
    c.arc(13, 13, 8, 3.5, 220, 270, 'Y')
    c.circle(13, 13, 2.5, 'W')
    c.bevel(['S'])
    c.outline()


@icon('timeshift', ['timeshift-gtk', 'backup', 'org.kde.kbackup', 'snapper-gui', 'btrfs-assistant', 'preferences-system-time'], 'system', 'Timeshift')
def timeshift(c):
    # clock face wrapped in a rewind arrow
    c.arc(16, 16, 12.5, 9.5, 300, 186, 'G')
    c.poly([(2.5, 13), (9.5, 13), (6, 18)], 'G')
    c.bevel(['G'])
    c.circle(16, 16, 9, 'W')
    c.ring(16, 16, 9, 8, 'w')
    c.vline(16, 10, 16, 'k')
    c.hline(16, 20, 16, 'k')
    c.px(16, 16, 'R')
    c.outline()


@icon('org.gnome.DejaDup', ['deja-dup', 'pika-backup', 'org.gnome.World.PikaBackup',
                            'vorta', 'com.borgbase.Vorta'], 'system', 'Déjà Dup')
def dejadup(c):
    # a vault
    c.rrect(3, 3, 28, 26, 'S', 1)
    c.bevel(['S'])
    c.rect(5, 5, 26, 24, 's')
    c.rect(6, 6, 25, 23, 'S')
    c.hline(6, 25, 6, 'w'); c.vline(6, 6, 23, 'w')
    c.circle(15, 14.5, 6, 'k')
    c.circle(15, 14.5, 5, 'w')
    c.circle(15, 14.5, 2, 's')
    for (x, y) in [(15, 10), (15, 19), (11, 14), (19, 14)]:
        c.px(x, y, 'k')
    c.rect(22, 11, 23, 18, 'R')
    c.vline(22, 11, 18, 'r')
    c.rect(5, 27, 8, 28, 'k')
    c.rect(23, 27, 26, 28, 'k')
    c.outline()


@icon('bleachbit', ['org.bleachbit.BleachBit', 'bleachbit-root', 'sweeper', 'org.kde.sweeper'],
      'system', 'BleachBit')
def bleachbit(c):
    # bleach jug with handle and cap
    c.rrect(5, 9, 24, 28, 'W', 2)
    c.rrect(17, 5, 27, 18, 'W', 2)
    c.rect(20, 8, 24, 14, '.')
    c.rect(9, 3, 14, 7, 'B')
    c.hline(9, 14, 3, 'b')
    c.rect(8, 7, 15, 9, 'W')
    c.bevel(['W'], light=False)
    c.rect(7, 15, 22, 24, 'B')
    c.bevel(['B'])
    c.sprite(11, 16, """
        ..#....
        .###...
        #####..
        #####..
        .###.#.
        .....#.
    """, {'#': 'W'})
    c.outline()


@icon('stacer', ['io.github.oguzhaninan.Stacer', 'system-optimizer'],
      'system', 'Stacer')
def stacer(c):
    # a rocket — speed up your system
    c.poly([(11, 13), (5, 20), (5, 24), (11, 20)], 'R')
    c.poly([(21, 13), (27, 20), (27, 24), (21, 20)], 'R')
    c.ellipse(16, 14, 6, 11.5, 'W')
    c.rect(10, 21, 22, 31, '.')
    c.rect(12, 21, 19, 21, 'W')
    c.replace('W', 'R', (0, 0, 31, 7))
    c.bevel(['W', 'R'])
    c.circle(16, 12.5, 2.5, 'B')
    c.px(15, 11, 'b')
    c.rect(13, 22, 18, 22, 's')
    c.rect(13, 23, 18, 25, 'O')
    c.rect(14, 26, 17, 27, 'O')
    c.rect(14, 23, 17, 24, 'Y')
    c.rect(15, 25, 16, 27, 'Y')
    c.vline(16, 28, 28, 'O') if False else None
    c.outline()


# ================================================================== capture
@icon('flameshot', ['org.flameshot.Flameshot', 'flameshot-tray'], 'system', 'Flameshot')
def flameshot(c):
    c.circle(16, 19, 10, 'R')
    c.poly([(7, 17), (13, 2), (16, 9), (20, 4), (25.5, 17)], 'R')
    c.circle(16, 21, 7, 'O')
    c.poly([(10, 19), (14, 9), (17, 15), (20, 11), (22.5, 19)], 'O')
    c.circle(16, 23, 4, 'Y')
    c.poly([(12.5, 22), (15, 15), (19.5, 22)], 'Y')
    c.bevel(['R'])
    c.px(15, 24, 'y'); c.px(14, 23, 'y')
    c.outline()


def big(c, x, y, art, col, scale=2):
    for j, line in enumerate(l.strip() for l in art.strip('\n').split('\n')):
        for i, ch in enumerate(line):
            if ch == '#':
                c.rect(x + i * scale, y + j * scale, x + i * scale + scale - 1, y + j * scale + scale - 1, col)


@icon('org.gnome.Screenshot', ['gnome-screenshot', 'applets-screenshooter', 'accessories-screenshot',
                               'screengrab', 'spectacle', 'org.kde.spectacle', 'ksnip',
                               'org.ksnip.ksnip', 'hyprshot', 'grim'], 'system', 'Screenshot')
def screenshot(c):
    c.rect(4, 6, 25, 23, 'c')
    c.circle(20, 11, 2.5, 'y')
    c.poly([(4, 23.5), (11, 14), (18, 23.5)], 'G')
    c.poly([(13, 23.5), (18, 17), (25.5, 23.5)], '4')
    # marching-ants selection
    for x in range(3, 27):
        c.px(x, 5, 'W' if x % 4 < 2 else 'k'); c.px(x, 24, 'W' if x % 4 < 2 else 'k')
    for y in range(5, 25):
        c.px(3, y, 'W' if y % 4 < 2 else 'k'); c.px(26, y, 'W' if y % 4 < 2 else 'k')
    # crosshair cursor
    c.rect(24, 20, 25, 28, 'W')
    c.rect(21, 23, 28, 24, 'W')
    c.rect(24, 23, 25, 24, 'R')
    c.outline()


@icon('satty', ['com.gabm.satty', 'swappy', 'annotator', 'com.github.phase1geo.annotator',
                'gradia', 'be.alexandervanhee.gradia'], 'system', 'Satty')
def satty(c):
    c.rect(4, 4, 22, 25, 'W')
    c.shade_below(['W'], 'w')
    c.rect(6, 6, 20, 22, 'b')
    c.poly([(6, 22.5), (11, 15), (16, 22.5)], 'B')
    c.ring(13, 12, 5.5, 4.2, 'R')
    # yellow pencil
    c.line(27, 7, 17, 17, 'Y', 3)
    c.line(28, 7, 18, 17, 'y')
    c.line(26, 10, 18, 18, '3')
    c.poly([(16.5, 17.5), (19.5, 20.5), (14, 23)], 'n')
    c.pixels([(15, 21), (14, 22)], 'k')
    c.rect(26, 5, 28, 7, 'P')
    c.rect(27, 4, 28, 4, 'P')
    c.outline()


@icon('org.gnome.Calculator', ['gnome-calculator', 'accessories-calculator', 'kcalc', 'org.kde.kcalc',
                               'galculator', 'speedcrunch', 'org.speedcrunch.SpeedCrunch',
                               'calculator'], 'utility', 'Calculator')
def calculator(c):
    c.rrect(6, 3, 25, 28, 'S', 2)
    c.bevel(['S'])
    c.rect(8, 5, 23, 11, 'k')
    c.rect(9, 6, 22, 10, 'g')
    c.text(15, 6, '42', '4', font=3)
    c.hline(9, 22, 10, 'G') if False else None
    for j in range(4):
        for i in range(4):
            x, y = 8 + i * 4, 13 + j * 4
            col = 'O' if (i == 3) else 'w'
            if i == 3 and j >= 2:
                continue
            c.rect(x, y, x + 2, y + 2, col)
            c.hline(x, x + 2, y + 2, 's' if col == 'w' else '2')
    c.rect(20, 21, 22, 27, 'O')
    c.hline(20, 22, 27, '2')
    c.outline()


@icon('qalculate', ['qalculate-gtk', 'io.github.Qalculate', 'qalculate-qt', 'io.github.Qalculate.qalculate-qt'],
      'utility', 'Qalculate!')
def qalculate(c):
    # dark scientific calculator: blue LCD, coloured function keys
    c.rrect(6, 3, 25, 28, 'k', 2)
    c.bevel(['k'])
    c.rect(8, 5, 23, 11, 'K')
    c.rect(9, 6, 22, 10, 'b')
    c.text(10, 6, 'F', 'K', font=3)
    c.sprite(14, 6, """
        #...#
        .#.#.
        ..#..
        .#.#.
        #...#
    """, {'#': 'K'})
    c.pixels([(13, 6), (13, 10), (20, 6), (20, 10)], 'K') if False else None
    c.vline(13, 6, 10, '6'); c.vline(20, 6, 10, '6')
    for j in range(4):
        for i in range(4):
            x, y = 8 + i * 4, 13 + j * 4
            col = 'B' if j == 0 else ('Y' if (i, j) == (3, 3) else 'S')
            c.rect(x, y, x + 2, y + 2, col)
            c.hline(x, x + 2, y + 2, {'B': '6', 'Y': '3', 'S': 's'}[col])
    c.outline()


@icon('org.gnome.clocks', ['gnome-clocks', 'clock', 'alarm-clock', 'kclock', 'org.kde.kclock',
                           'preferences-system-time-clock'], 'utility', 'Clocks')
def clocks(c):
    c.line(8, 23, 5, 26, 'k', 2)
    c.line(23, 23, 26, 26, 'k', 2)
    c.circle(8, 8, 4.5, 'Y')
    c.circle(24, 8, 4.5, 'Y')
    c.bevel(['Y'])
    c.rect(15, 3, 16, 6, 's')
    c.circle(16, 16, 11, 'R')
    c.bevel(['R'])
    c.circle(16, 16, 8, 'W')
    c.ring(16, 16, 8, 7, 'w')
    c.vline(16, 11, 16, 'k')
    c.line(16, 16, 19, 19, 'k')
    c.pixels([(16, 9), (23, 16), (16, 23), (9, 16)], 'S')
    c.outline()


@icon('org.gnome.Weather', ['gnome-weather', 'weather', 'org.gnome.Weather.Application', 'weather-few-clouds',
                            'io.github.amit9838.mousam', 'mousam'], 'utility', 'Weather')
def weather(c):
    c.circle(12, 12, 9, 'Y')
    c.bevel(['Y'])
    c.ring(12, 12, 9, 8, 'O') if False else None
    c.px(9, 8, 'W'); c.px(8, 9, 'y')
    c.circle(15, 20, 5, 'W')
    c.circle(21.5, 18, 6, 'W')
    c.rrect(6, 20, 28, 27, 'W', 3)
    c.shade_below(['W'], 'w')
    c.px(17, 15, 'W')
    c.outline()


@icon('org.gnome.Calendar', ['gnome-calendar', 'calendar', 'office-calendar', 'x-office-calendar',
                             'korganizer', 'org.kde.korganizer', 'org.kde.merkuro.calendar'], 'utility',
      'Calendar')
def calendar(c):
    c.rrect(3, 5, 28, 28, 'W', 1)
    c.shade_below(['W'], 'w')
    c.rect(3, 5, 28, 11, 'R')
    c.hline(4, 27, 5, 'r')
    c.hline(3, 28, 11, '1')
    c.rect(8, 3, 9, 7, 'k'); c.rect(22, 3, 23, 7, 'k')
    c.text(6, 13, '17', 'k', font=5, scale=2, gap=0) if False else None
    big(c, 6, 13, """
        .#..####
        ##.....#
        .#....#.
        .#....#.
        ###...#.
    """, 'k', 2)
    c.outline()


@icon('org.gnome.Contacts', ['gnome-contacts', 'contacts', 'x-office-address-book', 'office-address-book',
                             'kaddressbook', 'org.kde.kaddressbook', 'evolution-addressbook'], 'utility',
      'Contacts')
def contacts(c):
    c.rect(26, 7, 28, 10, 'R'); c.rect(26, 13, 28, 16, 'Y'); c.rect(26, 19, 28, 22, 'G')
    c.rrect(4, 3, 25, 28, 'B', 1)
    c.bevel(['B'])
    c.rect(4, 3, 7, 28, '6')
    c.vline(7, 3, 28, 'K') if False else None
    c.circle(16.5, 12, 3.5, 'W')
    c.ellipse(16.5, 23, 6.5, 5, 'W')
    c.rect(9, 23, 24, 26, 'B')
    c.hline(10, 23, 22, 'B') if False else None
    c.rect(4, 3, 28, 3, '.') if False else None
    c.outline()


@icon('org.gnome.Maps', ['gnome-maps', 'maps', 'marble', 'org.kde.marble',
                         'applications-geography'], 'utility', 'Maps')
def maps(c):
    c.poly([(3, 9), (11, 6), (11, 26), (3, 29)], 'G')
    c.poly([(11, 6), (20, 9), (20, 29), (11, 26)], 'g')
    c.poly([(20, 9), (28, 6), (28, 26), (20, 29)], 'G')
    c.line(3, 22, 11, 17, 'Y'); c.line(11, 17, 20, 21, 'Y'); c.line(20, 21, 28, 14, 'Y')
    c.circle(16, 9, 5.5, 'R')
    c.poly([(11.5, 11), (20.5, 11), (16, 20)], 'R')
    c.bevel(['R'])
    c.circle(16, 9, 2, 'W')
    c.outline()


@icon('org.gnome.Characters', ['gnome-characters', 'accessories-character-map', 'gucharmap',
                               'kcharselect', 'org.kde.kcharselect', 'charmap'], 'utility', 'Characters')
def characters(c):
    big(c, 3, 4, """
        ...####......
        ..##..##.....
        ..##..##.....
        ..##..##.....
        ...####......
        ..#####...##.
        .##..###.##..
        ##....####...
        ##.....###...
        ##....#####..
        .##..##..###.
        ..####....##.
    """, 'M', 2)
    c.bevel(['M'], dark=False)
    c.outline()


@icon('org.gnome.font-viewer', ['font-viewer', 'gnome-font-viewer', 'preferences-desktop-font',
                                'fontforge', 'org.fontforge.FontForge', 'kfontview', 'fonts'],
      'utility', 'Fonts')
def fonts(c):
    c.poly([(4, 27), (10, 3), (14, 3), (20, 27), (16, 27), (14.5, 21.5), (9.5, 21.5), (8, 27)], 'B')
    c.tri((10.5, 17.5), (12, 11), (13.5, 17.5), '.')
    c.rect(3, 25, 9, 27, 'B'); c.rect(15, 25, 21, 27, 'B')
    c.bevel(['B'])
    big(c, 20, 17, """
        .###.
        ....#
        .####
        #...#
        .####
    """, 'R', 2) if False else None
    c.sprite(22, 20, """
        .####..
        .....##
        .######
        ##...##
        ##...##
        .######
    """, {'#': 'R'})
    c.outline()


@icon('org.gnome.Logs', ['gnome-logs', 'logs', 'ksystemlog', 'org.kde.ksystemlog',
                         'utilities-log-viewer'], 'utility', 'Logs')
def logs(c):
    c.rect(6, 5, 25, 26, 'W')
    c.bevel(['W'], light=False)
    c.rrect(3, 3, 28, 7, 'w', 2)
    c.rrect(3, 24, 28, 28, 'w', 2)
    c.bevel(['w'])
    c.rect(3, 4, 4, 6, 'S'); c.rect(27, 25, 28, 27, 'S') if False else None
    for y, w, col in [(10, 14, 'S'), (13, 10, 'S'), (16, 12, 'R'), (19, 8, 'S')]:
        c.hline(8, 8 + w, y, col)
        c.hline(8, 8, y, col)
    c.outline()


@icon('org.gnome.SystemMonitor', ['gnome-system-monitor', 'utilities-system-monitor',
                                  'io.missioncenter.MissionCenter', 'mission-center', 'ksysguard',
                                  'org.kde.plasma-systemmonitor', 'plasma-systemmonitor', 'resources',
                                  'net.nokyan.Resources', 'xfce4-taskmanager', 'lxtask'],
      'system', 'System Monitor')
def sysmon(c):
    c.circle(16, 16, 13, 'S')
    c.bevel(['S'])
    c.circle(16, 16, 11, 'k')
    c.arc(16, 16, 10, 7.5, 135, 200, 'G')
    c.arc(16, 16, 10, 7.5, 200, 290, 'Y')
    c.arc(16, 16, 10, 7.5, 290, 405, 'R')
    c.arc(16, 16, 11, 0, 45, 135, 'k')
    c.line(16, 16, 22, 10, 'W')
    c.line(16, 15, 21, 10, 'W')
    c.circle(16, 16, 2.5, 'w')
    c.rect(13, 21, 18, 23, 'G') if False else None
    c.text(13, 21, '%', 'G', font=3) if False else None
    c.outline()



# ================================================================== archives / software
@icon('org.gnome.FileRoller', ['file-roller', 'ark', 'org.kde.ark', 'utilities-file-archiver', 'peazip',
                               'io.github.peazip.PeaZip', 'xarchiver', 'engrampa', 'org.gnome.Engrampa', 'squeeze', 'p7zip'],
      'utility', 'Archive Manager')
def fileroller(c):
    # cardboard box with flaps open and a zipper down the front
    c.poly([(3, 9), (7, 3), (15, 3), (15, 9)], 'n')
    c.poly([(17, 9), (17, 3), (25, 3), (29, 9)], 'n')
    c.rect(3, 9, 28, 28, 'N')
    c.bevel(['N'])
    c.hline(3, 28, 9, '8')
    for y in range(10, 27):
        c.px(15, y, 'w' if y % 2 else 's')
        c.px(16, y, 's' if y % 2 else 'w')
    c.rrect(13, 17, 18, 22, 'Y', 1)
    c.rect(15, 19, 16, 20, '3')
    c.outline()


@icon('org.gnome.Software', ['gnome-software', 'system-software-install', 'software-store',
                             'plasmadiscover', 'org.kde.discover', 'system-software-update',
                             'applications-other', 'bauh'], 'system', 'Software')
def software(c):
    c.ring(16, 10, 7, 5, 'S') if False else None
    c.arc(16, 11, 7, 5, 180, 360, 'w')
    c.poly([(5, 10), (27, 10), (28.5, 28.5), (3.5, 28.5)], 'B')
    c.bevel(['B'])
    c.rect(11, 9, 12, 12, 'w'); c.rect(20, 9, 21, 12, 'w')
    c.sprite(11, 15, """
        ...####...
        ...####...
        ...####...
        ##########
        .########.
        ..######..
        ...####...
        ....##....
    """, {'#': 'W'})
    c.outline()


@icon('pamac', ['pamac-manager', 'pamac-updater', 'org.manjaro.pamac.manager', 'octopi-notifier',
                'system-software-package-manager'], 'system', 'Pamac')
def pamac(c):
    # isometric package cube
    c.poly([(16, 3), (28, 9), (16, 15), (4, 9)], 'g')
    c.poly([(4, 9), (16, 15), (16, 28.5), (4, 22.5)], 'G')
    c.poly([(16, 15), (28, 9), (28, 22.5), (16, 28.5)], '4')
    c.line(10, 5, 22, 11, 'Y'); c.line(10, 6, 22, 12, 'Y')
    c.line(22, 12, 22, 25, 'Y'); c.line(23, 11, 23, 24, '3')
    c.outline()


@icon('octopi', ['octopi-cachecleaner', 'octopi-repoeditor'], 'system', 'Octopi')
def octopi(c):
    c.ellipse(16, 12, 10.5, 9.5, 'M')
    c.rect(7, 16, 25, 21, 'M')
    c.sprite(4, 21, """
        ##..###.###..##
        ##..###.###..##.
        .##.##...##.##..
        ..#.##...##.#...
        ....###.###.....
        .....##.##......
    """.replace('#', 'M'))
    c.bevel(['M'])
    c.rect(10, 11, 13, 15, 'W'); c.rect(19, 11, 22, 15, 'W')
    c.rect(11, 13, 12, 15, 'K'); c.rect(20, 13, 21, 15, 'K')
    c.pixels([(9, 6), (10, 5), (11, 5)], 'm')
    c.outline()


@icon('io.github.flattool.Warehouse', ['warehouse', 'flatpak'], 'system', 'Warehouse')
def warehouse(c):
    c.poly([(2.5, 13), (16, 3), (29.5, 13)], 'R')
    c.rect(3, 12, 28, 13, 'R')
    c.bevel(['R'])
    c.rect(5, 14, 26, 28, 'w')
    c.bevel(['w'])
    c.rect(9, 17, 22, 28, 'S')
    for y in range(18, 28, 2):
        c.hline(9, 22, y, 's')
    c.rect(14, 8, 17, 10, 'Y')
    c.outline()


@icon('org.gnome.seahorse.Application', ['seahorse', 'pinentry', 'security-medium', 'gcr-viewer', 'gnome-keyring', 'org.gnome.Seahorse',
                                         'dialog-password', 'kwalletmanager', 'org.kde.kwalletmanager5', 'password-manager'], 'utility', 'Passwords and Keys')
def seahorse(c):
    c.rect(13, 14, 28, 18, 'Y')
    c.rect(20, 18, 22, 22, 'Y'); c.rect(25, 18, 27, 21, 'Y')
    c.circle(9.5, 16, 7, 'Y')
    c.bevel(['Y'])
    c.circle(8, 16, 2.5, '.')
    c.hline(15, 26, 16, '3')
    c.outline()


@icon('kleopatra', ['org.kde.kleopatra', 'gpa', 'gnupg', 'application-pgp-keys', 'gpg',
                    'security-high'], 'utility', 'Kleopatra')
def kleopatra(c):
    c.arc(16, 13, 9, 5.5, 180, 360, 'S')
    c.rect(7, 13, 10, 14, 'S'); c.rect(22, 13, 25, 14, 'S')
    c.bevel(['S'])
    c.rrect(4, 14, 27, 28, 'B', 1)
    c.bevel(['B'])
    c.circle(16, 19.5, 2.5, 'k')
    c.rect(15, 20, 16, 25, 'k')
    c.outline()


# ================================================================== hardware
@icon('solaar', ['org.pwr.Solaar', 'input-keyboard', 'preferences-desktop-keyboard', 'keyboard'], 'system', 'Solaar')
def solaar(c):
    c.rrect(3, 9, 28, 23, 'S', 1)
    c.bevel(['S'])
    for row, (x0, n) in enumerate([(5, 8), (6, 7), (5, 8)]):
        for i in range(n):
            x = x0 + i * 3
            c.rect(x, 11 + row * 3, x + 1, 12 + row * 3, 'w')
    c.rect(9, 20, 22, 21, 'w')
    c.rect(5, 11, 6, 12, 'O')
    # unifying-receiver sun badge
    c.circle(25, 7, 4.5, 'O')
    c.circle(25, 7, 2.5, 'Y')
    c.outline()


@icon('piper', ['org.freedesktop.Piper', 'input-mouse', 'preferences-desktop-peripherals',
                'input-mouse-symbolic', 'ratbagd'], 'system', 'Piper')
def piper(c):
    c.line(16, 9, 16, 6, 'S')
    c.line(16, 6, 19, 3, 'S')
    c.line(19, 3, 25, 3, 'S')
    c.ellipse(16, 18.5, 9, 10.5, 'k')
    c.bevel(['k'])
    c.vline(16, 9, 15, 'K')
    c.hline(8, 24, 15, 'K')
    c.rect(15, 11, 16, 13, 'R')
    c.line(8, 19, 11, 26, 'R'); c.line(24, 19, 21, 26, 'R')
    c.outline()


@icon('openrgb', ['org.openrgb.OpenRGB', 'OpenRGB', 'ckb-next', 'polychromatic',
                  'app.polychromatic.controller'], 'system', 'OpenRGB')
def openrgb(c):
    centres = {'R': (11.5, 11.5), 'G': (20.5, 11.5), 'B': (16, 19.5)}
    mix = {frozenset('R'): 'R', frozenset('G'): 'G', frozenset('B'): 'B', frozenset('RG'): 'Y',
           frozenset('RB'): 'M', frozenset('GB'): 'C', frozenset('RGB'): 'W'}
    for y in range(32):
        for x in range(32):
            hit = frozenset(k for k, (cx, cy) in centres.items()
                            if math.hypot(x + .5 - cx, y + .5 - cy) <= 8.6)
            if hit:
                c.px(x, y, mix[hit])
    c.bevel(['R', 'G', 'B'], dark=False)
    c.outline()


@icon('corectrl', ['org.corectrl.CoreCtrl', 'CoreCtrl', 'lact', 'io.github.ilya_zlobintsev.LACT',
                   'nvidia-settings', 'gwe', 'com.leinardi.gwe', 'goverlay', 'mangohud'],
      'system', 'CoreCtrl')
def corectrl(c):
    # graphics card with twin fans
    c.rect(3, 6, 5, 25, 'w')
    c.rect(5, 8, 28, 23, 'k')
    c.bevel(['k'])
    c.rect(9, 24, 22, 26, 'Y')
    for x in range(10, 22, 2):
        c.px(x, 26, '3')
    for cx in (11, 22):
        c.circle(cx, 15.5, 6, 's')
        c.arc(cx, 15.5, 5, 1.5, 0, 50, 'S')
        c.arc(cx, 15.5, 5, 1.5, 120, 170, 'S')
        c.arc(cx, 15.5, 5, 1.5, 240, 290, 'S')
        c.circle(cx, 15.5, 1.5, 'R')
    c.hline(6, 27, 8, 'R')
    c.outline()


@icon('cpu-x', ['io.github.thetumultuousunicornofdarkness.cpu-x', 'cpu', 'cpu-g', 'cpuinfo',
                'hwinfo'], 'system', 'CPU-X')
def cpux(c):
    for i in range(7, 25, 3):
        c.rect(i, 3, i + 1, 28, 'w')
        c.rect(3, i, 28, i + 1, 'w')
    c.rect(6, 6, 25, 25, 'k')
    c.rect(8, 8, 23, 23, 'S')
    c.bevel(['S'])
    c.sprite(11, 11, """
        ##....##
        ###..###
        .######.
        ..####..
        ..####..
        .######.
        ###..###
        ##....##
    """, {'#': 'B'})
    c.outline()


@icon('hardinfo2', ['hardinfo', 'org.hardinfo2.Hardinfo2', 'hardinfo2-benchmark', 'system-info', 'inxi', 'hw-probe', 'dmidecode', 'kinfocenter',
                    'org.kde.kinfocenter'], 'system', 'HardInfo')
def hardinfo(c):
    # RAM stick with an info badge
    c.rect(3, 13, 28, 24, 'G')
    c.bevel(['G'])
    c.rect(3, 23, 28, 24, '4')
    for x in range(4, 28, 2):
        c.px(x, 24, 'Y')
    c.rect(14, 23, 15, 24, '.')
    for x in (5, 11, 17):
        c.rect(x, 15, x + 4, 20, 'k')
    c.circle(23, 9, 6.5, 'B')
    c.bevel(['B'])
    c.rect(22, 5, 23, 6, 'W')
    c.rect(22, 8, 23, 13, 'W')
    c.hline(21, 23, 8, 'W')
    c.outline()


@icon('input-remapper', ['input-remapper-gtk', 'io.github.sezanzeb.input_remapper', 'key-mapper',
                         'keymapper', 'antimicrox', 'io.github.antimicrox.antimicrox'], 'system',
      'Input Remapper')
def input_remapper(c):
    c.rrect(3, 4, 28, 28, 'S', 2)
    c.rrect(6, 5, 25, 23, 'w', 1)
    c.bevel(['w'])
    c.rect(4, 26, 27, 27, 's')
    c.sprite(9, 8, """
        ......#...
        .......#..
        #########.
        .......#..
        ......#...
        ..........
        ..#.......
        .#........
        #########.
        .#........
        ..#.......
    """, {'#': 'B'})
    c.outline()


# ================================================================== network / transfer
@icon('qbittorrent', ['org.qbittorrent.qBittorrent', 'qBittorrent', 'qbittorrent-nox'], 'internet', 'qBittorrent')
def qbittorrent(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.ring(16, 16, 11.5, 10.5, '6')
    big(c, 6, 9, """
        ....#...
        .##.###.
        #.#.#..#
        #.#.#..#
        .##.###.
        ..#.....
        ..#.....
    """, 'W', 2) if False else None
    c.sprite(7, 9, """
        ...........##...
        ...........##...
        .#####.....#####
        ##..##.....##..##
        ##..##.....##..##
        ##..##.....##..##
        .#####.....#####.
        ....##..........
        ....##..........
    """.replace('##..##.....##..##', '##..##.....##..##')[:0] or """
        .........##.....
        .........##.....
        .#####...#####..
        ##..##...##..##.
        ##..##...##..##.
        ##..##...##..##.
        .#####...#####..
        ....##..........
        ....##..........
    """, {'#': 'W'})
    c.outline()


@icon('transmission', ['transmission-gtk', 'com.transmissionbt.Transmission', 'transmission-qt',
                       'transmission-remote-gtk', 'io.github.TransmissionRemoteGtk', 'tremotesf'],
      'internet', 'Transmission')
def transmission(c):
    for r0, r1 in ((11, 9), (6.5, 4.5)):
        c.arc(16, 12, r0, r1, 195, 240, 'R'); c.arc(16, 12, r0, r1, 300, 345, 'R')
    c.poly([(16, 11), (22, 28), (10, 28)], 'S')
    c.poly([(16, 15), (19, 25), (13, 25)], '.')
    c.line(14, 19, 18, 19, 'S'); c.line(13, 23, 19, 23, 'S')
    c.circle(16, 12, 3, 'R')
    c.px(15, 11, 'r')
    c.outline()


@icon('deluge', ['deluge-gtk', 'org.deluge_torrent.deluge', 'deluge-torrent'], 'internet', 'Deluge')
def deluge(c):
    c.circle(16, 19, 9.5, 'B')
    c.poly([(7, 17), (16, 2), (25, 17)], 'B')
    c.bevel(['B'])
    c.circle(16, 19.5, 6.5, '6') if False else None
    c.pixels([(11, 18), (11, 19), (11, 20), (12, 21), (12, 22), (13, 23)], 'W')
    c.px(13, 13, 'b'); c.px(12, 15, 'b')
    c.outline()


@icon('de.haeckerfelix.Fragments', ['fragments', 'torrent',
                                    'ktorrent', 'org.kde.ktorrent', 'tixati', 'biglybt'],
      'internet', 'Fragments')
def fragments(c):
    # a magnet (BitTorrent magnet links)
    c.arc(16, 14, 12.5, 5.5, 0, 180, 'R')
    c.rect(4, 3, 10, 14, 'R')
    c.rect(22, 3, 28, 14, 'R')
    c.bevel(['R'])
    c.rect(4, 3, 10, 6, 'w'); c.rect(22, 3, 28, 6, 'w')
    c.hline(4, 10, 3, 'W'); c.hline(22, 28, 3, 'W')
    c.hline(4, 10, 6, 'S'); c.hline(22, 28, 6, 'S')
    c.outline()


@icon('motrix', ['net.agalwood.Motrix', 'Motrix', 'uget', 'uget-gtk', 'com.ugetdm.uGet', 'xdman',
                 'persepolis', 'kget', 'org.kde.kget', 'aria2', 'download-manager'], 'internet', 'Motrix')
def motrix(c):
    c.rect(13, 3, 21, 14, 'M')
    c.poly([(7.5, 14), (26.5, 14), (17, 24)], 'M')
    c.bevel(['M'])
    for y, x0 in [(5, 6), (9, 4), (13, 7)] if False else []:
        pass
    c.hline(4, 10, 6, 'm'); c.hline(3, 10, 10, 'm')
    c.rrect(5, 25, 28, 28, 'S', 1)
    c.hline(6, 27, 25, 'w')
    c.outline()


@icon('anydesk', ['com.anydesk.Anydesk', 'AnyDesk'], 'internet', 'AnyDesk')
def anydesk(c):
    c.poly([(16, 2.5), (29.5, 16), (16, 29.5), (2.5, 16)], 'R')
    c.bevel(['R'])
    c.poly([(16, 9), (23, 16), (16, 23), (9, 16)], 'W')
    c.poly([(16, 12.5), (19.5, 16), (16, 19.5), (12.5, 16)], 'R')
    c.outline()


@icon('rustdesk', ['com.rustdesk.RustDesk', 'RustDesk'], 'internet', 'RustDesk')
def rustdesk(c):
    c.rrect(3, 4, 28, 21, 'k', 1)
    c.rect(5, 6, 26, 19, 'B')
    c.bevel(['B'])
    c.sprite(13, 8, """
        W.....
        WW....
        WbW...
        WbbW..
        WbbbW.
        WbbbbW
        WbbWWW
        WW.Wb.
        ...W..
    """)
    c.rect(13, 22, 18, 24, 's')
    c.rrect(8, 25, 23, 27, 'O', 1)
    c.hline(9, 22, 25, 'o')
    c.outline()


@icon('org.remmina.Remmina', ['remmina', 'krdc', 'org.kde.krdc',
                              'org.gnome.Connections', 'gnome-connections', 'vinagre',
                              'preferences-desktop-remote-desktop', 'tigervnc', 'vncviewer',
                              'freerdp'], 'internet', 'Remmina')
def remmina(c):
    # laptop showing a remote session
    c.rrect(5, 5, 26, 21, 'k', 1)
    c.rect(7, 7, 24, 19, 'C')
    c.bevel(['C'])
    c.rect(10, 9, 21, 16, 'W')
    c.hline(10, 21, 9, 'B')
    c.rect(12, 12, 16, 14, 'b')
    c.poly([(5, 22), (27, 22), (29, 25), (3, 25)], 'S')
    c.hline(3, 28, 25, 's')
    c.hline(14, 17, 23, 'w')
    c.outline()


@icon('teamviewer', ['com.teamviewer.TeamViewer', 'TeamViewer', 'teamviewer-tray'], 'internet', 'TeamViewer')
def teamviewer(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.circle(16, 16, 9.5, 'W')
    c.sprite(8, 13, """
        ...#.........#...
        ..##.........##..
        .#############...
        ################
        .#############...
        ..##.........##..
        ...#.........#...
    """.replace('...\n', '...\n'), {'#': 'B'}) if False else None
    c.sprite(8, 13, """
        ...#.......#....
        ..##.......##...
        .###########....
        #############...
        .###########....
        ..##.......##...
        ...#.......#....
    """, {'#': 'B'}) if False else None
    c.sprite(8, 13, """
        ...#.......#...
        ..##.......##..
        .#############.
        ###############
        .#############.
        ..##.......##..
        ...#.......#...
    """, {'#': 'B'})
    c.outline()


@icon('org.kde.kdeconnect.app', ['kdeconnect', 'kdeconnect-app', 'org.kde.kdeconnect',
                                 'org.kde.kdeconnect-settings', 'kdeconnectindicator',
                                 'gsconnect', 'org.gnome.Shell.Extensions.GSConnect', 'valent',
                                 'ca.andyholmes.Valent', 'smartphone'], 'internet', 'KDE Connect')
def kdeconnect(c):
    c.rrect(4, 4, 18, 28, 'k', 2)
    c.rect(6, 7, 16, 24, 'B')
    c.bevel(['B'])
    c.hline(10, 12, 5, 's')
    c.rect(10, 26, 12, 26, 's')
    c.arc(18, 12, 10, 8, 300, 40, 'G')
    c.arc(18, 12, 6, 4, 300, 40, 'G')
    c.outline()


@icon('org.x.Warpinator', ['warpinator'], 'internet', 'Warpinator')
def warpinator(c):
    # paper plane
    c.poly([(3, 14), (29, 3), (13, 19)], 'W')
    c.poly([(13, 19), (29, 3), (20, 28)], 'w')
    c.poly([(13, 19), (17, 23), (13, 26)], 'S')
    c.line(13, 19, 28, 4, 'S')
    c.outline()


# ================================================================== file managers
@icon('org.kde.dolphin', ['dolphin'], 'system', 'Dolphin')
def dolphin(c):
    c.arc(16, 24, 13, 6.5, 195, 345, 'B')
    c.poly([(26, 16), (29.5, 22), (27, 24), (24, 19)], 'B')     # snout
    c.poly([(14, 11), (17, 4), (19, 11)], 'B')                  # dorsal fin
    c.poly([(5, 20), (2.5, 27), (5.5, 24), (9.5, 27), (7, 19)], 'B')  # tail flukes
    c.bevel(['B'])
    c.arc(16, 24, 7.6, 6.5, 200, 340, 'b')
    c.px(23, 16, 'K')
    c.outline()


@icon('thunar', ['org.xfce.thunar', 'Thunar', 'thunar-settings', 'xfce-filemanager'], 'system', 'Thunar')
def thunar(c):
    c.rrect(3, 7, 13, 11, 'B', 1)
    c.rect(3, 9, 28, 27, 'B')
    c.rect(3, 14, 28, 27, 'b')
    c.bevel(['b'])
    c.hline(3, 28, 14, 'W')
    # Thor's hammer
    c.rect(18, 3, 29, 9, 'S')
    c.bevel(['S'])
    c.rect(22, 10, 24, 25, 'N')
    c.vline(22, 10, 25, 'n')
    c.rect(21, 24, 25, 26, 's')
    c.rect(28, 3, 29, 9, '.')
    c.outline()


@icon('nemo', ['nemo-desktop', 'nemo-preview'], 'system', 'Nemo')
def nemo(c):
    c.poly([(20, 16), (28, 8), (28, 24)], 'O')
    c.ellipse(13, 16, 10, 8, 'O')
    c.poly([(10, 9), (15, 5), (17, 9)], 'O')
    c.bevel(['O'])
    for x0 in (8, 16):
        c.rect(x0, 0, x0 + 2, 31, 'W', ) if False else None
    for y in range(32):
        for x in (8, 9, 16, 17, 25):
            if c.get(x, y) in 'O2o':
                c.px(x, y, 'W')
        for x in (10, 18, 26):
            if c.get(x, y) in 'O2o':
                c.px(x, y, 'k') if False else c.px(x, y, '2')
    c.rect(5, 13, 6, 14, 'K')
    c.px(5, 13, 'W')
    c.outline()


@icon('pcmanfm', ['pcmanfm-qt', 'spacefm', 'caja', 'org.mate.Caja',
                  'doublecmd', 'krusader', 'org.kde.krusader', 'xfe', 'yazi', 'ranger', 'nnn', 'lf'],
      'system', 'PCManFM')
def pcmanfm(c):
    # filing cabinet
    c.rrect(6, 3, 25, 28, 'C', 1)
    c.bevel(['C'])
    for y0 in (5, 13, 21):
        c.rect(8, y0, 23, y0 + 5, 'c') if False else None
        c.frame(8, y0, 23, y0 + 5, '5')
        c.rect(13, y0 + 1, 18, y0 + 2, 'W')
        c.rect(14, y0 + 3, 17, y0 + 3, 's')
    c.outline()
