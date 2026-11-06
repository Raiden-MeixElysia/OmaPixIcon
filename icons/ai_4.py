"""API clients, database GUIs and programming languages / runtimes as app icons."""
import math
from pix import icon

DEV = 'dev'


def _db(c, col, x0=6, x1=25, y0=4, y1=27, bands=3):
    """Stacked database cylinder."""
    cx, rx = (x0 + x1 + 1) / 2, (x1 - x0 + 1) / 2
    c.rect(x0, y0 + 3, x1, y1 - 3, col)
    c.ellipse(cx, y1 - 2.5, rx, 3, col)
    c.bevel([col])
    c.ellipse(cx, y0 + 3.5, rx, 3, LIGHT_OF[col])
    h = (y1 - y0 - 6) / bands
    dark = DARK_OF[col]
    for i in range(1, bands):
        y = y0 + 3.5 + h * i
        for x in range(x0, x1 + 1):
            dy = 3 * math.sqrt(max(0, 1 - ((x + .5 - cx) / rx) ** 2))
            c.px(x, int(y + dy), dark)


LIGHT_OF = {'B': 'b', 'R': 'r', 'G': 'g', 'C': 'c', 'O': 'o', 'M': 'm', 'S': 'w', 'Y': 'y'}
DARK_OF = {'B': '6', 'R': '1', 'G': '4', 'C': '5', 'O': '2', 'M': '7', 'S': 's', 'Y': '3'}


def _glass(c, x, y, col='W'):
    """Small magnifying glass overlay (lens centre x,y)."""
    c.line(x + 3, y + 3, x + 7, y + 7, 'k', 2)
    c.circle(x + .5, y + .5, 4.5, 'K')
    c.circle(x + .5, y + .5, 3.5, col)


# ====================================================================== API clients

@icon('hoppscotch', ['io.hoppscotch.Hoppscotch', 'hoppscotch-bin', 'Hoppscotch', 'hoppscotch-desktop'], DEV,
      'Hoppscotch')
def hoppscotch(c):
    # green hopping blob with antennae
    c.line(11, 9, 8, 3, 'G', 2); c.line(20, 9, 23, 3, 'G', 2)
    c.ellipse(16, 18, 13, 10, 'G')
    c.bevel(['G'])
    c.circle(11, 16, 3, 'W'); c.circle(21, 16, 3, 'W')
    c.rect(11, 16, 12, 17, 'K'); c.rect(21, 16, 22, 17, 'K')
    c.hline(13, 18, 22, '4')
    c.outline()


@icon('httpie', ['httpie-desktop', 'io.httpie.Httpie', 'HTTPie', 'httpie-desktop-bin'], DEV, 'HTTPie')
def httpie(c):
    # pie with a slice out
    c.circle(16, 16, 13, 'G')
    c.bevel(['G'])
    c.ring(16, 16, 13, 10.5, 'O')
    c.poly([(16, 16), (31, 4), (31, 16)], '.')
    c.line(16, 16, 25, 9, '4')
    c.line(16, 16, 26, 16, '4')
    c.outline()


@icon('yaak', ['yaak-app', 'app.yaak.Yaak', 'Yaak', 'yaak-bin'], DEV, 'Yaak')
def yaak(c):
    # shaggy yak head with horns
    c.poly([(3, 5), (5, 11), (10, 11), (7, 8)], 'w')
    c.poly([(29, 5), (27, 11), (22, 11), (25, 8)], 'w')
    c.rrect(6, 9, 25, 24, 'N', 5)
    c.rrect(10, 19, 21, 28, 'n', 3)
    c.bevel(['N', 'n', 'w'])
    c.dither(7, 9, 24, 12, 'N', '8', only='N')
    c.rect(10, 14, 11, 15, 'K'); c.rect(20, 14, 21, 15, 'K')
    c.rect(13, 24, 14, 25, '8'); c.rect(17, 24, 18, 25, '8')
    c.outline()


