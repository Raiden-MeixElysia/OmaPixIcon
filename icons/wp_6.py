"""Security, privacy, passwords, VPNs and cloud storage."""
from pix import icon


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


def shield(c, col, x0=4, x1=28, y0=3, y1=29):
    mx = (x0 + x1) / 2
    c.poly([(x0, y0 + 3), (mx, y0), (x1, y0 + 3), (x1, y0 + 14), (mx, y1), (x0, y0 + 14)], col)
    c.bevel([col])


def padlock(c, body, shackle='S', x0=6, x1=26, y0=14, y1=28, sh_r=7.5, sh_w=3, lift=3):
    cx = (x0 + x1 + 1) / 2
    cy = y0 - lift
    c.arc(cx, cy, sh_r, sh_r - sh_w, 180, 360, shackle)
    c.rect(int(round(cx - sh_r)), int(cy), int(round(cx - sh_r + sh_w - 1)), y0, shackle)
    c.rect(int(round(cx + sh_r - sh_w)), int(cy), int(round(cx + sh_r - 1)), y0, shackle)
    c.bevel([shackle])
    c.rrect(x0, y0, x1, y1, body, 2)
    c.bevel([body])


def keyhole(c, cx, cy, col='K'):
    c.circle(cx, cy, 2, col)
    c.rect(int(cx) - 1, int(cy), int(cx), int(cy) + 4, col)


def cloud(c, col, dy=0):
    c.ellipse(16, 20 + dy, 13, 6.5, col)
    c.circle(13, 14 + dy, 7, col)
    c.circle(21.5, 16 + dy, 5.5, col)
    c.bevel([col])


# ================================================================ cloud storage

@icon('proton-drive', ['proton-drive-webapp', 'drive.proton.me', 'me.proton.drive', 'proton-drive-beta'], 'cloud',
      'Proton Drive')
def proton_drive(c):
    c.rrect(3, 6, 14, 10, '7', 1)
    c.rrect(3, 8, 28, 27, 'M', 2)
    c.bevel(['M'])
    c.rect(3, 12, 28, 13, '7')
    c.ellipse(16, 21, 6, 3, 'W')
    c.circle(14, 18.5, 3, 'W'); c.circle(18.5, 19.5, 2.5, 'W')
    c.outline()


@icon('proton-calendar', ['proton-calendar-webapp', 'calendar.proton.me'], 'office', 'Proton Calendar')
def proton_calendar(c):
    c.rrect(3, 5, 28, 28, 'W', 2)
    c.bevel(['W'])
    c.rect(3, 5, 28, 11, 'M'); c.rrect(3, 5, 28, 8, 'M', 2)
    c.rect(8, 3, 9, 7, 'S'); c.rect(22, 3, 23, 7, 'S')
    c.bevel(['M'])
    for y in (14, 19, 24):
        for x in (6, 11, 16, 21):
            c.rect(x, y, x + 3, y + 2, 'w')
    c.rect(11, 19, 14, 21, 'M')
    c.outline()


@icon('proton-authenticator', ['me.proton.Authenticator', 'proton-authenticator-bin'], 'security',
      'Proton Authenticator')
def proton_authenticator(c):
    shield(c, 'M')
    ctext(c, '123', 'W', 14, 1, 3)
    c.rect(9, 19, 22, 20, 'm')
    c.outline()


@icon('tutanota-desktop', ['tuta', 'tuta-mail', 'tutanota', 'com.tutanota.Tutanota', 'tutanota-desktop-bin',
                           'tuta-webapp'], 'mail', 'Tuta Mail')
def tuta(c):
    c.rrect(3, 3, 28, 28, 'R', 5)
    c.bevel(['R'])
    c.circle(12, 13, 4.5, 'W'); c.circle(20, 13, 4.5, 'W')
    c.poly([(7.5, 15), (24.5, 15), (16, 24)], 'W')
    c.outline()


