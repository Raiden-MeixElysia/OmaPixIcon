"""Video players, streaming, recording, editing and subtitle tools."""
from pix import icon
import math


def play(c, x, y, h, col):
    """Solid right-pointing play triangle, h rows tall (odd), top-left at x,y."""
    m = h // 2
    for j in range(h):
        c.hline(x, x + (m - abs(j - m)), y + j, col)


def big(c, x, y, art, col, k=2):
    lines = [l.strip() for l in art.strip('\n').split('\n')]
    for j, row in enumerate(lines):
        for i, ch in enumerate(row):
            if ch == '#':
                c.rect(x + i * k, y + j * k, x + i * k + k - 1, y + j * k + k - 1, col)


# =================================================================== players

@icon('finamp', ['com.unicornsonlsd.finamp'], 'media', 'Finamp')
def finamp(c):
    # jellyfin-ish triangle inside a headphone band
    c.arc(16, 16, 13, 10, 180, 360, 'M')
    c.rect(3, 16, 5, 18, 'M'); c.rect(26, 16, 28, 18, 'M')
    c.rrect(3, 17, 8, 28, 'B', 1); c.rrect(23, 17, 28, 28, 'B', 1)
    c.bevel(['M', 'B'])
    c.poly([(16, 12), (22.5, 26), (9.5, 26)], 'm')
    c.poly([(16, 17), (19, 24), (13, 24)], 'k')
    c.outline()


@icon('emby-theater', ['emby', 'emby-server', 'media.emby.EmbyTheater', 'embytheater'], 'media', 'Emby')
def emby(c):
    c.poly([(11, 3), (21, 3), (29, 11), (29, 21), (21, 29), (11, 29), (3, 21), (3, 11)], 'G')
    c.bevel(['G'])
    c.poly([(12, 9), (23, 16), (12, 23)], 'W')
    c.hline(12, 13, 22, 'w')
    c.outline()


@icon('cafe.avery.Delfin', ['delfin'], 'media', 'Delfin')
def delfin(c):
    # dolphin fin over two waves
    c.poly([(6, 20), (14, 4), (24, 3), (18, 9), (19, 20)], 'M')
    c.bevel(['M'])
    c.rect(3, 20, 28, 28, 'B')
    c.bevel(['B'])
    for x in range(3, 29):
        y = 22 + round(1.2 * math.sin((x - 3) / 2.2))
        c.px(x, y, 'b'); c.px(x, y + 3, '6')
    c.replace('B', '.', (3, 20, 4, 20)); c.replace('B', '.', (27, 20, 28, 20))
    c.outline()


@icon('org.gnome.Showtime', ['showtime', 'gnome-showtime'], 'media', 'Showtime')
def showtime(c):
    # admission ticket with notched sides
    c.rrect(3, 7, 28, 25, 'R', 1)
    for y in (14, 15, 16, 17, 18):
        d = 2 - abs(y - 16) // 2
        c.hline(3, 3 + d, y, '.'); c.hline(28 - d, 28, y, '.')
    c.bevel(['R'])
    for y in range(9, 24, 2):
        c.px(21, y, '1')
    c.rect(7, 11, 17, 21, 'r')
    play(c, 10, 13, 7, 'W')
    c.outline()


@icon('smplayer', ['info.smplayer.SMPlayer'], 'media', 'SMPlayer')
def smplayer(c):
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.arc(16, 16, 10, 7, 200, 340, 'b')
    c.circle(16, 16, 7, 'O')
    c.bevel(['O'])
    play(c, 14, 12, 9, 'W')
    c.outline()


@icon('mpc-qt', ['io.github.mpc_qt.mpc-qt', 'mpc-hc'], 'media', 'MPC-QT')
def mpcqt(c):
    # little TV set with rabbit ears
    c.line(10, 3, 15, 9, 's'); c.line(22, 3, 17, 9, 's')
    c.rrect(3, 9, 28, 28, 'N', 2)
    c.bevel(['N'])
    c.rrect(5, 11, 21, 26, 'k', 1)
    c.rect(6, 12, 20, 25, 'G')
    c.bevel(['G'], edge=('k',))
    play(c, 11, 15, 7, 'W')
    c.circle(24.5, 15.5, 1.5, 'y')
    c.circle(24.5, 21.5, 1.5, 'y')
    c.outline()


