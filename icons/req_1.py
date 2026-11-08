"""Icon requests from GitHub issues (#2: edneymatias)."""
from pix import icon


@icon('ai.storyteller.photocraft', ['photocraft', 'photocraft-bin', 'PhotoCraft'], 'graphics', 'PhotoCraft')
def photocraft(c):
    # white kitsune head on a blue disc, three tails fanning behind
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.poly([(7, 6), (12, 12), (8, 14)], 'W')          # left ear
    c.poly([(25, 6), (20, 12), (24, 14)], 'W')        # right ear
    c.poly([(8, 11), (24, 11), (24, 17), (16, 27), (8, 17)], 'W')
    c.poly([(9, 8), (11, 11), (9, 12)], 'p')
    c.poly([(23, 8), (21, 11), (23, 12)], 'p')
    c.rect(11, 15, 13, 16, 'K'); c.rect(19, 15, 21, 16, 'K')
    c.px(12, 15, 'b'); c.px(20, 15, 'b')
    c.rect(15, 23, 16, 24, 'K')
    c.hline(10, 13, 19, 'w'); c.hline(18, 21, 19, 'w')
    c.outline()


@icon('dbx', ['dbx-bin', 'DBX', 'io.github.dbx'], 'dev', 'DBX')
def dbx(c):
    # stacked database discs with a violet X cutting through
    for y in (19, 12, 5):
        c.ellipse(12, y + 6, 9, 3.5, '6')
        c.rect(3, y + 3, 20, y + 6, 'B')
        c.ellipse(12, y + 3, 9, 3.5, 'B')
        if y != 19:
            c.arc(12, y + 6, 9, 7.8, 20, 160, 'K')
    c.ellipse(12, 8, 9, 3.5, 'b')
    c.bevel(['B'], dark=False)
    c.line(18, 11, 26, 27, 'M', 3)
    c.line(26, 11, 18, 27, 'm', 3)
    c.outline()


@icon('dens-odontologia', ['dens', 'app.oiana.com.br', 'oiana'], 'web', 'Dens Odontologia')
def dens(c):
    # pink pulse disc with a white lightning bolt
    c.circle(16, 16, 13, 'P')
    c.ring(16, 16, 13, 11, 'p')
    c.bevel(['P'])
    c.poly([(18, 5), (9, 18), (15, 18), (13, 27), (23, 13), (17, 13), (20, 5)], 'W')
    c.outline()


@icon('f1multiviewer', ['f1multiviewer-bin', 'multiviewer', 'multiviewer-for-f1', 'MultiViewer for F1'],
      'media', 'MultiViewer for F1')
def f1mv(c):
    # red race tile with the white "MV" brushstroke
    c.rrect(3, 5, 28, 26, 'R', 3)
    c.bevel(['R'])
    pts = [(7, 21), (10, 11), (13, 19), (16, 11), (19, 19), (24, 9)]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        c.line(x0, y0, x1, y1, 'W', 2)
    c.hline(5, 26, 24, '1')
    c.outline()


@icon('herdr-gpui', ['herdr', 'so.pen.herdr-gpui', 'Herdr'], 'dev', 'Herdr')
def herdr(c):
    # ram's head (a herder's flock) on a cream disc
    c.circle(16, 16, 13, 'W')
    c.bevel(['W'])
    c.poly([(7, 12), (17, 9), (24, 12), (24, 25), (13, 25), (11, 19), (6, 18)], 'k')
    c.circle(19, 14, 4.5, 'S')
    c.circle(19, 14, 2.5, 'k')
    c.px(19, 14, 'S')
    c.rect(10, 13, 11, 13, 'W')     # eye
    c.hline(7, 9, 16, 'S')           # muzzle
    c.outline()


@icon('ichatr', ['app.ichatr.com.br', 'ichatr-webapp'], 'chat', 'iChatr')
def ichatr(c):
    # round blue chat bubble with a sharp lower-right tail
    c.circle(15, 15, 12, 'B')
    c.rect(15, 15, 27, 27, 'B')
    c.rrect(15, 15, 27, 27, 'B', 0)
    c.bevel(['B'])
    c.ellipse(11, 9, 3, 1.5, 'b')
    c.rect(9, 14, 11, 16, 'W'); c.rect(14, 14, 16, 16, 'W'); c.rect(19, 14, 21, 16, 'W')
    c.outline()


