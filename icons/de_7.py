"""XFCE settings dialogs (family: object + blue gear badge), LXQt, elementary
and Budgie desktop utilities."""
from pix import icon
import math

LT = {'R': 'r', 'O': 'o', 'Y': 'y', 'G': 'g', 'C': 'c', 'B': 'b', 'M': 'm', 'N': 'n', 'P': 'p', 'W': 'W', 'S': 'w'}


def gear(c, cx, cy, r, col, hole='W'):
    for a in range(0, 360, 45):
        t = math.radians(a)
        x, y = cx + (r + 0.8) * math.cos(t), cy + (r + 0.8) * math.sin(t)
        c.rect(round(x - 1), round(y - 1), round(x), round(y), col)
    c.circle(cx, cy, r, col)
    c.circle(cx, cy, r * 0.4, hole)


def xbadge(c):
    """XFCE settings family badge, bottom-right."""
    gear(c, 23, 23, 4.5, 'B', 'W')


def monitor(c, x0, y0, x1, y1, scr='B'):
    c.rrect(x0, y0, x1, y1, 'S', 1)
    c.bevel(['S'])
    c.rect(x0 + 2, y0 + 2, x1 - 2, y1 - 2, scr)
    mx = (x0 + x1) // 2
    c.rect(mx - 2, y1 + 1, mx + 2, y1 + 2, 's')
    c.rect(mx - 6, y1 + 3, mx + 6, y1 + 4, 'S')


# ================================================================== XFCE settings
@icon('org.xfce.settings.display', ['xfce4-display-settings', 'xfce-display'], 'system', 'Display')
def xdisplay(c):
    monitor(c, 3, 4, 25, 20, 'b')
    c.rect(5, 6, 23, 9, 'c')
    xbadge(c)
    c.outline()


@icon('org.xfce.settings.keyboard', ['xfce4-keyboard-settings'], 'system', 'Keyboard')
def xkeyboard(c):
    c.rrect(3, 7, 26, 22, 'S', 1)
    c.bevel(['S'])
    for j, off in enumerate((5, 6, 7)):
        for i in range(6):
            c.rect(off + i * 3 + j, 9 + j * 4, off + i * 3 + j + 1, 10 + j * 4, 'W')
    c.rect(9, 20, 18, 21, 'W') if False else None
    xbadge(c)
    c.outline()


@icon('org.xfce.settings.mouse', ['xfce4-mouse-settings'], 'system', 'Mouse and Touchpad')
def xmouse(c):
    c.line(13, 3, 13, 6, 'k')
    c.rrect(5, 6, 21, 27, 'W', 6)
    c.bevel(['W'])
    c.vline(13, 6, 13, 'S'); c.hline(5, 21, 13, 'S')
    c.rect(12, 8, 14, 11, 'k')
    xbadge(c)
    c.outline()


@icon('org.xfce.settings.appearance', ['xfce4-appearance-settings', 'xfce-theme-manager'], 'system', 'Appearance')
def xappearance(c):
    # paint brush over a swatch
    for i, col in enumerate(['R', 'Y', 'G', 'B']):
        c.rect(3 + i * 5, 3, 7 + i * 5, 10, col)
    c.line(9, 26, 19, 14, 'N', 3)
    c.rect(18, 11, 21, 15, 'S')
    c.poly([(5, 26), (9, 23), (11, 26), (6, 29)], 'M')
    xbadge(c)
    c.outline()


@icon('org.xfce.settings.accessibility', ['xfce4-accessibility-settings'], 'system', 'Accessibility')
def xaccess(c):
    c.circle(14, 15, 11, 'B')
    c.bevel(['B'])
    c.circle(13, 7.5, 2, 'W')
    c.hline(6, 20, 11, 'W'); c.hline(7, 19, 12, 'W')
    c.rect(12, 12, 14, 18, 'W')
    c.line(12, 18, 9, 23, 'W'); c.line(14, 18, 17, 23, 'W')
    gear(c, 23, 23, 4.5, 'S', 'W')
    c.outline()


@icon('org.xfce.session', ['xfce4-session-settings', 'xfce4-session'], 'system', 'Session and Startup')
def xsession(c):
    c.arc(14, 15, 11, 8, 300, 240, 'G')
    c.rect(12, 3, 15, 14, 'G')
    c.bevel(['G'])
    xbadge(c)
    c.outline()