@icon('insomnium', ['insomnium-bin', 'Insomnium', 'insomnium-appimage'], DEV, 'Insomnium')
def insomnium(c):
    c.circle(16, 16, 13, '6')
    c.bevel(['6'], dark=False)
    c.circle(15, 16, 8, 'y')
    c.circle(19, 13, 7, '6')
    for x, y in ((22, 21), (25, 17), (20, 8)):
        c.px(x, y, 'W')
    c.outline()


@icon('mqtt-explorer', ['MQTT-Explorer', 'mqtt-explorer-bin', 'mqttexplorer'], DEV, 'MQTT Explorer')
def mqtt_explorer(c):
    # node tree
    c.vline(9, 8, 24, 'M'); c.vline(10, 8, 24, 'M')
    for y in (15, 23):
        c.hline(9, 20, y, 'M'); c.hline(9, 20, y + 1, 'M')
    for x, y, col in ((9.5, 6.5, 'M'), (21, 15.5, 'C'), (21, 23.5, 'P')):
        c.circle(x, y, 4, col)
    c.bevel(['M', 'C', 'P'])
    c.outline()


# ====================================================================== databases

@icon('redisinsight', ['redis-insight', 'RedisInsight', 'com.redis.RedisInsight', 'redisinsight-bin',
                       'redis-insight-bin'], DEV, 'Redis Insight')
def redisinsight(c):
    for i, y in enumerate((18, 12, 6)):
        c.poly([(3, y + 3), (14, y - 1), (25, y + 3), (14, y + 7)], 'R' if i % 2 == 0 else '1')
        c.poly([(3, y + 3), (14, y + 7), (25, y + 3), (25, y + 5), (14, y + 9), (3, y + 5)], '1')
    c.poly([(3, 9), (14, 5), (25, 9), (14, 13)], 'r')
    _glass(c, 19, 19, 'W')
    c.outline()


@icon('another-redis-desktop-manager', ['another-redis-desktop-manager-bin', 'ardm', 'AnotherRedisDesktopManager'],
      DEV, 'Another Redis Desktop Manager')
def ardm(c):
    _db(c, 'R', 4, 23, 3, 27)
    c.poly([(21, 18), (28, 18), (28, 21), (25, 21), (25, 23), (23, 23), (23, 21)], 'Y')
    c.circle(21, 19.5, 4, 'Y')
    c.circle(20, 19.5, 1.5, 'k')
    c.outline()


@icon('redis', ['redis-server', 'redis-cli', 'valkey', 'valkey-server'], DEV, 'Redis')
def redis(c):
    for y in (19, 13, 7):
        c.poly([(3, y + 4), (16, y - 1), (29, y + 4), (16, y + 9)], 'R')
        c.poly([(3, y + 4), (16, y + 9), (29, y + 4), (29, y + 6), (16, y + 11), (3, y + 6)], '1')
    c.poly([(3, 11), (16, 6), (29, 11), (16, 16)], 'R')
    c.poly([(11, 10), (16, 8), (21, 10), (16, 12)], 'W')
    c.outline()


@icon('tableplus', ['TablePlus', 'tableplus-bin', 'com.tinyapp.TablePlus'], DEV, 'TablePlus')
def tableplus(c):
    c.rect(3, 5, 24, 25, 'W')
    c.rect(3, 5, 24, 9, 'O')
    c.bevel(['O'])
    for x in (10, 17):
        c.vline(x, 10, 25, 'S')
    for y in (14, 19):
        c.hline(4, 23, y, 'S')
    c.circle(22, 22, 6.5, 'Y')
    c.bevel(['Y'])
    c.rect(21, 18, 22, 25, 'K'); c.rect(18, 21, 25, 22, 'K')
    c.outline()


