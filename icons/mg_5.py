"""3D modelling, CAD, 3D printing/laser, pro photo and level editors."""
from pix import icon
import math


def cube(c, cx, top, s, ct, cl, cr):
    """Isometric cube: top centre x=cx, top y=top, half-width s."""
    h = s // 2
    c.poly([(cx, top), (cx + s, top + h), (cx, top + 2 * h), (cx - s, top + h)], ct)
    c.poly([(cx - s, top + h), (cx, top + 2 * h), (cx, top + 2 * h + s), (cx - s, top + h + s)], cl)
    c.poly([(cx, top + 2 * h), (cx + s, top + h), (cx + s, top + h + s), (cx, top + 2 * h + s)], cr)


def nozzle(c, x, y, col='O'):
    """Hotend block + nozzle, block top-left at x,y (12 wide)."""
    c.rect(x, y, x + 11, y + 6, col)
    c.rect(x + 3, y + 7, x + 8, y + 8, 's')
    c.poly([(x + 3, y + 9), (x + 9, y + 9), (x + 6, y + 12)], 'Y')


# =================================================================== 3D

@icon('net.blockbench.Blockbench', ['blockbench', 'blockbench-bin'], '3d', 'Blockbench')
def blockbench(c):
    # stacked blocky voxel bench shape: two cubes
    cube(c, 16, 3, 12, 'b', 'B', '6')
    c.line(16, 15, 16, 27, 'K') if False else None
    c.rect(10, 13, 13, 16, 'W') if False else None
    c.poly([(16, 9), (22, 12), (16, 15), (10, 12)], 'c')
    c.outline()


@icon('io.github.guillaumechereau.Goxel', ['goxel'], '3d', 'Goxel')
def goxel(c):
    # pile of three voxels
    cube(c, 10, 13, 7, 'r', 'R', '1')
    cube(c, 22, 13, 7, 'g', 'G', '4')
    cube(c, 16, 3, 7, 'b', 'B', '6')
    c.outline()


@icon('magicavoxel', ['MagicaVoxel'], '3d', 'MagicaVoxel')
def magicavoxel(c):
    # voxel wizard hat
    c.poly([(16, 2.5), (23, 22), (9, 22)], 'M')
    for y in range(4, 22, 3):
        c.hline(9, 23, y, '7') if False else None
    c.bevel(['M'])
    c.rect(3, 22, 28, 27, 'B')
    c.bevel(['B'])
    for x, y in ((14, 9), (18, 15), (12, 17)):
        c.rect(x, y, x + 1, y + 1, 'Y')
    c.outline()


@icon('wings3d', ['wings', 'Wings3D'], '3d', 'Wings 3D')
def wings3d(c):
    # pair of wings around a sphere
    for side in (-1, 1):
        for i in range(3):
            x0 = 16 + side * (3 + i * 2)
            c.poly([(16, 10 + i * 2), (x0 + side * 6.5, 3 + i * 4), (x0 + side * 4, 12 + i * 4)], 'W' if i % 2 == 0 else 'w')
    c.circle(16, 19, 7, 'R')
    c.bevel(['R'])
    c.px(13, 15, 'r'); c.px(14, 15, 'W')
    c.outline()


@icon('armorpaint', ['org.armorpaint.ArmorPaint', 'ArmorPaint'], '3d', 'ArmorPaint')
def armorpaint(c):
    # helmet half painted
    c.ellipse(16, 15, 12, 12, 's')
    c.rect(4, 15, 28, 27, 's')
    c.bevel(['s'])
    c.poly([(16, 3), (28, 3), (28, 27), (16, 27)], '.')
    c.ellipse(16, 15, 12, 12, 'O') if False else None
    for y in range(32):
        for x in range(16, 32):
            if math.hypot(x + .5 - 16, y + .5 - 15) <= 12 or (15 <= y <= 27 and x <= 27):
                c.px(x, y, 'O')
    c.bevel(['O'])
    c.rect(8, 15, 24, 18, 'K')
    c.rect(14, 18, 17, 25, 'K')
    c.outline()


