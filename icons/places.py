from pix import icon

"""Freedesktop 'places': one folder family (OmaPix yellow/orange, like Files)
plus the drives, trash, network and computer places."""

# --------------------------------------------------------------- folder family
EMBLEMS = {
    'home': """
        .....#.....
        ....###....
        ...#####...
        ..#######..
        .#########.
        ###########
        .###...###.
        .###...###.
        .###...###.
    """,
    'desktop': """
        ###########
        #.........#
        #.........#
        #.........#
        ###########
        ....###....
        ..#######..
    """,
    'documents': """
        ######...
        #....##..
        #.##.#.#.
        #....####
        #.#####.#
        #.......#
        #.#####.#
        #.......#
        #########
    """,
    'download': """
        ...###...
        ...###...
        ...###...
        .#######.
        ..#####..
        ...###...
        #...#...#
        #########
    """,
    'music': """
        ....######
        ....######
        ....#....#
        ....#....#
        ....#....#
        .####..###
        #####.####
        .###...##.
    """,
    'pictures': """
        ###########
        #.......#.#
        #.........#
        #...#.....#
        #..###..#.#
        #.#####.###
        ###########
    """,
    'videos': """
        #.#######.#
        ###.....###
        #.#.#...#.#
        ###.##..###
        #.#.#...#.#
        ###.....###
        #.#######.#
    """,
    'templates': """
        ##.##.##.
        #.......#
        .........
        #.......#
        #.......#
        .........
        #.......#
        ##.##.##.
    """,
    'publicshare': """
        .......##.
        ......####
        ....##.##.
        .###......
        #####.....
        .###......
        ....##.##.
        ......####
        .......##.
    """,
    'remote': """
        .....###...
        ....#####..
        .##.######.
        ###########
        ###########
        .#########.
    """,
    'recent': """
        ..#####..
        .##.#.##.
        ##..#..##
        #...#...#
        #...###.#
        ##.....##
        .##...##.
        ..#####..
    """,
}


def folder(c, emblem=None, opened=False):
    """The shared OmaPix folder: orange back with tab, paper, yellow front."""
    c.rrect(3, 5, 13, 9, 'O', 1)
    c.rect(3, 7, 28, 27, 'O')
    c.bevel(['O'], dark=False)
    c.rect(6, 9, 25, 14, 'W')
    c.hline(8, 23, 11, 'w')
    if opened:
        # back narrows, paper lifts out, front flap swings forward (parallelogram)
        c.rect(26, 7, 28, 27, '.')
        c.rect(7, 8, 22, 14, 'W')
        c.hline(9, 20, 10, 'w')
        c.hline(9, 18, 12, 'w')
        for y in range(14, 28):
            k = (y - 14) // 4 if y < 26 else 3
            c.hline(6 - k, 28 - k, y, 'Y')
            c.px(6 - k, y, 'y')
            c.px(28 - k, y, '3')
        c.hline(6, 27, 14, 'y')
        c.hline(4, 25, 27, '3')
        c.outline()
        return
    c.rect(3, 13, 28, 27, 'Y')
    c.bevel(['Y'])
    c.hline(3, 28, 13, 'y')
    if emblem:
        art = EMBLEMS[emblem]
        rows = [r.strip() for r in art.strip('\n').split('\n')]
        w, h = len(rows[0]), len(rows)
        x0 = 16 - (w + 1) // 2
        y0 = 20 - h // 2
        c.sprite(x0, y0 + 1, art, {'#': 'y'})
        c.sprite(x0, y0, art, {'#': '3'})
    c.outline()


def _f(emblem):
    return lambda c: folder(c, emblem)


@icon('folder', ['inode-directory', 'folder-new', 'gtk-directory'], 'places', 'Folder')
def p_folder(c):
    folder(c)


@icon('folder-open', ['folder-drag-accept', 'folder-visiting'], 'places', 'Folder (open)')
def p_folder_open(c):
    folder(c, opened=True)


