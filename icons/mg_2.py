"""Music players, streaming clients, taggers, rippers and converters."""
from pix import icon
import math


def play(c, x, y, h, col):
    m = h // 2
    for j in range(h):
        c.hline(x, x + (m - abs(j - m)), y + j, col)


def big(c, x, y, art, col, k=2):
    lines = [l.strip() for l in art.strip('\n').split('\n')]
    for j, row in enumerate(lines):
        for i, ch in enumerate(row):
            if ch == '#':
                c.rect(x + i * k, y + j * k, x + i * k + k - 1, y + j * k + k - 1, col)


def note(c, x, y, col):
    """Eighth note, 7 wide x 11 tall, top-left x,y."""
    c.sprite(x, y, """
        ...##..
        ...###.
        ...#.##
        ...#..#
        ...#...
        ...#...
        ...#...
        .###...
        ####...
        ####...
        .##....
    """, {'#': col})


def disc(c, cx, cy, r, col='k', groove='s', label='R'):
    c.circle(cx, cy, r, col)
    c.ring(cx, cy, r - 2, r - 3, groove)
    c.circle(cx, cy, r * 0.35, label)
    c.px(int(cx), int(cy), 'K')


def term(c, x0=3, y0=5, x1=28, y1=27):
    c.rrect(x0, y0, x1, y1, 'S', 1)
    c.rect(x0, y0, x1, y0 + 3, 'w')
    c.rect(x0 + 2, y0 + 5, x1 - 2, y1 - 2, 'k')


# =================================================================== spotify-likes

@icon('spotube', ['oss.krtirtho.spotube', 'com.github.KRTirtho.Spotube', 'spotube-bin'], 'audio', 'Spotube')
def spotube(c):
    # a tube (cylinder) with sound arcs
    c.rect(4, 7, 27, 24, 'G')
    c.ellipse(16, 24.5, 12, 3.5, 'G')
    c.bevel(['G'])
    c.ellipse(16, 7, 12, 3.5, 'g')
    c.ellipse(16, 7, 8, 1.7, '4')
    for r, w in ((9, 0), (6, 0), (3, 0)):
        c.arc(16, 21, r, r - 1.2, 225, 315, 'k')
    c.outline()


@icon('dev.alextren.Spot', ['spot'], 'audio', 'Spot')
def spot(c):
    # a paint-splat spot
    c.circle(16, 16, 9, 'G')
    for a, r, d in ((20, 3.5, 9.5), (95, 3, 10), (160, 3.5, 9.5), (230, 2.5, 10.5), (300, 3.5, 9.5)):
        x, y = 16 + d * math.cos(math.radians(a)), 16 + d * math.sin(math.radians(a))
        c.circle(x, y, r, 'G')
    c.bevel(['G'])
    c.circle(13, 13, 2.5, 'g')
    c.outline()


@icon('spotify-qt', ['spotify-qt-bin', 'io.github.kraxarn.spotify-qt'], 'audio', 'spotify-qt')
def spotifyqt(c):
    # green Q with spotify waves inside
    c.circle(15, 15, 12, 'G')
    c.poly([(19, 21), (24, 18), (29, 27), (24, 29)], 'G')
    c.bevel(['G'])
    c.circle(15, 15, 8, 'k')
    for y, x0, x1 in ((11, 10, 20), (14, 10, 19), (17, 11, 18)):
        c.hline(x0, x1, y, 'G')
        c.px(x0, y + 1, 'G'); c.px(x1, y + 1, 'G')
    c.outline()


@icon('com.jpochyla.Psst', ['psst', 'psst-gui'], 'audio', 'Psst')
def psst(c):
    # shushing finger over a mouth
    c.ellipse(16, 18, 13, 7, 'R')
    c.bevel(['R'])
    c.hline(5, 26, 18, '1')
    c.rrect(13, 3, 19, 28, 'p', 2)
    c.bevel(['p'])
    c.rect(14, 4, 18, 6, 'W')
    c.outline()


