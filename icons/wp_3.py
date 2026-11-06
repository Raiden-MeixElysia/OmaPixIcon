"""Writing, reading, notes, tasks and time tracking."""
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


def page(c, col='W', x0=5, y0=3, x1=26, y1=28, ear=6):
    c.poly([(x0, y0), (x1 - ear, y0), (x1 + 1, y0 + ear + 1), (x1 + 1, y1 + 1), (x0, y1 + 1)], col)
    c.bevel([col])
    c.poly([(x1 - ear, y0), (x1 + 1, y0 + ear + 1), (x1 - ear, y0 + ear + 1)], 'w' if col == 'W' else col)


def open_book(c, cover, pg='W', y0=7, y1=26):
    c.poly([(3, y0 + 2), (16, y0 + 4), (29, y0 + 2), (29, y1), (16, y1 + 2), (3, y1)], cover)
    c.bevel([cover])
    c.poly([(5, y0), (15, y0 + 2), (15, y1 - 1), (5, y1 - 3)], pg)
    c.poly([(17, y0 + 2), (27, y0), (27, y1 - 3), (17, y1 - 1)], pg)
    c.vline(16, y0 + 3, y1, 'S')


def pen(c, x0, y0, x1, y1, body, tip='y', w=3):
    c.line(x0, y0, x1, y1, body, w)


def checkmark(c, x, y, col='W'):
    g(c, x, y, """
        ..........##
        .........###
        ........###.
        ##.....###..
        ###...###...
        .###.###....
        ..#####.....
        ...###......
    """, col)


# ================================================================ writing

@icon('manuskript', ['ch.theologeek.Manuskript', 'manuskript-git'], 'office', 'Manuskript')
def manuskript(c):
    page(c, 'W', 4, 5, 21, 28)
    for y in (13, 16, 19, 22):
        c.hline(7, 17, y, 'S')
    # quill
    c.poly([(29, 3), (24, 5), (17, 14), (15, 21), (19, 16), (26, 9)], 'B')
    c.line(28, 4, 16, 19, '6')
    c.bevel(['B'])
    c.outline()


@icon('novelwriter', ['io.github.vkbo.novelWriter', 'novelWriter', 'novelwriter-git'], 'office', 'novelWriter')
def novelwriter(c):
    disc(c, '6')
    # fountain pen nib
    c.poly([(16, 5), (23, 13), (21, 21), (16, 27), (11, 21), (9, 13)], 'W')
    c.bevel(['W'])
    c.vline(16, 12, 26, '6')
    c.circle(16, 14, 1.5, '6')
    c.outline()


@icon('bibisco', ['com.bibisco.bibisco', 'bibisco-bin'], 'office', 'bibisco')
def bibisco(c):
    c.rrect(5, 3, 27, 28, 'R', 1)
    c.bevel(['R'])
    c.rect(5, 3, 7, 28, '1')
    c.rect(24, 6, 27, 26, 'W'); c.vline(27, 6, 26, 'w')
    g(c, 11, 9, """
        ###.....
        ###.....
        ###.....
        ######..
        #######.
        ###..###
        ###..###
        #######.
        ######..
    """)
    c.outline()


@icon('focuswriter', ['org.gottcode.FocusWriter'], 'office', 'FocusWriter')
def focuswriter(c):
    page(c, 'W', 4, 3, 22, 28)
    for y in (12, 15, 18):
        c.hline(7, 18, y, 'S')
    c.line(26, 6, 13, 22, 'k', 3)
    c.line(26, 6, 14, 21, 'B', 2)
    c.poly([(12, 23), (15, 25), (11, 27)], 'y')
    c.outline()


@icon('apostrophe', ['org.gnome.gitlab.somas.Apostrophe', 'apostrophe-git'], 'office', 'Apostrophe')
def apostrophe(c):
    page(c, 'W', 5, 3, 26, 28)
    c.circle(15.5, 13, 5, 'k')
    c.poly([(19, 14), (20, 18), (13, 25), (15, 18)], 'k')
    c.outline()


