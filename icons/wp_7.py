"""System utilities: USB writers, boot, backups, Wine, Android, KVM sharing."""
from pix import icon
import math


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


def usb_stick(c, body, x0=9, x1=22):
    """Vertical USB stick: metal plug on top, body below."""
    c.rect(x0 + 2, 3, x1 - 2, 9, 'w')
    c.rect(x0 + 4, 5, x0 + 5, 6, 's'); c.rect(x1 - 5, 5, x1 - 4, 6, 's')
    c.rrect(x0, 9, x1, 28, body, 2)
    c.bevel(['w', body])


def monitor(c, x0, y0, x1, y1, frame='k', screen='B', stand=True):
    c.rrect(x0, y0, x1, y1, frame, 1)
    c.bevel([frame])
    c.rect(x0 + 2, y0 + 2, x1 - 2, y1 - 2, screen)
    if stand:
        mx = (x0 + x1) // 2
        c.rect(mx - 1, y1 + 1, mx + 1, y1 + 2, 's')
        c.rect(mx - 4, y1 + 3, mx + 4, y1 + 3, 's')


def gear(c, cx, cy, r, col, teeth=8, tooth=2.5):
    for i in range(teeth):
        a = math.radians(i * 360 / teeth)
        c.circle(cx + r * math.cos(a), cy + r * math.sin(a), tooth, col)
    c.circle(cx, cy, r, col)


# ================================================================ USB / boot media

@icon('ventoy', ['ventoygui', 'ventoy-bin', 'Ventoy', 'ventoy-gui'], 'system', 'Ventoy')
def ventoy(c):
    usb_stick(c, 'G', 8, 23)
    g(c, 11, 13, """
        ##......##
        ##......##
        .##....##.
        .##....##.
        ..##..##..
        ..##..##..
        ...####...
        ....##....
    """)
    c.outline()


@icon('balena-etcher', ['balenaEtcher', 'etcher', 'balena-etcher-electron', 'io.balena.etcher',
                        'balena-etcher-bin', 'etcher-bin'], 'system', 'balenaEtcher')
def etcher(c):
    # isometric cube
    c.poly([(16, 3), (28, 9.5), (16, 16), (4, 9.5)], 'g')
    c.poly([(4, 9.5), (16, 16), (16, 29), (4, 22.5)], 'G')
    c.poly([(16, 16), (28, 9.5), (28, 22.5), (16, 29)], '4')
    c.poly([(10, 9.5), (16, 6.5), (22, 9.5), (16, 12.5)], 'G')
    c.outline()


@icon('woeusb', ['woeusb-ng', 'com.github.woeusb.woeusb-ng', 'woeusbgui'], 'system', 'WoeUSB')
def woeusb(c):
    usb_stick(c, 'b', 9, 22)
    for (x, y, col) in ((11, 13, 'R'), (16, 13, 'G'), (11, 19, 'B'), (16, 19, 'Y')):
        c.rect(x, y, x + 4, y + 4, col)
    c.outline()


@icon('com.system76.Popsicle', ['popsicle', 'popsicle-gtk'], 'system', 'Popsicle')
def popsicle(c):
    c.rrect(8, 3, 24, 22, 'P', 6)
    c.rect(8, 13, 24, 22, 'P')
    c.rect(8, 13, 24, 22, 'C')
    c.rrect(8, 3, 24, 14, 'P', 6)
    c.rect(8, 10, 24, 14, 'P')
    c.bevel(['P', 'C'])
    c.rect(14, 23, 17, 28, 'n')
    c.bevel(['n'])
    c.pixels([(11, 6), (10, 7), (10, 8)], 'W')
    c.outline()


@icon('rpi-imager', ['org.raspberrypi.rpi-imager', 'raspberry-pi-imager', 'rpi-imager-bin'], 'system',
      'Raspberry Pi Imager')
def rpi_imager(c):
    # raspberry
    c.poly([(16, 9), (8, 3), (13, 4)], 'G')
    c.poly([(16, 9), (24, 3), (19, 4)], 'G')
    for (x, y) in ((11, 11.5), (21, 11.5), (16, 12.5), (8.5, 17), (16, 18), (23.5, 17), (12, 22.5), (20, 22.5),
                   (16, 25)):
        c.circle(x, y, 3.8, 'R')
    c.bevel(['R', 'G'])
    for (x, y) in ((10, 11), (20, 11), (15, 12), (8, 17), (15, 18), (22, 17), (11, 23), (19, 23)):
        c.px(x, y, 'r')
    c.outline()


@icon('org.fedoraproject.MediaWriter', ['mediawriter', 'fedora-media-writer', 'liveusb-creator'], 'system',
      'Fedora Media Writer')