@icon('antares', ['antares-sql', 'it.fabiodistasio.AntaresSQL', 'antares-bin', 'AntaresSQL'], DEV, 'Antares SQL')
def antares(c):
    c.poly([(16, 2), (19, 12), (29, 16), (19, 20), (16, 30), (13, 20), (3, 16), (13, 12)], 'R')
    c.circle(16, 16, 6, 'O')
    c.bevel(['R', 'O'])
    c.circle(15, 15, 2, 'y')
    c.outline()


@icon('dbgate', ['dbgate-bin', 'org.dbgate.DbGate', 'DbGate', 'dbgate-appimage'], DEV, 'DbGate')
def dbgate(c):
    # torii-like gate in front of a db
    c.rect(3, 4, 28, 7, 'R')
    c.rect(5, 9, 26, 11, 'R')
    c.rect(7, 7, 10, 28, '1'); c.rect(21, 7, 24, 28, '1')
    c.bevel(['R'])
    c.ellipse(16, 18, 4, 2, 'b') if False else None
    c.rect(12, 14, 19, 26, 'B')
    c.ellipse(16, 14.5, 4, 1.5, 'b')
    c.hline(12, 19, 20, '6')
    c.outline()


@icon('org.sqlitebrowser.sqlitebrowser', ['sqlitebrowser', 'db-browser-for-sqlite', 'DB Browser for SQLite',
                                         'sqlitebrowser-bin'], DEV, 'DB Browser for SQLite')
def sqlitebrowser(c):
    _db(c, 'B', 3, 22, 4, 28)
    _glass(c, 19, 19, 'c')
    c.outline()


@icon('sqlitestudio', ['SQLiteStudio', 'pl.com.salsoft.SQLiteStudio', 'sqlitestudio-bin'], DEV, 'SQLiteStudio')
def sqlitestudio(c):
    # feather quill
    c.poly([(27, 3), (17, 7), (9, 18), (7, 26), (13, 24), (23, 14), (29, 5)], 'C')
    c.bevel(['C'])
    c.line(26, 5, 4, 28, '6')
    c.outline()


@icon('mysql-workbench', ['mysql-workbench-community', 'MySQLWorkbench', 'mysql-workbench-bin', 'mysql'], DEV,
      'MySQL Workbench')
def mysql_workbench(c):
    # leaping dolphin
    c.poly([(3, 25), (8, 14), (15, 8), (24, 6), (28, 8), (25, 10), (21, 10), (17, 13), (13, 19), (9, 27)], 'B')
    c.poly([(16, 9), (19, 3), (21, 8)], 'B')
    c.poly([(3, 25), (2, 29), (8, 27)], 'O')
    c.bevel(['B'])
    c.px(23, 8, 'K')
    c.outline()


@icon('studio-3t', ['studio3t', 'Studio 3T', 'studio-3t-bin'], DEV, 'Studio 3T')
def studio3t(c):
    c.poly([(16, 3), (24, 10), (25, 19), (18, 26), (16, 29), (14, 26), (7, 19), (8, 10)], 'G')
    c.bevel(['G'])
    c.text(10, 12, '3T', 'W', font=3)
    c.vline(16, 22, 28, '4')
    c.outline()


@icon('robo3t', ['robo3t-bin', 'robomongo', 'Robo3T'], DEV, 'Robo 3T')
def robo3t(c):
    c.rect(15, 2, 16, 5, 's')
    c.rrect(5, 6, 26, 26, 'G', 5)
    c.bevel(['G'])
    c.rrect(8, 10, 23, 19, 'k', 3)
    c.rect(11, 13, 13, 15, 'g'); c.rect(18, 13, 20, 15, 'g')
    c.hline(11, 20, 23, '4')
    c.outline()