@icon('ghostwriter', ['org.kde.ghostwriter', 'io.github.wereturtle.ghostwriter'], 'office', 'ghostwriter')
def ghostwriter(c):
    c.ellipse(16, 13, 11, 10, 'W')
    c.rect(5, 13, 27, 24, 'W')
    for i, x in enumerate(range(5, 28, 6)):
        c.poly([(x, 24), (x + 3, 28), (x + 6, 24)], 'W')
    c.bevel(['W'])
    c.rect(11, 11, 13, 14, 'K'); c.rect(19, 11, 21, 14, 'K')
    c.rect(14, 18, 18, 19, 'S')
    c.outline()


@icon('abiword', ['com.abisource.AbiWord'], 'office', 'AbiWord')
def abiword(c):
    page(c, 'W', 4, 3, 25, 28)
    for y in (11, 14, 17, 20, 23):
        c.hline(8, 21, y, 'w')
    c.circle(21, 22, 7, 'B')
    c.bevel(['B'])
    ctext(c, 'A', 'W', 22, 1, 5, 21)
    c.outline()


@icon('gnumeric', ['org.gnome.Gnumeric'], 'office', 'Gnumeric')
def gnumeric(c):
    c.rect(3, 5, 28, 27, 'W')
    c.bevel(['W'])
    c.rect(3, 5, 28, 9, 'G')
    for x in (10, 17, 24):
        c.vline(x, 10, 26, 'w')
    for y in (13, 17, 21, 25):
        c.hline(4, 27, y, 'w')
    c.rect(11, 18, 16, 21, 'g')
    c.rect(3, 10, 9, 26, 'w')
    c.outline()


@icon('freeoffice-textmaker', ['textmaker', 'softmaker-freeoffice-textmaker', 'freeoffice', 'softmaker-freeoffice',
                               'softmaker-office'], 'office', 'SoftMaker FreeOffice')
def freeoffice(c):
    page(c, 'W', 5, 3, 26, 28)
    c.rect(5, 12, 27, 22, 'B')
    c.bevel(['B'])
    ctext(c, 'TM', 'W', 17, 1)
    c.outline()


# ================================================================ reading / PDFs / references

@icon('com.github.johnfactotum.Foliate', ['foliate'], 'office', 'Foliate')
def foliate(c):
    open_book(c, 'C')
    c.poly([(20, 7), (24, 6), (24, 16), (22, 14), (20, 16)], 'R')
    for y in (12, 15, 18):
        c.hline(7, 13, y, 'w')
    c.outline()


@icon('koodo-reader', ['io.github.troyeguo.koodo-reader', 'koodo-reader-bin', 'koodo-reader-appimage'], 'office',
      'Koodo Reader')
def koodo(c):
    c.rrect(5, 3, 27, 28, 'B', 2)
    c.bevel(['B'])
    c.rect(5, 3, 8, 28, '6')
    ctext(c, 'K', 'W', 15.5, 2, 5, 17.5)
    c.outline()


@icon('readest', ['com.bilingify.readest', 'readest-bin'], 'office', 'Readest')
def readest(c):
    c.rrect(3, 3, 28, 28, 'k', 5)
    c.bevel(['k'])
    c.poly([(7, 10), (16, 12), (16, 24), (7, 22)], 'W')
    c.poly([(16, 12), (25, 10), (25, 22), (16, 24)], 'w')
    c.outline()


@icon('thorium-reader', ['org.edrlab.thorium', 'thorium-reader-bin', 'EDRLab.ThoriumReader'], 'office',
      'Thorium Reader')
def thorium_reader(c):
    disc(c, 'B')
    c.poly([(7, 10), (16, 12), (16, 23), (7, 21)], 'W')
    c.poly([(16, 12), (25, 10), (25, 21), (16, 23)], 'w')
    c.rect(15, 6, 16, 9, 'Y'); c.rect(13, 7, 18, 8, 'Y')
    c.outline()