FAMILY = [
    ('user-home', ['folder-home', 'gnome-fs-home'], 'home', 'Home'),
    ('user-desktop', ['folder-desktop'], 'desktop', 'Desktop'),
    ('folder-documents', ['folder-document'], 'documents', 'Documents'),
    ('folder-download', ['folder-downloads'], 'download', 'Downloads'),
    ('folder-music', ['folder-sound'], 'music', 'Music'),
    ('folder-pictures', ['folder-images', 'folder-image'], 'pictures', 'Pictures'),
    ('folder-videos', ['folder-video'], 'videos', 'Videos'),
    ('folder-templates', ['folder-template'], 'templates', 'Templates'),
    ('folder-publicshare', ['folder-public'], 'publicshare', 'Public'),
    ('folder-remote', ['folder-network', 'folder-cloud'], 'remote', 'Remote'),
    ('folder-recent', ['document-open-recent'], 'recent', 'Recent'),
]
for _id, _names, _em, _label in FAMILY:
    icon(_id, _names, 'places', _label)(_f(_em))


@icon('user-bookmarks', ['bookmarks', 'bookmark-new', 'starred'], 'places', 'Bookmarks')
def p_bookmarks(c):
    folder(c)
    # red ribbon tucked into the folder, hanging over the front
    c.rect(18, 3, 24, 21, 'R')
    c.vline(18, 3, 21, 'r')
    c.vline(24, 4, 21, '1')
    c.pixels([(20, 21), (21, 21), (22, 21), (21, 20)], '.')
    c.px(20, 20, '1'); c.px(22, 20, '1')
    c.sprite(19, 7, '''
        ..W..
        WWWWW
        .WWW.
        .W.W.
    ''')
    c.hline(18, 24, 3, 'r')
    c.replace('K', '.')
    c.outline()


def _bin(c, bottom=29):
    c.poly([(5, 9), (27, 9), (25, bottom), (7, bottom)], 'w')
    c.bevel(['w'])
    for x in (11, 16, 21):
        c.vline(x, 11, 26, 'S')
        c.vline(x - 1, 11, 26, 'W') if x != 11 else None
    c.vline(10, 11, 26, 'W')


@icon('user-trash', ['trash-empty', 'gnome-fs-trash-empty'], 'places', 'Trash')
def p_trash(c):
    _bin(c)
    c.rrect(13, 3, 19, 5, 'S', 1)
    c.rect(15, 4, 17, 5, '.')
    c.rect(3, 6, 28, 8, 'S')
    c.hline(3, 28, 6, 'w')
    c.hline(4, 28, 8, 's')
    c.outline()


@icon('user-trash-full', ['trash-full', 'gnome-fs-trash-full'], 'places', 'Trash (full)')
def p_trash_full(c):
    _bin(c, 28)
    # crumpled paper heaped over the rim
    c.circle(10, 7.5, 3.5, 'W')
    c.circle(17, 6.5, 3.5, 'W')
    c.circle(23, 7.5, 3, 'y')
    c.pixels([(9, 6), (11, 8), (16, 5), (18, 7), (17, 4)], 'w')
    c.pixels([(22, 7), (24, 8)], 'Y')
    c.rect(4, 9, 27, 10, 'S')
    c.hline(4, 27, 9, 'w')
    c.hline(5, 27, 10, 's')
    c.outline()


@icon('network-workgroup', ['network-server', 'network', 'gnome-fs-network',
                            'network-wired'], 'places', 'Network')
def p_network(c):
    c.rect(6, 3, 25, 21, 'k')
    for y in (4, 10, 16):
        c.rect(7, y, 24, y + 4, 'S')
        c.hline(7, 24, y, 'w')
        c.hline(7, 24, y + 4, 's')
        c.hline(14, 21, y + 2, 'k')
        c.px(9, y + 2, 'G'); c.px(11, y + 2, 'g' if y == 4 else 'Y')
    c.rect(15, 22, 16, 24, 'B')
    c.rrect(3, 25, 28, 28, 'B', 1)
    c.hline(4, 27, 25, 'b')
    c.hline(4, 27, 28, '6')
    for x in (6, 25):
        c.rect(x, 26, x + 1, 27, '6')
    c.outline()