@icon('megasync', ['mega', 'nz.mega.MegaSync', 'mega-desktop', 'megasync-bin', 'mega-webapp'], 'cloud', 'MEGA')
def mega(c):
    disc(c, 'R')
    g(c, 8, 9, """
        ##.............##
        ###...........###
        ####.........####
        ##.##.......##.##
        ##..##.....##..##
        ##...##...##...##
        ##....##.##....##
        ##.....###.....##
        ##......#......##
        ##.............##
        ##.............##
        ##.............##
        ##.............##
        ##.............##
    """)
    c.shift(0, 0)
    c.rect(8, 9, 8, 9, 'W')
    c.outline()


@icon('pcloud', ['pcloud-drive', 'com.pcloud.pcloud', 'pcloud-webapp'], 'cloud', 'pCloud')
def pcloud(c):
    c.ellipse(16, 20, 13, 7.5, 'C')
    c.circle(14, 13, 8, 'C')
    c.circle(22, 16, 6, 'C')
    c.bevel(['C'])
    g(c, 12, 11, """
        ######.
        #######
        ##...##
        #######
        ######.
        ##.....
        ##.....
    """)
    c.outline()


@icon('box-drive', ['box-webapp', 'box.com', 'com.box.Box'], 'cloud', 'Box')
def box(c):
    c.rrect(3, 7, 28, 25, 'B', 3)
    c.bevel(['B'])
    g(c, 5, 12, """
        #.........................
        #.........................
        ####...###..#...#.........
        #...#.#...#..#.#..........
        #...#.#...#...#...........
        #...#.#...#..#.#..........
        ####...###..#...#.........
    """)
    c.outline()


@icon('filen-desktop', ['filen', 'io.filen.desktop', 'filen-desktop-bin', 'filen-webapp'], 'cloud', 'Filen')
def filen(c):
    c.rrect(3, 3, 28, 28, 'k', 5)
    c.bevel(['k'])
    c.ellipse(16, 19, 9.5, 5, 'W')
    c.circle(13.5, 15, 5, 'W'); c.circle(19.5, 16, 4, 'W')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('koofr', ['net.koofr.Koofr', 'koofr-desktop'], 'cloud', 'Koofr')
def koofr(c):
    c.ellipse(16, 20, 13, 7.5, 'b')
    c.circle(13, 13, 8, 'b')
    c.circle(22, 16, 6, 'b')
    c.bevel(['b'])
    ctext(c, 'K', 'B', 18, 2, 3)
    c.outline()


@icon('seafile', ['seafile-client', 'com.seafile.Client', 'seafile-applet', 'seadrive', 'seadrive-gui'], 'cloud',
      'Seafile')
def seafile(c):
    c.ellipse(16, 20, 13, 7.5, 'O')
    c.circle(13, 13, 8, 'O')
    c.circle(22, 16, 6, 'O')
    c.bevel(['O'])
    c.arc(16, 30, 13, 10, 220, 320, 'W')
    c.arc(16, 30, 9, 6.5, 230, 310, 'W')
    c.outline()


@icon('owncloud', ['com.owncloud.desktopclient.owncloud', 'owncloud-client', 'owncloud-desktop'], 'cloud',
      'ownCloud')
def owncloud(c):
    c.ellipse(16, 20, 13, 7.5, '6')
    c.circle(13, 13, 8, '6')
    c.circle(22, 16, 6, '6')
    c.bevel(['6'])
    c.ring(14, 15, 5, 3, 'W')
    c.ring(21, 19, 3.5, 2, 'W')
    c.outline()


@icon('resilio-sync', ['rslsync', 'resilio', 'com.resilio.Sync'], 'cloud', 'Resilio Sync')
def resilio(c):
    disc(c, 'O')
    c.ring(16, 16, 9, 6.5, 'W')
    c.ring(16, 16, 4.5, 2, 'W')
    c.rect(16, 16, 26, 17, 'O')
    c.outline()


# ================================================================ encryption / passwords