@icon('com.github.babluboy.bookworm', ['bookworm'], 'office', 'Bookworm')
def bookworm(c):
    c.rrect(3, 12, 22, 28, 'R', 1)
    c.bevel(['R'])
    c.rect(4, 25, 21, 27, 'W')
    # worm peeking out
    c.ellipse(23, 14, 5.5, 9, 'G')
    c.circle(22, 8, 5, 'G')
    c.bevel(['G'])
    c.rect(20, 6, 21, 7, 'K'); c.rect(24, 6, 25, 7, 'K')
    c.outline()


@icon('mendeleydesktop', ['mendeley', 'mendeley-reference-manager', 'com.elsevier.MendeleyDesktop',
                          'mendeley-desktop', 'mendeley-reference-manager-bin'], 'office', 'Mendeley')
def mendeley(c):
    disc(c, 'R')
    c.circle(16, 12, 3.5, 'W')
    c.circle(10, 19, 3.5, 'W')
    c.circle(22, 19, 3.5, 'W')
    c.ellipse(16, 21, 4, 3, 'W')
    c.rect(10, 15, 22, 20, 'W')
    c.circle(16, 12, 2, 'R')
    c.outline()


@icon('jabref', ['org.jabref.jabref', 'JabRef', 'jabref-bin'], 'office', 'JabRef')
def jabref(c):
    c.rrect(5, 3, 26, 28, 'M', 2)
    c.bevel(['M'])
    g(c, 10, 8, """
        ....######
        ....######
        ......##..
        ......##..
        ......##..
        ......##..
        ......##..
        ##....##..
        ##....##..
        .######...
        ..####....
    """)
    c.outline()


@icon('org.pwmt.zathura', ['zathura', 'zathura-pdf-mupdf', 'zathura-pdf-poppler'], 'office', 'zathura')
def zathura(c):
    page(c, 'W', 5, 3, 26, 28)
    c.rect(5, 3, 8, 28, 'k')
    g(c, 12, 11, """
        ##########
        ##########
        ......###.
        .....###..
        ....###...
        ...###....
        ..###.....
        .###......
        ##########
        ##########
    """, 'k')
    c.outline()


@icon('sioyek', ['com.github.ahrm.sioyek', 'sioyek-git', 'sioyek-appimage'], 'office', 'Sioyek')
def sioyek(c):
    page(c, 'W', 5, 3, 26, 28)
    c.ellipse(16, 17, 9, 5, 'k')
    c.ellipse(16, 17, 7.5, 3.8, 'W')
    c.circle(16, 17, 3, 'B')
    c.circle(16, 17, 1.2, 'k')
    c.outline()


@icon('com.github.jeromerobert.pdfarranger', ['pdfarranger'], 'office', 'PDF Arranger')
def pdfarranger(c):
    page(c, 'w', 3, 3, 17, 22, 4)
    page(c, 'W', 13, 9, 27, 28, 4)
    c.rect(15, 21, 26, 25, 'R')
    c.poly([(5, 25), (11, 25), (11, 22), (15, 26), (11, 29), (11, 27), (5, 27)], 'B')
    c.outline()


# ================================================================ notes

@icon('org.gnome.Gnote', ['gnote'], 'office', 'Gnote')
def gnote(c):
    c.poly([(4, 6), (28, 6), (28, 22), (22, 28), (4, 28)], 'Y')
    c.bevel(['Y'])
    c.poly([(22, 22), (28, 22), (22, 28)], '3')
    for y in (13, 17, 21):
        c.hline(8, 20, y, '3')
    c.circle(16, 6, 3, 'R')
    c.bevel(['R'])
    c.outline()


@icon('cherrytree', ['com.giuspen.cherrytree'], 'office', 'CherryTree')
def cherrytree(c):
    c.line(10, 19, 16, 7, 'G', 2); c.line(22, 19, 17, 7, 'G', 2)
    c.poly([(16, 6), (25, 3), (21, 9)], 'G')
    c.bevel(['G'])
    c.circle(9, 22, 6.5, 'R'); c.circle(22.5, 22, 6.5, 'R')
    c.bevel(['R'])
    c.pixels([(6, 19), (7, 18), (19, 19), (20, 18)], 'W')
    c.outline()


