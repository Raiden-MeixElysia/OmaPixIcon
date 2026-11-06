"""Music production, synths, notation, JACK/PipeWire tools and voice chat."""
from pix import icon
import math


def knob(c, cx, cy, r, col='w', mark='k', ang=-60):
    c.circle(cx, cy, r, col)
    a = math.radians(ang - 90)
    c.line(int(cx), int(cy), int(cx + (r - 1) * math.cos(a)), int(cy + (r - 1) * math.sin(a)), mark)


def notehead(c, x, y, col):
    c.rect(x, y, x + 2, y + 1, col)


# =================================================================== DAWs / sequencers

@icon('org.hydrogenmusic.Hydrogen', ['hydrogen', 'h2cli'], 'audio', 'Hydrogen')
def hydrogen(c):
    # snare drum with crossed sticks
    c.ellipse(16, 13, 12, 4.5, 'W')
    c.rect(4, 13, 27, 24, 'R')
    c.ellipse(16, 24, 12, 4.5, 'R')
    c.ellipse(16, 13, 12, 4.5, 'W')
    c.bevel(['R'])
    for x in range(6, 27, 4):
        c.line(x, 15, x + 2, 25, 'Y') if False else c.vline(x, 17, 25, 'y')
    c.ellipse(16, 13, 9, 2.5, 'w')
    c.line(5, 3, 15, 11, 'n', 2); c.line(26, 3, 17, 11, 'n', 2)
    c.outline()


@icon('studio.kx.carla', ['carla', 'carla-control', 'carla-patchbay', 'carla-rack'], 'audio', 'Carla')
def carla(c):
    # rack unit with ears and two knobs
    c.rect(3, 9, 28, 23, 'O')
    c.bevel(['O'])
    c.rect(3, 9, 5, 23, 's'); c.rect(26, 9, 28, 23, 's')
    c.px(4, 11, 'k'); c.px(4, 21, 'k'); c.px(27, 11, 'k'); c.px(27, 21, 'k')
    knob(c, 11, 16, 3.5, 'k', 'W', -40)
    knob(c, 20, 16, 3.5, 'k', 'W', 50)
    c.rect(8, 4, 23, 8, 'k')
    c.hline(10, 21, 6, 'G')
    c.rect(8, 24, 23, 28, 'k')
    c.hline(10, 21, 26, 'R')
    c.outline()


@icon('org.zrythm.Zrythm', ['zrythm'], 'audio', 'Zrythm')
def zrythm(c):
    c.poly([(4, 3), (28, 3), (28, 8), (13, 23), (28, 23), (28, 29), (4, 29), (4, 24), (19, 9), (4, 9)], 'O')
    c.bevel(['O'])
    c.line(9, 26, 26, 26, '2') if False else None
    c.outline()


@icon('org.rncbc.qtractor', ['qtractor'], 'audio', 'Qtractor')
def qtractor(c):
    # little tractor
    c.rect(11, 6, 19, 15, 'G')
    c.rect(13, 8, 18, 12, 'c')
    c.rect(4, 13, 27, 20, 'G')
    c.bevel(['G'])
    c.rect(24, 7, 25, 13, 's')
    c.circle(10, 22, 6.5, 'k'); c.circle(10, 22, 3, 'Y')
    c.circle(24, 24, 4, 'k'); c.circle(24, 24, 1.5, 'Y')
    c.outline()


@icon('com.rosegardenmusic.rosegarden', ['rosegarden'], 'audio', 'Rosegarden')
def rosegarden(c):
    c.circle(16, 10, 7.5, 'R')
    c.bevel(['R'])
    c.arc(16, 10, 5, 3.5, 90, 360, '1')
    c.arc(17, 9, 2.5, 1, 0, 270, '1')
    c.rect(15, 17, 16, 28, '4')
    c.poly([(16, 22), (26, 17), (23, 24)], 'G')
    c.poly([(15, 25), (5, 20), (8, 27)], 'G')
    c.bevel(['G'])
    c.outline()


@icon('org.frescobaldi.Frescobaldi', ['frescobaldi'], 'audio', 'Frescobaldi')
def frescobaldi(c):
    # lily flower (LilyPond)
    c.poly([(16, 3), (20, 12), (16, 20), (12, 12)], 'W')
    c.poly([(3, 9), (13, 13), (16, 20), (8, 17)], 'w')
    c.poly([(29, 9), (19, 13), (16, 20), (24, 17)], 'w')
    c.bevel(['W', 'w'])
    c.vline(16, 9, 18, 'y')
    c.poly([(4, 24), (16, 20), (28, 24), (16, 28)], 'G')
    c.bevel(['G'])
    c.outline()