@icon('org.xfce.notification', ['xfce4-notifyd-config', 'xfce4-notifyd'], 'system', 'Notifications')
def xnotify(c):
    c.ellipse(14, 12, 9, 9, 'Y')
    c.rect(5, 12, 23, 20, 'Y')
    c.rrect(3, 19, 25, 22, 'Y', 1)
    c.bevel(['Y'])
    c.circle(14, 24, 2.5, '3')
    xbadge(c)
    c.outline()


@icon('org.xfce.workspaces', ['xfwm4-workspace-settings', 'xfce-workspaces'], 'system', 'Workspaces')
def xworkspaces(c):
    for i in range(2):
        for j in range(2):
            x, y = 3 + i * 11, 3 + j * 11
            c.rect(x, y, x + 9, y + 9, 'B' if (i, j) == (0, 0) else 'b')
    c.rect(5, 5, 9, 8, 'W')
    xbadge(c)
    c.outline()


@icon('org.xfce.settings.default-applications', ['xfce4-mime-settings', 'org.xfce.settings.mime',
                                                  'xfce4-settings-default-applications'], 'system', 'Default Applications')
def xmime(c):
    c.rect(3, 3, 22, 27, 'W')
    c.bevel(['W'])
    for i, col in enumerate(['R', 'G', 'O', 'M']):
        y = 6 + i * 5
        c.rect(5, y, 8, y + 3, col)
        c.hline(10, 19, y + 1, 'S')
        c.hline(10, 15, y + 3, 'w')
    xbadge(c)
    c.outline()


@icon('org.xfce.settings.color', ['xfce4-color-settings'], 'system', 'Color Profiles')
def xcolor(c):
    c.circle(9, 10, 6.5, 'R')
    c.circle(19, 10, 6.5, 'G')
    c.circle(14, 18, 6.5, 'B')
    c.ellipse(14, 13, 3, 2.5, 'W')
    xbadge(c)
    c.outline()


@icon('org.xfce.volman', ['thunar-volman-settings', 'thunar-volman'], 'system', 'Removable Drives')
def xvolman(c):
    c.rrect(5, 3, 20, 9, 'w', 1)
    c.rect(8, 5, 9, 6, 'k'); c.rect(15, 5, 16, 6, 'k')
    c.rrect(3, 9, 22, 27, 'O', 2)
    c.bevel(['O'])
    c.rect(7, 14, 18, 19, 'o')
    xbadge(c)
    c.outline()


@icon('org.xfce.xfdesktop', ['xfdesktop-settings', 'xfdesktop', 'xfce4-backdrop'], 'system', 'Desktop')
def xfdesktop(c):
    c.rect(3, 4, 26, 22, 'b')
    c.rect(3, 4, 26, 4, 'c')
    c.poly([(3, 22.5), (3, 17), (10, 11), (16, 17), (20, 14), (26.5, 19), (26.5, 22.5)], 'G')
    c.circle(20, 9, 2, 'Y')
    for y in (6, 11):
        c.rect(5, y, 7, y + 2, 'W')
    xbadge(c)
    c.outline()


@icon('org.xfce.settings.editor', ['xfce4-settings-editor'], 'system', 'Settings Editor')
def xsettingseditor(c):
    c.rect(3, 3, 23, 27, 'W')
    c.bevel(['W'])
    c.rect(3, 3, 23, 6, 'B')
    for i in range(4):
        y = 9 + i * 4
        c.rect(5 + (i % 2) * 3, y, 6 + (i % 2) * 3, y + 1, 'S')
        c.hline(9 + (i % 2) * 3, 19, y, 'k') if False else c.hline(9 + (i % 2) * 3, 19, y + 1, 'S')
    xbadge(c)
    c.outline()


@icon('xfce4-sensors', ['xfce4-sensors-plugin', 'psensor', 'sensors'], 'system', 'Sensor Viewer')
def xsensors(c):
    c.circle(14, 23, 5.5, 'R')
    c.rrect(11, 3, 17, 22, 'W', 3)
    c.bevel(['W'])
    c.rect(13, 10, 15, 22, 'R')
    c.px(13, 10, 'r')
    for y in (6, 9, 12, 15):
        c.hline(18, 20, y, 'S')
    c.outline()