@icon('org.kde.dragonplayer', ['dragonplayer', 'dragon'], 'media', 'Dragon Player')
def dragon(c):
    c.sprite(3, 4, """
        ......RRR.................
        ....RRRRRR................
        ...RRRRRRRRR..............
        ..RRRRRRRRRRRRRR..........
        .RRRRWkRRRRRRRRRRRR.......
        RRRRRkkRRRRRRRRRRRRRR.....
        RRRRRRRRRRRRRRRRRRRRRRR...
        .RRRRRRRRRRRRRRRRRRRRRRRR.
        ..RRRRRRRRRRRRRRRRRRRRRRRR
        ...........RRRRRRRRRRRRRRR
        .........WWRRRRRRRRRRRRRRR
        .......WWWRRRRRRRRRRRRRRRR
        ......WWRRRRRRRRRRRRRRRRR.
        ....RRRRRRRRRRRRRRRRRRRRR.
        ...RRRRRRRRRRRRRRRRRRRRR..
        ..RRRRRRRRRRRRRRRRRRRRR...
        .RRRRRRRRRRRRRRRRRRRRR....
        .RRRRRRRRRRRRRRRRRRRR.....
        ..RRRRRRRRRRRRRRRRRR......
        ....RRRRRRRRRRRRRR........
    """)
    # horns
    c.poly([(13, 7), (19, 1.5), (17, 8)], 'y')
    c.poly([(17, 8), (25, 4), (21, 10)], 'y')
    c.bevel(['R'])
    c.px(3, 10, '1'); c.px(5, 10, '1')
    c.outline()