@icon('org.cryptomator.Cryptomator', ['cryptomator', 'cryptomator-bin'], 'security', 'Cryptomator')
def cryptomator(c):
    padlock(c, 'G', 'S', 5, 26, 13, 28)
    # robot face
    c.rect(9, 17, 22, 24, '4')
    c.rect(11, 19, 13, 21, 'W'); c.rect(18, 19, 20, 21, 'W')
    c.outline()


@icon('veracrypt', ['VeraCrypt', 'veracrypt-console', 'veracrypt-bin'], 'security', 'VeraCrypt')
def veracrypt(c):
    c.poly([(3, 4), (10, 4), (16, 20), (22, 4), (29, 4), (19, 29), (13, 29)], 'B')
    c.bevel(['B'])
    keyhole(c, 16, 9, 'W')
    c.outline()


@icon('picocrypt', ['io.github.picocrypt.Picocrypt', 'Picocrypt', 'picocrypt-bin'], 'security', 'Picocrypt')
def picocrypt(c):
    padlock(c, 'C', 'S')
    keyhole(c, 16, 19, '5')
    c.outline()


@icon('keepass', ['keepass2', 'KeePass', 'org.keepass.KeePass'], 'security', 'KeePass')
def keepass(c):
    padlock(c, 'B', 'S', 4, 21, 13, 27, 6, 2.5, 1)
    keyhole(c, 12.5, 18, 'W')
    # key
    c.ring(23.5, 16, 4, 2, 'Y')
    c.rect(22, 19, 24, 29, 'Y')
    c.rect(25, 24, 27, 25, 'Y'); c.rect(25, 27, 26, 28, 'Y')
    c.bevel(['Y'])
    c.outline()


@icon('enpass', ['io.enpass.Enpass', 'enpass-bin'], 'security', 'Enpass')
def enpass(c):
    disc(c, 'B')
    c.ring(12, 13, 5.5, 2.5, 'W')
    c.line(15, 16, 23, 24, 'W', 3)
    c.line(20, 22, 23, 19, 'W', 2)
    c.outline()


@icon('nordpass', ['nordpass-bin', 'com.nordpass.NordPass', 'nordpass-webapp'], 'security', 'NordPass')
def nordpass(c):
    disc(c, 'C')
    c.ring(16, 12, 5, 2.5, 'W')
    c.rect(14, 15, 18, 25, 'W')
    c.rect(18, 20, 21, 21, 'W'); c.rect(18, 23, 20, 24, 'W')
    c.outline()


@icon('dashlane', ['dashlane-webapp', 'dashlane.com'], 'security', 'Dashlane')
def dashlane(c):
    c.rrect(3, 3, 28, 28, '5', 5)
    c.bevel(['5'])
    c.poly([(9, 7), (17, 7), (23, 12), (23, 20), (17, 25), (9, 25)], 'W')
    c.poly([(13, 11), (17, 11), (19, 14), (19, 18), (17, 21), (13, 21)], '5')
    c.outline()


@icon('lastpass', ['lastpass-webapp', 'lastpass.com'], 'security', 'LastPass')
def lastpass(c):
    c.rrect(3, 7, 28, 25, 'R', 3)
    c.bevel(['R'])
    for x in (6, 12, 18):
        c.circle(x + 2, 16, 2.6, 'W')
    c.rect(24, 10, 25, 22, 'W')
    c.outline()


@icon('io.ente.auth', ['ente-auth', 'enteauth', 'ente-auth-bin'], 'security', 'Ente Auth')
def ente_auth(c):
    shield(c, 'k')
    c.ring(16, 14, 5.5, 3, 'M')
    c.rect(16, 14, 22, 15, 'k')
    c.rect(11, 22, 21, 23, 'm')
    c.outline()


@icon('io.ente.photos', ['ente', 'ente-photos', 'ente-desktop', 'ente-photos-bin'], 'cloud', 'Ente Photos')
def ente_photos(c):
    c.rrect(3, 5, 28, 26, 'G', 3)
    c.bevel(['G'])
    c.rect(6, 8, 25, 23, 'W')
    c.poly([(7, 22), (13, 14), (17, 19), (20, 16), (24, 22)], '4')
    c.circle(20, 11.5, 2, 'Y')
    c.outline()