@icon('integrador', ['integrador.dentaluni.com.br', 'dentaluni'], 'web', 'Integrador')
def integrador(c):
    # wine-red tile with a white infinity loop
    c.rrect(3, 5, 28, 26, 'R', 2)
    c.replace('R', '1')
    c.rect(3, 5, 28, 6, 'R')
    c.ring(11, 16, 6, 3, 'W')
    c.ring(21, 16, 6, 3, 'W')
    c.rect(15, 14, 17, 18, '1')
    c.line(14, 19, 18, 13, 'W', 2)
    c.px(12, 21, '1')
    c.outline()


@icon('n8n', ['n8n-dentaluni', 'n8n-ichatr', 'n8n-desktop', 'n8n-webapp', 'n8n.io', 'n8n-cloud'], 'dev', 'n8n')
def n8n(c):
    # workflow: three chained nodes branching into two
    c.line(6, 16, 20, 16, 'P', 2)
    c.line(18, 16, 23, 9, 'P', 2)
    c.line(18, 16, 23, 23, 'P', 2)
    for x, y in ((6, 16.5), (13.5, 16.5), (24, 9), (24, 24)):
        c.circle(x, y, 3.5, 'P')
        c.circle(x, y, 1.5, 'W')
    c.bevel(['P'])
    c.outline()


@icon('chatwoot', ['chatwoot-desktop', 'app.chatwoot.com', 'chatwoot-webapp'], 'chat', 'Chatwoot')
def chatwoot(c):
    # blue disc holding a white bubble whose tail points down-left
    c.circle(16, 16, 13, 'B')
    c.bevel(['B'])
    c.circle(16.5, 15, 7.5, 'W')
    c.poly([(9, 17), (14, 21), (8, 24)], 'W')
    c.hline(13, 19, 14, 'w'); c.hline(13, 17, 17, 'w')
    c.outline()


@icon('omaland', ['bobbynicholas.omaland', 'omarchy-omaland'], 'omarchy', 'Omaland')
def omaland(c):
    # Omarchy window with live-preview bars and a settings gear
    c.rrect(3, 4, 26, 23, 'k', 2)
    c.rect(3, 4, 26, 7, 'A')
    c.px(5, 5, 'a'); c.px(7, 5, 'a')
    c.rect(6, 10, 15, 16, '0')
    c.frame(6, 10, 15, 16, 'A')
    c.hline(18, 23, 11, 's'); c.hline(18, 22, 14, 's'); c.hline(6, 14, 20, 's')
    # gear badge, lower right
    for a, b in ((0, -6), (0, 6), (-6, 0), (6, 0), (-4, -4), (4, 4), (-4, 4), (4, -4)):
        c.circle(22 + a * .8, 22 + b * .8, 1.8, 'S')
    c.circle(22, 22, 4.5, 'S')
    c.bevel(['S'])
    c.circle(22, 22, 2, 'k')
    c.outline()


@icon('org.vinegarhq.Sober', ['sober', 'Sober', 'auto_sober', 'autosober', 'roblox', 'vinegar',
                              'org.vinegarhq.Vinegar'], 'games', 'Sober')
def sober(c):
    # tilted green block with a square window (Roblox-style)
    c.poly([(9, 2.5), (29.5, 8), (23, 29.5), (2.5, 24)], 'G')
    c.bevel(['G'])
    c.poly([(14.5, 11), (21, 13), (19.5, 19.5), (13, 17.5)], '4')
    c.poly([(9, 2.5), (29.5, 8), (29, 10), (8.5, 4.5)], 'g')
    c.outline()


@icon('rawmakase', ['rawmakase-bin', 'RAWmakase'], 'photo', 'RAWmakase')
def rawmakase(c):
    # a maki roll: nori ring, rice, and a salmon centre shaped like an aperture
    c.circle(16, 16, 13, 'k')
    c.ring(16, 16, 13, 12, 's')
    c.circle(16, 16, 10, 'W')
    c.bevel(['W'], dark=False)
    c.circle(16, 16, 6, 'O')
    for a in range(0, 360, 60):
        c.arc(16, 16, 6, 3, a, a + 22, 'o')
    c.circle(16, 16, 2, '2')
    c.outline()


@icon('startdrive', ['io.github.bmaltais.startdrive', 'StartDrive'], 'cloud', 'StartDrive')
def startdrive(c):
    # lavender cloud with an upload arrow
    c.circle(11, 18, 7, 'm')
    c.circle(18, 13, 8.5, 'm')
    c.circle(24, 19, 5.5, 'm')
    c.rect(6, 19, 26, 24, 'm')
    c.rrect(5, 16, 28, 24, 'm', 3)
    c.bevel(['m'])
    c.rect(16, 13, 17, 22, 'k')
    c.poly([(12.5, 17), (16.5, 11.5), (20.5, 17)], 'k')
    c.outline()