def fedora_mw(c):
    disc(c, 'B')
    c.ring(18, 13, 6.5, 3.5, 'W')
    c.rect(10, 12, 18, 25, 'B')
    c.rect(12, 13, 15, 25, 'W')
    c.rect(9, 15, 18, 18, 'W')
    c.rect(18, 11, 25, 13, 'B')
    c.outline()


@icon('grub-customizer', ['grub-customizer-git'], 'system', 'Grub Customizer')
def grub_customizer(c):
    monitor(c, 3, 4, 28, 22, 'k', 'k')
    c.rect(7, 8, 24, 9, 'W')
    c.rect(7, 11, 24, 12, 'S'); c.rect(7, 14, 24, 15, 'S'); c.rect(7, 17, 18, 18, 'S')
    c.rect(6, 8, 24, 9, 'W')
    c.outline()


@icon('cockpit', ['cockpit-desktop', 'cockpit-client', 'org.cockpit_project.CockpitClient'], 'system', 'Cockpit')
def cockpit(c):
    disc(c, 'B')
    c.ring(16, 17, 9, 7, 'W')
    for y in range(22, 30):
        for x in range(32):
            if c.get(x, y) == 'W':
                c.px(x, y, 'B')
    c.line(16, 17, 21, 11, 'W', 2)
    c.circle(16, 17, 2, 'W')
    c.bevel(['B'])
    c.outline()


@icon('webmin', ['webmin-webapp', 'usermin'], 'system', 'Webmin')
def webmin(c):
    disc(c, 'B')
    c.ellipse(16, 16, 5.5, 13, 'b')
    c.ellipse(16, 16, 4, 11.5, 'B')
    c.hline(4, 27, 11, 'b'); c.hline(3, 28, 16, 'b'); c.hline(4, 27, 21, 'b')
    c.rrect(13, 20, 28, 28, 'k', 1)
    c.text(15, 22, 'WM', 'G', 3, 1)
    c.outline()


# ================================================================ disks / cleanup / monitors

@icon('kdiskmark', ['io.github.jonmagon.kdiskmark'], 'system', 'KDiskMark')
def kdiskmark(c):
    c.circle(16, 18, 13, 'S')
    c.rect(3, 23, 29, 31, '.')
    c.bevel(['S'])
    c.arc(16, 18, 11, 8, 180, 240, 'G')
    c.arc(16, 18, 11, 8, 240, 300, 'Y')
    c.arc(16, 18, 11, 8, 300, 360, 'R')
    c.line(16, 18, 23, 11, 'k', 2)
    c.circle(16, 18, 2.5, 'k')
    c.rect(3, 23, 28, 26, 's')
    c.outline()


@icon('com.github.qarmin.czkawka', ['czkawka', 'czkawka-gui', 'krokiet', 'com.github.qarmin.krokiet'], 'system',
      'Czkawka')
def czkawka(c):
    c.rrect(3, 3, 19, 21, 'w', 1)
    c.bevel(['w'])
    c.rrect(12, 10, 28, 28, 'O', 1)
    c.bevel(['O'])
    c.rect(15, 14, 25, 15, 'W'); c.rect(15, 18, 25, 19, 'W'); c.rect(15, 22, 21, 23, 'W')
    c.outline()


# ================================================================ backup

@icon('kopia-ui', ['kopia', 'kopia-ui-bin', 'io.kopia.KopiaUI'], 'system', 'KopiaUI')
def kopia(c):
    c.rrect(3, 5, 28, 26, 'Y', 3)
    c.bevel(['Y'])
    c.rrect(7, 9, 18, 22, 'W', 1)
    c.rrect(12, 13, 24, 25, 'O', 1)
    c.bevel(['O'])
    c.outline()


# ================================================================ Wine & Windows compat

@icon('playonlinux', ['PlayOnLinux', 'playonlinux4', 'phoenicis-playonlinux'], 'system', 'PlayOnLinux')
def playonlinux(c):
    for (x, y, col) in ((10.5, 10.5, 'R'), (21.5, 10.5, 'B'), (10.5, 21.5, 'G'), (21.5, 21.5, 'Y')):
        c.circle(x, y, 7, col)
    c.bevel(['R', 'B', 'G', 'Y'], light=False)
    c.circle(16, 16, 5, 'W')
    c.poly([(14.5, 13), (19, 16), (14.5, 19)], 'k')
    c.outline()


@icon('crossover', ['cxsetup', 'com.codeweavers.CrossOver', 'cxoffice', 'crossover-bin'], 'system',
      'CrossOver')
def crossover(c):
    disc(c, 'R')
    c.line(9, 9, 22, 22, 'W', 3); c.line(22, 9, 9, 22, 'W', 3)
    c.outline()