@icon('org.denemo.Denemo', ['denemo'], 'audio', 'Denemo')
def denemo(c):
    # staff with notes on a sheet
    c.rect(3, 6, 28, 26, 'W')
    c.bevel(['W'])
    for y in (10, 13, 16, 19, 22):
        c.hline(4, 27, y, 'S')
    for x, y in ((7, 18), (13, 15), (19, 12), (24, 18)):
        c.rect(x, y, x + 2, y + 1, 'G')
        c.vline(x + 2, y - 6, y, 'G')
    c.hline(15, 21, 6, 'G') if False else None
    c.outline()


@icon('org.tenacityaudio.Tenacity', ['tenacity'], 'audio', 'Tenacity')
def tenacity(c):
    # waveform clamped by a purple bracket
    c.rrect(3, 6, 28, 26, 'M', 3)
    c.bevel(['M'])
    c.rect(6, 9, 25, 23, '7')
    for x, h in zip(range(7, 25), (1, 3, 5, 3, 7, 11, 6, 9, 13, 8, 5, 10, 6, 3, 5, 2, 1, 1)):
        c.vline(x, 16 - h // 2, 16 + h // 2, 'm')
    c.outline()


@icon('ocenaudio', ['com.ocenaudio.ocenaudio'], 'audio', 'ocenaudio')
def ocenaudio(c):
    # ocean wave curl
    c.circle(16, 16, 13, 'C')
    c.bevel(['C'])
    c.arc(17, 18, 8, 4.5, 180, 450, 'W')
    c.poly([(3, 22), (29, 22), (28, 26), (4, 26)], 'B') if False else None
    c.rect(3, 22, 29, 30, 'B')
    c.ellipse(16, 16, 13, 13, 'C') if False else None
    for y in range(22, 32):
        for x in range(32):
            if c.get(x, y) == 'B' and math.hypot(x + .5 - 16, y + .5 - 16) > 13:
                c.px(x, y, '.')
    c.bevel(['B'])
    c.outline()


@icon('org.sonicvisualiser.SonicVisualiser', ['sonic-visualiser', 'sonicvisualiser'], 'audio', 'Sonic Visualiser')
def sonicvisualiser(c):
    # spectrogram window
    c.rect(3, 5, 28, 27, 'k')
    for x in range(5, 27):
        h = int(7 + 6 * math.sin(x / 3.0) + 3 * math.sin(x / 1.3))
        for y in range(25 - h, 26):
            d = 25 - y
            c.px(x, y, 'R' if d < 3 else 'O' if d < 6 else 'Y' if d < 10 else 'G' if d < 13 else 'C')
    c.rect(3, 5, 28, 6, 'S')
    c.outline()


@icon('com.giadamusic.Giada', ['giada'], 'audio', 'Giada')
def giada(c):
    # 3x3 loop pads, one lit
    c.rrect(3, 3, 28, 28, 'k', 2)
    for i in range(3):
        for j in range(3):
            x, y = 5 + i * 8, 5 + j * 8
            lit = (i, j) in ((1, 0), (0, 2), (2, 1))
            c.rect(x, y, x + 5, y + 5, 'R' if lit else 's')
            c.hline(x, x + 5, y, 'r' if lit else 'S')
    c.outline()


@icon('com.vcvrack.Rack', ['vcvrack', 'Rack', 'vcv-rack', 'rack'], 'audio', 'VCV Rack')
def vcvrack(c):
    # eurorack module with jacks and a patch cable
    c.rect(4, 3, 20, 28, 'w')
    c.bevel(['w'])
    c.px(5, 4, 'S'); c.px(5, 27, 'S'); c.px(19, 4, 'S'); c.px(19, 27, 'S')
    knob(c, 12, 9, 3.5, 'k', 'W', 30)
    for x, y in ((8, 17), (16, 17), (8, 23), (16, 23)):
        c.circle(x, y, 2, 'S'); c.px(x - 1, y - 1, 'k')
    c.line(16, 22, 27, 17, 'R', 2)
    c.line(27, 17, 25, 9, 'R', 2)
    c.outline()


@icon('surge-xt', ['org.surge-synthesizer.surge-xt', 'surge', 'Surge XT'], 'audio', 'Surge XT')
def surge(c):
    # sine wave in a dark disc, yellow accent
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'])
    for x in range(5, 27):
        y = int(16 - 6 * math.sin((x - 5) / 21 * 2 * math.pi))
        c.rect(x, y, x, y + 1, 'Y')
    c.outline()


@icon('vital', ['Vital', 'vital-synth'], 'audio', 'Vital')
def vital(c):
    # bold V
    c.poly([(3, 4), (11, 4), (16, 19), (21, 4), (29, 4), (20, 28), (12, 28)], 'w')
    c.bevel(['w'])
    c.poly([(11, 4), (16, 19), (14, 22)], 'S') if False else None
    c.outline()


@icon('studio.kx.distrho.Cardinal', ['cardinal', 'Cardinal'], 'audio', 'Cardinal')
def cardinal(c):
    # red cardinal bird with crest
    c.poly([(9, 3), (14, 8), (12, 10)], 'R')
    c.circle(13, 12, 5.5, 'R')
    c.ellipse(16, 19, 9, 7, 'R')
    c.poly([(22, 19), (29, 28), (24, 28), (19, 23)], '1')
    c.bevel(['R'])
    c.poly([(6, 11), (8, 9), (9, 13)], 'O')
    c.poly([(8, 10), (13, 10), (13, 14), (9, 15)], 'k')
    c.px(12, 11, 'W')
    c.ellipse(18, 19, 5, 3, '1')
    c.outline()


@icon('org.guitarix.Guitarix', ['guitarix', 'gx_head'], 'audio', 'Guitarix')
def guitarix(c):
    # amp head: grill + knobs
    c.rrect(3, 5, 28, 27, 'k', 2)
    c.bevel(['k'])
    c.rect(5, 7, 26, 12, 'Y')
    for x in (8, 13, 18, 23):
        knob(c, x, 9.5, 1.5, 'k', 'k')
    c.rect(5, 14, 26, 25, 'N')
    c.dither(5, 14, 26, 25, '8', 'N')
    c.rect(22, 3, 25, 4, 's') if False else None
    c.outline()


@icon('org.tuxguitar.TuxGuitar', ['tuxguitar'], 'audio', 'TuxGuitar')
def tuxguitar(c):
    # acoustic guitar diagonal
    c.line(17, 15, 25, 6, 'N', 3)
    c.rect(24, 3, 28, 6, '8')
    c.circle(10, 22, 6.5, 'O')
    c.circle(15, 16, 5, 'O')
    c.bevel(['O'])
    c.circle(12, 19, 2.5, 'k')
    c.line(8, 25, 11, 22, '2')
    c.outline()


@icon('cadence', ['cadence-jacksettings', 'claudia', 'catia'], 'audio', 'Cadence')
def cadence(c):
    # JACK: TRS plug
    c.rect(13, 3, 18, 5, 'w')
    c.rect(14, 6, 17, 8, 'k')
    c.rect(13, 9, 18, 12, 'w')
    c.rect(14, 13, 17, 13, 'k')
    c.rect(12, 14, 19, 17, 'w')
    c.bevel(['w'])
    c.rrect(10, 18, 21, 28, 'R', 1)
    c.bevel(['R'])
    for y in (20, 23, 26):
        c.hline(11, 20, y, '1')
    c.outline()


@icon('raysession', ['ray-session', 'patchance'], 'audio', 'RaySession')
def raysession(c):
    # sunburst
    for i in range(12):
        a = math.radians(i * 30)
        c.line(16, 16, round(16 + 11.5 * math.cos(a)), round(16 + 11.5 * math.sin(a)), 'O', 2)
    c.circle(16.5, 16.5, 7.5, 'Y')
    c.bevel(['Y'])
    c.outline()


@icon('org.rncbc.qjackctl', ['qjackctl'], 'audio', 'QjackCtl')
def qjackctl(c):
    # jack socket face
    c.circle(16, 16, 13, 'S')
    c.bevel(['S'])
    c.circle(16, 16, 9, 'w')
    c.circle(16, 16, 5, 'K')
    c.circle(16, 16, 2.5, 'k')
    c.poly([(16, 3), (19, 7), (13, 7)], 'R')
    c.outline()


@icon('noisetorch', ['NoiseTorch', 'noisetorch-bin'], 'audio', 'NoiseTorch')
def noisetorch(c):
    # flaming torch
    c.poly([(13, 14), (19, 14), (17, 29), (15, 29)], 'N')
    c.rect(12, 13, 20, 15, 's')
    c.poly([(16, 2), (22, 9), (20, 13), (12, 13), (10, 8), (13, 6)], 'O')
    c.poly([(16, 6), (19, 10), (17, 13), (14, 13), (13, 10)], 'Y')
    c.bevel(['N'])
    c.outline()


@icon('yoshimi', ['zynaddsubfx', 'zynaddsubfx-fltk', 'zynaddsubfx-ntk'], 'audio', 'Yoshimi / ZynAddSubFX')
def yoshimi(c):
    # keyboard synth with keys
    c.rect(3, 8, 28, 15, 'k')
    for x, col in ((6, 'R'), (11, 'Y'), (16, 'G'), (21, 'C')):
        knob(c, x + 1, 11.5, 1.8, col, 'k')
    c.rect(3, 16, 28, 24, 'W')
    for x in range(6, 28, 3):
        c.vline(x, 16, 24, 'S')
    for x in (5, 8, 14, 17, 20, 26):
        c.rect(x, 16, x + 1, 20, 'K')
    c.outline()


@icon('sooperlooper', ['slgui'], 'audio', 'SooperLooper')
def sooperlooper(c):
    # loop arrow around a record dot
    c.arc(16, 16, 13, 9.5, 300, 600, 'G')
    c.poly([(20, 3), (28, 9), (19, 12)], 'G')
    c.bevel(['G'])
    c.circle(16, 16, 5, 'R')
    c.px(14, 14, 'r')
    c.outline()


@icon('org.rncbc.qsynth', ['qsynth', 'fluidsynth'], 'audio', 'Qsynth')
def qsynth(c):
    # soundfont: font letter on a keyboard wave
    c.rrect(3, 4, 28, 27, 'C', 3)
    c.bevel(['C'])
    for x in range(5, 27):
        y = int(15 - 6 * math.sin((x - 5) / 21 * 2 * math.pi) * (1 if x % 2 else -0.3))
        c.px(x, y, 'W')
    c.rect(5, 21, 26, 25, 'W')
    for x in range(8, 26, 3):
        c.vline(x, 21, 25, 'S')
    c.outline()


@icon('com.adrienplazas.Metronome', ['metronome', 'gnome-metronome'], 'audio', 'Metronome')
def metronome(c):
    c.poly([(12, 3), (20, 3), (27, 28), (5, 28)], 'N')
    c.bevel(['N'])
    c.poly([(11, 8), (21, 8), (24, 21), (8, 21)], 'y')
    c.line(16, 23, 22, 5, 'k')
    c.rect(19, 10, 21, 12, 'S')
    c.rect(5, 23, 27, 28, '8')
    c.outline()


@icon('lingot', ['gxtuner', 'org.nongnu.lingot', 'guitar-tuner'], 'audio', 'Tuner')
def lingot(c):
    # tuning fork
    c.rect(9, 3, 12, 17, 'w'); c.rect(19, 3, 22, 17, 'w')
    c.arc(15.5, 17, 6.5, 3, 0, 180, 'w')
    c.rect(14, 23, 17, 28, 'w')
    c.bevel(['w'])
    for x in (4, 26):
        c.vline(x, 5, 11, 'C'); c.vline(x + (2 if x > 16 else -1), 7, 9, 'C')
    c.outline()


@icon('org.drumgizmo.DrumGizmo', ['drumgizmo'], 'audio', 'DrumGizmo')
def drumgizmo(c):
    # kick drum front with pedal
    c.circle(16, 15, 12, 'B')
    c.bevel(['B'])
    c.circle(16, 15, 9, 'W')
    c.circle(16, 15, 4, 'w')
    c.rect(13, 27, 18, 28, 's')
    c.rect(6, 25, 9, 28, 's'); c.rect(23, 25, 26, 28, 's')
    c.outline()


@icon('polyphone', ['io.github.davy7125.polyphone'], 'audio', 'Polyphone')
def polyphone(c):
    # tall waveform bars stacked over piano keys
    c.rect(3, 18, 28, 28, 'W')
    for x in range(6, 28, 3):
        c.vline(x, 18, 28, 'S')
    for x in (5, 8, 14, 17, 20, 26):
        c.rect(x, 18, x + 1, 23, 'K')
    for i, h in enumerate((5, 9, 12, 7, 13, 10, 6, 11)):
        x = 4 + i * 3 + (1 if i > 3 else 0)
        c.rect(x, 17 - h, x + 1, 17, 'O')
    c.outline()


@icon('dexed', ['com.asb2m10.Dexed', 'Dexed'], 'audio', 'Dexed')
def dexed(c):
    # FM operator panel: 6 numbered boxes
    c.rrect(3, 5, 28, 26, 'N', 1)
    c.bevel(['N'])
    for i in range(6):
        x, y = 5 + (i % 3) * 8, 8 + (i // 3) * 9
        c.rect(x, y, x + 5, y + 6, 'k')
        c.px(x + 2, y + 2, 'G'); c.px(x + 2, y + 3, 'G'); c.px(x + 2, y + 4, 'G')
    c.outline()