@icon('com.yubico.yubioath', ['yubico-authenticator', 'yubioath-flutter', 'yubioath-desktop', 'yubikey-manager',
                              'ykman-gui', 'com.yubico.yubikey_manager'], 'security', 'Yubico Authenticator')
def yubico(c):
    # security key
    c.rrect(9, 3, 23, 22, 'k', 3)
    c.bevel(['k'])
    c.rect(11, 22, 21, 28, 'w')
    c.bevel(['w'])
    c.hline(13, 19, 25, 'S')
    c.circle(16, 12, 4.5, 'G')
    c.circle(16, 12, 2, 'g')
    c.outline()


# ================================================================ VPN / network security

@icon('tailscale', ['tailscale-systray', 'com.tailscale.Tailscale', 'trayscale', 'dev.deedles.Trayscale',
                    'tailscale-gui', 'ktailctl', 'org.fkoehler.KTailctl'], 'network', 'Tailscale')
def tailscale(c):
    c.rrect(3, 3, 28, 28, 'k', 4)
    c.bevel(['k'])
    for j, y in enumerate((8, 16, 24)):
        for i, x in enumerate((8, 16, 24)):
            on = (j == 1) or (j == 2 and i == 1)
            c.circle(x, y, 2.6, 'W' if on else 's')
    c.outline()


@icon('zerotier', ['zerotier-one', 'com.zerotier.ZeroTierOne', 'zerotier-ui', 'zerotier-gui'], 'network',
      'ZeroTier')
def zerotier(c):
    disc(c, 'Y')
    c.ring(16, 17, 8.5, 6.5, 'k')
    c.rect(8, 6, 24, 7, 'k')
    c.rect(15, 6, 16, 20, 'k')
    c.outline()


@icon('wireguard', ['wireguard-gui', 'com.wireguard', 'wireguard-tools', 'wireguird', 'wg-gui',
                    'io.github.wireguard_gui'], 'network', 'WireGuard')
def wireguard(c):
    disc(c, 'R')
    # coiled dragon / serpent
    c.arc(16, 16, 9, 6.5, 120, 400, 'W')
    c.arc(17, 16, 4.5, 2, 300, 520, 'W')
    c.circle(10, 22, 2.5, 'W')
    c.px(9, 21, 'R')
    c.outline()


@icon('openvpn', ['openvpn3', 'openvpn-connect', 'net.openvpn.openvpn3', 'net.openvpn.openvpn_connect',
                  'openvpn-gui'], 'network', 'OpenVPN')
def openvpn(c):
    disc(c, 'O')
    c.circle(16, 13, 6, 'W')
    c.poly([(13, 15), (19, 15), (21, 26), (11, 26)], 'W')
    c.circle(16, 13, 2.5, 'O')
    c.rect(15, 15, 16, 22, 'O')
    c.outline()


@icon('nordvpn', ['nordvpn-gui', 'com.nordvpn.NordVPN', 'nordvpn-bin', 'nordvpn-webapp'], 'network', 'NordVPN')
def nordvpn(c):
    disc(c, 'B')
    c.poly([(5, 24), (13, 9), (17, 16), (19, 13), (27, 24), (24, 24), (19, 17), (17, 20), (13, 13), (8, 24)], 'W')
    c.outline()


@icon('expressvpn', ['expressvpn-gui', 'expressvpn-bin'], 'network', 'ExpressVPN')
def expressvpn(c):
    c.rrect(3, 5, 28, 26, 'R', 4)
    c.bevel(['R'])
    g(c, 7, 9, """
        ...##########...
        ..###...........
        ..##............
        .#########......
        .##.............
        ##..............
        ##########......
        ................
        ....######......
    """)
    c.outline()


@icon('surfshark', ['surfshark-gui', 'com.surfshark.Surfshark', 'surfshark-client', 'surfshark-vpn'], 'network',
      'Surfshark')