# ================================================================== LXQt
@icon('lxqt-runner', ['lxqt-runner-symbolic'], 'system', 'LXQt Runner')
def lxrunner(c):
    c.rrect(3, 8, 28, 23, 'k', 2)
    c.rect(5, 10, 26, 21, 's')
    c.sprite(7, 12, """
        #......
        .#.....
        ..#....
        .#.....
        #...###
    """, {'#': 'C'})
    c.line(18, 13, 21, 13, 'W') if False else None
    c.outline()


@icon('lxqt-about', ['lxqt', 'lxqt-logo'], 'system', 'About LXQt')
def lxabout(c):
    c.circle(16, 16, 12.5, 'B')
    c.bevel(['B'])
    c.ring(16, 16, 8.5, 6, 'W')
    c.line(19, 19, 25, 25, 'W', 2)
    c.circle(16, 16, 3, 'C')
    c.outline()


@icon('lxqt-panel', ['lxqt-panel-settings'], 'system', 'LXQt Panel')
def lxpanel(c):
    c.rrect(3, 4, 28, 27, 'c', 1)
    c.rect(3, 21, 28, 27, 'B')
    c.bevel(['B'])
    c.circle(7, 24, 2, 'W')
    for x in (11, 15, 19):
        c.rect(x, 23, x + 2, 25, 'b')
    c.rect(23, 23, 26, 24, 'W')
    c.outline()


@icon('lxqt-leave', ['system-log-out', 'system-shutdown', 'lxqt-leave-symbolic'], 'system', 'Leave')
def lxleave(c):
    c.circle(16, 16, 12.5, 'R')
    c.bevel(['R'])
    c.arc(16, 16, 7.5, 5.5, 300, 240, 'W')
    c.rect(15, 6, 16, 15, 'W')
    c.outline()


@icon('lxqt-sudo', ['lxqt-admin', 'lxqt-policykit'], 'system', 'LXQt Sudo')
def lxsudo(c):
    c.poly([(16, 3), (28, 8), (26, 21), (16, 29), (6, 21), (4, 8)], 'Y')
    c.bevel(['Y'])
    c.arc(16, 13, 4.5, 2.5, 180, 360, 'k')
    c.rect(11, 13, 21, 21, 'k')
    c.rect(15, 16, 16, 18, 'Y')
    c.outline()


@icon('lxqt-notificationd', ['lxqt-config-notificationd'], 'system', 'LXQt Notifications')
def lxnotify(c):
    c.rrect(3, 6, 28, 18, 'W', 2)
    c.bevel(['W'])
    c.rect(5, 8, 9, 12, 'B')
    c.hline(11, 25, 9, 'k'); c.hline(11, 21, 12, 'S')
    c.rrect(6, 20, 25, 26, 'w', 1)
    c.outline()


# ================================================================== elementary / Budgie
@icon('io.elementary.feedback', ['feedback'], 'system', 'Feedback')
def efeedback(c):
    c.rrect(3, 4, 28, 22, 'O', 3)
    c.poly([(20, 21), (26, 21), (25, 28.5)], 'O')
    c.bevel(['O'])
    c.sprite(9, 8, """
        .##.##..
        ########
        ########
        .######.
        ..####..
        ...##...
    """, {'#': 'W'})
    c.outline()


@icon('io.elementary.onboarding', ['onboarding'], 'system', 'Welcome')
def eonboarding(c):
    # waving pennant flag
    c.vline(6, 3, 28, 'N')
    c.vline(7, 3, 28, 'n')
    c.poly([(8, 4), (28.5, 9), (8, 18)], 'B')
    c.bevel(['B'])
    c.circle(13, 10.5, 2, 'W')
    c.outline()


@icon('io.elementary.sideload', ['sideload'], 'system', 'Sideload')
def esideload(c):
    c.rrect(5, 11, 26, 28, 'S', 3)
    c.bevel(['S'])
    c.sprite(11, 3, """
        ...####...
        ...####...
        ...####...
        ...####...
        ##########
        .########.
        ..######..
        ...####...
        ....##....
    """, {'#': 'B'})
    c.rect(9, 21, 22, 23, 's')
    c.outline()