@icon('zapfast', ['zapfast-bin', 'ZapFast'], 'chat', 'ZapFast')
def zapfast(c):
    # green ring with a dark speech bubble inside (a fast WhatsApp client)
    c.circle(16, 16, 13, 'G')
    c.bevel(['G'])
    c.circle(16, 15.5, 8, 'k')
    c.circle(16, 15.5, 6, '4')
    c.poly([(9, 19), (12, 22), (7, 25)], 'k')
    c.poly([(19, 9), (14, 16), (17, 16), (14, 22), (20, 14), (17, 14)], 'y')
    c.outline()


@icon('io.github.lgse.Strata', ['strata', 'Strata'], 'utility', 'Strata')
def strata(c):
    # hexagonal "S" made of two folded layers
    c.poly([(16, 2.5), (28, 9), (28, 23), (16, 29.5), (4, 23), (4, 9)], 'W')
    c.bevel(['W'])
    c.poly([(16, 7), (24, 11.5), (24, 15), (12, 15), (12, 13), (16, 11), (20, 13), (20, 12.5), (16, 10.3),
            (8, 14.5), (8, 11.5)], 'k')
    c.poly([(16, 25), (8, 20.5), (8, 17), (20, 17), (20, 19), (16, 21), (12, 19), (12, 19.5), (16, 21.7),
            (24, 17.5), (24, 20.5)], 'k')
    c.outline()


# ---- #4: Raiden-MeixElysia

@icon('com.zacharyzhang.elyterminal', ['elyterminal', 'ely-terminal', 'ELYTerminal'], 'dev', 'ELYTerminal')
def elyterminal(c):
    # pink-haired girl peeking over a terminal she holds up
    c.circle(16, 10.5, 8, 'P')                  # hair
    c.rect(7, 10, 10, 22, 'P'); c.rect(22, 10, 25, 22, 'P')   # side locks
    c.rect(10, 9, 22, 17, 'p')                  # face
    c.rect(10, 6, 22, 9, 'P')                   # fringe
    c.px(12, 9, 'P'); c.px(16, 9, 'P'); c.px(20, 9, 'P')
    c.rect(12, 12, 13, 14, '7'); c.rect(19, 12, 20, 14, '7')  # eyes
    c.px(12, 12, 'W'); c.px(19, 12, 'W')
    c.px(11, 15, 'r'); c.px(21, 15, 'r')        # blush
    c.px(21, 6, 'Y'); c.px(22, 7, 'Y')          # hair clip
    c.bevel(['P'])
    c.rrect(6, 17, 26, 27, 'k', 1)              # terminal
    c.frame(6, 17, 26, 27, 'K')
    c.sprite(9, 20, """
        P.....
        .P....
        P..PPP
    """)
    c.rect(5, 19, 6, 21, 'p'); c.rect(26, 19, 27, 21, 'p')    # hands
    c.outline()


@icon('hplip', ['hp-toolbox', 'hp_logo', 'hplip-gui', 'hp-device-manager', 'HP Device Manager'],
      'system', 'HP Device Manager')
def hplip(c):
    # blue globe with the italic white "hp"
    c.circle(16, 16, 13, 'B')
    c.ring(16, 16, 13, 11.5, '6')
    c.bevel(['B'])
    c.ellipse(11, 9, 5, 2, 'b')
    c.poly([(10, 8), (13, 8), (9, 25), (6, 25)], 'W')          # h stem
    c.poly([(11, 15), (17, 15), (15, 23), (12, 23), (13.5, 17.5), (10.5, 17.5)], 'W')
    c.poly([(19, 13), (22, 13), (18, 29), (15, 29)], 'W')      # p stem
    c.poly([(20, 15), (26, 15), (24, 23), (17, 23), (18, 20.5), (21.5, 20.5), (22.5, 17.5), (19.5, 17.5)], 'W')
    c.outline()


# ---- #5: Raiden-MeixElysia

@icon('cindy', ['com.xd.cindy', 'com.xd.cindy.user', 'com.xd.cindy.user.h69297e92b23bcb60', 'Cindy',
                'cindy-user'], 'dev', 'Cindy')