@icon('drive-harddisk', ['drive-harddisk-system', 'gnome-dev-harddisk', 'harddrive', 'drive-multidisk',
                         'drive-harddisk-solidstate'], 'places', 'Hard disk')
def p_hdd(c):
    c.rrect(5, 3, 26, 28, 'S', 1)
    c.bevel(['S'])
    c.circle(15, 13, 9, 'w')
    c.ring(15, 13, 9, 8, 's')
    c.arc(15, 13, 8, 5.5, 190, 260, 'W')
    c.circle(15, 13, 2, 'k')
    c.px(14, 12, 'S')
    # actuator arm
    c.rect(22, 21, 24, 24, 'k')
    c.line(23, 22, 17, 15, 'k', 2)
    c.px(23, 22, 'S')
    for x, y in ((7, 5), (24, 5), (7, 26), (24, 26)):
        c.px(x, y, 's')
    c.rect(9, 24, 14, 25, 's')
    c.px(18, 25, 'G')
    c.outline()


@icon('drive-removable-media', ['drive-removable-media-usb', 'media-removable', 'drive-removable-media-usb-pendrive',
                                'media-flash', 'gnome-dev-removable-usb'], 'places', 'USB drive')
def p_usb(c):
    c.poly([(17.5, 9.5), (22.5, 14.5), (28.5, 8.5), (23.5, 3.5)], 'w')
    c.bevel(['w'])
    c.pixels([(23, 7), (24, 8), (25, 6), (26, 7)], 's')
    c.poly([(5.5, 19.5), (12.5, 26.5), (23.5, 15.5), (16.5, 8.5)], 'B')
    c.bevel(['B'])
    c.pixels([(9, 21), (10, 22), (11, 23)], '6')
    c.px(16, 13, 'G'); c.px(17, 14, 'g')
    c.outline()


@icon('media-optical', ['drive-optical', 'media-optical-cd', 'media-optical-dvd', 'media-cdrom', 'cdrom',
                        'gnome-dev-cdrom', 'media-optical-bd', 'brasero'], 'places', 'Optical disc')
def p_disc(c):
    c.circle(16, 16, 13, 'w')
    c.arc(16, 16, 12, 6, 200, 250, 'c')
    c.arc(16, 16, 12, 6, 250, 290, 'W')
    c.arc(16, 16, 12, 6, 20, 70, 'm')
    c.arc(16, 16, 12, 6, 70, 110, 'y')
    c.ring(16, 16, 13, 12, 'S')
    c.circle(16, 16, 5, 'S')
    c.circle(16, 16, 4, 'w')
    c.circle(16, 16, 2, '.')
    c.outline()


@icon('computer', ['user-computer', 'computer-laptop', 'gnome-fs-client', 'device_computer'],
      'places', 'Computer')
def p_computer(c):
    # beige retro desktop: monitor sitting on the case
    c.rrect(6, 3, 25, 18, 'w', 1)
    c.bevel(['w'])
    c.rect(8, 5, 23, 15, 'k')
    c.rect(9, 6, 22, 14, 'B')
    c.rect(11, 7, 17, 11, 'W')
    c.hline(11, 17, 7, 'b')
    c.rect(18, 9, 20, 13, 'b')
    c.hline(9, 22, 14, '6')
    c.rect(12, 19, 19, 20, 'S')
    c.rrect(3, 21, 28, 27, 'w', 1)
    c.bevel(['w'])
    c.rect(6, 23, 15, 24, 'k')
    c.px(24, 24, 'G'); c.px(22, 24, 'S')
    c.outline()