@icon('QOwnNotes', ['qownnotes', 'org.qownnotes.QOwnNotes', 'PBEK.QOwnNotes'], 'office', 'QOwnNotes')
def qownnotes(c):
    page(c, 'Y', 5, 3, 26, 28)
    c.ring(16, 16, 7, 4, 'k')
    c.line(19, 19, 23, 24, 'k', 2)
    c.outline()


@icon('zim', ['org.zim_wiki.Zim', 'zim-wiki'], 'office', 'Zim')
def zim(c):
    c.rrect(5, 3, 27, 28, 'O', 1)
    c.bevel(['O'])
    for y in range(6, 27, 4):
        c.rect(3, y, 6, y + 1, 'S')
    c.rect(10, 8, 24, 23, 'W')
    ctext(c, 'Z', 'k', 15.5, 2, 3, 17)
    c.outline()


# ================================================================ tasks

@icon('io.github.alainm23.planify', ['planify', 'com.github.alainm23.planner', 'planner'], 'office', 'Planify')
def planify(c):
    disc(c, 'B')
    c.circle(16, 16, 9, 'W')
    c.circle(16, 16, 7, 'B')
    checkmark(c, 10, 12)
    c.outline()


@icon('io.github.mrvladus.List', ['errands', 'io.github.mrvladus.Errands'], 'office', 'Errands')
def errands(c):
    c.rrect(5, 3, 26, 28, 'W', 2)
    c.bevel(['W'])
    for i, y in enumerate((8, 15, 22)):
        c.rrect(8, y, 12, y + 3, 'B' if i < 2 else 'S', 1)
        c.rect(15, y + 1, 23, y + 2, 'S')
    c.outline()


@icon('org.gnome.Todo', ['gnome-todo', 'endeavour', 'org.gnome.Todo.Devel'], 'office', 'Endeavour')
def endeavour(c):
    c.rrect(3, 4, 28, 28, 'b', 3)
    c.bevel(['b'])
    c.rect(6, 7, 25, 25, 'W')
    checkmark(c, 10, 11, 'G')
    c.outline()


@icon('asana', ['asana-webapp', 'asana.com', 'asana-desktop'], 'office', 'Asana')
def asana(c):
    c.circle(16, 10, 6, 'P')
    c.circle(9, 22, 6, 'P')
    c.circle(23, 22, 6, 'P')
    c.bevel(['P'])
    c.outline()


@icon('monday', ['monday-webapp', 'monday.com', 'monday-desktop'], 'office', 'monday.com')
def monday(c):
    c.line(4, 24, 9, 8, 'R', 5)
    c.line(12, 24, 17, 8, 'Y', 5)
    c.circle(25, 24.5, 4, 'G')
    c.bevel(['R', 'Y', 'G'], light=False)
    c.outline()


@icon('clickup', ['clickup-webapp', 'clickup-desktop', 'com.clickup.ClickUp'], 'office', 'ClickUp')
def clickup(c):
    c.poly([(4, 15), (16, 5), (28, 15), (24, 19), (16, 12), (8, 19)], 'M')
    c.arc(16, 15, 13, 9, 30, 150, 'C')
    c.bevel(['M', 'C'], light=False)
    c.outline()


@icon('jira', ['jira-webapp', 'atlassian-jira', 'jira-software'], 'office', 'Jira')
def jira(c):
    c.poly([(16, 3), (29, 16), (16, 29), (3, 16)], 'B')
    c.bevel(['B'])
    c.poly([(16, 9), (23, 16), (16, 23), (9, 16)], '6')
    c.poly([(16, 12), (20, 16), (16, 20), (12, 16)], 'b')
    c.outline()


@icon('confluence', ['confluence-webapp', 'atlassian-confluence'], 'office', 'Confluence')
def confluence(c):
    c.poly([(3, 22), (8, 15), (15, 18), (28, 23), (25, 29), (12, 24), (7, 26)], 'B')
    c.poly([(29, 10), (24, 17), (17, 14), (4, 9), (7, 3), (20, 8), (25, 6)], 'C')
    c.bevel(['B', 'C'])
    c.outline()