@icon('waydroid', ['Waydroid', 'id.waydro.waydroid', 'waydroid-container', 'waydroid-helper',
                   'com.jaoushingan.WaydroidHelper'], 'system', 'Waydroid')
def waydroid(c):
    # droid head with a wave
    c.ellipse(16, 17, 12, 10, 'G')
    c.rect(4, 17, 28, 27, 'G')
    c.line(9, 9, 6, 4, 'G', 2); c.line(22, 9, 25, 4, 'G', 2)
    c.bevel(['G'])
    c.rect(10, 12, 12, 14, 'W'); c.rect(20, 12, 22, 14, 'W')
    for x in range(4, 29):
        y = 21 + int(round(1.6 * math.sin((x - 4) / 3)))
        c.rect(x, y, x, 27, 'B')
    c.bevel(['B'], light=False)
    c.outline()


@icon('genymotion', ['genymotion-player', 'genymotion-bin'], 'system', 'Genymotion')
def genymotion(c):
    c.rrect(8, 3, 24, 28, 'k', 3)
    c.bevel(['k'])
    c.rect(10, 6, 22, 23, 'M')
    c.rect(14, 25, 18, 26, 's')
    ctext(c, 'G', 'W', 14.5, 2, 3)
    c.outline()


@icon('virt-viewer', ['remote-viewer', 'org.virt-manager.virt-viewer'], 'system', 'Virt Viewer')
def virt_viewer(c):
    monitor(c, 3, 4, 28, 22, 'k', 'B')
    c.rrect(8, 8, 23, 18, 'k', 1)
    c.rect(9, 9, 22, 10, 'S')
    c.rect(10, 12, 15, 16, 'C')
    c.outline()


# ================================================================ sharing / KVM / casting

@icon('barrier', ['com.github.debauchee.barrier', 'barrierc', 'barriers'], 'network', 'Barrier')
def barrier(c):
    monitor(c, 4, 3, 15, 13, 'k', 'B', False)
    monitor(c, 17, 3, 28, 13, 'k', 'B', False)
    c.rect(8, 14, 9, 15, 's'); c.rect(22, 14, 23, 15, 's')
    c.rect(5, 16, 27, 17, 's')
    c.poly([(11, 21), (21, 21), (21, 18), (26, 23.5), (21, 29), (21, 26), (11, 26), (11, 29), (5.5, 23.5), (11, 18)],
           'O')
    c.bevel(['O'])
    c.outline()


@icon('input-leap', ['io.github.input_leap.input-leap', 'org.input-leap.InputLeap', 'input-leapc',
                     'input-leap-git'], 'network', 'Input Leap')
def input_leap(c):
    monitor(c, 4, 3, 15, 13, 'k', 'G', False)
    monitor(c, 17, 3, 28, 13, 'k', 'G', False)
    c.rect(8, 14, 9, 15, 's'); c.rect(22, 14, 23, 15, 's')
    c.rect(5, 16, 27, 17, 's')
    c.arc(16, 30, 10, 7, 200, 340, 'Y')
    c.poly([(23, 20), (28, 24), (22, 27)], 'Y')
    c.bevel(['Y'])
    c.outline()


@icon('deskflow', ['org.deskflow.deskflow', 'deskflow-bin', 'deskflow-git'], 'network', 'Deskflow')
def deskflow(c):
    c.rrect(3, 5, 28, 26, 'B', 4)
    c.bevel(['B'])
    c.poly([(7, 11), (18, 11), (18, 8), (24, 13), (18, 18), (18, 15), (7, 15)], 'W')
    c.poly([(25, 18), (14, 18), (14, 15), (8, 20), (14, 25), (14, 22), (25, 22)], 'c')
    c.outline()


@icon('synergy', ['synergy3', 'synergy-core', 'com.symless.Synergy', 'synergy1'], 'network', 'Synergy')
def synergy(c):
    disc(c, 'k')
    c.arc(16, 16, 10, 6.5, 200, 340, 'O')
    c.arc(16, 16, 10, 6.5, 20, 160, 'C')
    c.poly([(26, 11), (27, 17), (22, 15)], 'O')
    c.poly([(6, 21), (5, 15), (10, 17)], 'C')
    c.outline()


@icon('nitroshare', ['net.nitroshare.NitroShare', 'nitroshare-desktop'], 'network', 'NitroShare')
def nitroshare(c):
    disc(c, 'O')
    c.poly([(18, 5), (9, 17), (15, 17), (13, 27), (23, 14), (17, 14), (19, 5)], 'W')
    c.outline()