@icon('pgmodeler', ['pgmodeler-bin', 'io.pgmodeler.pgModeler', 'pgModeler'], DEV, 'pgModeler')
def pgmodeler(c):
    c.rect(3, 3, 14, 13, 'B'); c.rect(3, 3, 14, 5, '6')
    c.rect(17, 18, 28, 28, 'B'); c.rect(17, 18, 28, 20, '6')
    c.bevel(['B'])
    c.line(9, 14, 9, 22, 'S'); c.line(9, 22, 16, 22, 'S')
    c.hline(5, 12, 8, 'b'); c.hline(5, 10, 10, 'b')
    c.hline(19, 26, 23, 'b'); c.hline(19, 24, 25, 'b')
    c.outline()


# ====================================================================== languages

@icon('python', ['python3', 'python-interpreter', 'org.python.python', 'python3.12', 'python3.13', 'pypy3'], DEV,
      'Python')
def python(c):
    # interlocking blue / yellow snakes
    c.rrect(9, 3, 22, 13, 'B', 3)
    c.rrect(3, 9, 15, 22, 'B', 3)
    c.rect(9, 9, 15, 13, 'B')
    c.rrect(10, 19, 22, 28, 'Y', 3)
    c.rrect(17, 10, 28, 22, 'Y', 3)
    c.rect(17, 19, 22, 22, 'Y')
    c.rect(12, 14, 15, 15, '.') if False else None
    c.bevel(['B', 'Y'])
    c.rect(11, 5, 12, 6, 'W'); c.rect(19, 25, 20, 26, 'W')
    c.outline()


@icon('idle', ['idle3', 'python-idle', 'idle-python3', 'idle3.12', 'idle3.13'], DEV, 'IDLE')
def idle(c):
    c.rect(3, 3, 20, 28, 'W')
    c.shade_below(['W'], 'w')
    for i in range(6):
        c.hline(6, 15, 7 + i * 3, 'S')
    c.rrect(14, 12, 23, 19, 'B', 2)
    c.rrect(19, 17, 28, 25, 'Y', 2)
    c.bevel(['B', 'Y'])
    c.px(16, 14, 'W'); c.px(25, 22, 'W')
    c.outline()


