from pix import icon
"""Chinese & Asian software III: the deepin / UOS app suite.
Family look: every object is built from deepin blue (B/b/6) + paper white,
with at most one accent hue, and the same chunky 2px rounding."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cn_lib import g, gc, disc, doc, cloud, shield, play, note  # noqa: E402


def _win(c, body='W', bar='B', x0=3, y0=4, x1=28, y1=27):
    """deepin window: rounded frame with a blue title strip."""
    c.rrect(x0, y0, x1, y1, body, 2)
    c.rect(x0, y0 + 2, x1, y0 + 4, bar)
    c.rrect(x0, y0, x1, y0 + 4, bar, 2)
    c.bevel([body, bar])


def _page(c, col='W', ear='w'):
    doc(c, col, ear, 6, 3, 26, 28, 6)


# ---------------------------------------------------------------- core apps

@icon('deepin-music', ['com.deepin.music', 'org.deepin.music', 'deepin-music-player'], 'deepin', 'deepin Music')
def deepin_music(c):
    disc(c, 'B', 13)
    c.ring(16, 16, 11, 10.2, '6')
    note(c, 11, 8, 'W', 15)
    c.outline()


@icon('deepin-movie', ['com.deepin.movie', 'org.deepin.movie', 'deepin-movie-reborn'], 'deepin', 'deepin Movie')
def deepin_movie(c):
    c.rrect(3, 5, 28, 26, 'k', 2)
    for x in range(5, 28, 4):
        c.rect(x, 6, x + 1, 7, 'w')
        c.rect(x, 24, x + 1, 25, 'w')
    c.rect(4, 9, 27, 22, 'B')
    c.bevel(['B'])
    play(c, 13, 11, 9, 'W')
    c.outline()


@icon('deepin-image-viewer', ['com.deepin.image-viewer', 'org.deepin.image.viewer', 'deepin-imageviewer'],
      'deepin', 'deepin Image Viewer')
def deepin_image_viewer(c):
    c.rrect(3, 5, 28, 26, 'W', 2)
    c.rect(5, 7, 26, 24, 'b')
    c.circle(21, 11, 2.5, 'Y')
    c.poly([(5, 24.5), (12, 14), (19, 24.5)], 'B')
    c.poly([(13, 24.5), (19, 17), (26.5, 24.5)], '6')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('deepin-screen-recorder', ['deepin-screenshot', 'com.deepin.screen-recorder', 'org.deepin.screen.recorder',
                                 'deepin-screen-capture'], 'deepin', 'deepin Screen Capture')
def deepin_screen_recorder(c):
    c.rect(3, 3, 10, 5, 'B'); c.rect(3, 3, 5, 10, 'B')
    c.rect(21, 3, 28, 5, 'B'); c.rect(26, 3, 28, 10, 'B')
    c.rect(3, 26, 10, 28, 'B'); c.rect(3, 21, 5, 28, 'B')
    c.rect(21, 26, 28, 28, 'B'); c.rect(26, 21, 28, 28, 'B')
    c.circle(16, 16, 7.5, 'W')
    c.circle(16, 16, 5, 'R')
    c.bevel(['R'])
    c.outline()


@icon('deepin-calculator', ['com.deepin.calculator', 'org.deepin.calculator'], 'deepin', 'deepin Calculator')
def deepin_calculator(c):
    c.rrect(6, 3, 25, 28, 'B', 2)
    c.bevel(['B'])
    c.rect(9, 6, 22, 10, 'W')
    c.text(15, 6, '7', 'k', font=3) if False else c.rect(18, 7, 21, 9, 'S')
    for j in range(3):
        for i in range(3):
            col = 'O' if (i == 2 and j == 2) else 'W'
            c.rect(9 + i * 5, 13 + j * 5, 11 + i * 5, 15 + j * 5, col)
    c.outline()


@icon('deepin-editor', ['com.deepin.editor', 'org.deepin.editor', 'deepin-text-editor'], 'deepin',
      'deepin Editor')
def deepin_editor(c):
    _page(c)
    for y, w in ((10, 12), (14, 10), (18, 12), (22, 6)):
        c.hline(9, 9 + w, y, 'b')
    c.line(28, 13, 18, 25, 'B', 2)
    c.px(17, 26, 'k'); c.px(18, 26, 'k')
    c.outline()


@icon('deepin-system-monitor', ['com.deepin.system-monitor', 'org.deepin.system.monitor'], 'deepin',
      'deepin System Monitor')
def deepin_system_monitor(c):
    c.rrect(3, 4, 28, 22, 'B', 2)
    c.bevel(['B'])
    c.rect(5, 6, 26, 20, 'k')
    pts = [(6, 14), (10, 14), (12, 9), (15, 18), (18, 11), (20, 14), (25, 14)]
    for (a, b), (x, y) in zip(pts, pts[1:]):
        c.line(a, b, x, y, 'G')
    c.rect(13, 23, 18, 25, 'S')
    c.rrect(8, 26, 23, 27, 'S', 1)
    c.outline()


@icon('deepin-app-store', ['deepin-appstore', 'com.deepin.app-store', 'org.deepin.app.store', 'deepin-home-appstore',
                           'uos-app-store', 'deepin-app-store-tool'], 'deepin', 'deepin App Store')
def deepin_app_store(c):
    c.ring(16, 10, 6, 4, '6')
    c.rect(9, 10, 22, 12, '.')
    c.vline(10, 9, 12, '6'); c.vline(21, 9, 12, '6')
    c.poly([(4, 11), (28, 11), (26, 28), (6, 28)], 'B')
    c.bevel(['B'])
    c.ring(16, 10, 6, 4.2, '6')
    c.rect(4, 11, 28, 11, 'B') if False else None
    g(c, 12, 16, """
        ..##....
        .#..#...
        #....#..
        #....#..
        .#..#.#.
        ..##...#
    """, 'W')
    c.outline()


@icon('dde-file-manager', ['deepin-file-manager', 'com.deepin.file-manager', 'org.deepin.file.manager'], 'deepin',
      'deepin File Manager')
def dde_file_manager(c):
    c.rrect(3, 6, 13, 10, '6', 1)
    c.rect(3, 8, 28, 26, '6')
    c.rect(6, 9, 25, 13, 'W')
    c.rect(3, 12, 28, 26, 'B')
    c.bevel(['B'])
    c.hline(3, 28, 12, 'b')
    c.rect(13, 18, 18, 19, 'W')
    c.outline()


@icon('deepin-draw', ['com.deepin.draw', 'org.deepin.draw', 'deepin-paint'], 'deepin', 'deepin Draw')
def deepin_draw(c):
    # painter's palette with a brush
    c.ellipse(15, 17, 12, 10.5, 'W')
    c.circle(19, 22, 2.5, '.')
    c.bevel(['W'])
    for (x, y, col) in ((9, 13, 'R'), (14, 10, 'Y'), (20, 11, 'G'), (9, 19, 'B')):
        c.circle(x, y, 2, col)
    c.line(26, 4, 18, 15, 'N', 2)
    c.rect(16, 16, 18, 18, 'B')
    c.outline()


@icon('deepin-album', ['com.deepin.album', 'org.deepin.album'], 'deepin', 'deepin Album')
def deepin_album(c):
    c.poly([(5, 8), (22, 3), (26, 18), (9, 23)], 'b')
    c.bevel(['b'])
    c.rect(4, 9, 25, 27, 'W')
    c.rect(6, 11, 23, 23, 'B')
    c.circle(19, 15, 2, 'Y')
    c.poly([(6, 23.5), (12, 16), (18, 23.5)], 'W')
    c.poly([(14, 23.5), (18, 19), (23.5, 23.5)], 'c')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('deepin-voice-note', ['com.deepin.voice-note', 'org.deepin.voice.note', 'deepin-voice-notes'], 'deepin',
      'deepin Voice Notes')
def deepin_voice_note(c):
    c.rect(4, 4, 22, 28, 'Y')
    c.bevel(['Y'])
    for y in (9, 13, 17, 21):
        c.hline(7, 18, y, '3')
    c.rrect(19, 12, 26, 23, 'B', 3)
    c.bevel(['B'])
    c.arc(22.5, 20, 6, 4.8, 0, 180, 'B')
    c.rect(22, 25, 23, 28, 'B')
    c.outline()


@icon('deepin-mail', ['com.deepin.mail', 'org.deepin.mail', 'deepin-mail-client'], 'deepin', 'deepin Mail')
def deepin_mail(c):
    c.rect(3, 7, 28, 25, 'B')
    c.bevel(['B'])
    c.poly([(4, 8), (27.5, 8), (16, 18)], 'W')
    c.line(4, 24, 13, 16, 'b'); c.line(27, 24, 18, 16, 'b')
    c.outline()


@icon('deepin-compressor', ['com.deepin.compressor', 'org.deepin.compressor', 'deepin-archive-manager'], 'deepin',
      'deepin Archive Manager')
def deepin_compressor(c):
    c.rect(4, 6, 27, 28, 'B')
    c.rect(3, 3, 28, 8, 'b')
    c.bevel(['B', 'b'])
    for y in range(9, 22, 2):
        c.rect(15 + (y // 2) % 2, y, 16 + (y // 2) % 2, y, 'W')
    c.rrect(13, 21, 18, 26, 'Y', 1)
    c.rect(15, 23, 16, 24, '3')
    c.outline()


@icon('deepin-font-manager', ['com.deepin.font-manager', 'org.deepin.font.manager'], 'deepin',
      'deepin Font Manager')
def deepin_font_manager(c):
    _page(c)
    c.text(9, 8, 'A', 'B', font=5, scale=2, gap=0)
    c.hline(9, 22, 25, 'b')
    c.outline()


@icon('deepin-log-viewer', ['com.deepin.log-viewer', 'org.deepin.log.viewer'], 'deepin', 'deepin Log Viewer')
def deepin_log_viewer(c):
    c.rrect(5, 5, 26, 28, 'B', 2)
    c.bevel(['B'])
    c.rect(7, 8, 24, 26, 'W')
    c.rrect(11, 3, 20, 7, 'S', 1)
    for y in (12, 16, 20):
        c.rect(9, y, 10, y + 1, 'O')
        c.hline(12, 22, y, 'S'); c.hline(12, 19, y + 1, 'w')
    c.outline()


@icon('deepin-boot-maker', ['com.deepin.boot-maker', 'org.deepin.boot.maker', 'deepin-bootmaker'], 'deepin',
      'deepin Boot Maker')
def deepin_boot_maker(c):
    # USB stick, slanted
    c.poly([(13, 3), (21, 3), (21, 10), (13, 10)], 'w')
    c.rect(15, 5, 16, 6, 'S'); c.rect(18, 5, 19, 6, 'S')
    c.rrect(10, 10, 24, 28, 'B', 2)
    c.bevel(['B', 'w'])
    c.ellipse(17, 20, 3.5, 3.5, 'W')
    c.circle(17, 20, 1.5, 'B')
    c.outline()


@icon('dde-calendar', ['deepin-calendar', 'com.deepin.calendar', 'org.deepin.calendar'], 'deepin',
      'deepin Calendar')
def dde_calendar(c):
    c.rrect(3, 5, 28, 28, 'W', 2)
    c.rect(3, 5, 28, 11, 'R')
    c.rrect(3, 5, 28, 11, 'R', 2)
    c.rect(3, 9, 28, 11, 'R')
    c.bevel(['R', 'W'])
    c.rect(8, 3, 9, 7, 'k'); c.rect(22, 3, 23, 7, 'k')
    c.text(9, 14, '31', 'B', font=5, gap=2)
    c.outline()


@icon('deepin-reader', ['com.deepin.reader', 'org.deepin.reader', 'deepin-document-viewer'], 'deepin',
      'deepin Document Viewer')
def deepin_reader(c):
    c.poly([(3, 6), (15, 8), (15, 27), (3, 25)], 'W')
    c.poly([(17, 8), (29, 6), (29, 25), (17, 27)], 'W')
    c.bevel(['W'])
    c.rect(15, 8, 16, 28, 'B')
    c.hline(3, 15, 26, 'B') if False else None
    for y in (12, 15, 18):
        c.hline(6, 12, y, 'b'); c.hline(19, 26, y, 'b')
    c.outline()


@icon('deepin-camera', ['com.deepin.camera', 'org.deepin.camera', 'deepin-webcam'], 'deepin', 'deepin Camera')
def deepin_camera(c):
    # webcam on a stand
    c.circle(16, 13, 10.5, 'W')
    c.bevel(['W'])
    c.circle(16, 13, 7, 'k')
    c.circle(16, 13, 5, 'B')
    c.circle(16, 13, 2.5, '6')
    c.px(14, 11, 'b'); c.px(13, 12, 'W')
    c.rect(14, 24, 17, 25, 'S')
    c.rrect(8, 26, 23, 28, 'w', 1)
    c.shade_below(['w'], 'S')
    c.outline()


@icon('deepin-devicemanager', ['com.deepin.devicemanager', 'org.deepin.device.manager', 'deepin-device-manager'],
      'deepin', 'deepin Device Manager')
def deepin_devicemanager(c):
    for i in range(5):
        for x, y in ((8 + i * 4, 3), (8 + i * 4, 27)):
            c.rect(x, y, x + 1, y + 1, 'S')
        for x, y in ((3, 8 + i * 4), (27, 8 + i * 4)):
            c.rect(x, y, x + 1, y + 1, 'S')
    c.rrect(5, 5, 26, 26, 'B', 2)
    c.bevel(['B'])
    c.rect(10, 10, 21, 21, '6')
    c.rect(11, 11, 20, 20, 'b')
    c.outline()


@icon('deepin-defender', ['com.deepin.defender', 'org.deepin.defender', 'deepin-security-center'], 'deepin',
      'deepin Security Center')
def deepin_defender(c):
    shield(c, 'B', 5, 26, 3, 28)
    c.line(10, 16, 14, 20, 'W', 2)
    c.line(14, 20, 21, 11, 'W', 2)
    c.outline()


@icon('deepin-diskmanager', ['com.deepin.diskmanager', 'org.deepin.disk.manager', 'deepin-disk-manager'], 'deepin',
      'deepin Disk Manager')
def deepin_diskmanager(c):
    c.rrect(3, 7, 28, 25, 'w', 2)
    c.bevel(['w'])
    c.circle(13, 16, 7, 'B')
    c.circle(13, 16, 2, 'W')
    c.line(13, 16, 24, 21, 'k')
    c.rect(22, 9, 25, 10, 'G')
    c.outline()


@icon('deepin-manual', ['com.deepin.manual', 'org.deepin.manual', 'dde-manual'], 'deepin', 'deepin Manual')
def deepin_manual(c):
    c.rrect(5, 3, 26, 28, 'B', 1)
    c.bevel(['B'])
    c.rect(5, 25, 26, 28, 'W')
    c.hline(6, 26, 26, 'w')
    c.vline(8, 3, 24, '6')
    g(c, 13, 8, """
        .###.
        #...#
        ....#
        ...#.
        ..#..
        .....
        ..#..
    """, 'W')
    c.outline()


@icon('deepin-picker', ['com.deepin.picker', 'org.deepin.picker', 'deepin-color-picker'], 'deepin',
      'deepin Color Picker')
def deepin_picker(c):
    # eyedropper
    c.line(5, 26, 16, 15, 'W', 3)
    c.line(5, 26, 13, 18, 'B', 2)
    c.rect(3, 27, 4, 28, 'B')
    c.poly([(15, 11), (21, 17), (19, 19), (13, 13)], 'S')
    c.circle(22.5, 9.5, 6, 'k')
    c.bevel(['k'], dark=False)
    c.outline()


@icon('deepin-deb-installer', ['com.deepin.deb-installer', 'org.deepin.deb.installer', 'deepin-package-installer'],
      'deepin', 'deepin Package Installer')
def deepin_deb_installer(c):
    c.poly([(16, 3), (28, 9), (16, 15), (4, 9)], 'b')
    c.poly([(4, 9), (16, 15), (16, 29), (4, 23)], 'B')
    c.poly([(16, 15), (28, 9), (28, 23), (16, 29)], '6')
    c.poly([(9, 6.5), (21, 12.5), (21, 15), (9, 9)], 'N') if False else None
    c.poly([(19.5, 16), (24.5, 16), (24.5, 19), (26, 19), (22, 24), (18, 19), (19.5, 19)], 'W')
    c.outline()


@icon('deepin-browser', ['org.deepin.browser', 'com.deepin.browser', 'uos-browser'], 'deepin', 'deepin Browser')
def deepin_browser(c):
    disc(c, 'B', 13)
    c.ring(16, 16, 10, 8.8, 'b')
    c.ellipse(16, 16, 4.5, 10, '6') if False else None
    c.arc(16, 16, 10, 8.8, 0, 360, 'b')
    c.vline(16, 6, 25, 'b'); c.hline(6, 25, 16, 'b')
    c.ring(16, 16, 5, 4, 'b')
    c.poly([(19, 10), (25, 7), (22, 13)], 'O')
    c.poly([(13, 22), (7, 25), (10, 19)], 'O')
    c.outline()


@icon('deepin-voice-recorder', ['com.deepin.voice-recorder', 'org.deepin.voice.recorder', 'deepin-recorder'],
      'deepin', 'deepin Voice Recorder')
def deepin_voice_recorder(c):
    c.rrect(11, 3, 20, 19, 'B', 4)
    c.bevel(['B'])
    for y in (7, 10, 13):
        c.hline(13, 18, y, '6')
    c.arc(15.5, 14, 9.5, 8, 0, 180, 'S')
    c.rect(15, 23, 16, 26, 'S')
    c.rrect(10, 27, 21, 28, 'S', 1)
    c.outline()


@icon('deepin-shortcut-viewer', ['com.deepin.shortcut-viewer', 'org.deepin.shortcut.viewer'], 'deepin',
      'deepin Shortcut Viewer')
def deepin_shortcut_viewer(c):
    c.rrect(3, 9, 28, 24, 'w', 2)
    c.bevel(['w'])
    for j in range(2):
        for i in range(6):
            c.rect(5 + i * 4, 11 + j * 4, 7 + i * 4, 13 + j * 4, 'W')
    c.rect(9, 19, 22, 21, 'B')
    c.rect(5, 19, 7, 21, 'W'); c.rect(25, 19, 27, 21, 'W') if False else c.rect(24, 19, 26, 21, 'W')
    c.outline()


@icon('dde-control-center', ['deepin-control-center', 'com.deepin.control-center', 'org.deepin.dde.control.center',
                             'dde-control-center-settings'], 'deepin', 'deepin Control Center')
def dde_control_center(c):
    import math
    c.circle(16, 16, 9.5, 'B')
    for a in range(0, 360, 45):
        x = 16 + 10.5 * math.cos(math.radians(a))
        y = 16 + 10.5 * math.sin(math.radians(a))
        c.circle(x, y, 2.5, 'B')
    c.bevel(['B'])
    c.circle(16, 16, 4.5, 'W')
    c.circle(16, 16, 2, '6')
    c.outline()


@icon('dde-launcher', ['deepin-launcher', 'com.deepin.launcher', 'org.deepin.dde.launcher', 'dde-launchpad'],
      'deepin', 'deepin Launcher')
def dde_launcher(c):
    for (x, y, col) in ((4, 4, 'B'), (17, 4, 'C'), (4, 17, 'C'), (17, 17, 'B')):
        c.rrect(x, y, x + 10, y + 10, col, 3)
    c.bevel(['B', 'C'])
    c.outline()


@icon('deepin-clone', ['com.deepin.clone', 'org.deepin.clone', 'deepin-backup'], 'deepin', 'deepin Clone')
def deepin_clone(c):
    c.rrect(3, 3, 17, 17, 'b', 2)
    c.rrect(13, 13, 28, 28, 'B', 2)
    c.bevel(['b', 'B'])
    c.circle(10, 10, 3, 'W')
    c.circle(20.5, 20.5, 3, 'W')
    c.poly([(22, 5), (28, 5), (28, 11)], 'G')
    c.line(21, 12, 26, 7, 'G', 2)
    c.outline()


@icon('deepin-screensaver', ['com.deepin.screensaver', 'org.deepin.screensaver', 'deepin-screen-saver'], 'deepin',
      'deepin Screensaver')
def deepin_screensaver(c):
    c.circle(16, 16, 13, 'B')
    c.circle(21, 12, 11, '.')
    c.bevel(['B'])
    for x, y in ((21, 9), (25, 17), (17, 5)):
        c.px(x, y, 'Y'); c.px(x - 1, y, 'Y'); c.px(x, y - 1, 'Y'); c.px(x, y + 1, 'Y'); c.px(x + 1, y, 'Y')
    c.outline()


@icon('deepin-ocr', ['com.deepin.ocr', 'org.deepin.ocr'], 'deepin', 'deepin OCR')
def deepin_ocr(c):
    c.rect(3, 3, 9, 5, 'B'); c.rect(3, 3, 5, 9, 'B')
    c.rect(22, 3, 28, 5, 'B'); c.rect(26, 3, 28, 9, 'B')
    c.rect(3, 26, 9, 28, 'B'); c.rect(3, 22, 5, 28, 'B')
    c.rect(22, 26, 28, 28, 'B'); c.rect(26, 22, 28, 28, 'B')
    c.rect(9, 9, 22, 11, 'k')
    c.rect(14, 9, 17, 23, 'k')
    c.outline()


@icon('deepin-downloader', ['com.deepin.downloader', 'org.deepin.downloader', 'deepin-download-manager'], 'deepin',
      'deepin Downloader')
def deepin_downloader(c):
    cloud(c, 'B', 0)
    c.bevel(['B'])
    c.rect(15, 11, 16, 19, 'W')
    c.poly([(11, 18), (20.5, 18), (16, 23)], 'W')
    c.outline()


@icon('dde-printer', ['deepin-printer', 'com.deepin.printer', 'org.deepin.printer', 'dde-printer-manager'], 'deepin',
      'deepin Printer')
def dde_printer(c):
    c.rect(9, 3, 22, 10, 'W')
    c.rrect(3, 9, 28, 22, 'B', 2)
    c.bevel(['B', 'W'])
    c.rect(24, 12, 25, 13, 'G')
    c.rect(8, 18, 23, 28, 'W')
    c.hline(10, 21, 22, 'S'); c.hline(10, 18, 25, 'S')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('deepin-scanner', ['com.deepin.scanner', 'org.deepin.scanner', 'deepin-scan'], 'deepin', 'deepin Scanner')
def deepin_scanner(c):
    c.poly([(5, 13), (25, 4), (27, 7), (7, 16)], 'b')
    c.rrect(3, 15, 28, 26, 'B', 2)
    c.bevel(['B', 'b'])
    c.rect(5, 17, 26, 18, 'c')
    c.rect(22, 22, 25, 23, 'G')
    c.outline()


@icon('deepin-lianliankan', ['com.deepin.lianliankan', 'org.deepin.lianliankan'], 'deepin', 'deepin Lianliankan')
def deepin_lianliankan(c):
    for (x, y, col) in ((3, 3, 'R'), (16, 3, 'B'), (3, 16, 'G'), (16, 16, 'R')):
        c.rrect(x, y, x + 12, y + 12, 'W', 1)
        c.rect(x, y + 11, x + 12, y + 12, 'w')
        c.circle(x + 6.5, y + 6, 3.5, col)
    c.line(9, 9, 22, 22, 'Y') if False else None
    c.outline()


@icon('deepin-gomoku', ['com.deepin.gomoku', 'org.deepin.gomoku'], 'deepin', 'deepin Gomoku')
def deepin_gomoku(c):
    c.rect(3, 3, 28, 28, 'n')
    c.bevel(['n'])
    for i in range(6, 28, 4):
        c.hline(4, 27, i, '8'); c.vline(i, 4, 27, '8')
    for (x, y, col) in ((10, 10, 'k'), (14, 14, 'k'), (18, 18, 'k'), (14, 10, 'W'), (18, 14, 'W'), (22, 10, 'W')):
        c.circle(x + .5, y + .5, 2, col)
    c.outline()


@icon('deepin-service-support', ['deepin-feedback', 'com.deepin.service-support', 'uos-service-support',
                                 'deepin-service-and-support'], 'deepin', 'deepin Service & Support')
def deepin_support(c):
    # headset
    c.arc(16, 16, 12, 10, 180, 360, 'B')
    c.rrect(3, 14, 9, 24, 'B', 2); c.rrect(22, 14, 28, 24, 'B', 2)
    c.bevel(['B'])
    c.line(25, 24, 20, 28, 'S')
    c.rrect(15, 27, 20, 29, 'S', 1)
    g(c, 12, 11, """
        .##.##.
        #######
        #######
        .#####.
        ..###..
        ...#...
    """, 'R')
    c.outline()


@icon('deepin-graphics-driver-manager', ['com.deepin.graphics-driver-manager', 'org.deepin.graphics.driver.manager'],
      'deepin', 'deepin Graphics Driver Manager')
def deepin_gdm(c):
    c.rect(3, 7, 28, 22, 'B')
    c.bevel(['B'])
    c.circle(19, 14.5, 5.5, 'k')
    c.circle(19, 14.5, 4, 'S')
    c.circle(19, 14.5, 1.5, 'k')
    c.rect(6, 10, 10, 13, 'W')
    for x in range(7, 22, 2):
        c.rect(x, 23, x, 25, 'Y')
    c.rect(3, 23, 4, 28, 'S')
    c.outline()


@icon('dde-introduction', ['deepin-introduction', 'com.deepin.introduction', 'org.deepin.dde.introduction'],
      'deepin', 'deepin Welcome')
def dde_introduction(c):
    # lightbulb
    c.circle(16, 12, 9.5, 'Y')
    c.rect(12, 18, 19, 21, 'Y')
    c.bevel(['Y'])
    c.rect(12, 22, 19, 26, 'B')
    c.hline(12, 19, 24, '6')
    c.rect(14, 27, 17, 28, '6')
    c.px(11, 8, 'W'); c.px(12, 7, 'W')
    c.outline()


@icon('deepin-wine', ['deepin-wine5', 'deepin-wine6-stable', 'deepin-wine8-stable', 'deepin-wine-helper',
                      'deepin-wine-runner', 'spark-dwine-helper'], 'deepin', 'deepin-wine')
def deepin_wine(c):
    # a wine glass in deepin blue
    c.ellipse(16, 9, 9, 8, 'W')
    c.rect(0, 0, 31, 3, '.')
    c.ellipse(16, 9, 7.5, 6.5, 'B')
    c.rect(0, 0, 31, 8, '.')
    c.ellipse(16, 9, 9, 8, 'W') if False else None
    for y in range(4, 9):
        for x in range(32):
            if (x + .5 - 16) ** 2 / 81 + (y + .5 - 9) ** 2 / 64 <= 1:
                c.px(x, y, 'W')
    c.rect(15, 17, 16, 25, 'w')
    c.rrect(9, 26, 22, 28, 'w', 1)
    c.bevel(['W', 'B'])
    c.outline()


@icon('deepin-system-update', ['com.deepin.system-update', 'deepin-update', 'dde-update'], 'deepin',
      'deepin Update')
def deepin_update(c):
    disc(c, 'B', 13)
    c.arc(16, 16, 9, 6.5, 200, 520 - 360 + 360, 'W') if False else c.arc(16, 16, 9, 6.5, 300, 210, 'W')
    c.poly([(5, 13), (11, 11), (9, 17)], 'W')
    c.rect(15, 11, 16, 17, 'W')
    c.rect(15, 16, 20, 17, 'W')
    c.outline()


@icon('deepin-logo', ['distributor-logo-deepin', 'deepin', 'start-here-deepin', 'uos-logo', 'distributor-logo-uos'],
      'deepin', 'deepin')
def deepin_logo(c):
    # the deepin swirl
    disc(c, 'B', 13)
    c.arc(16, 16, 10.5, 8.5, 200, 120, 'W')
    c.arc(17, 15, 6.5, 4.5, 30, 300, 'W')
    c.circle(18, 14, 2, 'W')
    c.outline()