@icon('com.github.stsdc.monitor', ['io.elementary.monitor'], 'system', 'Monitor')
def emonitor(c):
    c.rrect(3, 4, 28, 27, 'W', 2)
    c.bevel(['W'])
    c.rect(5, 6, 26, 21, 'k')
    pts = [(6, 18), (9, 15), (12, 17), (15, 9), (18, 14), (21, 12), (25, 16)]
    for a, b in zip(pts, pts[1:]):
        c.line(*a, *b, 'G')
    c.rect(5, 23, 12, 24, 'B'); c.rect(15, 23, 19, 24, 'O')
    c.outline()


@icon('budgie-desktop-settings', ['budgie-control-center', 'org.buddiesofbudgie.Settings', 'budgie'],
      'system', 'Budgie Settings')
def budgie(c):
    # budgie bird
    c.ellipse(14, 17, 9.5, 8, 'G')
    c.circle(20, 10, 6, 'G')
    c.poly([(5, 19), (2.5, 28.5), (10, 23)], 'B')
    c.bevel(['G'])
    c.poly([(25, 9), (29, 11), (25, 13)], 'Y')
    c.circle(21.5, 9, 1.2, 'k')
    c.arc(13, 17, 6, 4.5, 30, 160, '4')
    c.outline()


@icon('mozo', ['mozo-menu-editor', 'org.mate.Mozo'], 'system', 'Main Menu')
def mozo(c):
    c.rrect(3, 3, 21, 28, 'G', 1)
    c.bevel(['G'])
    for i in range(5):
        y = 6 + i * 4
        c.rect(5, y, 7, y + 2, 'W')
        c.hline(9, 18, y + 1, 'g')
    c.line(16, 25, 25, 16, 'Y', 3)
    c.px(15, 27, 'k'); c.px(16, 27, 'n'); c.px(15, 26, 'n')
    c.outline()


@icon('io.github.realmazharhussain.GdmSettings', ['gdm-settings'], 'system', 'Login Manager Settings')
def gdmsettings(c):
    monitor(c, 3, 4, 28, 21, 'k')
    c.circle(15.5, 10, 2.5, 'W')
    c.rrect(10, 14, 21, 16, 'w', 1)
    c.outline()


@icon('com.github.d4nj1.tlpui', ['tlpui'], 'system', 'TLP UI')
def tlpui(c):
    c.rrect(3, 8, 25, 24, 'G', 2)
    c.rect(26, 13, 28, 19, 'G')
    c.bevel(['G'])
    c.rect(5, 10, 23, 22, '4')
    c.rect(5, 10, 16, 22, 'g')
    c.sprite(11, 11, """
        ...##
        ..##.
        .####
        ..##.
        .##..
        ##...
    """, {'#': 'Y'})
    c.outline()


@icon('page.codeberg.libre_menu_editor.LibreMenuEditor', ['libre-menu-editor'], 'system', 'Menu Editor')
def libremenu(c):
    c.rrect(3, 3, 28, 28, 'k', 3)
    for i, col in enumerate(['R', 'O', 'G', 'B']):
        y = 6 + i * 5
        c.rrect(6, y, 9, y + 3, col, 1)
        c.hline(12, 24, y + 1, 's'); c.hline(12, 19, y + 2, 's')
    c.outline()


@icon('io.github.vikdevelop.SaveDesktop', ['savedesktop'], 'system', 'SaveDesktop')
def savedesktop(c):
    monitor(c, 3, 4, 28, 21, 'b')
    c.sprite(11, 7, """
        ##########
        #.##..##.#
        #.##..##.#
        #........#
        #.######.#
        #.######.#
        ##########
    """, {'#': 'W'})
    c.outline()


@icon('app.drey.KeyRack', ['keyrack'], 'system', 'Key Rack')
def keyrack(c):
    c.rrect(3, 4, 28, 9, 'N', 1)
    c.bevel(['N'])
    for x, col in [(8, 'Y'), (16, 'S'), (24, 'Y')]:
        c.vline(x, 9, 12, 'k')
        c.circle(x, 15, 3.5, col)
        c.circle(x, 15, 1.2, 'N')
        c.rect(x - 1, 18, x, 27, col)
        c.rect(x + 1, 23, x + 2, 24, col); c.rect(x + 1, 26, x + 2, 27, col)
    c.outline()