def cindy(c):
    # dark-haired girl on a red disc, black cat peeking from the lower left
    c.circle(16, 16, 13, 'R')
    c.bevel(['R'])
    c.circle(17, 12.5, 8.5, 'k')                # hair crown
    c.rect(9, 12, 25, 23, 'k')                  # hair falling to the shoulders
    c.poly([(24, 8), (28.5, 13), (27, 21), (25, 23)], 'k')   # windswept strands
    c.rrect(12, 11, 22, 21, 'p', 2)             # face
    c.hline(13, 21, 21, 'k'); c.hline(14, 20, 21, 'p')       # chin
    c.rect(11, 8, 23, 11, 'k')                  # fringe
    c.pixels([(13, 12), (16, 12), (17, 12), (20, 12), (22, 12), (22, 13)], 'k')
    c.pixels([(15, 6), (16, 6), (17, 6), (18, 7), (19, 7), (24, 10), (25, 11), (26, 13)], '6')  # blue sheen
    c.rect(13, 14, 15, 16, 'O'); c.rect(18, 14, 20, 16, 'O')  # amber eyes
    c.px(15, 15, 'k'); c.px(20, 15, 'k')
    c.px(13, 14, 'W'); c.px(18, 14, 'W')
    c.px(13, 18, 'r'); c.px(20, 18, 'r')        # blush
    c.hline(16, 17, 19, '9')                    # mouth
    c.rect(15, 22, 18, 23, 'p')                 # neck
    c.rrect(10, 24, 26, 28, 'W', 2)             # sweater
    c.hline(11, 25, 27, 'w')
    # black cat on her shoulder
    c.rrect(3, 20, 12, 27, 'K', 2)
    c.poly([(3.5, 21.5), (4, 16.5), (7.5, 20)], 'K')
    c.poly([(8, 20), (11.5, 16.5), (12, 21.5)], 'K')
    c.rect(5, 23, 6, 24, 'Y'); c.rect(9, 23, 10, 24, 'Y')
    c.px(5, 23, 'W'); c.px(9, 23, 'W')
    c.hline(4, 11, 26, 'R')                     # red collar
    c.px(7, 27, 'Y')
    c.outline()


# ---- #6: Raiden-MeixElysia

@icon('alma', ['Alma', 'alma-native', 'alma-desktop', 'alma.now', 'com.yetone.alma'], 'ai', 'Alma')
def alma(c):
    # ink line-art manga girl on a white tile: bob haircut, leaf clip, sailor collar
    c.rrect(3, 3, 28, 28, 'W', 4)
    c.bevel(['W'])
    # hair: ink silhouette, soft grey fill, two strand lines
    c.circle(16, 14.5, 9, 'K'); c.rect(7, 14, 25, 24, 'K')
    c.circle(16, 14.5, 8, 'w'); c.rect(8, 14, 24, 23, 'w')
    c.line(15, 7, 12, 11, 'K'); c.line(18, 7, 21, 11, 'K')
    c.rect(8, 21, 9, 23, 'K'); c.rect(23, 21, 24, 23, 'K')   # shadowed ends of the bob
    # face with a jagged fringe
    c.rrect(11, 12, 21, 23, 'W', 2)
    c.vline(10, 15, 22, 'K'); c.vline(22, 15, 22, 'K')
    c.pixels([(11, 12), (11, 13), (12, 12), (14, 12), (14, 13), (15, 12), (17, 12), (18, 12), (18, 13),
              (20, 12), (21, 12), (21, 13)], 'w')
    c.pixels([(11, 14), (12, 13), (13, 13), (15, 13), (16, 13), (17, 13), (19, 13), (20, 13), (21, 14)], 'K')
    # big eyes with a highlight
    for x in (12, 18):
        c.rect(x, 15, x + 2, 18, 'K')
        c.px(x, 15, 'W'); c.px(x + 1, 18, 'S')
    c.px(16, 20, 'K')                           # mouth
    c.hline(13, 19, 23, 'w')                    # jaw shadow
    # neck and sailor collar
    c.vline(14, 23, 25, 'K'); c.vline(18, 23, 25, 'K')
    c.poly([(13, 25), (19.5, 25), (16, 28.5)], 'K')
    c.line(9, 28, 13, 25, 'K'); c.line(23, 28, 19, 25, 'K')
    # green leaf clip on her left
    c.sprite(20, 7, """
        .G.G.
        GgGgG
        .GgG.
        ..G..
    """)
    c.outline()