@icon('material-maker', ['io.github.RodZill4.Material-Maker', 'materialmaker'], '3d', 'Material Maker')
def materialmaker(c):
    # shaded material sphere on a checker
    for x in range(4, 28, 4):
        for y in range(20, 28, 4):
            c.rect(x, y, x + 3, y + 3, 'w' if (x + y) // 4 % 2 else 'S')
    c.circle(16, 14.5, 10.5, 'O')
    c.circle(13, 11.5, 6.5, 'o')
    c.circle(11, 9.5, 3, 'y')
    c.arc(16, 14.5, 10.5, 8.5, 0, 120, '2')
    c.outline()


@icon('meshlab', ['net.meshlab.MeshLab', 'MeshLab'], '3d', 'MeshLab')
def meshlab(c):
    # triangulated sphere wireframe
    c.circle(16, 16, 13, 'C')
    c.bevel(['C'])
    for y in (9, 16, 23):
        c.hline(4, 28, y, '5') if False else None
    pts = [(16, 4), (7, 9), (25, 9), (4, 16), (16, 14), (27, 16), (7, 24), (25, 24), (16, 28)]
    for a, b in ((0, 1), (0, 2), (1, 4), (2, 4), (1, 3), (2, 5), (3, 4), (4, 5), (3, 6), (4, 6), (4, 7), (5, 7), (6, 8), (7, 8), (4, 8)):
        c.line(*pts[a], *pts[b], '5')
    for x, y in pts[4:5]:
        c.rect(x - 1, y - 1, x, y, 'W')
    c.outline()


@icon('meshroom', ['Meshroom', 'alicevision-meshroom'], '3d', 'Meshroom')
def meshroom(c):
    # photos converging into a point-cloud mesh
    c.rect(3, 3, 11, 10, 'W'); c.rect(5, 5, 9, 8, 'C')
    c.rect(20, 3, 28, 10, 'W'); c.rect(22, 5, 26, 8, 'C')
    c.line(9, 10, 16, 18, 'S'); c.line(22, 10, 16, 18, 'S')
    c.poly([(16, 15), (27, 21.5), (16, 28), (5, 21.5)], 'G')
    c.bevel(['G'])
    c.line(5, 21, 26, 21, '4'); c.line(16, 15, 16, 27, '4')
    c.outline()


@icon('openscad', ['org.openscad.OpenSCAD', 'OpenSCAD', 'openscad-nightly'], '3d', 'OpenSCAD')
def openscad(c):
    # CSG: cube with a sphere subtracted, yellow
    cube(c, 16, 3, 12, 'y', 'Y', '3')
    c.ellipse(21, 19, 4, 5, 'k')
    c.ellipse(21, 19, 2.5, 3.5, 'N')
    c.outline()


@icon('solvespace', ['com.solvespace.SolveSpace', 'SolveSpace'], '3d', 'SolveSpace')
def solvespace(c):
    # constrained sketch: rectangle with dimension arrows
    c.rect(3, 3, 28, 28, 'k')
    c.frame(8, 9, 23, 22, 'G')
    c.frame(9, 10, 22, 21, 'G')
    c.hline(8, 23, 6, 'm'); c.vline(8, 5, 7, 'm'); c.vline(23, 5, 7, 'm')
    c.vline(25, 9, 22, 'm')
    c.rect(7, 8, 9, 10, 'W'); c.rect(22, 21, 24, 23, 'W')
    c.outline()


@icon('librecad', ['org.librecad.librecad', 'LibreCAD'], '3d', 'LibreCAD')
def librecad(c):
    # drafting compass over blueprint
    c.rect(3, 8, 28, 28, 'B')
    c.bevel(['B'])
    for x in range(6, 28, 5):
        c.vline(x, 9, 27, '6')
    c.arc(16, 9, 15, 14, 45, 135, 'W')
    c.line(16, 5, 9, 26, 'w', 2); c.line(16, 5, 23, 26, 'w', 2)
    c.circle(16, 5, 2.5, 'S')
    c.outline()


@icon('qcad', ['org.qcad.QCAD', 'QCAD', 'qcad-bin'], '3d', 'QCAD')
def qcad(c):
    # set square + ruler
    c.poly([(3, 28), (3, 3), (28, 28)], 'O')
    c.poly([(8, 23), (8, 15), (16, 23)], '.')
    c.bevel(['O'])
    for y in range(6, 28, 3):
        c.hline(4, 5, y, '2')
    c.outline()


@icon('brlcad', ['brl-cad', 'mged', 'archer'], '3d', 'BRL-CAD')
def brlcad(c):
    # tank silhouette (BRL-CAD's heritage)
    c.rrect(3, 18, 28, 26, 'G', 3)
    c.bevel(['G'])
    for x in range(7, 26, 4):
        c.circle(x + .5, 22.5, 1.6, '4')
    c.rect(8, 12, 22, 17, 'G')
    c.bevel(['G'])
    c.rect(22, 13, 29, 15, 'g') if False else c.rect(22, 13, 28, 14, '4')
    c.outline()


@icon('com.eteks.sweethome3d', ['sweethome3d', 'SweetHome3D'], '3d', 'Sweet Home 3D')
def sweethome3d(c):
    # house with a heart window
    c.poly([(16, 3), (29, 14), (3, 14)], 'R')
    c.bevel(['R'])
    c.rect(6, 14, 26, 28, 'y')
    c.bevel(['y'])
    c.rect(13, 20, 18, 28, 'N')
    c.rect(20, 17, 24, 21, 'C')
    c.rect(8, 17, 11, 21, 'C')
    c.outline()


@icon('com.ultimaker.cura', ['cura', 'UltiMaker-Cura', 'ultimaker-cura', 'cura-bin'], '3d', 'UltiMaker Cura')
def cura(c):
    # blue printer frame with nozzle over a part
    c.rect(3, 3, 28, 28, 'B')
    c.rect(6, 6, 25, 25, 'k')
    c.bevel(['B'])
    c.hline(6, 25, 9, 's')
    nozzle(c, 10, 8, 'w')
    c.rect(9, 22, 22, 25, 'C')
    c.rect(11, 20, 20, 21, 'C')
    c.outline()


@icon('com.prusa3d.PrusaSlicer', ['PrusaSlicer', 'prusa-slicer', 'prusaslicer', 'PrusaGcodeviewer'], '3d',
      'PrusaSlicer')
def prusaslicer(c):
    # orange hotend with a sliced cube under it
    nozzle(c, 10, 3, 'O')
    for i, col in enumerate(('o', 'O', '2', 'O', 'o')):
        c.rect(4 + i, 19 + i * 2, 27 - i, 20 + i * 2, col)
    c.outline()


@icon('io.github.softfever.OrcaSlicer', ['orca-slicer', 'OrcaSlicer', 'orcaslicer', 'orca-slicer-bin'], '3d',
      'OrcaSlicer')
def orcaslicer(c):
    # orca whale
    c.ellipse(15, 17, 12, 7.5, 'k')
    c.poly([(22, 14), (29, 6), (27, 15)], 'k')
    c.poly([(14, 11), (17, 3), (19, 11)], 'k')
    c.poly([(3, 18), (7, 23), (9, 19)], 'k') if False else None
    c.ellipse(13, 21, 9, 3, 'W')
    c.ellipse(8, 14, 2, 1.2, 'W')
    c.bevel(['k'], dark=False)
    c.outline()


@icon('com.bambulab.BambuStudio', ['bambu-studio', 'BambuStudio', 'bambustudio', 'bambustudio-bin'], '3d',
      'Bambu Studio')
def bambu(c):
    # bamboo-split square mark in green
    c.poly([(3, 3), (13, 3), (13, 28), (3, 28)], 'G')
    c.poly([(16, 3), (28, 3), (28, 14), (16, 19)], 'G')
    c.poly([(16, 22), (28, 17), (28, 28), (16, 28)], 'G')
    c.bevel(['G'])
    c.outline()


@icon('superslicer', ['SuperSlicer', 'com.superslicer.SuperSlicer', 'superslicer-bin'], '3d', 'SuperSlicer')
def superslicer(c):
    # lightning-bolt hotend
    nozzle(c, 10, 3, 'B')
    c.poly([(14, 4), (19, 4), (16, 7), (19, 7), (13, 11), (15, 8), (12, 8)], 'Y')
    for i in range(4):
        c.rect(4 + i * 2, 19 + i * 2, 27 - i * 2, 20 + i * 2, 'b' if i % 2 else 'B')
    c.outline()


@icon('lightburn', ['LightBurn', 'com.lightburnsoftware.LightBurn'], '3d', 'LightBurn')
def lightburn(c):
    # laser head beaming onto a burning sheet
    c.rect(10, 3, 21, 10, 'S')
    c.bevel(['S'])
    c.rect(14, 11, 17, 12, 'k')
    c.vline(15, 13, 21, 'R'); c.vline(16, 13, 21, 'r')
    c.poly([(3, 24), (28, 24), (25, 28), (6, 28)], 'n')
    c.circle(16, 22.5, 3, 'O')
    c.circle(16, 22.5, 1.5, 'Y')
    c.outline()


@icon('hugin', ['net.sourceforge.Hugin', 'Hugin', 'PTBatcherGUI', 'calibrate_lens_gui'], 'photo', 'Hugin')
def hugin(c):
    # wide panorama strip curved
    c.poly([(3, 9), (16, 6), (28, 9), (28, 24), (16, 21), (3, 24)], 'C')
    c.poly([(3, 24), (8, 15), (13, 20), (19, 13), (28, 22), (28, 24), (16, 21)], 'G')
    c.bevel(['C', 'G'])
    c.circle(22, 11, 1.5, 'Y')
    c.outline()


@icon('net.sourceforge.qtpfsgui.LuminanceHDR', ['luminance-hdr', 'luminance'], 'photo', 'Luminance HDR')
def luminancehdr(c):
    # three stacked exposures
    for i, col in enumerate(('k', 'S', 'W')):
        x = 3 + i * 6
        y = 3 + i * 6
        c.rect(x, y, x + 13, y + 13, col)
    c.circle(20, 20, 3, 'Y')
    c.outline()


@icon('org.entangle_photo.Manager', ['entangle'], 'photo', 'Entangle')
def entangle(c):
    # DSLR tethered by a cable
    c.rect(3, 9, 22, 22, 'k')
    c.rect(7, 6, 13, 8, 'k')
    c.bevel(['k'])
    c.circle(12.5, 15.5, 5, 's')
    c.circle(12.5, 15.5, 3, 'B')
    c.px(11, 14, 'W')
    c.line(22, 18, 26, 22, 'O', 2); c.line(26, 22, 26, 28, 'O', 2)
    c.outline()


@icon('art', ['us.pixls.art.ART', 'ART', 'art-rawconverter'], 'photo', 'ART')
def art(c):
    # aperture blades inside a picture frame
    c.rect(3, 3, 28, 28, 'N')
    c.bevel(['N'])
    c.rect(6, 6, 25, 25, 'k')
    for i in range(6):
        a = math.radians(i * 60)
        c.poly([(15.5 + 9 * math.cos(a), 15.5 + 9 * math.sin(a)),
                (15.5 + 9 * math.cos(a + 1.05), 15.5 + 9 * math.sin(a + 1.05)),
                (15.5 + 3 * math.cos(a + 2), 15.5 + 3 * math.sin(a + 2))], ('R', 'O', 'Y', 'G', 'B', 'M')[i])
    c.outline()


@icon('ansel', ['photos.ansel.app', 'Ansel'], 'photo', 'Ansel')
def ansel(c):
    # mountain peak (Ansel Adams) in monochrome
    c.circle(16, 16, 13, 'S')
    c.bevel(['S'])
    c.poly([(3, 26), (13, 9), (18, 17), (22, 12), (29, 26)], 'k')
    c.poly([(11, 12.5), (13, 9), (15.5, 13), (13, 12)], 'W')
    for y in range(26, 32):
        for x in range(32):
            if math.hypot(x + .5 - 16, y + .5 - 16) > 13:
                c.px(x, y, '.')
    c.outline()


@icon('org.filmulator.Filmulator', ['filmulator', 'filmulator-gui'], 'photo', 'Filmulator')
def filmulator(c):
    # developing tray with film
    c.poly([(3, 15), (28, 15), (26, 26), (5, 26)], 'w')
    c.bevel(['w'])
    c.rect(5, 17, 26, 20, 'Y')
    c.rect(8, 6, 23, 15, 'N')
    for x in range(9, 23, 3):
        c.px(x, 7, 'k'); c.px(x, 14, 'k')
    c.rect(10, 9, 21, 12, 'O')
    c.outline()


@icon('vkdt', [], 'photo', 'vkdt')
def vkdt(c):
    # node graph sheet with tone curve
    c.rect(3, 3, 28, 28, 'k')
    for x in range(5, 27):
        y = int(26 - 21 * (1 / (1 + math.exp(-(x - 16) / 3.2))))
        c.rect(x, y, x, y + 1, 'A')
    c.hline(5, 26, 26, 's'); c.vline(5, 5, 26, 's')
    c.outline()


@icon('org.siril.Siril', ['siril'], 'photo', 'Siril')
def siril(c):
    # spiral galaxy
    c.circle(16, 16, 13, 'k')
    for t in range(0, 600):
        a = t / 60.0
        r = 1.2 * a
        for s_ in (0, math.pi):
            x, y = 16 + r * math.cos(a + s_), 16 + r * math.sin(a + s_) * 0.8
            c.px(int(x), int(y), 'm' if r < 6 else 'M')
    c.circle(16, 16, 2.5, 'W')
    c.px(7, 7, 'W'); c.px(24, 22, 'W'); c.px(22, 6, 'w')
    c.outline()


@icon('org.fritzing.Fritzing', ['fritzing', 'Fritzing'], '3d', 'Fritzing')
def fritzing(c):
    # breadboard with an LED
    c.rect(3, 12, 28, 28, 'W')
    c.bevel(['W'])
    for x in range(5, 28, 2):
        for y in (15, 17, 23, 25):
            c.px(x, y, 'S')
    c.hline(4, 27, 20, 'R')
    c.vline(13, 7, 14, 's'); c.vline(18, 7, 14, 's')
    c.ellipse(15.5, 7, 4.5, 4, 'R')
    c.rect(11, 7, 20, 9, 'R')
    c.px(14, 5, 'r')
    c.outline()


@icon('io.github.f3d_app.f3d', ['f3d'], '3d', 'F3D')
def f3d(c):
    # wireframe cube with axis gizmo
    cube(c, 16, 3, 12, 'w', 'S', 's')
    c.line(16, 15, 16, 27, 'k')
    c.line(16, 15, 4, 9, 'R'); c.line(16, 15, 28, 9, 'G')
    c.outline()


@icon('org.mapeditor.Tiled', ['tiled', 'Tiled'], '3d', 'Tiled')
def tiled(c):
    # isometric tile map: grass, water, sand tiles
    for (dx, dy, t, l, r) in ((0, 0, 'g', 'G', '4'), (-6, 3, 'c', 'C', '5'), (6, 3, 'y', 'Y', '3'), (0, 6, 'g', 'G', '4')):
        cube(c, 16 + dx, 6 + dy, 6, t, l, r)
    c.outline()


@icon('trenchbroom', ['TrenchBroom', 'com.kristianduske.TrenchBroom'], '3d', 'TrenchBroom')
def trenchbroom(c):
    # brush cube with a broom stick
    cube(c, 13, 9, 10, 'n', 'N', '8')
    c.line(17, 15, 27, 4, 'y', 2)
    c.poly([(14, 17), (19, 13), (22, 18), (16, 22)], 'Y')
    c.outline()


@icon('makehuman', ['org.makehumancommunity.makehuman', 'MakeHuman'], '3d', 'MakeHuman')
def makehuman(c):
    # T-pose figure
    c.circle(16, 6, 3.5, 'p')
    c.rect(4, 11, 28, 13, 'p')
    c.rect(12, 10, 20, 20, 'p')
    c.rect(12, 20, 15, 28, 'p'); c.rect(17, 20, 20, 28, 'p')
    c.bevel(['p'])
    c.outline()


@icon('dune3d', ['org.dune3d.dune3d'], '3d', 'Dune 3D')
def dune3d(c):
    # sand dunes under a sun
    c.circle(22, 9, 5, 'Y')
    c.bevel(['Y'])
    c.poly([(3, 28), (3, 20), (12, 13), (20, 20), (28, 16), (28, 28)], 'O')
    c.poly([(3, 28), (12, 22), (20, 25), (28, 21), (28, 28)], '2')
    c.outline()


@icon('cq-editor', ['CQ-editor', 'cadquery'], '3d', 'CQ-editor')
def cqeditor(c):
    # code brackets carving a cube
    cube(c, 18, 7, 10, 'c', 'C', '5')
    c.sprite(3, 6, """
        ..##
        .##.
        ##..
        ##..
        .##.
        ..##
    """, {'#': 'O'})
    c.outline()