@icon('feishin', ['org.jeffvli.feishin', 'feishin-bin', 'Feishin'], 'audio', 'Feishin')
def feishin(c):
    # rhombus with a stylised F
    c.poly([(16, 2.5), (29.5, 16), (16, 29.5), (2.5, 16)], 'M')
    c.poly([(16, 16), (29.5, 16), (16, 29.5)], 'B')
    c.bevel(['M', 'B'])
    c.rect(12, 9, 14, 23, 'W')
    c.rect(12, 9, 20, 11, 'W')
    c.rect(12, 15, 18, 17, 'W')
    c.outline()


@icon('sonixd', ['Sonixd', 'sonixd-bin'], 'audio', 'Sonixd')
def sonixd(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    for i, h in enumerate((3, 6, 10, 14, 10, 6, 3)):
        x = 7 + i * 3
        c.rect(x, 16 - h // 2, x + 1, 16 + h // 2, 'W' if i == 3 else 'b')
    c.outline()


@icon('io.github.dweymouth.supersonic', ['supersonic', 'supersonic-desktop', 'supersonic-bin'], 'audio', 'Supersonic')
def supersonic(c):
    # jet piercing sonic-boom rings
    c.arc(10, 16, 14, 11, 295, 65, 'c')
    c.arc(10, 16, 9, 7, 295, 65, 'C')
    c.poly([(3, 14), (22, 14), (29, 16), (22, 18), (3, 18)], 'w')
    c.poly([(8, 14), (16, 14), (8, 4)], 'S')
    c.poly([(8, 18), (16, 18), (8, 28)], 'S')
    c.poly([(3, 14), (7, 14), (3, 9)], 'S')
    c.bevel(['w', 'S'])
    c.rect(21, 15, 23, 15, 'B')
    c.outline()


@icon('nuclear', ['nuclear-player', 'org.js.nuclear.Nuclear', 'nuclear-player-bin'], 'audio', 'Nuclear')
def nuclear(c):
    c.circle(16, 16, 13, 'Y')
    c.bevel(['Y'])
    for a in (-90, 30, 150):
        c.arc(16, 16, 11, 4, a - 30, a + 30, 'k')
    c.circle(16, 16, 2.5, 'k')
    c.outline()


@icon('museeks', ['Museeks', 'museeks-bin'], 'audio', 'Museeks')
def museeks(c):
    # bold M with waveform ticks
    c.poly([(3, 28), (3, 4), (9, 4), (16, 14), (23, 4), (29, 4), (29, 28), (23, 28), (23, 15), (16, 24), (9, 15), (9, 28)], 'O')
    c.bevel(['O'])
    for x, h in ((5, 6), (26, 6)):
        c.vline(x, 14 - h // 2, 14 + h // 2, '2')
    c.outline()


@icon('deadbeef', ['music.deadbeef.player', 'deadbeef-gtk3'], 'audio', 'DeaDBeeF')
def deadbeef(c):
    # cow skull
    c.poly([(3, 7), (8, 9), (8, 11), (4, 10)], 'w')
    c.poly([(29, 7), (24, 9), (24, 11), (28, 10)], 'w')
    c.rrect(7, 6, 25, 18, 'W', 4)
    c.poly([(9, 16), (23, 16), (20, 28.5), (12, 28.5)], 'W')
    c.bevel(['W', 'w'])
    c.ellipse(12, 13, 3, 2.5, 'k'); c.ellipse(20, 13, 3, 2.5, 'k')
    c.px(12, 13, 'R'); c.px(19, 13, 'R')
    c.vline(14, 23, 25, 'S'); c.vline(17, 23, 25, 'S')
    c.outline()


@icon('audacious', ['audacious-qt', 'audacious-gtk'], 'audio', 'Audacious')
def audacious(c):
    # orange disc with a blue tilted note
    c.circle(16, 16, 13, 'O')
    c.bevel(['O'])
    c.circle(16, 16, 9, 'o')
    c.sprite(9, 7, """
        .......BBB
        .....BBBBB
        ....BBB..B
        ....B....B
        ....B....B
        ....B....B
        ..BBB..BBB
        .BBBB.BBBB
        .BBB..BBB.
    """)
    c.outline()


@icon('clementine', ['org.clementine_player.Clementine', 'clementine-player'], 'audio', 'Clementine')
def clementine(c):
    c.circle(16, 18, 11, 'O')
    c.bevel(['O'])
    c.circle(12, 14, 2, 'o')
    for (x, y) in ((19, 21), (22, 17), (14, 23), (20, 25)):
        c.px(x, y, '2')
    c.line(16, 7, 16, 5, 'N')
    c.poly([(17, 6), (26, 3), (23, 8)], 'G')
    c.bevel(['G'])
    c.outline()


@icon('io.github.quodlibet.QuodLibet', ['quodlibet', 'quod-libet'], 'audio', 'Quod Libet')
def quodlibet(c):
    # parchment scroll with a note
    c.rect(6, 6, 25, 25, 'y')
    c.bevel(['y'])
    c.rrect(3, 3, 28, 7, 'n', 2)
    c.rrect(3, 24, 28, 28, 'n', 2)
    c.bevel(['n'])
    note(c, 12, 10, '8')
    c.outline()


@icon('org.exaile.Exaile', ['exaile'], 'audio', 'Exaile')
def exaile(c):
    # record half-out of its sleeve
    disc(c, 20, 13, 9.5, 'k', 's', 'O')
    c.rect(3, 8, 18, 28, 'B')
    c.bevel(['B'])
    c.ring(10.5, 18, 5, 3, 'b')
    c.outline()


@icon('guayadeque', [], 'audio', 'Guayadeque')
def guayadeque(c):
    # guitar pick
    c.poly([(4, 6), (10, 3), (22, 3), (28, 6), (27, 13), (16, 29), (5, 13)], 'O')
    c.bevel(['O'])
    note(c, 12, 8, 'W')
    c.outline()


@icon('cantata', ['io.github.cdrummond.cantata'], 'audio', 'Cantata')
def cantata(c):
    # treble clef on a red medallion
    c.circle(16, 16, 13, 'R')
    c.bevel(['R'])
    c.sprite(10, 4, """
        ......##...
        .....####..
        .....#..#..
        .....#..#..
        .....#.##..
        .....###...
        ....###....
        ...###.....
        ..####.....
        .##.##.....
        ##..######.
        #..#.##..##
        #..#..#...#
        #..#..#...#
        ##....#..##
        .##...#.##.
        ..#######..
        ......#....
        ......#....
        ..##..#....
        .####.#....
        .####.#....
        ..#####....
        ...###.....
    """.replace('\n        .##.##.....', '\n        .##.##.....'), {'#': 'W'})
    c.outline()


@icon('ncmpcpp', ['ncmpc', 'mpd'], 'audio', 'ncmpcpp')
def ncmpcpp(c):
    term(c)
    note(c, 7, 12, 'C')
    c.rect(16, 13, 24, 13, 'G')
    c.hline(16, 22, 16, 'g')
    c.hline(16, 23, 19, 'g')
    c.hline(7, 24, 23, 's'); c.hline(7, 14, 23, 'C')
    c.outline()


@icon('cmus', ['cmus-remote'], 'audio', 'cmus')
def cmus(c):
    term(c)
    c.text(7, 12, 'CMUS', 'Y', font=3)
    play(c, 8, 18, 5, 'G')
    c.hline(13, 24, 20, 's'); c.hline(13, 18, 20, 'G')
    c.outline()


@icon('org.musicbrainz.Picard', ['picard', 'musicbrainz-picard'], 'audio', 'MusicBrainz Picard')
def picard(c):
    # isometric brain-cube: purple + orange faces
    c.poly([(16, 3), (28, 9.5), (16, 16), (4, 9.5)], 'm')
    c.poly([(4, 9.5), (16, 16), (16, 29), (4, 22.5)], 'M')
    c.poly([(16, 16), (28, 9.5), (28, 22.5), (16, 29)], 'O')
    c.bevel(['O'], light=False)
    c.line(8, 13, 13, 22, '7'); c.line(20, 22, 25, 13, '2')
    c.outline()


@icon('org.kde.kid3', ['kid3', 'kid3-qt', 'kid3-kde'], 'audio', 'Kid3')
def kid3(c):
    # price tag with a note
    c.poly([(3, 12), (12, 3), (28, 3), (28, 21), (12, 29), (3, 20)], 'C')
    c.bevel(['C'])
    c.circle(9, 16, 2, 'k')
    big(c, 15, 7, """
        ##.
        ..#
        .#.
        ..#
        ##.
    """, 'W', 3)
    c.outline()


@icon('org.gnome.EasyTAG', ['easytag'], 'audio', 'EasyTAG')
def easytag(c):
    disc(c, 14, 16, 11.5, 'w', 'S', 'B')
    c.replace('K', 'k')
    c.poly([(17, 17), (24, 14), (29, 22), (22, 26)], 'Y')
    c.bevel(['Y', 'w'])
    c.px(20, 18, 'k')
    c.outline()


@icon('puddletag', [], 'audio', 'Puddletag')
def puddletag(c):
    # a drop falling into a puddle
    c.poly([(16, 4), (21, 12), (11, 12)], 'B')
    c.circle(16, 14, 5, 'B')
    c.bevel(['B'])
    c.ellipse(16, 25, 13, 3.6, 'C')
    c.ellipse(16, 25, 7, 2, 'c')
    c.ellipse(16, 25, 5, 1, 'C')
    c.bevel(['C'])
    c.outline()


@icon('org.soundconverter.SoundConverter', ['soundconverter'], 'audio', 'SoundConverter')
def soundconverter(c):
    c.arc(16, 16, 12, 9, 200, 340, 'G')
    c.poly([(23, 15), (29, 15), (26, 19)], 'G')
    c.arc(16, 16, 12, 9, 20, 160, 'B')
    c.poly([(3, 17), (9, 17), (6, 13)], 'B')
    c.bevel(['G', 'B'])
    note(c, 12, 10, 'O')
    c.outline()


@icon('org.freac.freac', ['freac', 'fre:ac'], 'audio', 'fre:ac')
def freac(c):
    # CD with a big arrow coming out into a file
    disc(c, 12, 13, 9.5, 'w', 'S', 'O')
    c.replace('K', 'k')
    c.rect(18, 15, 28, 28, 'W')
    c.poly([(24, 15), (28, 19), (24, 19)], 'S')
    c.bevel(['W', 'w'])
    c.poly([(14, 20), (22, 20), (22, 18), (26, 22), (22, 26), (22, 24), (14, 24)], 'G')
    c.outline()


@icon('org.gnome.SoundJuicer', ['sound-juicer', 'soundjuicer'], 'audio', 'Sound Juicer')
def soundjuicer(c):
    # citrus juicer cone with a cd on it
    c.poly([(9, 7), (16, 3), (23, 7), (23, 13), (9, 13)], 'y')
    c.vline(12, 5, 12, '3'); c.vline(16, 3, 12, '3'); c.vline(20, 5, 12, '3')
    c.ellipse(16, 14, 13, 3.5, 'w')
    c.rect(5, 15, 27, 22, 'O')
    c.ellipse(16, 22, 11, 3, 'O')
    c.bevel(['O', 'w', 'y'])
    c.circle(16, 22, 6, 'S'); c.circle(16, 22, 1.5, 'k')
    c.rect(5, 27, 26, 28, 'O') if False else None
    c.outline()


@icon('asunder', [], 'audio', 'Asunder')
def asunder(c):
    # CD broken in two halves
    c.arc(13, 16, 10.5, 2.5, 90, 270, 'w')
    c.arc(19, 16, 10.5, 2.5, 270, 90, 'C')
    c.ring(13, 16, 7, 6, 'S'); c.ring(19, 16, 7, 6, 'c')
    c.rect(13, 0, 18, 31, '.')
    for y in range(4, 28, 4):
        c.px(12, y, '.'); c.px(19, y + 2, '.')
    c.bevel(['w', 'C'])
    c.outline()


# =================================================================== more players

@icon('org.gnome.SoundRecorder', ['gnome-sound-recorder', 'sound-recorder', 'audio-recorder'], 'audio',
      'Sound Recorder')
def soundrecorder(c):
    # studio microphone on a stand
    c.rrect(10, 3, 21, 19, 'R', 5)
    c.bevel(['R'])
    for y in (7, 10, 13):
        c.hline(12, 19, y, '1')
    c.arc(15.5, 13, 9, 7, 0, 180, 's')
    c.rect(6, 12, 7, 13, 's'); c.rect(24, 12, 25, 13, 's')
    c.rect(15, 22, 16, 25, 's')
    c.rrect(8, 26, 23, 28, 'S', 1)
    c.outline()


@icon('com.github.neithern.g4music', ['g4music', 'gapless'], 'audio', 'Gapless')
def g4music(c):
    # two linked rings (no gap)
    c.ring(11, 16, 8.5, 5, 'O')
    c.ring(21, 16, 8.5, 5, 'M')
    c.arc(11, 16, 8.5, 5, 300, 60, 'O')
    c.bevel(['O', 'M'])
    c.outline()


@icon('tauonmb', ['com.github.taiko2k.tauonmb', 'tauon', 'tauon-music-box'], 'audio', 'Tauon')
def tauon(c):
    # particle with orbits
    for a in (0, 60, 120):
        for t in range(0, 360, 2):
            r = math.radians(t)
            x, y = 12.5 * math.cos(r), 5 * math.sin(r)
            ra = math.radians(a)
            c.px(int(16 + x * math.cos(ra) - y * math.sin(ra)), int(16 + x * math.sin(ra) + y * math.cos(ra)), 'P')
    c.circle(16, 16, 4, 'p')
    c.bevel(['p'])
    c.outline()


@icon('com.github.geigi.cozy', ['cozy', 'cozy-audiobooks'], 'audio', 'Cozy')
def cozy(c):
    # open book under headphones
    c.arc(16, 18, 13, 10.5, 180, 360, 'k')
    c.rrect(3, 15, 7, 25, 'O', 1); c.rrect(24, 15, 28, 25, 'O', 1)
    c.poly([(8, 13), (16, 16), (24, 13), (24, 27), (16, 29), (8, 27)], 'W')
    c.vline(16, 16, 28, 'S')
    c.bevel(['O'])
    for y in (18, 21, 24):
        c.hline(10, 14, y, 'w'); c.hline(18, 22, y, 'w')
    c.outline()


@icon('app.drey.EarTag', ['eartag', 'ear-tag'], 'audio', 'Ear Tag')
def eartag(c):
    # ear with a tag hanging off the lobe
    c.ellipse(13, 13, 9.5, 11, 'p')
    c.bevel(['p'])
    c.arc(13, 12, 6, 4, 180, 400, '9')
    c.vline(11, 13, 17, '9')
    c.line(14, 23, 20, 22, 's')
    c.poly([(19, 18), (28, 18), (28, 28), (19, 28)], 'Y')
    c.bevel(['Y'])
    c.px(21, 20, 'k')
    c.outline()


@icon('io.github.seadve.Mousai', ['mousai'], 'audio', 'Mousai')
def mousai(c):
    # listening waves around a note
    c.circle(16, 16, 13, 'C')
    c.bevel(['C'])
    c.ring(16, 16, 10, 9, 'c')
    c.ring(16, 16, 7, 6, 'c')
    note(c, 12, 10, 'k')
    c.outline()


@icon('io.gitlab.Goodvibes', ['goodvibes'], 'audio', 'Goodvibes')
def goodvibes(c):
    # vintage radio with a big dial
    c.rrect(3, 9, 28, 28, 'N', 3)
    c.bevel(['N'])
    c.line(10, 3, 18, 9, 's')
    c.circle(11, 18.5, 6, 'y')
    for y in range(13, 24, 2):
        c.hline(7, 15, y, '3') if False else None
    c.ring(11, 18.5, 6, 5, '3')
    c.line(11, 18, 14, 15, 'R')
    for y in (14, 17, 20, 23):
        c.hline(19, 25, y, '8')
    c.outline()


@icon('io.github.Pithos', ['pithos'], 'audio', 'Pithos')
def pithos(c):
    # greek amphora
    c.rect(12, 3, 19, 4, 'O')
    c.rect(13, 5, 18, 8, 'O')
    c.ellipse(16, 17, 10, 10, 'O')
    c.rect(12, 26, 19, 28, 'O')
    c.arc(9, 10, 4, 2.5, 180, 360, 'O') if False else None
    c.ring(9, 10, 4, 2.5, 'O'); c.ring(23, 10, 4, 2.5, 'O')
    c.rect(11, 5, 20, 8, 'O')
    c.bevel(['O'])
    c.rect(6, 15, 25, 18, 'k')
    for x in range(7, 25, 3):
        c.px(x, 16, 'O'); c.px(x + 1, 17, 'O')
    c.outline()


@icon('org.kde.audiotube', ['audiotube'], 'audio', 'AudioTube')
def audiotube(c):
    # red tube (pipe segment) with note
    c.rrect(3, 9, 28, 23, 'R', 3)
    c.bevel(['R'])
    c.ellipse(25.5, 16, 3, 7, '1')
    c.ellipse(25.5, 16, 1.5, 5, 'k')
    note(c, 11, 11, 'W')
    c.outline()


@icon('org.gnome.Decibels', ['decibels'], 'audio', 'Decibels')
def decibels(c):
    # waveform blob, rounded symmetrical
    for i, h in enumerate((4, 8, 14, 20, 24, 18, 22, 14, 10, 6, 4)):
        x = 3 + i * 2 + (i // 1) * 0
        c.rect(4 + i * 2 + i // 3, 16 - h // 2, 5 + i * 2 + i // 3, 16 + h // 2, 'O')
    c.bevel(['O'])
    c.outline()


@icon('me.timschneeberger.jdsp4linux', ['jamesdsp', 'jdsp4linux'], 'audio', 'JamesDSP')
def jamesdsp(c):
    # mixing desk sliders
    c.rrect(3, 3, 28, 28, 'k', 2)
    for i, k in enumerate((14, 8, 18, 11, 21)):
        x = 6 + i * 5
        c.vline(x, 6, 25, 's')
        c.rect(x - 1, k - 1, x + 1, k + 1, 'O')
        c.vline(x, k + 2, 25, '2')
    c.outline()


@icon('ncspot', [], 'audio', 'ncspot')
def ncspot(c):
    term(c)
    c.circle(11.5, 16, 5, 'G')
    for y, x1 in ((14, 14), (16, 13)):
        c.hline(9, x1, y, 'k')
    c.hline(17, 24, 12, 'g'); c.hline(17, 22, 15, 'g'); c.hline(17, 24, 18, 'g'); c.hline(17, 21, 21, 'g')
    c.outline()


@icon('musikcube', [], 'audio', 'musikcube')
def musikcube(c):
    c.poly([(16, 3), (28, 9), (16, 15), (4, 9)], 'b')
    c.poly([(4, 9), (16, 15), (16, 29), (4, 23)], 'B')
    c.poly([(16, 15), (28, 9), (28, 23), (16, 29)], '6')
    note(c, 7, 13, 'W')
    c.outline()


@icon('org.kde.kasts', ['kasts'], 'audio', 'Kasts')
def kasts(c):
    # podcast: mic inside broadcast arcs
    c.arc(16, 14, 12.5, 10, 150, 390, 'M')
    c.arc(16, 14, 8.5, 6.5, 150, 390, 'm')
    c.circle(16, 14, 4, 'W')
    c.rect(14, 17, 17, 27, 'W')
    c.bevel(['W', 'M'])
    c.outline()


@icon('org.gnome.Podcasts', ['gnome-podcasts', 'podcasts'], 'audio', 'Podcasts')
def podcasts(c):
    # purple speech bubble with mic
    c.circle(16, 15, 12.5, 'M')
    c.poly([(8, 23), (14, 26), (6, 29)], 'M')
    c.bevel(['M'])
    c.rrect(13, 7, 18, 17, 'W', 2)
    c.arc(15.5, 14, 6, 4.8, 0, 180, 'm')
    c.vline(15, 20, 22, 'm'); c.hline(12, 19, 22, 'm')
    c.outline()


@icon('deezer', ['deezer-desktop', 'com.deezer.Deezer', 'deezer-webapp', 'deezer-enhanced'], 'audio', 'Deezer')
def deezer(c):
    # equaliser bars stacked like the classic Deezer logo
    cols = ['M', 'P', 'O', 'Y', 'G']
    heights = (2, 4, 1, 3, 5)
    for i in range(5):
        x = 3 + i * 5 + (1 if i else 0)
        x = 3 + i * 5
        for j in range(heights[i] + 1):
            y = 25 - j * 4
            c.rect(x, y, x + 4, y + 2, ['M', 'P', 'O', 'Y', 'G', 'C'][j])
    c.outline()


@icon('plexamp', ['com.plexapp.plexamp', 'plexamp-bin', 'Plexamp'], 'audio', 'Plexamp')
def plexamp(c):
    # amp/speaker cabinet with plex chevron
    c.rrect(3, 3, 28, 28, 'k', 2)
    c.bevel(['k'])
    c.circle(16, 18, 8, 's')
    c.circle(16, 18, 4, 'K')
    c.poly([(12, 5), (16, 5), (20, 9), (16, 13), (12, 13), (16, 9)], 'Y')
    c.outline()


@icon('harmonoid', ['com.alexmercerind.harmonoid'], 'audio', 'Harmonoid')
def harmonoid(c):
    # harmonica
    c.rrect(3, 9, 28, 22, 'w', 1)
    c.bevel(['w'])
    c.rect(3, 13, 28, 18, 'B')
    for x in range(5, 27, 3):
        c.rect(x, 14, x + 1, 17, 'k')
    c.outline()


@icon('org.feichtmeier.Musicpod', ['musicpod'], 'audio', 'MusicPod')
def musicpod(c):
    # pea pod with notes as peas
    c.poly([(4, 20), (10, 10), (22, 5), (28, 6), (24, 16), (12, 24)], 'G')
    c.bevel(['G'])
    for x, y in ((10, 17), (16, 13), (22, 10)):
        c.circle(x, y, 2.5, 'g')
        c.px(int(x) - 1, int(y) - 2, 'W')
    c.line(26, 5, 27, 3, '4')
    c.outline()


@icon('com.saivert.pwvucontrol', ['pwvucontrol'], 'audio', 'pwvucontrol')
def pwvucontrol(c):
    # analog VU meter
    c.rrect(3, 5, 28, 26, 'k', 2)
    c.rect(5, 7, 26, 21, 'y')
    c.arc(15.5, 22, 12, 11, 200, 340, '3')
    c.arc(15.5, 22, 12, 10, 300, 340, 'R')
    c.line(15, 21, 21, 10, 'k')
    c.text(6, 22, 'VU', 'w', font=3)
    c.outline()