@icon('nodejs', ['node', 'node-js', 'nodejs-lts', 'org.nodejs.node', 'npm'], DEV, 'Node.js')
def nodejs(c):
    pts = [(16 + 13 * math.cos(math.radians(a)), 16 + 13 * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
    c.poly(pts, 'G')
    c.bevel(['G'])
    c.poly(pts[:1] + pts[1:3] + [(16, 16)], 'G')
    c.poly([(16, 16), pts[3], pts[4], pts[5]], '4') if False else None
    c.text(10, 12, 'JS', 'W', font=3)
    c.rect(13, 12, 13, 16, 'W') if False else None
    c.outline()


@icon('rust', ['rustup', 'rust-lang', 'cargo', 'rustc'], DEV, 'Rust')
def rust(c):
    # cog ring with an R
    for k in range(16):
        a = math.radians(k * 22.5)
        cx, cy = 16 + 12 * math.cos(a), 16 + 12 * math.sin(a)
        c.rect(int(cx) - 1, int(cy) - 1, int(cx), int(cy), 'N')
    c.circle(16, 16, 12, 'N')
    c.bevel(['N'])
    c.circle(16, 16, 9, 'k')
    c.sprite(11, 10, """
        ######..
        ##...##.
        ##...##.
        ######..
        ##..##..
        ##...##.
        ##....##
    """, {'#': 'W'})
    c.outline()


@icon('go', ['golang', 'go-lang', 'gopher', 'go-tools'], DEV, 'Go')
def go(c):
    # gopher face
    c.circle(6, 7, 3, 'C'); c.circle(26, 7, 3, 'C')
    c.rrect(4, 5, 27, 28, 'C', 6)
    c.bevel(['C'])
    c.circle(10.5, 12, 4.5, 'W'); c.circle(21.5, 12, 4.5, 'W')
    c.rect(11, 11, 13, 13, 'K'); c.rect(22, 11, 24, 13, 'K')
    c.ellipse(16, 19, 4, 2.5, 'n')
    c.rect(15, 18, 16, 18, 'K')
    c.rect(14, 21, 17, 23, 'W')
    c.vline(15, 21, 23, 'w') if False else None
    c.outline()


@icon('java', ['openjdk', 'java-openjdk', 'jdk', 'openjdk-java', 'jshell', 'java-runtime', 'java-17-openjdk',
               'java-21-openjdk', 'jdk-openjdk', 'sun-java', 'oracle-java', 'javaws'], DEV, 'Java')
def java(c):
    # steaming coffee cup
    for x in (11, 16):
        c.line(x, 3, x + 2, 6, 'R', 2); c.line(x + 2, 6, x, 9, 'R', 2)
    c.rrect(5, 11, 22, 25, 'W', 3)
    c.rect(5, 11, 22, 16, 'W')
    c.ring(23, 17, 5, 2.8, 'W')
    c.rrect(3, 25, 27, 28, 'B', 1)
    c.bevel(['W', 'B'])
    c.rect(6, 13, 21, 14, 'b')
    c.outline()


@icon('ruby', ['irb', 'ruby-lang', 'ruby3', 'rubygems'], DEV, 'Ruby')
def ruby(c):
    c.poly([(8, 4), (24, 4), (29, 11), (16, 29), (3, 11)], 'R')
    c.poly([(8, 4), (24, 4), (29, 11), (3, 11)], 'r')
    c.poly([(11, 11), (21, 11), (16, 27)], '1')
    c.poly([(11, 11), (16, 4), (21, 11)], 'R')
    c.px(9, 6, 'W'); c.px(10, 5, 'W')
    c.outline()


@icon('php', ['php-cli', 'php8', 'php-lang', 'php-fpm'], DEV, 'PHP')
def php(c):
    c.ellipse(16, 16, 13, 9, 'M')
    c.bevel(['M'])
    c.sprite(6, 12, """
        ###..#.....###
        #..#.#.....#..#
        #..#.###...#..#
        ###..#..#..###.
        #....#..#..#...
    """, {'#': 'W'})
    c.outline()


@icon('lua', ['lua5.4', 'lua-lang', 'luajit', 'lua5.1'], DEV, 'Lua')
def lua(c):
    c.circle(15, 16.5, 12, '6')
    c.bevel(['6'], dark=False)
    c.circle(19, 12, 4, 'W')
    c.circle(25.5, 6, 3, '6')
    c.text(8, 17, 'LUA', 'W', font=3)
    c.outline()


@icon('julia', ['julialang', 'org.julialang.Julia', 'julia-bin', 'julia-lts'], DEV, 'Julia')
def julia(c):
    for (x, y), col in (((16, 9), 'G'), ((9, 21), 'R'), ((23, 21), 'M')):
        c.circle(x, y, 6.5, col)
    c.bevel(['G', 'R', 'M'])
    c.outline()


@icon('ghci', ['haskell', 'ghc', 'haskell-ghc', 'stack', 'ghcup', 'cabal'], DEV, 'Haskell (GHCi)')
def ghci(c):
    c.poly([(3, 4), (8, 4), (15, 15.5), (8, 27), (3, 27), (10, 15.5)], '7')
    c.poly([(9, 4), (14, 4), (28, 27), (23, 27), (18.5, 20), (14, 27), (9, 27), (16, 15.5)], 'M')
    c.poly([(20, 11), (28, 11), (28, 14.5), (22, 14.5)], 'm')
    c.poly([(23, 16.5), (28, 16.5), (28, 20), (25, 20)], 'm')
    c.bevel(['M'])
    c.outline()


@icon('elixir', ['iex', 'elixir-lang', 'mix'], DEV, 'Elixir')
def elixir(c):
    # purple drop
    c.circle(16, 20, 9, 'M')
    c.poly([(16, 2), (24, 15), (8, 15)], 'M')
    c.poly([(14, 3), (17, 2), (9, 15), (8, 18)], 'M') if False else None
    c.bevel(['M'])
    c.poly([(15, 6), (11, 15), (10, 21), (13, 25), (12, 19), (13, 13)], 'm')
    c.outline()


@icon('zig', ['zig-bin', 'ziglang', 'zig-dev'], DEV, 'Zig')
def zig(c):
    c.rect(3, 4, 28, 9, 'O')
    c.rect(3, 22, 28, 27, 'O')
    c.poly([(21, 9.5), (28, 9.5), (11, 22.5), (4, 22.5)], 'O')
    c.bevel(['O'])
    c.poly([(1, 4), (6, 4), (3, 9)], '.')
    c.poly([(31, 27), (26, 27), (29, 22)], '.')
    c.outline()


@icon('deno', ['deno-bin', 'deno-lang'], DEV, 'Deno')
def deno(c):
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'], dark=False)
    # little dino head
    c.ellipse(16, 13, 8, 5.5, 'W')
    c.rect(9, 13, 16, 24, 'W')
    c.poly([(9, 24), (11, 27), (13, 24)], 'W')
    c.rect(18, 11, 19, 12, 'K')
    c.outline()


@icon('bun', ['bun-bin', 'oven-sh-bun', 'bunx'], DEV, 'Bun')
def bun(c):
    c.ellipse(16, 17, 13, 11, 'y')
    c.bevel(['y'])
    c.ellipse(16, 12, 10, 4, 'n') if False else None
    c.rect(10, 16, 11, 18, 'K'); c.rect(20, 16, 21, 18, 'K')
    c.hline(14, 17, 20, 'K')
    c.pixels([(8, 20), (9, 20), (22, 20), (23, 20)], 'P')
    c.line(13, 8, 15, 10, '3'); c.line(18, 7, 19, 10, '3')
    c.outline()


@icon('dotnet', ['dotnet-sdk', 'dotnet-runtime', 'dotnet-host', 'csharp', 'mono', 'dotnet-sdk-bin', 'microsoft-dotnet'],
      DEV, '.NET')
def dotnet(c):
    c.circle(16, 16, 13, 'M')
    c.bevel(['M'])
    c.rect(6, 19, 7, 20, 'W')
    c.sprite(9, 13, """
        #...#.####.#####
        ##..#.#......#..
        #.#.#.###....#..
        #..##.#......#..
        #...#.####...#..
    """, {'#': 'W'})
    c.outline()


@icon('kotlin', ['kotlinc', 'kotlin-native', 'kotlin-lang'], DEV, 'Kotlin')
def kotlin(c):
    c.poly([(4, 4), (28, 4), (16, 16), (28, 28), (4, 28)], 'M')
    c.poly([(4, 4), (16, 4), (4, 16)], 'B')
    c.poly([(16, 16), (28, 28), (4, 28)], 'O')
    c.bevel(['M'], dark=False)
    c.outline()


@icon('swift', ['swift-lang', 'swiftc', 'swift-bin'], DEV, 'Swift')
def swift(c):
    c.rrect(3, 3, 28, 28, 'O', 5)
    c.bevel(['O'])
    c.poly([(7, 13), (18, 21), (12, 9), (23, 18), (19, 6), (26, 16), (27, 23), (24, 21), (20, 24), (11, 23), (6, 18)],
           'W')
    c.outline()


@icon('scala', ['scala-lang', 'scala-cli', 'sbt'], DEV, 'Scala')
def scala(c):
    for y in (4, 12, 20):
        c.poly([(8, y + 3), (24, y), (24, y + 5), (8, y + 8)], 'R')
    c.bevel(['R'])
    for y in (7, 15):
        c.poly([(8, y + 3), (24, y + 1), (24, y + 5), (8, y + 5)], '1')
    c.outline()


@icon('erlang', ['erl', 'erlang-lang', 'rebar3'], DEV, 'Erlang')
def erlang(c):
    c.rrect(3, 5, 28, 26, 'R', 2)
    c.bevel(['R'])
    c.ellipse(16, 15.5, 8, 8, 'W')
    c.ellipse(16, 13, 6, 3.5, 'R')
    c.rect(10, 15, 22, 16, 'W')
    c.rect(18, 17, 24, 20, 'R')
    c.outline()


@icon('perl', ['perl5', 'perl-lang', 'cpan'], DEV, 'Perl')
def perl(c):
    # camel
    c.poly([(5, 17), (9, 9), (13, 15), (16, 8), (20, 15), (22, 12), (25, 5), (29, 6), (27, 9), (25, 17), (23, 20),
            (6, 20)], 'n')
    c.bevel(['n'])
    for x in (7, 11, 18, 22):
        c.rect(x, 20, x + 1, 28, 'N')
    c.px(26, 6, 'K')
    c.outline()


@icon('nim', ['nim-lang', 'nimble'], DEV, 'Nim')
def nim(c):
    # golden crown
    c.poly([(3, 11), (9, 17), (12, 6), (16, 14), (20, 6), (23, 17), (29, 11), (26, 26), (6, 26)], 'Y')
    c.bevel(['Y'])
    c.hline(7, 25, 22, '3')
    c.outline()


@icon('crystal', ['crystal-lang', 'shards'], DEV, 'Crystal')
def crystal(c):
    c.poly([(11, 3), (28, 9), (21, 29), (4, 23)], 'k')
    c.poly([(11, 3), (28, 9), (16, 16)], 's')
    c.poly([(4, 23), (16, 16), (11, 3)], 'S')
    c.line(16, 16, 21, 28, 'K')
    c.outline()


@icon('dart', ['dart-sdk', 'dart-lang'], DEV, 'Dart')
def dart(c):
    c.poly([(9, 3), (21, 3), (29, 11), (29, 23), (23, 29), (11, 29), (3, 21), (3, 9)], 'C')
    c.poly([(9, 3), (21, 3), (29, 11), (16, 11), (9, 18), (3, 21), (3, 9)], 'B')
    c.poly([(16, 11), (29, 11), (29, 23), (23, 29), (16, 22)], '5')
    c.bevel(['B', 'C'], dark=False)
    c.outline()


@icon('clojure', ['clj', 'clojure-lang', 'leiningen'], DEV, 'Clojure')
def clojure(c):
    c.circle(16, 16, 13, 'G')
    c.arc(16, 16, 13, 0, 200, 340, 'B') if False else None
    c.poly([(3, 16), (29, 16), (29, 30), (3, 30)], 'B') if False else None
    for y in range(32):
        for x in range(32):
            if c.get(x, y) == 'G' and y < 16 and x > 12:
                c.px(x, y, 'B')
    c.bevel(['G', 'B'])
    c.circle(16, 16, 7, 'W')
    c.poly([(12, 22), (16, 14), (14, 10), (16, 10), (21, 22), (19, 22), (16, 17), (14, 22)], 'k')
    c.outline()


@icon('typescript', ['tsc', 'typescript-lang', 'ts-node'], DEV, 'TypeScript')
def typescript(c):
    c.rect(3, 3, 28, 28, 'B')
    c.bevel(['B'])
    c.text(10, 15, 'TS', 'W', scale=1)
    c.rect(9, 14, 13, 14, 'B') if False else None
    c.outline()


@icon('gleam', ['gleam-bin', 'gleam-lang'], DEV, 'Gleam')
def gleam(c):
    # Lucy the star
    pts = []
    for k in range(10):
        r = 13.5 if k % 2 == 0 else 6
        a = math.radians(-90 + k * 36)
        pts.append((16 + r * math.cos(a), 17 + r * math.sin(a)))
    c.poly(pts, 'p')
    c.bevel(['p'])
    c.rect(13, 16, 13, 17, 'K'); c.rect(18, 16, 18, 17, 'K')
    c.hline(14, 17, 19, 'K')
    c.outline()

