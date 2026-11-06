"""Media, audio, graphics and games apps."""
from pix import icon


def play(c, x, y, h, col):
    """Solid right-pointing play triangle, h rows tall (odd), top-left at x,y."""
    m = h // 2
    for j in range(h):
        c.hline(x, x + (m - abs(j - m)), y + j, col)


def big(c, x, y, art, col, k=2):
    """Blit an ASCII glyph ('#' = on) scaled k times."""
    lines = [l.strip() for l in art.strip('\n').split('\n')]
    for j, row in enumerate(lines):
        for i, ch in enumerate(row):
            if ch == '#':
                c.rect(x + i * k, y + j * k, x + i * k + k - 1, y + j * k + k - 1, col)


# =================================================================== video

@icon('vlc', ['org.videolan.VLC', 'vlc-qt', 'vlc-xspf'], 'media', 'VLC')
def vlc(c):
    c.rrect(3, 23, 28, 28, 'O', 1)
    c.bevel(['O'])
    c.poly([(14, 3.5), (18, 3.5), (24.5, 25), (7.5, 25)], 'O')
    c.replace('O', 'W', (0, 8, 31, 10))
    c.replace('O', 'W', (0, 15, 31, 17))
    c.bevel(['O', 'W'])
    c.hline(4, 27, 23, '2')
    c.outline()


@icon('org.gnome.Totem', ['totem', 'org.gnome.Totem-symbolic', 'gnome-videos'], 'media', 'Videos')
def totem(c):
    c.rrect(3, 6, 28, 25, 'k', 1)
    for x in range(5, 28, 3):
        c.rect(x, 8, x + 1, 9, 'w')
        c.rect(x, 22, x + 1, 23, 'w')
    for x0 in (5, 13, 21):
        c.rect(x0, 11, x0 + 5, 20, 'b')
        c.hline(x0, x0 + 5, 11, 'c')
        c.rect(x0, 17, x0 + 5, 20, '6')
    c.px(14, 12, 'W')
    play(c, 15, 13, 5, 'W')
    c.outline()


@icon('celluloid', ['io.github.celluloid_player.Celluloid', 'gnome-mpv', 'io.github.GnomeMpv'],
      'media', 'Celluloid')
def celluloid(c):
    c.poly([(5, 3), (28.5, 16), (5, 29)], 'B')
    c.replace('B', '.', (5, 3, 5, 4))
    c.replace('B', '.', (5, 27, 5, 28))
    c.bevel(['B'])
    c.poly([(9, 10), (21, 16), (9, 22)], 'b')
    c.poly([(10, 12.5), (17, 16), (10, 19.5)], 'W')
    c.outline()


@icon('haruna', ['org.kde.haruna'], 'media', 'Haruna')
def haruna(c):
    import math
    for i in range(5):
        a = math.radians(-90 + 72 * i)
        c.circle(16 + 7.5 * math.cos(a), 16.5 + 7.5 * math.sin(a), 6, 'P')
    c.bevel(['P'])
    c.circle(16, 16.5, 5.5, '9')
    c.circle(16, 16.5, 4.5, 'W')
    play(c, 15, 14, 5, '9')
    c.outline()


@icon('handbrake', ['fr.handbrake.ghb', 'ghb', 'HandBrake'], 'media', 'HandBrake')
def handbrake(c):
    # crown
    c.sprite(6, 3, """
        ...G.G...
        G..GGG..G
        GG.G4G.GG
        .GG4G4GG.
        ..GG4GG..
        .GG4G4GG.
    """)
    # pineapple body
    c.ellipse(10.5, 19, 7, 9.5, 'Y')
    for y in range(10, 29):
        for x in range(3, 19):
            if c.get(x, y) == 'Y' and ((x + y) % 4 == 0 or (x - y) % 4 == 0):
                c.px(x, y, 'O')
    c.bevel(['Y', 'O'])
    # tropical drink
    c.poly([(19, 15), (29, 15), (27.5, 28.5), (20.5, 28.5)], 'w')
    c.replace('w', 'O', (0, 19, 31, 31))
    c.hline(19, 28, 15, 'W')
    c.vline(21, 16, 27, 'W')
    c.line(26, 15, 28, 11, 'R')
    c.outline()


@icon('shotcut', ['org.shotcut.Shotcut', 'Shotcut'], 'media', 'Shotcut')
def shotcut(c):
    # clapper arm, hinged open at the right (stepped blocks) + board
    for x in range(4, 28):
        b = (x - 4) // 4
        c.vline(x, 9 - b, 12 - b, 'k' if b % 2 else 'W')
    c.rect(4, 14, 28, 18, 'W')
    for x in range(4, 28, 6):
        c.poly([(x + 3, 14), (x + 6, 14), (x + 3, 18.9), (x, 18.9)], 'k')
    c.hline(4, 28, 18, 'w')
    c.rect(4, 19, 28, 28, 'C')
    c.bevel(['C'])
    c.hline(7, 18, 23, '5'); c.hline(7, 14, 25, '5')
    c.rect(22, 23, 25, 25, 'c')
    c.outline()