def surfshark(c):
    c.rrect(3, 3, 28, 28, '5', 5)
    c.bevel(['5'])
    g(c, 9, 7, """
        ..########...
        .##..........
        ##...........
        ##...........
        .########....
        ..########...
        ..........##.
        ..........##.
        .........##..
        .########....
    """)
    c.outline()


@icon('ivpn', ['ivpn-ui', 'net.ivpn.client', 'ivpn-client'], 'network', 'IVPN')
def ivpn(c):
    shield(c, 'k')
    ctext(c, 'IV', 'W', 14, 2, 3)
    c.outline()


@icon('windscribe', ['com.windscribe.Windscribe', 'windscribe-v2', 'windscribe-bin'], 'network', 'Windscribe')
def windscribe(c):
    disc(c, '6')
    for i, (y, x0, x1) in enumerate(((10, 8, 22), (15, 6, 25), (20, 9, 20))):
        c.rect(x0, y, x1, y + 1, 'W')
    c.arc(22, 12, 3, 1.6, 180, 450, 'W')
    c.arc(25, 17, 3, 1.6, 270, 540, 'W')
    c.outline()


@icon('cloudflare-warp', ['warp-taskbar', 'com.cloudflare.WarpTaskbar', '1.1.1.1', 'cloudflare-warp-bin',
                          'cloudflare'], 'network', 'Cloudflare WARP')
def cloudflare_warp(c):
    c.ellipse(16, 20, 13, 6.5, 'O')
    c.circle(15, 14, 8, 'O')
    c.circle(23, 17, 5, 'o')
    c.ellipse(24, 21, 5, 4, 'o')
    c.bevel(['O'])
    c.hline(6, 24, 22, '2')
    c.outline()


@icon('portmaster', ['io.safing.portmaster', 'portmaster-start'], 'security', 'Portmaster')
def portmaster(c):
    shield(c, 'B')
    c.ring(16, 15, 6, 4, 'W')
    c.circle(16, 15, 2, 'W')
    c.outline()


@icon('opensnitch-ui', ['opensnitch', 'io.github.evilsocket.opensnitch', 'opensnitch-git'], 'security',
      'OpenSnitch')
def opensnitch(c):
    # the snitch: winged golden ball
    c.poly([(3, 8), (12, 12), (12, 18), (5, 16)], 'W')
    c.poly([(29, 8), (20, 12), (20, 18), (27, 16)], 'W')
    c.bevel(['W'])
    c.circle(16, 16, 6.5, 'Y')
    c.bevel(['Y'])
    c.arc(16, 16, 6.5, 5, 60, 120, '3')
    c.px(13, 13, 'W')
    c.outline()


@icon('gufw', ['gufw-gtk', 'ufw', 'firewall-config', 'org.fedoraproject.FirewallConfig'], 'security', 'Gufw')
def gufw(c):
    # brick wall shield
    shield(c, 'R')
    for y in (9, 14, 19):
        c.hline(5, 27, y, '1')
    for y, xs in ((5, (16,)), (10, (10, 22)), (15, (16,)), (20, (11, 21))):
        for x in xs:
            c.vline(x, y, y + 3, '1')
    c.outline()


@icon('clamtk', ['com.gitlab.davem.ClamTk', 'clamav', 'clamav-gui', 'com.github.clamav'], 'security', 'ClamTk')
def clamtk(c):
    import math
    for y in range(22):
        for x in range(32):
            if ((x + .5 - 16) / 13) ** 2 + ((y + .5 - 19) / 14) ** 2 <= 1:
                c.px(x, y, 'P')
    for y in range(22, 32):
        for x in range(32):
            if ((x + .5 - 16) / 10) ** 2 + ((y + .5 - 22) / 5.5) ** 2 <= 1:
                c.px(x, y, '9')
    c.bevel(['P'])
    for a in (-150, -120, -90, -60, -30):
        r = math.radians(a)
        c.line(16, 20, 16 + 11 * math.cos(r), 19 + 12 * math.sin(r), '9')
    c.rect(14, 21, 17, 22, '9')
    c.outline()