@icon('superproductivity', ['super-productivity', 'com.super_productivity.SuperProductivity',
                            'superproductivity-bin', 'super-productivity-bin'], 'office', 'Super Productivity')
def superproductivity(c):
    disc(c, 'C')
    c.ring(16, 16, 9, 6.5, 'W')
    c.poly([(16, 16), (16, 7), (24, 11)], 'W')
    checkmark(c, 10, 12, '5')
    c.outline()


@icon('motion', ['usemotion', 'motion-webapp', 'app.usemotion.com'], 'office', 'Motion')
def motion(c):
    c.rrect(3, 3, 28, 28, 'k', 6)
    c.bevel(['k'])
    c.poly([(8, 22), (12, 9), (16, 17), (20, 9), (24, 22), (21, 22), (19.5, 16), (16, 23), (12.5, 16), (11, 22)], 'W')
    c.outline()


@icon('sunsama', ['sunsama-webapp', 'sunsama-desktop'], 'office', 'Sunsama')
def sunsama(c):
    c.ellipse(16, 22, 12, 6, 'O')
    c.circle(16, 16, 9, 'Y')
    c.rect(3, 22, 29, 29, '.')
    c.rrect(3, 22, 28, 26, 'B', 1)
    c.bevel(['Y', 'B'])
    c.outline()


# ================================================================ time

@icon('toggl-track', ['toggldesktop', 'com.toggl.TogglDesktop', 'toggl', 'toggl-track-bin', 'toggl-webapp'],
      'office', 'Toggl Track')
def toggl(c):
    disc(c, 'M')
    c.arc(16, 17, 8.5, 6, 300, 240, 'W')
    c.rect(15, 6, 17, 16, 'W')
    c.outline()


@icon('clockify', ['clockify-desktop', 'clockify-webapp', 'com.clockify.Clockify'], 'office', 'Clockify')
def clockify(c):
    c.arc(16, 16, 13, 8.5, 45, 315, 'B')
    c.poly([(20, 9), (26, 4), (28, 7), (23, 12)], 'B')
    c.poly([(20, 23), (26, 28), (28, 25), (23, 20)], 'C')
    c.bevel(['B', 'C'])
    c.circle(16, 16, 3, 'C')
    c.outline()


@icon('org.gnome.Pomodoro', ['gnome-pomodoro', 'pomodoro'], 'office', 'Pomodoro')
def gnome_pomodoro(c):
    c.ellipse(16, 18, 13, 11, 'R')
    c.bevel(['R'])
    c.poly([(16, 9), (9, 5), (13, 9), (8, 10), (14, 11), (16, 12), (18, 11), (24, 10), (19, 9), (23, 5)], 'G')
    c.vline(16, 4, 9, '4')
    c.pixels([(8, 14), (9, 13), (10, 13)], 'r')
    c.outline()


@icon('org.gnome.Solanum', ['solanum'], 'office', 'Solanum')
def solanum(c):
    disc(c, 'R')
    c.circle(16, 17, 8.5, 'W')
    c.poly([(16, 4), (11, 2.5), (13, 6), (19, 6), (21, 2.5)], 'G')
    c.vline(16, 11, 17, 'k'); c.hline(16, 20, 17, 'k')
    c.outline()


@icon('io.github.diegoivanme.flowtime', ['flowtime'], 'office', 'Flowtime')
def flowtime(c):
    # hourglass
    c.rect(6, 3, 26, 5, 'N'); c.rect(6, 26, 26, 28, 'N')
    c.poly([(8, 6), (24, 6), (24, 8), (17, 15.5), (17, 16.5), (24, 23), (24, 25), (8, 25), (8, 23), (15, 16.5),
            (15, 15.5), (8, 8)], 'c')
    c.bevel(['N'])
    c.poly([(10, 9), (22, 9), (16, 15)], 'Y')
    c.poly([(16, 20), (22, 25), (10, 25)], 'Y')
    c.vline(16, 16, 20, 'Y')
    c.outline()


# ================================================================ more web productivity