@icon('dukto', ['dukto-r6', 'msec.it.dukto'], 'network', 'Dukto')
def dukto(c):
    c.poly([(3, 4), (28, 4), (28, 20), (16, 28), (3, 20)], 'O')
    c.bevel(['O'])
    c.poly([(11, 8), (21, 8), (21, 14), (25, 14), (16, 23), (7, 14), (11, 14)], 'W')
    c.outline()


# ================================================================ more boot media / remote desktop / transfer

@icon('unetbootin', ['unetbootin-bin', 'unetbootin-git'], 'system', 'UNetbootin')
def unetbootin(c):
    disc(c, 'w')
    c.circle(16, 16, 10, 'W')
    c.ring(16, 16, 12, 10.5, 'S')
    c.circle(16, 16, 3, 'S')
    c.circle(16, 16, 1.5, '.')
    c.rrect(17, 16, 28, 28, 'B', 1)
    c.bevel(['B'])
    c.text(21, 19, 'U', 'W', 3, 1)
    c.outline()


@icon('org.gnome.MultiWriter', ['gnome-multi-writer'], 'system', 'MultiWriter')
def multiwriter(c):
    for x0, col in ((4, 'B'), (12, 'G'), (20, 'O')):
        c.rect(x0 + 2, 4, x0 + 5, 9, 'w')
        c.rrect(x0, 9, x0 + 7, 27, col, 1)
    c.bevel(['w'])
    c.bevel(['B', 'G', 'O'], light=False)
    c.outline()


@icon('nomachine', ['NoMachine', 'nxplayer', 'com.nomachine.nxplayer', 'nomachine-client', 'nxclient'],
      'network', 'NoMachine')
def nomachine(c):
    c.rrect(3, 3, 28, 28, 'O', 5)
    c.bevel(['O'])
    c.rect(8, 8, 10, 19, 'W'); c.rect(8, 22, 10, 24, 'W')
    c.text(13, 11, 'M', 'W', 5, 1)
    c.rect(13, 11, 23, 24, 'O')
    g(c, 13, 8, """
        ##.......##
        ###.....###
        ####...####
        ##.##.##.##
        ##..###..##
        ##...#...##
        ##.......##
        ##.......##
        ##.......##
        ##.......##
        ##.......##
        ##.......##
        ##.......##
        ##.......##
        ##.......##
        ##.......##
        ##.......##
    """)
    c.outline()


@icon('x2goclient', ['x2go', 'org.x2go.x2goclient', 'pyhoca-gui'], 'network', 'X2Go Client')
def x2go(c):
    monitor(c, 3, 4, 28, 22, 'k', 'G')
    c.line(9, 8, 17, 18, 'W', 2); c.line(17, 8, 9, 18, 'W', 2)
    c.text(20, 10, '2', 'W', 3, 1)
    c.outline()


@icon('io.github.nozwock.Packet', [], 'network', 'Packet')
def packet(c):
    c.poly([(16, 3), (28, 9), (16, 15), (4, 9)], 'n')
    c.poly([(4, 10), (15, 16), (15, 29), (4, 23)], 'N')
    c.poly([(17, 16), (28, 10), (28, 23), (17, 29)], '8')
    c.poly([(9, 6), (21, 12), (21, 15), (9, 9)], 'Y')
    c.outline()


@icon('rquickshare', ['r-quick-share', 'dev.mandre.rquickshare', 'rquickshare-bin', 'rquickshare-appimage'],
      'network', 'RQuickShare')
def rquickshare(c):
    disc(c, 'B')
    c.arc(16, 16, 9, 6.5, 200, 340, 'W')
    c.arc(16, 16, 9, 6.5, 20, 160, 'c')
    c.poly([(23, 9), (27, 15), (20, 14)], 'W')
    c.poly([(9, 23), (5, 17), (12, 18)], 'c')
    c.outline()


@icon('openmtp', ['OpenMTP', 'io.github.ganeshrvel.openmtp', 'openmtp-bin'], 'network', 'OpenMTP')
def openmtp(c):
    c.rrect(3, 3, 15, 28, 'k', 2)
    c.bevel(['k'])
    c.rect(5, 6, 13, 24, 'G')
    c.rrect(19, 8, 28, 23, 'W', 1)
    c.bevel(['W'])
    c.poly([(16, 15), (16, 12), (21, 16.5), (16, 21), (16, 18)], 'G')
    c.outline()


@icon('pairdrop', ['pairdrop-webapp', 'snapdrop', 'snapdrop-webapp'], 'network', 'PairDrop')
def pairdrop(c):
    disc(c, 'C')
    c.ring(16, 16, 9, 7.5, 'c')
    c.ring(16, 16, 5.5, 4, 'W')
    c.circle(16, 16, 2, 'W')
    c.outline()