@icon('firejail', ['firetools', 'firejail-ui'], 'security', 'Firejail')
def firejail(c):
    c.poly([(16, 3), (24, 12), (26, 20), (22, 27), (10, 27), (6, 20), (9, 11), (12, 15)], 'O')
    c.poly([(16, 12), (21, 19), (19, 26), (13, 26), (11, 20)], 'Y')
    c.bevel(['O'])
    for x in (8, 13, 18, 23):
        c.rect(x, 5, x + 1, 28, 's')
    c.rect(5, 26, 26, 28, 's')
    c.outline()


# ================================================================ more privacy tools

@icon('org.onionshare.OnionShare', ['onionshare', 'onionshare-gui', 'onionshare-desktop', 'onionshare-cli'],
      'security', 'OnionShare')
def onionshare(c):
    c.ellipse(16, 18, 11, 10, 'M')
    c.poly([(11, 10), (16, 3), (21, 10)], 'M')
    c.bevel(['M'])
    c.arc(16, 18, 7.5, 6.5, 0, 360, '7')
    c.arc(16, 18, 4, 3, 0, 360, '7')
    c.poly([(13, 21), (16, 16), (19, 21)], 'W')
    c.rect(15, 20, 16, 23, 'W')
    c.outline()


@icon('qtpass', ['QtPass', 'org.qtpass.QtPass', 'qtpass-git'], 'security', 'QtPass')
def qtpass(c):
    padlock(c, 'G', 'S')
    ctext(c, 'QT', 'W', 21, 1, 3)
    c.outline()


@icon('com.bktus.gpgfrontend', ['gpgfrontend', 'GpgFrontend', 'gpgfrontend-bin'], 'security', 'GpgFrontend')
def gpgfrontend(c):
    c.rrect(3, 9, 24, 26, 'W', 1)
    c.bevel(['W'])
    c.line(4, 10, 13, 18, 'S'); c.line(23, 10, 14, 18, 'S')
    c.ring(23, 10, 6, 3, 'Y')
    c.line(19, 14, 12, 21, 'Y', 3)
    c.bevel(['Y'])
    c.outline()


@icon('org.mozilla.vpn', ['mozillavpn', 'mozilla-vpn', 'mozillavpn-bin'], 'network', 'Mozilla VPN')
def mozillavpn(c):
    shield(c, 'M')
    c.arc(16, 16, 8, 5.5, 160, 380, 'O')
    c.circle(16, 15, 2.5, 'W')
    c.outline()


@icon('AmneziaVPN', ['amneziavpn', 'amnezia-vpn', 'org.amnezia.AmneziaVPN', 'amnezia-vpn-bin', 'amneziawg'],
      'network', 'AmneziaVPN')
def amnezia(c):
    disc(c, 'k')
    c.ring(16, 16, 10, 7.5, 'Y')
    c.poly([(16, 9), (22, 23), (19, 23), (16, 15), (13, 23), (10, 23)], 'Y')
    c.outline()


@icon('io.github.mhogomchungu.sirikali', ['sirikali', 'SiriKali'], 'security', 'SiriKali')
def sirikali(c):
    padlock(c, 'O', 'S')
    c.rect(9, 18, 22, 19, '2'); c.rect(9, 22, 22, 23, '2')
    c.outline()


@icon('riseup-vpn', ['riseupvpn', 'se.leap.riseupvpn', 'bitmask-vpn'], 'network', 'RiseupVPN')
def riseup(c):
    disc(c, 'R')
    c.poly([(16, 6), (24, 15), (19, 15), (19, 25), (13, 25), (13, 15), (8, 15)], 'W')
    c.outline()


@icon('outline-client', ['org.getoutline.OutlineClient', 'outline-vpn', 'outline-manager'], 'network',
      'Outline VPN')
def outline_client(c):
    disc(c, 's')
    c.ring(16, 16, 9, 6, 'W')
    c.poly([(16, 10), (21, 16), (16, 22)], 'W')
    c.outline()