@icon('airtable', ['airtable-webapp', 'airtable.com'], 'office', 'Airtable')
def airtable(c):
    c.poly([(16, 3), (29, 8), (16, 13), (3, 8)], 'Y')
    c.poly([(17, 15), (29, 10), (29, 23), (17, 28)], 'C')
    c.poly([(3, 11), (15, 16), (15, 27), (3, 22)], 'R')
    c.bevel(['Y', 'C', 'R'], light=False)
    c.outline()


@icon('deepl', ['deepl-webapp', 'deepl-desktop', 'com.deepl.DeepL', 'deepl-linux', 'deepl.com'], 'office', 'DeepL')
def deepl(c):
    c.poly([(16, 3), (28, 9), (28, 22), (17, 28), (14, 29), (14, 27), (4, 22), (4, 9)], '6')
    c.bevel(['6'])
    c.line(11, 11, 20, 15, 'W'); c.line(11, 20, 20, 15, 'W')
    for x, y in ((11, 11), (11, 20), (20, 15)):
        c.circle(x + .5, y + .5, 2.2, 'W')
    c.outline()


@icon('grammarly', ['grammarly-webapp', 'grammarly-desktop'], 'office', 'Grammarly')
def grammarly(c):
    disc(c, 'G')
    c.arc(16, 16, 8.5, 5.5, 30, 330, 'W')
    c.rect(16, 15, 24, 17, 'W')
    c.outline()


@icon('loom', ['loom-webapp', 'loom-desktop', 'loom.com'], 'office', 'Loom')
def loom(c):
    for i in range(8):
        a = math.radians(i * 45)
        c.line(15 + 3 * math.cos(a), 15 + 3 * math.sin(a), 15 + 11 * math.cos(a), 15 + 11 * math.sin(a), 'M', 3)
    c.circle(16.5, 16.5, 5.5, 'M')
    c.bevel(['M'])
    c.circle(16.5, 16.5, 3, 'W')
    c.outline()


@icon('habitica', ['habitica-webapp', 'habitica.com'], 'office', 'Habitica')
def habitica(c):
    c.poly([(4, 4), (28, 4), (28, 17), (16, 29), (4, 17)], 'M')
    c.bevel(['M'])
    c.poly([(16, 7), (18, 13), (24, 13), (19, 17), (21, 23), (16, 19), (11, 23), (13, 17), (8, 13), (14, 13)], 'Y')
    c.outline()


@icon('vikunja', ['vikunja-desktop', 'io.vikunja.Vikunja', 'vikunja-webapp'], 'office', 'Vikunja')
def vikunja(c):
    c.rrect(3, 3, 28, 28, 'B', 4)
    c.bevel(['B'])
    for y in (8, 14, 20):
        c.rect(7, y, 10, y + 3, 'W')
        c.rect(13, y + 1, 24, y + 2, 'b')
    c.line(7, 10, 8, 11, 'B'); c.line(8, 11, 10, 8, 'B')
    c.outline()


@icon('heptabase', ['heptabase-webapp', 'heptabase-bin', 'Heptabase'], 'office', 'Heptabase')
def heptabase(c):
    pts = [(16 + 13 * math.cos(math.radians(-90 + i * 360 / 7)), 16.5 + 13 * math.sin(math.radians(-90 + i * 360 / 7)))
           for i in range(7)]
    c.poly(pts, '6')
    c.bevel(['6'])
    c.rrect(9, 10, 17, 16, 'W', 1); c.rrect(15, 18, 23, 24, 'W', 1)
    c.line(13, 16, 19, 18, 'b')
    c.outline()


@icon('capacities', ['capacities-webapp', 'capacities-bin', 'Capacities'], 'office', 'Capacities')
def capacities(c):
    c.rrect(3, 3, 28, 28, 'k', 5)
    c.bevel(['k'])
    c.poly([(16, 7), (24, 11), (16, 15), (8, 11)], 'W')
    c.poly([(8, 12), (15, 16), (15, 25), (8, 21)], 'w')
    c.poly([(17, 16), (24, 12), (24, 21), (17, 25)], 'S')
    c.outline()