@icon('openshot-qt', ['org.openshot.OpenShot', 'openshot'], 'media', 'OpenShot')
def openshot(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.circle(16, 16, 3, 'w')
    c.circle(16, 16, 1.5, 'k')
    import math
    for i in range(5):
        a = math.radians(-90 + 72 * i)
        c.circle(16 + 7.5 * math.cos(a), 16 + 7.5 * math.sin(a), 3.2, 'k')
        c.px(int(15.5 + 7.5 * math.cos(a)) - 1, int(15.5 + 7.5 * math.sin(a)) - 1, '6')
    c.outline()


@icon('resolve', ['davinci-resolve', 'DaVinci Resolve', 'com.blackmagicdesign.resolve', 'davinci-resolve-studio'],
      'media', 'DaVinci Resolve')
def resolve(c):
    for cx, cy, col in ((16, 9.5, 'C'), (10, 21.5, 'R'), (22, 21.5, 'G')):
        c.circle(cx, cy, 7, 'K')
        c.circle(cx, cy, 6, col)
        c.bevel([col], edge=('.', 'K'))
    c.outline()


@icon('freetube', ['io.freetubeapp.FreeTube', 'FreeTube'], 'media', 'FreeTube')
def freetube(c):
    c.rrect(3, 3, 10, 28, 'B', 1)
    c.rrect(12, 3, 28, 9, 'B', 1)
    c.poly([(12, 12), (24, 18.5), (12, 25)], 'R')
    c.bevel(['B', 'R'])
    c.outline()


@icon('stremio', ['com.stremio.Stremio', 'Stremio'], 'media', 'Stremio')
def stremio(c):
    c.poly([(16, 3), (29, 16), (16, 29), (3, 16)], 'M')
    c.bevel(['M'])
    c.poly([(13, 10), (22, 16), (13, 22)], 'W')
    c.outline()


@icon('jellyfin-media-player', ['com.github.iwalton3.jellyfin-media-player', 'jellyfin', 'org.jellyfin.JellyfinDesktop',
                                'jellyfinmediaplayer'], 'media', 'Jellyfin')
def jellyfin(c):
    c.poly([(16, 3), (29, 27), (3, 27)], 'M')
    c.dither(0, 15, 31, 17, 'M', 'B', only='M')
    c.replace('M', 'B', (0, 18, 31, 31))
    c.bevel(['M', 'B'])
    c.poly([(16, 10), (23.5, 23.5), (8.5, 23.5)], 'k')
    c.poly([(16, 15), (19.5, 21.5), (12.5, 21.5)], 'b')
    c.outline()


@icon('plex', ['plexmediaplayer', 'tv.plex.PlexDesktop', 'plex-desktop', 'tv.plex.PlexHTPC', 'plex-htpc'],
      'media', 'Plex')
def plex(c):
    c.poly([(5, 3), (14, 3), (27, 16), (14, 29), (5, 29), (18, 16)], 'Y')
    c.bevel(['Y'])
    c.outline()


@icon('kodi', ['tv.kodi.Kodi', 'kodi-standalone'], 'media', 'Kodi')
def kodi(c):
    c.poly([(16, 3), (29, 16), (16, 29), (3, 16)], 'C')
    c.rect(15, 0, 16, 31, '.')
    c.rect(0, 15, 31, 16, '.')
    c.bevel(['C'])
    c.outline()


# =================================================================== audio

@icon('audacity', ['org.audacityteam.Audacity', 'audacity-bin'], 'audio', 'Audacity')
def audacity(c):
    c.arc(16, 17, 13, 10, 180, 360, 'B')
    c.rect(3, 17, 5, 18, 'B'); c.rect(26, 17, 28, 18, 'B')
    c.rrect(3, 16, 9, 28, '6', 1); c.rrect(22, 16, 28, 28, '6', 1)
    c.rect(5, 18, 9, 27, 'B'); c.rect(22, 18, 26, 27, 'B')
    c.bevel(['B'])
    for x, h in zip(range(11, 21), (2, 4, 7, 4, 9, 6, 3, 6, 4, 2)):
        c.vline(x, 21 - h // 2 - (h > 6), 21 + h // 2, 'O' if h < 6 else 'R')
    c.outline()


@icon('ardour', ['ardour8', 'ardour7', 'ardour6', 'Ardour', 'org.ardour.Ardour', 'ardour-8'], 'audio', 'Ardour')
def ardour(c):
    c.poly([(7, 3), (25, 3), (28, 28.5), (4, 28.5)], 'S')
    c.bevel(['S'])
    for i, (x, y, col) in enumerate(((9, 15, 'R'), (15, 9, 'Y'), (21, 19, 'G'))):
        c.rect(x + 1, 6, x + 1, 26, 'k')
        c.rect(x - 1, y, x + 3, y + 3, col)
        c.hline(x - 1, x + 3, y, LIGHT_OF[col])
        c.hline(x - 1, x + 3, y + 3, 's')
    c.outline()


LIGHT_OF = {'R': 'r', 'Y': 'y', 'G': 'g', 'B': 'b', 'C': 'c', 'O': 'o', 'M': 'm', 'P': 'p', 'N': 'n', 'w': 'W'}
DARK_OF = {'R': '1', 'Y': '3', 'G': '4', 'B': '6', 'C': '5', 'O': '2', 'M': '7', 'P': '9', 'N': '8', 'w': 'S'}


@icon('lmms', ['io.lmms.LMMS', 'lmms-bin'], 'audio', 'LMMS')
def lmms(c):
    c.rrect(3, 7, 28, 25, 'G', 2)
    c.bevel(['G'])
    c.rect(5, 12, 26, 23, 'W')
    for x in range(8, 26, 3):
        c.vline(x, 12, 23, 's')
    for x in (7, 10, 16, 19, 22):
        c.rect(x, 12, x + 1, 17, 'k')
    c.hline(5, 26, 23, 'w')
    c.rect(5, 9, 9, 10, 'g'); c.rect(23, 9, 24, 10, '4'); c.rect(20, 9, 21, 10, '4')
    c.outline()


@icon('reaper', ['cockos-reaper', 'REAPER', 'fm.reaper.Reaper'], 'audio', 'REAPER')
def reaper(c):
    c.circle(16, 16, 13, 'S')
    c.bevel(['S'])
    c.circle(16, 16, 10.5, 'k')
    c.sprite(11, 9, """
        #######.
        ########
        ##....##
        ##....##
        ########
        #######.
        ##..##..
        ##...##.
        ##....##
        ##....##
    """, {'#': 'W'})
    c.replace('W', 'w', (11, 18, 20, 18))
    c.outline()


@icon('bitwig-studio', ['com.bitwig.BitwigStudio', 'bitwig', 'Bitwig Studio'], 'audio', 'Bitwig Studio')
def bitwig(c):
    heights = (2, 3, 4, 3, 2)
    for i, h in enumerate(heights):
        x = 3 + i * 5
        for j in range(h):
            y = 24 - j * 5 - (4 - h) * 0
            col = 'O'
            c.rrect(x, y, x + 3, y + 3, col, 1)
    c.bevel(['O'])
    c.outline()


@icon('musescore', ['org.musescore.MuseScore', 'mscore', 'mscore4', 'musescore4', 'mscore3', 'musescore3',
                    'MuseScore4', 'MuseScore'], 'audio', 'MuseScore')
def musescore(c):
    c.poly([(5, 3), (22, 3), (27, 8), (27, 29), (5, 29)], 'W')
    c.bevel(['W'], light=False)
    c.sprite(22, 3, """
        K....
        wK...
        wwK..
        wwwK.
        SSSSK
    """)
    c.rect(5, 3, 21, 5, 'B'); c.hline(5, 21, 3, 'b')
    for y in range(11, 26, 3):
        c.hline(7, 25, y, 'S')
    c.sprite(9, 13, """
        .......####
        .....####.#
        ...###....#
        ...#......#
        ...#......#
        ...#......#
        ...#......#
        ...#....###
        ..##...####
        ####...###.
        ####.......
        .##........
    """, {'#': 'B'})
    c.outline()


@icon('mixxx', ['org.mixxx.Mixxx', 'mixxx-bin'], 'audio', 'Mixxx')
def mixxx(c):
    c.rrect(3, 4, 28, 27, 'S', 2)
    c.bevel(['S'])
    c.circle(14, 16, 10, 'K')
    c.circle(14, 16, 9, 'k')
    c.ring(14, 16, 7, 6, 's')
    c.ring(14, 16, 4.5, 3.5, 's')
    c.circle(14, 16, 3, 'O')
    c.circle(14, 16, 1, 'k')
    c.px(10, 10, 'w'); c.px(9, 11, 'w')
    c.circle(25, 7, 2, 'w')
    c.line(25, 8, 25, 19, 'W')
    c.line(25, 19, 21, 22, 'W')
    c.rect(20, 22, 21, 23, 'w')
    c.outline()


@icon('rhythmbox', ['org.gnome.Rhythmbox3', 'org.gnome.Rhythmbox', 'rhythmbox-bin'], 'audio', 'Rhythmbox')
def rhythmbox(c):
    c.rrect(5, 3, 26, 28, 'N', 2)
    c.bevel(['N'])
    c.circle(16, 9.5, 4, 'K'); c.circle(16, 9.5, 3, 's'); c.circle(16, 9.5, 1.2, 'w')
    c.circle(16, 20.5, 7, 'K'); c.circle(16, 20.5, 6, 'k')
    c.ring(16, 20.5, 6, 4.5, 's')
    c.circle(16, 20.5, 2.5, 'S'); c.px(15, 19, 'w')
    c.outline()


@icon('lollypop', ['org.gnome.Lollypop'], 'audio', 'Lollypop')
def lollypop(c):
    import math
    c.rect(15, 20, 17, 28, 'W')
    c.vline(17, 21, 28, 'w')
    for y in range(32):
        for x in range(32):
            dx, dy = x + .5 - 16, y + .5 - 13
            r = math.hypot(dx, dy)
            if r <= 9.6:
                t = (math.atan2(dy, dx) / (2 * math.pi)) % 1
                band = int(r / 2.6 + t * 1.0 + 0.4)
                c.px(x, y, 'P' if band % 2 else 'W')
    c.bevel(['P', 'W'], edge=('.',))
    c.px(11, 7, 'W'); c.px(12, 6, 'W')
    c.outline()


@icon('io.bassi.Amberol', ['amberol'], 'audio', 'Amberol')
def amberol(c):
    c.poly([(9, 3), (23, 3), (29, 11), (16, 29), (3, 11)], 'O')
    c.poly([(9, 3), (23, 3), (29, 11), (3, 11)], 'Y')
    c.poly([(12, 3), (20, 3), (22, 10.9), (10, 10.9)], 'y')
    c.poly([(10, 11), (22, 11), (16, 29)], 'o')
    c.bevel(['O', 'Y'])
    c.sprite(13, 13, """
        ..####
        ..#..#
        ..#..#
        ###.##
        ##.###
        ...##.
    """, {'#': '2'})
    c.outline()


@icon('strawberry', ['org.strawberrymusicplayer.strawberry', 'strawberry-music-player'], 'audio', 'Strawberry')
def strawberry(c):
    c.poly([(5, 13), (9, 8), (23, 8), (27, 13), (25, 21), (16, 29.5), (7, 21)], 'R')
    c.ellipse(16, 14.5, 11.5, 7.5, 'R')
    c.bevel(['R'])
    for x, y in ((10, 12), (15, 11), (20, 12), (8, 16), (13, 15), (18, 15), (23, 16), (11, 19),
                 (16, 19), (21, 19), (14, 23), (18, 23)):
        c.px(x, y, 'y')
    c.sprite(8, 3, """
        .......4.......
        ...GG..4..GG...
        .GGGGG.G.GGGGG.
        GgGGGGGGGGGGGgG
        .G..GGG.GGG..G.
    """)
    c.outline()


@icon('org.kde.elisa', ['elisa'], 'audio', 'Elisa')
def elisa(c):
    c.circle(16, 16, 13, 'k')
    c.ring(16, 16, 11, 10, 's')
    c.ring(16, 16, 8.5, 7.5, 's')
    c.circle(16, 16, 5, 'C')
    c.bevel(['C'], edge=('k', 's'))
    c.circle(16, 16, 1.2, 'K')
    c.arc(16, 16, 12, 10.5, 200, 250, 'S')
    c.outline()


@icon('org.gnome.Music', ['gnome-music', 'org.gnome.Music-symbolic'], 'audio', 'Music')
def gnome_music(c):
    c.rect(9, 6, 11, 22, 'O')
    c.rect(24, 3, 26, 19, 'O')
    c.poly([(9, 6), (26.9, 2), (26.9, 7), (9, 11)], 'O')
    c.ellipse(7.5, 24, 4.5, 3.5, 'O')
    c.ellipse(22.5, 21, 4.5, 3.5, 'O')
    c.bevel(['O'])
    c.outline()


@icon('tidal-hifi', ['com.mastermindzh.tidal-hifi', 'tidal', 'Tidal'], 'audio', 'TIDAL')
def tidal(c):
    for cx, cy in ((7.5, 12), (16, 12), (24.5, 12), (16, 20.5)):
        c.poly([(cx, cy - 4.5), (cx + 4.5, cy), (cx, cy + 4.5), (cx - 4.5, cy)], 'W')
    c.bevel(['W'], light=False)
    c.outline()


@icon('youtube-music', ['com.github.th_ch.youtube_music', 'youtube-music-desktop-app',
                        'com.github.th-ch.youtube-music', 'ytmdesktop'], 'audio', 'YouTube Music')
def youtube_music(c):
    c.circle(16, 16, 13, 'R')
    c.bevel(['R'])
    c.ring(16, 16, 8.5, 7, 'W')
    play(c, 14, 12, 9, 'W')
    c.outline()


@icon('cider', ['sh.cider.Cider', 'Cider', 'cider-2'], 'audio', 'Cider')
def cider(c):
    c.rect(5, 8, 21, 28, 'O')
    c.rrect(4, 4, 22, 9, 'W', 2)
    c.ellipse(9, 9, 2.5, 2, 'W'); c.ellipse(17, 9.5, 2, 2, 'W')
    c.bevel(['O'])
    c.ring(23, 17.5, 6, 3, 'w')
    c.rect(18, 9, 21, 28, 'O')
    c.vline(21, 10, 27, '2')
    for x, y in ((9, 15), (13, 19), (8, 23), (15, 25), (11, 12)):
        c.px(x, y, 'y')
    c.vline(7, 11, 26, 'o')
    c.outline()


@icon('de.haeckerfelix.Shortwave', ['shortwave'], 'audio', 'Shortwave')
def shortwave(c):
    c.line(22, 10, 26, 5, 'S')
    c.circle(27, 4.5, 1.5, 'w')
    c.rrect(3, 10, 28, 28, 'R', 2)
    c.bevel(['R'])
    c.rect(5, 13, 15, 25, 'n')
    for y in range(14, 25, 2):
        c.hline(6, 14, y, '8')
    c.rect(18, 13, 26, 17, 'W')
    c.vline(22, 13, 17, 'R')
    c.circle(22, 22.5, 3, 'w'); c.circle(22, 22.5, 1.5, 'S')
    c.outline()


@icon('gpodder', ['org.gpodder.gpodder', 'gPodder'], 'audio', 'gPodder')
def gpodder(c):
    c.ellipse(16, 18, 13, 9, 'G')
    c.ellipse(16, 13, 12, 7, '.')
    c.ellipse(16, 15, 10.5, 5.5, '4')
    for x in (9, 16, 23):
        c.circle(x, 16, 3.5, 'g')
        c.px(x - 1, 14, 'W')
    c.bevel(['G'])
    c.outline()


@icon('com.github.wwmm.easyeffects', ['easyeffects', 'pulseeffects', 'com.github.wwmm.pulseeffects'],
      'audio', 'Easy Effects')
def easyeffects(c):
    import math
    for i in range(9):
        a = math.radians(135 + 33.75 * i)
        x, y = 15.5 + 12.2 * math.cos(a), 16 + 12.2 * math.sin(a)
        c.rect(round(x - .5), round(y - .5), round(x - .5) + 1, round(y - .5) + 1, 'C' if i < 6 else 'S')
    c.circle(16, 16.5, 9, 'S')
    c.bevel(['S'])
    c.circle(16, 16.5, 6.5, 'w')
    c.line(15, 16, 10, 11, 'C', w=2)
    c.outline()


@icon('pavucontrol', ['org.pulseaudio.pavucontrol', 'multimedia-volume-control', 'pavucontrol-qt'], 'audio', 'Volume Control')
def pavucontrol(c):
    c.rect(3, 12, 8, 20, 'S')
    c.poly([(8, 12), (15, 5), (15, 27), (8, 20)], 'w')
    c.bevel(['w', 'S'])
    c.arc(13, 16, 7, 5, -55, 55, 'C')
    c.arc(13, 16, 11, 9, -55, 55, 'C')
    c.arc(13, 16, 15, 13, -55, 55, 'C')
    c.outline()


@icon('helvum', ['org.pipewire.Helvum'], 'audio', 'Helvum')
def helvum(c):
    c.line(10, 9, 15, 9, 'G', w=2)
    c.line(15, 9, 17, 22, 'G', w=2)
    c.line(17, 22, 21, 22, 'G', w=2)
    c.line(10, 13, 13, 13, 'Y', w=1)
    c.rrect(3, 4, 11, 15, 'B', 1)
    c.rrect(20, 17, 28, 28, 'M', 1)
    c.bevel(['B', 'M'])
    c.outline()


@icon('qpwgraph', ['org.rncbc.qpwgraph'], 'audio', 'qpwgraph')
def qpwgraph(c):
    # 6.35mm jack plug on a curling cable
    c.rect(15, 3, 16, 4, 'w'); c.px(15, 3, 'W')
    c.rect(14, 5, 17, 5, 'k')
    c.rect(14, 6, 17, 8, 'w'); c.vline(14, 6, 8, 'W'); c.vline(17, 6, 8, 'S')
    c.rect(12, 9, 19, 10, 'S'); c.hline(12, 19, 9, 'w')
    c.rrect(11, 11, 20, 19, 'B', 1)
    c.bevel(['B'], edge=('.', 'S'))
    for y in (13, 15, 17):
        c.hline(13, 18, y, '6')
    c.rect(13, 20, 18, 21, 'k')
    c.arc(20.5, 22, 6, 3, 90, 180, 'k')
    c.rect(20, 25, 27, 27, 'k')
    c.hline(21, 26, 25, 's')
    c.outline()


# =================================================================== graphics

@icon('gimp', ['org.gimp.GIMP', 'gimp-2.10', 'gimp-3.0', 'gimp3', 'gimp-2.99'], 'graphics', 'GIMP')
def gimp(c):
    # Wilber: ears, goggle eyes, long snout, brush in the mouth
    c.poly([(4, 3), (11, 8), (6, 12)], 'N')
    c.poly([(13, 3), (19, 9), (13, 11)], 'N')
    c.ellipse(13, 17, 9.5, 8.5, 'N')
    c.ellipse(21, 20, 7.5, 4.5, 'N')
    c.bevel(['N'])
    c.poly([(6, 5.5), (9, 8), (7, 10)], '8')
    c.circle(9, 13, 3.5, 'W'); c.circle(16.5, 12, 3.5, 'W')
    c.rect(9, 13, 10, 14, 'K'); c.rect(16, 12, 17, 13, 'K')
    c.px(7, 11, 'w'); c.px(14, 10, 'w')
    c.rect(27, 18, 28, 19, 'K')
    c.hline(17, 26, 22, '8')
    # brush clamped in the mouth
    c.line(7, 27, 18, 22, 'O', w=2)
    c.line(19, 22, 21, 21, 'S', w=2)
    c.rect(22, 20, 24, 22, 'k')
    c.outline()


@icon('krita', ['org.kde.krita', 'calligrakrita'], 'graphics', 'Krita')
def krita(c):
    # bold crescent brush-swoosh with a brush dipping into it
    c.circle(14.5, 17.5, 11.5, 'M')
    c.circle(19, 13, 9, '.')
    c.bevel(['M'])
    c.line(26, 3, 19, 10, 'b', w=3)
    c.line(27, 5, 21, 11, '6')
    c.rect(17, 12, 19, 14, 'w')
    c.px(17, 12, 'W')
    c.poly([(12, 18), (16, 14.5), (19, 17), (15, 20)], 'm')
    c.outline()


@icon('inkscape', ['org.inkscape.Inkscape', 'inkscape-logo'], 'graphics', 'Inkscape')
def inkscape(c):
    c.ellipse(16, 25.5, 12.5, 3.5, 'S')
    c.poly([(16, 2.5), (29, 24), (3, 24)], 's')
    c.bevel(['s'], dark=False)
    c.sprite(10, 4, """
        .....WW.....
        ....WWWW....
        ...WWWWWw...
        ..WWWWWWWw..
        .WWWwWWWwWw.
        WWWw.wWw.Ww.
        .Ww..wW...w.
        .w...wW.....
        .....wW.....
        ......w.....
    """)
    c.circle(23, 27, 1.5, '.')
    c.outline()


@icon('blender', ['org.blender.Blender', 'blender-4.2', 'blender-4.1', 'blender-3.6', 'blender-lts'],
      'graphics', 'Blender')
def blender(c):
    c.poly([(3, 7.5), (17, 7.5), (19, 12), (5, 12)], 'O')
    c.poly([(7, 14), (16, 14), (16, 18), (9, 18)], 'O')
    c.poly([(3, 27), (13, 17), (17, 22), (8, 29)], 'O')
    c.circle(19, 17.5, 9.5, 'O')
    c.bevel(['O'])
    c.circle(19.5, 17, 6, 'W')
    c.circle(20, 17, 4, 'B')
    c.px(18, 15, 'b'); c.px(19, 15, 'b'); c.px(18, 16, 'b')
    c.outline()


@icon('darktable', ['org.darktable.Darktable'], 'graphics', 'darktable')
def darktable(c):
    import math
    c.circle(16, 16, 13, 'S')
    c.bevel(['S'])
    c.circle(16, 16, 10.5, 'k')
    for y in range(32):
        for x in range(32):
            dx, dy = x + .5 - 16, y + .5 - 16
            r = math.hypot(dx, dy)
            if 4 < r <= 10.5:
                a = (math.degrees(math.atan2(dy, dx)) - 25 * (r - 4) / 6.5) % 360
                seg = int(a // 60)
                c.px(x, y, 'sSws S'[seg] if seg != 4 else 's')
    c.replace(' ', 'S')
    c.circle(16, 16, 4, 'k')
    c.px(14, 14, 'b'); c.px(15, 14, 'b')
    c.outline()


@icon('rawtherapee', ['com.rawtherapee.RawTherapee', 'RawTherapee'], 'graphics', 'RawTherapee')
def rawtherapee(c):
    import math
    cols = 'RYOGCBM'
    for y in range(32):
        for x in range(32):
            dx, dy = x + .5 - 16, y + .5 - 16
            r = math.hypot(dx, dy)
            if r <= 13:
                a = (math.degrees(math.atan2(dy, dx)) + 360 + 20 * r / 13) % 360
                c.px(x, y, 'ROYGCBM'[int(a // (360 / 7))])
    c.circle(16, 16, 4, 'k')
    c.px(14, 14, 's')
    c.outline()


@icon('digikam', ['org.kde.digikam', 'showfoto', 'org.kde.showfoto'], 'graphics', 'digiKam')
def digikam(c):
    c.rrect(19, 5, 25, 8, 'S', 1)
    c.rrect(3, 7, 28, 26, 'B', 2)
    c.bevel(['B'])
    c.hline(4, 27, 12, '6')
    c.circle(15, 17, 8, 'K')
    c.circle(15, 17, 7, 'w')
    c.circle(15, 17, 5, 'k')
    c.circle(15, 17, 3, 'C')
    c.px(13, 15, 'W'); c.px(14, 15, 'c'); c.px(13, 16, 'c')
    c.rect(24, 9, 26, 10, 'Y')
    c.outline()


@icon('shotwell', ['org.gnome.Shotwell', 'shotwell-viewer'], 'graphics', 'Shotwell')
def shotwell(c):
    c.rect(9, 3, 28, 21, 'w')
    c.rect(3, 9, 22, 28, 'W')
    c.shade_below(['W'], 'w')
    c.rect(5, 11, 20, 24, 'O')
    c.dither(5, 15, 20, 16, 'O', 'Y', only='O')
    c.rect(5, 17, 20, 24, 'Y')
    c.circle(12.5, 19, 4, 'R')
    c.rect(5, 20, 20, 24, '8')
    c.hline(5, 20, 20, 'N')
    c.outline()


@icon('aseprite', ['org.aseprite.Aseprite', 'Aseprite'], 'graphics', 'Aseprite')
def aseprite(c):
    c.rrect(4, 5, 27, 24, 'w', 3)
    c.bevel(['w'])
    c.rect(8, 25, 11, 27, 'S'); c.rect(20, 25, 23, 27, 'S')
    c.rect(9, 11, 11, 15, 'K'); c.rect(20, 11, 22, 15, 'K')
    c.px(9, 11, 'W'); c.px(20, 11, 'W')
    c.rect(7, 17, 8, 18, 'p'); c.rect(23, 17, 24, 18, 'p')
    c.hline(14, 17, 18, 'K'); c.px(13, 17, 'K'); c.px(18, 17, 'K')
    c.outline()


@icon('libresprite', ['com.github.libresprite.LibreSprite', 'LibreSprite'], 'graphics', 'LibreSprite')
def libresprite(c):
    # chunky pixel pencil drawing a stepped line
    for i in range(14):
        x, y = 9 + i, 22 - i
        c.line(x - 3, y, x + 3, y, 'Y')
    c.poly([(3, 29), (5, 22), (10, 27)], 'n')
    c.poly([(3, 29), (4, 26), (6, 28)], 'k')
    for i in range(14):
        x, y = 9 + i, 22 - i
        c.px(x + 3, y, '3')
        c.px(x - 3, y, 'y')
    for i in range(4):
        c.line(20 + i - 3, 9 - i, 20 + i + 3, 9 - i, 'P' if i < 3 else 'p')
    for i in range(3):
        c.line(19 + i - 3, 10 - i, 19 + i + 3, 10 - i, 'S')
    c.bevel(['P'])
    c.outline()


@icon('com.orama_interactive.Pixelorama', ['pixelorama', 'Pixelorama'], 'graphics', 'Pixelorama')
def pixelorama(c):
    grid = ["XXXX.",
            "XC.XX",
            "XXXX.",
            "XC...",
            "XX..."]
    cols = {'X': 'B', 'C': 'C'}
    for j, row in enumerate(grid):
        for i, ch in enumerate(row):
            if ch != '.':
                x, y = 3 + i * 5 + (1 if i else 0) * 0, 3 + j * 5
                c.rect(x, y, x + 4, y + 4, cols[ch])
                c.hline(x, x + 4, y, LIGHT_OF[cols[ch]]); c.vline(x, y, y + 4, LIGHT_OF[cols[ch]])
                c.hline(x, x + 4, y + 4, DARK_OF[cols[ch]]); c.vline(x + 4, y + 1, y + 4, DARK_OF[cols[ch]])
    c.outline()


@icon('mypaint', ['org.mypaint.MyPaint', 'MyPaint'], 'graphics', 'MyPaint')
def mypaint(c):
    c.ellipse(16, 17, 13, 10.5, 'n')
    c.circle(22, 23, 3.5, '.')
    c.bevel(['n'], edge=('.',))
    c.circle(22, 23, 2.5, '.')
    for x, y, col in ((9, 12, 'R'), (15, 10, 'Y'), (21, 11, 'G'), (8, 19, 'B')):
        c.circle(x, y, 2.5, col)
        c.px(int(x) - 1, int(y) - 1, LIGHT_OF[col])
    c.outline()


@icon('upscayl', ['org.upscayl.Upscayl', 'Upscayl'], 'graphics', 'Upscayl')
def upscayl(c):
    c.poly([(16, 3), (28, 15), (21, 15), (21, 21), (11, 21), (11, 15), (4, 15)], 'M')
    c.bevel(['M'])
    c.rect(11, 22, 13, 24, 'm'); c.rect(17, 22, 19, 24, 'm')
    c.rect(14, 25, 16, 27, '7')
    c.rect(11, 26, 12, 27, '7')
    c.outline()


@icon('freecad', ['org.freecad.FreeCAD', 'FreeCAD', 'freecad-daily'], 'graphics', 'FreeCAD')
def freecad(c):
    import math
    for i in range(8):
        a = math.radians(22.5 + 45 * i)
        cx, cy = 16 + 11 * math.cos(a), 16 + 11 * math.sin(a)
        c.circle(cx, cy, 2.6, 'S')
    c.circle(16, 16, 11, 'S')
    c.bevel(['S'])
    c.circle(16, 16, 8, 's')
    c.rect(11, 9, 22, 12, 'R')
    c.rect(11, 9, 14, 24, 'R')
    c.rect(11, 15, 19, 18, 'R')
    c.hline(11, 22, 9, 'r'); c.vline(11, 9, 24, 'r')
    c.hline(15, 22, 12, '1'); c.hline(15, 19, 18, '1'); c.vline(14, 19, 24, '1')
    c.outline()


@icon('kicad', ['org.kicad.KiCad', 'org.kicad.kicad', 'eeschema', 'pcbnew'], 'graphics', 'KiCad')
def kicad(c):
    for y in (8, 12, 16, 20, 24):
        c.rect(3, y, 6, y + 1, 'w'); c.rect(25, y, 28, y + 1, 'w')
    c.rrect(6, 3, 25, 28, 's', 1)
    c.bevel(['s'], edge=('.', 'w'))
    c.circle(10, 7, 1.5, 'k')
    c.sprite(10, 11, """
        ##..##..##
        ##.##...##
        ####......
        ###.....##
        ####....##
        ##.##...##
        ##..##..##
    """, {'#': 'B'})
    c.outline()


@icon('org.gnome.Loupe', ['loupe', 'eog', 'org.gnome.eog', 'org.gnome.Loupe-symbolic'], 'graphics', 'Image Viewer')
def loupe(c):
    c.line(19, 19, 26, 26, 'k', w=3)
    c.line(20, 19, 27, 26, 's')
    c.circle(13, 13, 10, 'S')
    c.bevel(['S'])
    c.circle(13, 13, 7.5, 'c')
    c.poly([(5, 21), (11, 13), (17, 19), (20, 16), (22, 21)], 'G')
    c.ring(13, 13, 10, 7.5, 'S')
    c.arc(13, 13, 10, 7.5, 180, 270, 'w')
    c.arc(13, 13, 10, 7.5, 0, 90, 's')
    c.rect(15, 8, 16, 9, 'y')
    c.px(9, 9, 'W')
    c.outline()


# =================================================================== games

@icon('steam', ['com.valvesoftware.Steam', 'steam-native', 'steam-runtime', 'steam-launcher', 'Steam'], 'games', 'Steam')
def steam(c):
    c.ellipse(9, 21, 6, 7.5, 'B')
    c.ellipse(23, 21, 6, 7.5, 'B')
    c.rrect(3, 9, 28, 21, 'B', 4)
    c.bevel(['B'])
    c.rect(11, 22, 20, 23, '.')
    # d-pad
    c.rect(6, 14, 12, 16, 'k'); c.rect(8, 12, 10, 18, 'k')
    # face buttons
    for x, y, col in ((22, 12, 'g'), (25, 15, 'r'), (19, 15, 'b'), (22, 18, 'y')):
        c.rect(x, y, x + 1, y + 1, col)
    c.hline(14, 15, 13, '6'); c.hline(17, 18, 13, '6')
    c.outline()


@icon('lutris', ['net.lutris.Lutris'], 'games', 'Lutris')
def lutris(c):
    c.circle(6.5, 7.5, 3, 'O'); c.circle(25.5, 7.5, 3, 'O')
    c.ellipse(16, 16, 13, 12, 'O')
    c.bevel(['O'])
    c.circle(6.5, 7.5, 1.3, '2'); c.circle(25.5, 7.5, 1.3, '2')
    c.ellipse(16, 21, 7.5, 5.5, 'y')
    c.rect(10, 12, 11, 14, 'K'); c.rect(21, 12, 22, 14, 'K')
    c.px(10, 12, 'W'); c.px(21, 12, 'W')
    c.rect(14, 17, 17, 18, 'K'); c.hline(15, 16, 19, 'K')
    c.pixels([(13, 22), (14, 23), (15, 22), (16, 22), (17, 23), (18, 22)], '2')
    c.outline()


@icon('heroic', ['com.heroicgameslauncher.hgl', 'heroic-games-launcher', 'Heroic'], 'games', 'Heroic')
def heroic(c):
    c.poly([(5, 4), (27, 4), (27, 15), (16, 29), (5, 15)], 'B')
    c.bevel(['B'])
    c.rect(15, 6, 16, 22, 'W'); c.vline(16, 6, 22, 'w')
    c.rect(11, 18, 20, 19, 'Y')
    c.rect(15, 20, 16, 24, 'N')
    c.rect(14, 25, 17, 26, 'Y')
    c.outline()


@icon('com.usebottles.bottles', ['bottles', 'Bottles'], 'games', 'Bottles')
def bottles(c):
    c.rect(13, 3, 18, 6, 'N'); c.hline(13, 18, 3, 'n')
    c.rect(13, 7, 18, 10, 'R')
    c.rrect(8, 10, 23, 28, 'R', 4)
    c.bevel(['R'])
    c.rrect(10, 16, 21, 23, 'W', 1)
    c.shade_below(['W'], 'w')
    c.hline(12, 19, 18, 'r'); c.hline(12, 17, 20, 'r')
    c.px(10, 12, 'r'); c.px(10, 13, 'r')
    c.outline()


@icon('org.prismlauncher.PrismLauncher', ['prismlauncher', 'PrismLauncher'], 'games', 'Prism Launcher')
def prismlauncher(c):
    import math
    # hexagon (isometric cube) split into six coloured wedges
    hexp = [(16, 2.5), (28, 9.5), (28, 22.5), (16, 29.5), (4, 22.5), (4, 9.5)]
    c.poly(hexp, 'k')
    cols = ['G', 'C', 'B', 'M', 'R', 'Y']
    for i in range(6):
        a, b = hexp[i], hexp[(i + 1) % 6]
        c.poly([(16, 16), a, b], cols[i])
    c.bevel(cols, dark=False)
    c.outline()


@icon('minecraft-launcher', ['com.mojang.Minecraft', 'minecraft', 'Minecraft'], 'games', 'Minecraft')
def minecraft(c):
    c.poly([(16, 2.5), (28, 8.5), (16, 14.5), (4, 8.5)], 'G')
    c.poly([(4, 8.5), (16, 14.5), (16, 29.5), (4, 23.5)], 'N')
    c.poly([(16, 14.5), (28, 8.5), (28, 23.5), (16, 29.5)], '8')
    for x, y in ((12, 6), (19, 6), (15, 9), (22, 9), (9, 9), (17, 4)):
        c.px(x, y, 'g')
    # grass skirt on the sides
    for x in range(4, 16):
        h = 3 + (x % 3 == 1) + (x % 5 == 0)
        y0 = int(8.5 + (x + .5 - 4) * 0.5)
        c.vline(x, y0, y0 + h, '4' if x > 4 else 'G')
    for x in range(16, 28):
        h = 2 + (x % 3 == 0) + (x % 4 == 1)
        y0 = int(14.5 - (x + .5 - 16) * 0.5)
        c.vline(x, y0, y0 + h, '4')
    for x, y in ((7, 18), (11, 22), (9, 25), (20, 22), (24, 18), (22, 25)):
        c.px(x, y, 'n' if x < 16 else 'N')
    c.outline()


@icon('retroarch', ['org.libretro.RetroArch', 'RetroArch', 'com.libretro.RetroArch'], 'games', 'RetroArch')
def retroarch(c):
    c.sprite(3, 6, """
        ...ww..............ww...
        ...ww..............ww...
        .....ww..........ww.....
        .....ww..........ww.....
        ...wwwwwwwwwwwwwwwwwww..
        ...wwwwwwwwwwwwwwwwwww..
        .wwwwwKKKwwwwwwwKKKwwwww
        .wwwwwKKKwwwwwwwKKKwwwww
        wwwwwwwwwwwwwwwwwwwwwwww
        wwwwwwwwwwwwwwwwwwwwwwww
        ww.wwwwwwwwwwwwwwwwww.ww
        ww.wwwwwwwwwwwwwwwwww.ww
        ww.ww..............ww.ww
        ww.ww..............ww.ww
        .....wwwww....wwwww.....
        .....wwwww....wwwww.....
    """)
    c.bevel(['w'])
    c.outline()


@icon('dolphin-emu', ['org.DolphinEmu.dolphin-emu', 'dolphin-emulator', 'dolphin-emu-qt', 'dolphin-emu-nogui'],
      'games', 'Dolphin')
def dolphin_emu(c):
    c.sprite(3, 4, """
        .............CCC..........
        ..........CCCCCCCC........
        .......CCCCCCCCCCCCC......
        .....CCCCCCCCCCCCCCCC.....
        ...CCCCCCCCCCCCCCCCCCC....
        ..CCCCCCCCCCCCCCCCCCCCC...
        .CCCCKCCCCCCCCCCCCCCCCCC..
        CCCCCCCCCCCCCCCCCCCCCCCCC.
        CCCCWWWWWWCCCCCCCCCCCCCCCC
        WWWWWWW....WWWWCCCCCCCCCCC
        ...........WWWWWWCC..CCCCC
        .............WWWWW....CCCC
        ..............WWW......CCC
        ........................CC
        .......................CCC
        ....................CCCCCC
        ...................CCCC.CC
        .....................CC...
    """)
    c.bevel(['C'], edge=('.',))
    c.outline()


@icon('pcsx2', ['net.pcsx2.PCSX2', 'PCSX2', 'pcsx2-qt'], 'games', 'PCSX2')
def pcsx2(c):
    big(c, 4, 3, """
        ..########..
        .##########.
        ####....####
        ###......###
        .........###
        ........####
        ......#####.
        ....#####...
        ..#####.....
        .####.......
        ####........
        ###.........
        ############
    """, 'B')
    c.bevel(['B'])
    c.outline()


@icon('rpcs3', ['net.rpcs3.RPCS3', 'RPCS3'], 'games', 'RPCS3')
def rpcs3(c):
    big(c, 4, 4, """
        ###########.
        ############
        .........###
        ........###.
        ......####..
        .....######.
        ..........##
        ..........##
        ###.......##
        ####....####
        .##########.
        ..########..
    """, 'w')
    c.bevel(['w'])
    c.outline()


@icon('ppsspp', ['org.ppsspp.PPSSPP', 'PPSSPP', 'ppsspp-qt', 'ppsspp-sdl'], 'games', 'PPSSPP')
def ppsspp(c):
    c.rrect(3, 9, 28, 23, 's', 4)
    c.bevel(['s'])
    c.rect(9, 11, 22, 21, 'k')
    c.rect(10, 12, 21, 20, 'C')
    c.hline(10, 21, 12, 'c'); c.dither(10, 18, 21, 20, 'C', '5')
    c.rect(4, 15, 6, 15, 'w'); c.rect(5, 14, 5, 16, 'w')
    c.px(26, 13, 'G'); c.px(27, 15, 'R'); c.px(24, 15, 'M'); c.px(26, 17, 'B')
    c.outline()


@icon('ryujinx', ['org.ryujinx.Ryujinx', 'Ryujinx', 'io.github.ryubing.Ryujinx'], 'games', 'Ryujinx')
def ryujinx(c):
    c.circle(16, 16, 13, 'B')
    for y in range(32):
        for x in range(16):
            if c.get(x, y) == 'B':
                c.px(x, y, 'R')
    c.circle(16, 9.5, 6.5, 'B')
    c.circle(16, 22.5, 6.5, 'R')
    c.bevel(['R', 'B'])
    c.circle(16, 9.5, 2, 'W')
    c.circle(16, 22.5, 2, 'k')
    c.outline()


@icon('duckstation', ['org.duckstation.DuckStation', 'DuckStation', 'duckstation-qt'], 'games', 'DuckStation')
def duckstation(c):
    c.ellipse(15, 21, 12, 7.5, 'Y')
    c.poly([(24, 16), (28.5, 12), (28.5, 18), (25, 21)], 'Y')
    c.circle(10, 10, 7, 'Y')
    c.bevel(['Y'])
    c.poly([(2.5, 11), (5, 9), (5, 14)], 'O')
    c.hline(3, 4, 12, '2')
    c.rect(8, 8, 9, 9, 'K'); c.px(8, 8, 'W')
    c.sprite(13, 18, """
        3.......3
        .3.....3.
        ..33333..
    """)
    c.outline()


@icon('protonup-qt', ['net.davidotek.pupgui2', 'pupgui2', 'ProtonUp-Qt'], 'games', 'ProtonUp-Qt')
def protonup(c):
    c.ellipse(16, 16, 13, 5, 'C')
    c.ellipse(16, 16, 11, 3, '.')
    c.ellipse(16, 16, 5, 13, 'C')
    c.ellipse(16, 16, 3, 11, '.')
    c.circle(16, 16, 5, 'M')
    c.bevel(['M'])
    c.sprite(13, 13, """
        ..#..
        .###.
        #####
        .###.
        .###.
    """, {'#': 'W'})
    c.outline()


@icon('itch', ['io.itch.itch', 'itch.io', 'itch-setup'], 'games', 'itch')
def itch(c):
    # scalloped shop awning over a grinning storefront
    c.rect(4, 13, 27, 27, 'R')
    c.bevel(['R'])
    for i in range(5):
        x = 3 + i * 5
        c.rect(x, 4, x + 4, 10, 'r' if i % 2 == 0 else 'W')
        c.rrect(x, 8, x + 4, 12, 'r' if i % 2 == 0 else 'W', 1)
    c.rect(5, 2, 26, 3, '.')
    c.circle(11, 19, 2.5, 'W'); c.circle(21, 19, 2.5, 'W')
    c.rect(10, 19, 11, 20, 'K'); c.rect(20, 19, 21, 20, 'K')
    c.rect(12, 23, 19, 27, '1')
    c.outline()