@icon('popcorntime', ['popcorn-time', 'popcorntime-bin', 'popcorntime-ce'], 'media', 'Popcorn Time')
def popcorn(c):
    # kernels
    for cx, cy in ((9, 8), (14, 6), (19, 6), (23, 9), (12, 11), (17, 10), (21, 12), (7, 12)):
        c.circle(cx, cy, 3.2, 'y')
    c.bevel(['y'], dark=False)
    for cx, cy in ((9, 8), (19, 6), (17, 10)):
        c.px(cx, cy, 'Y')
    # bucket
    c.poly([(4, 13), (28, 13), (25, 29), (7, 29)], 'W')
    for x in range(4, 29):
        for y in range(13, 30):
            if c.get(x, y) == 'W' and ((x - 4) // 4) % 2 == 1:
                c.px(x, y, 'R')
    c.hline(4, 27, 13, 'w')
    c.replace('R', '1', (4, 28, 28, 29))
    c.replace('W', 'w', (4, 28, 28, 29))
    c.outline()


@icon('hypnotix', ['org.x.Hypnotix'], 'media', 'Hypnotix')
def hypnotix(c):
    c.rrect(3, 8, 28, 28, 'k', 2)
    c.line(9, 3, 13, 8, 's'); c.line(23, 3, 19, 8, 's')
    c.rect(5, 10, 26, 26, 'W')
    # spiral
    for t in range(0, 900):
        a = t / 50.0
        r = 0.8 * a
        x, y = 15.5 + r * math.cos(a), 18 + r * math.sin(a) * 0.95
        if 5 <= x <= 26 and 10 <= y <= 26:
            c.px(int(x), int(y), 'M')
    c.outline()


# =================================================================== recorders

@icon('io.github.seadve.Kooha', ['kooha'], 'media', 'Kooha')
def kooha(c):
    # screen-selection corners around a record dot
    for (x, y, dx, dy) in ((3, 3, 1, 1), (28, 3, -1, 1), (3, 28, 1, -1), (28, 28, -1, -1)):
        c.rect(min(x, x + 7 * dx), min(y, y + 2 * dy), max(x, x + 7 * dx), max(y, y + 2 * dy), 'w')
        c.rect(min(x, x + 2 * dx), min(y, y + 7 * dy), max(x, x + 2 * dx), max(y, y + 7 * dy), 'w')
    c.circle(16, 16, 8, 'R')
    c.bevel(['R', 'w'])
    c.px(12, 12, 'r'); c.px(13, 11, 'r'); c.px(12, 13, 'W'); c.px(13, 12, 'W')
    c.outline()


@icon('vokoscreenNG', ['vokoscreen-ng', 'vokoscreen', 'com.github.vkohaupt.vokoscreenNG'], 'media', 'vokoscreenNG')
def vokoscreen(c):
    # old cine camera: two reels on top, body, lens
    c.circle(10, 8, 5.5, 'k'); c.circle(20, 7, 4.5, 'k')
    c.circle(10, 8, 2, 's'); c.circle(20, 7, 1.5, 's')
    c.rrect(3, 13, 22, 27, 'R', 1)
    c.bevel(['R'])
    c.poly([(22, 17), (28.5, 13.5), (28.5, 26.5), (22, 23)], 's')
    c.bevel(['s'])
    c.rect(6, 16, 12, 19, 'k')
    c.px(7, 17, 'R')
    c.outline()


@icon('simplescreenrecorder', ['ssr', 'com.maartenbaert.simplescreenrecorder'], 'media', 'SimpleScreenRecorder')
def ssr(c):
    c.rrect(3, 4, 28, 22, 's', 1)
    c.bevel(['s'])
    c.rect(5, 6, 26, 20, 'B')
    c.dither(5, 6, 26, 8, 'b', 'B')
    c.rect(13, 23, 18, 25, 's')
    c.rrect(8, 26, 23, 28, 'S', 1)
    c.circle(23, 17, 5.5, 'K')
    c.circle(23, 17, 4.5, 'R')
    c.bevel(['R'], edge=('K',))
    c.outline()


@icon('com.uploadedlobster.peek', ['peek'], 'media', 'Peek')
def peek(c):
    # window with an eye peeking through
    c.rrect(3, 5, 28, 27, 'w', 1)
    c.rect(3, 5, 28, 9, 'S')
    c.px(5, 7, 'R'); c.px(7, 7, 'Y'); c.px(9, 7, 'G')
    c.rect(5, 11, 26, 25, 'k')
    c.ellipse(16, 18, 9, 5.5, 'W')
    c.circle(16, 18, 4, 'C')
    c.circle(16, 18, 2, 'K')
    c.px(17, 16, 'W')
    c.bevel(['w'])
    c.outline()


@icon('gifski', ['net.gif.gifski', 'gifski-gui'], 'media', 'Gifski')
def gifski(c):
    # skier on a slope + "GIF"
    c.poly([(3, 26), (28, 14), (28, 28), (3, 28)], 'W')
    c.bevel(['W'])
    c.hline(3, 28, 28, 'w')
    c.text(5, 4, 'GIF', 'B', font=5)
    c.rect(4, 3, 22, 11, 'B')
    c.text(5, 4, 'GIF', 'W', font=5)
    c.line(8, 23, 21, 17, 'R', 1)
    c.circle(15, 14, 2, 'O')
    c.line(14, 15, 14, 19, 'k')
    c.outline()


@icon('kazam', [], 'media', 'Kazam')
def kazam(c):
    # handheld camcorder, side view
    c.rrect(3, 10, 21, 26, 'O', 2)
    c.bevel(['O'])
    c.rect(21, 13, 24, 23, 's')
    c.poly([(24, 11), (28.5, 9), (28.5, 27), (24, 25)], 'S')
    c.bevel(['S', 's'])
    c.rect(6, 5, 13, 9, 'k')
    c.rect(7, 6, 12, 8, 'C')
    c.circle(8, 18, 3, 'W')
    c.circle(8, 18, 1.5, 'R')
    c.hline(13, 18, 15, '2'); c.hline(13, 18, 18, '2'); c.hline(13, 18, 21, '2')
    c.outline()


@icon('com.dec05eba.gpu_screen_recorder', ['gpu-screen-recorder', 'gpu-screen-recorder-gtk'], 'media',
      'GPU Screen Recorder')
def gsr(c):
    # graphics card with a rec dot
    c.rect(3, 8, 28, 24, 'k')
    c.bevel(['k'])
    c.rect(3, 25, 9, 27, 'Y'); c.rect(12, 25, 24, 27, 'Y')
    c.circle(11, 16, 6, 's')
    c.circle(11, 16, 1.5, 'K')
    for a in range(0, 360, 60):
        c.line(11, 16, 11 + round(5 * math.cos(math.radians(a))), 16 + round(5 * math.sin(math.radians(a))), 'S')
    c.circle(22.5, 16, 3.5, 'R')
    c.px(21, 14, 'r')
    c.outline()


@icon('sa.sy.bluerecorder', ['blue-recorder', 'bluerecorder'], 'media', 'Blue Recorder')
def bluerecorder(c):
    # reel-to-reel tape in blue
    c.rrect(3, 7, 28, 25, 'B', 2)
    c.bevel(['B'])
    for cx in (10, 22):
        c.circle(cx, 14, 4.5, 'W')
        c.circle(cx, 14, 2, 'k')
    c.rect(9, 20, 23, 23, '6')
    c.hline(10, 22, 18, 'b')
    c.outline()


# =================================================================== editors

@icon('avidemux', ['avidemux-qt', 'avidemux3-qt5', 'avidemux3-qt6', 'org.avidemux.Avidemux', 'avidemux2'],
      'media', 'Avidemux')
def avidemux(c):
    # 35mm film canister with strip pulled out
    c.ellipse(12, 7, 9, 3.5, 's')
    c.rect(3, 7, 20, 24, 'S')
    c.ellipse(12, 24, 9, 3.5, 'S')
    c.bevel(['S'])
    c.ellipse(12, 7, 9, 3.5, 'w')
    c.ellipse(12, 7, 3, 1.5, 'k')
    c.rect(18, 14, 28, 22, 'N')
    for x in range(19, 28, 3):
        c.px(x, 15, 'k'); c.px(x, 21, 'k')
    c.rect(19, 17, 27, 19, 'O')
    c.rect(6, 13, 15, 19, 'B')
    c.text(7, 14, 'AV', 'W', font=3)
    c.outline()


@icon('losslesscut', ['no.mifi.losslesscut', 'losslesscut-bin'], 'media', 'LosslessCut')
def losslesscut(c):
    # open scissors over a timeline bar
    c.rect(3, 21, 28, 27, 'B')
    c.bevel(['B'])
    c.rect(13, 21, 18, 27, 'C')
    c.vline(15, 18, 28, 'W'); c.vline(16, 18, 28, 'W')
    c.line(7, 3, 15, 15, 'w', 2); c.line(24, 3, 16, 15, 'w', 2)
    c.ring(9, 13, 4, 2, 'R'); c.ring(23, 13, 4, 2, 'R')
    c.outline()


@icon('olive-editor', ['org.olivevideoeditor.Olive', 'olive'], 'media', 'Olive')
def olive(c):
    c.line(19, 3, 22, 8, 'N', 2)
    c.poly([(21, 5), (28, 2.5), (26, 7)], 'G')
    c.ellipse(14, 18, 10, 11, 'g')
    c.bevel(['g'])
    c.replace('g', 'G', (14, 20, 31, 31))
    c.ellipse(14, 18, 4, 4.5, 'R')
    c.ellipse(14, 18, 2, 2.5, 'r')
    c.px(8, 12, 'W'); c.px(9, 11, 'W')
    c.outline()


@icon('natron', ['fr.natron.Natron', 'Natron'], 'media', 'Natron')
def natron(c):
    # compositing node graph
    c.line(9, 9, 22, 16, 'S', 2); c.line(9, 23, 22, 16, 'S', 2)
    c.rrect(3, 4, 14, 13, 'O', 2)
    c.rrect(3, 19, 14, 28, 'R', 2)
    c.rrect(18, 11, 28, 21, 'Y', 2)
    c.bevel(['O', 'R', 'Y'])
    c.outline()


@icon('flowblade', ['io.github.jliljebl.Flowblade'], 'media', 'Flowblade')
def flowblade(c):
    # long knife blade with a flowing groove
    c.poly([(3, 23), (24, 3), (28, 6), (9, 27)], 'w')
    c.bevel(['w'])
    c.line(7, 23, 24, 6, 'B', 1)
    c.line(8, 24, 25, 7, 'b', 1)
    c.poly([(3, 23), (9, 27), (6, 29), (2.5, 27)], 'N')
    c.outline()


@icon('org.pitivi.Pitivi', ['pitivi'], 'media', 'Pitivi')
def pitivi(c):
    # timeline: three clips + playhead
    c.rrect(3, 6, 28, 26, 'k', 1)
    c.rect(5, 9, 18, 12, 'O'); c.rect(20, 9, 26, 12, 'R')
    c.rect(5, 15, 11, 18, 'B'); c.rect(13, 15, 26, 18, 'C')
    c.rect(5, 21, 22, 23, 'G')
    c.vline(15, 4, 28, 'Y')
    c.rect(14, 3, 16, 5, 'Y')
    c.outline()


@icon('cinelerra', ['cinelerra-gg', 'cin', 'cinelerra-cv'], 'media', 'Cinelerra')
def cinelerra(c):
    # film projector beaming light
    c.poly([(16, 15), (28.5, 8), (28.5, 26), (16, 19)], 'y')
    c.circle(8, 7, 4.5, 's'); c.circle(16, 7, 4.5, 's')
    c.circle(8, 7, 1.5, 'k'); c.circle(16, 7, 1.5, 'k')
    c.rrect(3, 12, 17, 24, 'B', 1)
    c.bevel(['B', 's'])
    c.rect(17, 15, 19, 19, 'k')
    c.rect(6, 25, 8, 28, 's'); c.rect(13, 25, 15, 28, 's')
    c.outline()


@icon('lightworks', ['Lightworks', 'lwks'], 'media', 'Lightworks')
def lightworks(c):
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'])
    c.ring(16, 16, 9, 6, 'W')
    c.rect(15, 3, 16, 13, 'k')
    c.rect(15, 5, 16, 15, 'W')
    c.outline()


@icon('mkvtoolnix-gui', ['org.bunkus.mkvtoolnix-gui', 'mkvtoolnix', 'mkvtoolnix-cli'], 'media', 'MKVToolNix')
def mkvtoolnix(c):
    # matryoshka doll
    c.circle(16, 9.5, 6.5, 'R')
    c.ellipse(16, 20.5, 10.5, 8.5, 'R')
    c.bevel(['R'])
    c.ellipse(16, 10, 4.5, 4, 'p')
    c.px(14, 9, 'k'); c.px(17, 9, 'k'); c.hline(15, 16, 11, '1')
    c.ellipse(16, 21.5, 6, 4.5, 'Y')
    c.circle(16, 21.5, 2.5, 'R')
    c.px(15, 20, 'r')
    c.outline()


@icon('mediainfo-gui', ['net.mediaarea.MediaInfo', 'mediainfo', 'mediainfo-gui-qt'], 'media', 'MediaInfo')
def mediainfo(c):
    # film frame with a big info "i" badge
    c.rect(3, 4, 21, 28, 'k')
    for y in range(6, 28, 3):
        c.px(4, y, 'w'); c.px(20, y, 'w')
    c.rect(6, 6, 18, 15, 'C'); c.rect(6, 17, 18, 26, 'C')
    c.bevel(['C'], edge=('k',))
    c.circle(21, 20, 7.5, 'B')
    c.bevel(['B'])
    c.rect(20, 15, 21, 16, 'W')
    c.rect(20, 18, 21, 24, 'W')
    c.outline()


@icon('subtitleedit', ['subtitle-edit', 'SubtitleEdit'], 'media', 'Subtitle Edit')
def subtitleedit(c):
    # screen with yellow subtitle lines + pencil
    c.rrect(3, 5, 26, 23, 'B', 1)
    c.bevel(['B'])
    c.rect(5, 7, 24, 21, '6')
    c.hline(8, 21, 16, 'Y'); c.hline(10, 19, 19, 'Y')
    c.line(17, 28, 27, 18, 'O', 2)
    c.px(17, 28, 'k')
    c.outline()


@icon('aegisub', ['org.aegisub.Aegisub', 'Aegisub'], 'media', 'Aegisub')
def aegisub(c):
    # shield with a speech eye
    c.poly([(4, 4), (28, 4), (28, 15), (16, 29), (4, 15)], 'R')
    c.bevel(['R'])
    c.ellipse(16, 13, 8, 4.5, 'W')
    c.circle(16, 13, 2.5, 'k')
    c.px(17, 12, 'W')
    c.hline(10, 22, 20, 'r'); c.hline(12, 20, 22, 'r')
    c.outline()


@icon('io.otsaloma.gaupol', ['gaupol'], 'media', 'Gaupol')
def gaupol(c):
    c.rrect(3, 4, 28, 21, 'Y', 3)
    c.poly([(8, 21), (14, 21), (7, 28)], 'Y')
    c.bevel(['Y'])
    c.hline(7, 23, 9, '3'); c.hline(7, 19, 12, '3'); c.hline(7, 21, 15, '3')
    c.outline()


@icon('jubler', ['Jubler', 'com.panayotis.jubler'], 'media', 'Jubler')
def jubler(c):
    # speech balloon (pointing right) with a "J"
    c.rrect(3, 4, 28, 21, 'C', 3)
    c.poly([(19, 21), (25, 21), (26, 28)], 'C')
    c.bevel(['C'])
    big(c, 9, 7, """
        ..###
        ...#.
        ...#.
        #..#.
        .##..
    """, 'W', 2)
    c.outline()


@icon('vidcutter', ['com.ozmartians.VidCutter'], 'media', 'VidCutter')
def vidcutter(c):
    # film strip sliced diagonally
    c.poly([(3, 5), (19, 5), (13, 28), (3, 28)], 'k')
    c.poly([(22, 3), (28, 3), (28, 26), (16, 26)], 'k')
    for y in range(7, 27, 3):
        c.px(4, y, 'w')
    for y in range(5, 25, 3):
        c.px(27, y, 'w')
    c.rect(6, 8, 12, 14, 'M'); c.rect(6, 18, 10, 24, 'M')
    c.rect(22, 8, 25, 14, 'M'); c.rect(20, 17, 25, 23, 'M')
    c.bevel(['M'], edge=('k',))
    c.outline()


@icon('shutter-encoder', ['ShutterEncoder', 'shutterencoder'], 'media', 'Shutter Encoder')
def shutterencoder(c):
    # hexagonal iris
    pts = [(16 + 13 * math.cos(math.radians(a)), 16 + 13 * math.sin(math.radians(a))) for a in range(30, 390, 60)]
    c.poly(pts, 'k')
    for i in range(6):
        a = math.radians(30 + 60 * i)
        b = math.radians(30 + 60 * (i + 1))
        p0 = (16 + 12 * math.cos(a), 16 + 12 * math.sin(a))
        p1 = (16 + 12 * math.cos(b), 16 + 12 * math.sin(b))
        q = (16 + 5 * math.cos(a + 1.1), 16 + 5 * math.sin(a + 1.1))
        c.poly([p0, p1, q], 'O' if i % 2 else 'Y')
    c.outline()


@icon('ffmpeg', ['ffmpeg-gui', 'qwinff', 'ffmulticonverter'], 'media', 'FFmpeg')
def ffmpeg(c):
    # the stepped zig-zag
    c.rect(3, 3, 28, 28, 'G')
    c.bevel(['G'])
    pts = [(5, 5), (9, 5), (9, 13), (14, 8), (14, 17), (19, 12), (19, 21), (23, 17), (23, 26), (27, 26)]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        c.line(x0, y0, x1, y1, 'W', 2)
    c.outline()


# =================================================================== more players / tools

@icon('app.grayjay.Grayjay', ['grayjay', 'grayjay-bin', 'Grayjay'], 'media', 'Grayjay')
def grayjay(c):
    c.poly([(3, 12), (12, 15), (11, 21), (3, 17)], 'S')
    c.ellipse(15, 17.5, 9, 6, 'w')
    c.circle(21, 10, 5.5, 'w')
    c.bevel(['w', 'S'])
    c.arc(21, 10, 5.5, 3.5, 200, 330, 'S')
    c.poly([(26, 9), (29, 11), (26, 12)], 'k')
    c.px(22, 10, 'K')
    c.ellipse(13, 17, 6, 3, 'S')
    c.hline(9, 16, 18, 's')
    c.vline(13, 23, 25, 'k'); c.vline(18, 23, 25, 'k')
    c.rect(3, 25, 28, 27, 'N')
    c.bevel(['N'])
    c.outline()


@icon('org.xfce.Parole', ['parole'], 'media', 'Parole')
def parole(c):
    # disc with an orange play wedge cut into it
    c.circle(16, 16, 13, 'w')
    c.bevel(['w'])
    c.ring(16, 16, 10, 9, 'S')
    c.circle(16, 16, 3, 's'); c.circle(16, 16, 1.5, 'k')
    c.poly([(16, 16), (29, 9), (29, 23)], 'O')
    c.bevel(['O'])
    c.outline()


@icon('com.github.rafostar.Clapper', ['clapper'], 'media', 'Clapper')
def clapper(c):
    # rounded TV-ish body with a clapstick crown
    c.poly([(4, 10), (26, 3), (27.5, 7), (5.5, 14)], 'W')
    for i in range(3):
        x0 = 8 + i * 6
        c.poly([(x0, 9 - i * 2), (x0 + 3, 8 - i * 2), (x0 + 5, 12 - i * 2), (x0 + 2, 13 - i * 2)], 'k')
    c.rrect(3, 14, 28, 28, 'B', 2)
    c.bevel(['B'])
    play(c, 13, 17, 9, 'W')
    c.outline()


@icon('qmplay2', ['QMPlay2', 'io.github.zaps166.QMPlay2'], 'media', 'QMPlay2')
def qmplay2(c):
    c.circle(15, 15, 12, 'G')
    c.poly([(20, 21), (25, 19), (29, 27), (24, 29)], 'G')
    c.bevel(['G'])
    c.circle(15, 15, 7, 'W')
    play(c, 13, 11, 9, 'G')
    c.outline()


@icon('org.gnome.gitlab.YaLTeR.VideoTrimmer', ['video-trimmer', 'videotrimmer'], 'media', 'Video Trimmer')
def videotrimmer(c):
    # film clip held between yellow trim handles
    c.rect(7, 8, 24, 23, 'B')
    c.bevel(['B'])
    play(c, 13, 12, 7, 'W')
    for x in (3, 25):
        c.rrect(x, 4, x + 3, 27, 'Y', 1)
    c.bevel(['Y'])
    c.rect(4, 4, 7, 5, 'Y'); c.rect(4, 26, 7, 27, 'Y')
    c.rect(24, 4, 27, 5, 'Y'); c.rect(24, 26, 27, 27, 'Y')
    c.outline()


@icon('org.nickvision.tubeconverter', ['parabolic', 'tube-converter', 'tubeconverter'], 'media', 'Parabolic')
def parabolic(c):
    # parabolic arc dropping into a down arrow
    c.arc(16, 22, 12.5, 8.5, 180, 360, 'R')
    c.rect(4, 22, 7, 23, 'R'); c.rect(24, 22, 27, 23, 'R')
    c.bevel(['R'])
    c.rect(13, 6, 18, 18, 'W')
    c.poly([(8, 17), (24, 17), (16, 27)], 'W')
    c.bevel(['W'])
    c.outline()


@icon('io.gitlab.adhami3310.Footage', ['footage'], 'media', 'Footage')
def footage(c):
    # strip of three frames, slightly tilted feel via offsets
    c.rect(3, 9, 28, 24, 'k')
    for x in range(4, 28, 3):
        c.px(x, 10, 'w'); c.px(x, 23, 'w')
    c.rect(5, 12, 11, 21, 'O'); c.rect(13, 12, 19, 21, 'Y'); c.rect(21, 12, 27, 21, 'O')
    c.dither(5, 12, 11, 15, 'o', 'O'); c.dither(21, 12, 27, 15, 'o', 'O')
    c.outline()


@icon('org.gnome.gitlab.YaLTeR.Identity', ['identity'], 'media', 'Identity')
def identity(c):
    # two overlapping photos with = between
    c.rrect(3, 4, 18, 19, 'b', 1)
    c.rrect(13, 12, 28, 27, 'P', 1)
    c.bevel(['b', 'P'])
    c.rect(5, 6, 16, 17, 'B')
    c.poly([(5, 17), (10, 10), (14, 17)], '6')
    c.rect(15, 14, 26, 25, 'p')
    c.poly([(15, 25), (21, 18), (26, 25)], '9')
    c.outline()


@icon('guvcview', ['guvcview-qt'], 'media', 'guvcview')
def guvcview(c):
    # round webcam on a clip
    c.circle(16, 13, 10.5, 'k')
    c.bevel(['k'])
    c.circle(16, 13, 6.5, 's')
    c.circle(16, 13, 4.5, 'B')
    c.circle(16, 13, 2, 'K')
    c.px(14, 11, 'W')
    c.px(24, 7, 'G')
    c.rect(14, 23, 17, 25, 's')
    c.rrect(6, 26, 25, 28, 'S', 1)
    c.outline()


@icon('hu.irl.cameractrls', ['cameractrls'], 'media', 'Cameractrls')
def cameractrls(c):
    # webcam lens + slider knobs
    c.rrect(3, 3, 28, 13, 'S', 2)
    c.bevel(['S'])
    c.circle(16, 8, 4, 'k'); c.circle(16, 8, 2, 'C')
    for y, k in ((17, 10), (22, 20), (27, 15)):
        c.rect(3, y - 1, 28, y, 'w') if False else c.hline(4, 27, y, 's')
        c.rrect(k - 2, y - 2, k + 2, y + 1, 'O', 1)
    c.outline()


@icon('de.schmidhuberj.tubefeeder', ['pipeline', 'tubefeeder'], 'media', 'Pipeline')
def pipeline(c):
    # bent pipe pouring a play triangle
    c.rect(3, 4, 20, 10, 'G')
    c.rect(14, 4, 20, 18, 'G')
    c.bevel(['G'])
    c.rect(20, 3, 22, 11, '4') if False else None
    c.rect(12, 18, 22, 20, 'g')
    c.poly([(11, 21), (23, 21), (17, 28.5)], 'R')
    c.bevel(['R'])
    c.outline()


@icon('org.kde.kaffeine', ['kaffeine'], 'media', 'Kaffeine')
def kaffeine(c):
    # coffee cup with steam (TV player)
    for x in (11, 17):
        c.line(x, 3, x + 1, 5, 'w'); c.line(x + 1, 6, x, 8, 'w')
    c.rrect(4, 10, 22, 28, 'W', 2)
    c.ring(22, 18, 5, 2.5, 'W')
    c.rect(19, 13, 22, 23, 'W')
    c.bevel(['W'])
    c.rect(6, 12, 20, 14, 'N')
    play(c, 11, 17, 7, 'B')
    c.outline()
