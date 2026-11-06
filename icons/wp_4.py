"""Finance, crypto wallets, shopping and learning apps."""
from pix import icon


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


def bag(c, col, handle='k'):
    c.poly([(5, 10), (27, 10), (29, 29), (3, 29)], col)
    c.bevel([col])
    c.arc(16, 10, 6.5, 4.5, 180, 360, handle)


BTC = """
    ..#.#...
    ######..
    .##..##.
    .##..##.
    .#####..
    .##..##.
    .##..##.
    ######..
    ..#.#...
"""


# ================================================================ payments / banking

@icon('stripe', ['stripe-webapp', 'dashboard.stripe.com', 'stripe-cli'], 'finance', 'Stripe')
def stripe(c):
    c.rrect(3, 3, 28, 28, 'M', 4)
    c.bevel(['M'])
    g(c, 10, 7, """
        ..#######.
        .########.
        ###.......
        ###.......
        .######...
        ..#######.
        .......###
        .......###
        #########.
        ########..
    """)
    c.shift(0, 2)
    c.outline()


@icon('paypal', ['paypal-webapp', 'paypal.com', 'com.paypal'], 'finance', 'PayPal')
def paypal(c):
    c.poly([(9, 3), (21, 3), (26, 7), (25, 14), (19, 18), (14, 18), (12, 27), (5, 27)], '6')
    c.poly([(12, 7), (24, 7), (28, 11), (27, 18), (21, 22), (16, 22), (15, 29), (9, 29)], 'B')
    c.bevel(['6', 'B'])
    c.poly([(14, 10), (21, 10), (22, 14), (19, 16), (13, 16)], '6')
    c.outline()


@icon('wise', ['wise-webapp', 'transferwise', 'wise.com'], 'finance', 'Wise')
def wise(c):
    c.poly([(3, 6), (29, 6), (17, 17), (24, 17), (12, 27), (13, 21), (9, 21), (14, 11), (8, 11)], 'g')
    c.bevel(['g'])
    c.outline()


@icon('revolut', ['revolut-webapp', 'revolut.com'], 'finance', 'Revolut')
def revolut(c):
    disc(c, 'k')
    g(c, 10, 7, """
        ########..
        #########.
        ###....###
        ###....###
        #########.
        #######...
        ###..###..
        ###...###.
        ###....###
        ###....###
    """)
    c.shift(0, 1)
    c.outline()


@icon('monzo', ['monzo-webapp', 'monzo.com'], 'finance', 'Monzo')
def monzo(c):
    c.poly([(3, 26), (3, 6), (9, 4), (9, 22)], 'C')
    c.poly([(29, 26), (29, 6), (23, 4), (23, 22)], 'Y')
    c.poly([(9, 4), (16, 13), (16, 20), (9, 12)], 'R')
    c.poly([(23, 4), (16, 13), (16, 20), (23, 12)], 'O')
    c.bevel(['C', 'Y', 'R', 'O'], light=False)
    c.outline()


@icon('robinhood', ['robinhood-webapp', 'robinhood.com'], 'finance', 'Robinhood')
def robinhood(c):
    c.poly([(28, 3), (18, 6), (10, 13), (6, 22), (5, 29), (10, 22), (14, 21), (22, 15), (26, 9)], 'g')
    c.bevel(['g'])
    c.line(25, 6, 8, 25, '4')
    c.outline()


@icon('gnucash', ['org.gnucash.GnuCash', 'gnucash-docs'], 'finance', 'GnuCash')
def gnucash(c):
    c.rrect(3, 9, 26, 24, '4', 1)
    c.rrect(5, 7, 28, 22, 'G', 1)
    c.bevel(['G', '4'])
    c.circle(16.5, 14.5, 4.5, 'g')
    ctext(c, '$', 'W', 14.5, 1)
    c.rect(7, 9, 8, 10, 'g'); c.rect(24, 19, 25, 20, 'g')
    c.outline()


@icon('kmymoney', ['org.kde.kmymoney'], 'finance', 'KMyMoney')
def kmymoney(c):
    for i, y in enumerate((23, 18, 13)):
        c.ellipse(13, y + 2, 9, 3.5, '3')
        c.ellipse(13, y, 9, 3.5, 'Y')
    c.bevel(['Y'])
    c.circle(22, 10, 7, 'B')
    c.bevel(['B'])
    ctext(c, 'K', 'W', 10, 1, 5, 22)
    c.outline()


@icon('homebank', ['fr.free.homebank', 'homebank-git'], 'finance', 'HomeBank')
def homebank(c):
    # piggy bank
    c.ellipse(15, 17, 12, 9, 'P')
    c.poly([(9, 10), (8, 4), (14, 9)], 'P')
    c.rect(7, 22, 10, 28, 'P'); c.rect(19, 22, 22, 28, 'P')
    c.ellipse(27, 17, 2, 3, 'p')
    c.bevel(['P'])
    c.rect(13, 9, 18, 10, 'k')
    c.rect(9, 13, 10, 14, 'K')
    c.outline()


@icon('org.kde.skrooge', ['skrooge'], 'finance', 'Skrooge')
def skrooge(c):
    # wallet
    c.rrect(3, 7, 28, 27, 'N', 2)
    c.bevel(['N'])
    c.rect(4, 11, 27, 11, '8')
    c.rrect(19, 14, 28, 21, '8', 1)
    c.circle(23, 17.5, 1.5, 'Y')
    c.rect(6, 3, 22, 7, 'G')
    c.outline()


@icon('firefly-iii', ['firefly', 'fireflyiii', 'firefly-iii-webapp'], 'finance', 'Firefly III')
def firefly(c):
    c.ellipse(19, 20, 9, 8, 'Y')
    c.ellipse(19, 20, 6, 5, 'y')
    c.ellipse(11, 11, 6, 5, 'k')
    c.circle(6, 7, 3.5, 'k')
    c.ellipse(13, 6, 4, 2.5, 'c'); c.ellipse(8, 14, 2.5, 4, 'c')
    c.bevel(['k'])
    c.px(5, 6, 'W')
    c.outline()


@icon('org.nickvision.money', ['denaro', 'nickvision-money'], 'finance', 'Denaro')
def denaro(c):
    c.circle(16, 16, 13, '4')
    c.circle(15, 15, 12, 'G')
    c.bevel(['G'])
    c.ring(15, 15, 9.5, 8.5, 'g')
    ctext(c, '$', 'W', 15, 2)
    c.outline()


# ================================================================ crypto

@icon('coinbase', ['coinbase-webapp', 'coinbase.com', 'coinbase-wallet'], 'finance', 'Coinbase')
def coinbase(c):
    disc(c, 'B')
    c.circle(16, 16, 8, 'W')
    c.rect(13, 13, 18, 18, 'B')
    c.outline()


@icon('binance', ['binance-webapp', 'binance-desktop', 'binance.com', 'Binance'], 'finance', 'Binance')
def binance(c):
    def dia(cx, cy, r):
        c.poly([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], 'Y')
    dia(16, 16, 4)
    dia(16, 7, 4); dia(16, 25, 4); dia(7, 16, 3.5); dia(25, 16, 3.5)
    c.poly([(16, 3), (24, 11), (21, 14), (16, 9), (11, 14), (8, 11)], 'Y')
    c.poly([(16, 29), (24, 21), (21, 18), (16, 23), (11, 18), (8, 21)], 'Y')
    c.bevel(['Y'])
    c.outline()


@icon('kraken', ['kraken-webapp', 'kraken.com', 'kraken-desktop'], 'finance', 'Kraken')
def kraken(c):
    disc(c, 'M')
    c.ellipse(16, 14, 8, 7, 'W')
    c.rect(8, 14, 24, 21, 'W')
    for x in (8, 12, 16, 20, 23):
        c.rect(x, 21, x + 1, 24, 'W')
    for x in (10, 14, 18, 22):
        c.rect(x, 17, x, 24, 'M')
    c.rect(8, 22, 24, 24, 'M')
    for x in (8, 12, 16, 20):
        c.rrect(x, 18, x + 1, 24, 'W', 0)
    c.rect(23, 18, 24, 24, 'W')
    c.outline()


@icon('tradingview', ['tradingview-webapp', 'tradingview-desktop', 'com.tradingview.tradingview'], 'finance',
      'TradingView')
def tradingview(c):
    c.rrect(3, 6, 28, 26, 'k', 3)
    c.bevel(['k'])
    c.rect(6, 10, 14, 13, 'W'); c.rect(10, 13, 13, 22, 'W')
    c.circle(17, 12, 2, 'W')
    c.poly([(21, 10), (26, 10), (20, 22), (15, 22)], 'W')
    c.outline()


@icon('yahoo-finance', ['yahoo-finance-webapp', 'finance.yahoo.com', 'yahoo', 'yahoo-mail'], 'finance',
      'Yahoo Finance')
def yahoo_finance(c):
    c.rrect(3, 4, 28, 27, 'M', 4)
    c.bevel(['M'])
    g(c, 6, 10, """
        ###....###.#
        .##....##..#
        ..##..##...#
        ...####....#
        ....##......
        ....##.....#
        ...####.....
    """)
    c.outline()


@icon('exodus', ['exodus-bin', 'com.exodus.Exodus', 'Exodus'], 'finance', 'Exodus')
def exodus(c):
    c.poly([(3, 4), (12, 4), (16, 9), (20, 4), (29, 4), (20, 16), (29, 28), (20, 28), (16, 23), (12, 28), (3, 28),
            (12, 16)], 'M')
    c.poly([(20, 4), (29, 4), (20, 16), (16, 9)], 'C')
    c.poly([(3, 28), (12, 16), (16, 23), (12, 28)], 'B')
    c.bevel(['M', 'C', 'B'], light=False)
    c.outline()


@icon('electrum', ['org.electrum.electrum', 'electrum-appimage', 'Electrum'], 'finance', 'Electrum')
def electrum(c):
    disc(c, 'b')
    c.ring(16, 16, 10, 8.5, 'W')
    c.poly([(18, 6), (10, 17), (15, 17), (13, 26), (22, 14), (17, 14), (19, 6)], 'W')
    c.outline()


@icon('ledger-live', ['ledger-live-desktop', 'com.ledger.live', 'ledger-live-bin', 'Ledger Live'], 'finance',
      'Ledger Live')
def ledger(c):
    c.rrect(3, 3, 28, 28, 'k', 3)
    c.bevel(['k'])
    c.rect(7, 7, 9, 13, 'W'); c.rect(7, 7, 13, 9, 'W')
    c.rect(22, 7, 24, 13, 'W'); c.rect(18, 7, 24, 9, 'W')
    c.rect(7, 18, 9, 24, 'W'); c.rect(7, 22, 13, 24, 'W')
    c.rect(22, 18, 24, 24, 'W'); c.rect(18, 22, 24, 24, 'W')
    c.rect(12, 12, 14, 19, 'W'); c.rect(12, 17, 19, 19, 'W')
    c.outline()


@icon('trezor-suite', ['trezor-suite-appimage', 'io.trezor.suite', 'trezor-suite-bin', 'trezor'], 'finance',
      'Trezor Suite')
def trezor(c):
    c.arc(16, 11, 8, 4.5, 180, 360, 'k')
    c.rect(8, 11, 11, 13, 'k'); c.rect(21, 11, 24, 13, 'k')
    c.poly([(5, 13), (27, 13), (27, 24), (16, 29), (5, 24)], 'k')
    c.bevel(['k'])
    c.rect(11, 17, 20, 21, 'W')
    c.outline()


@icon('monero-gui', ['monero', 'monero-wallet-gui', 'org.getmonero.Monero', 'monero-gui-bin'], 'finance',
      'Monero GUI')
def monero(c):
    c.circle(16, 16, 13, 'O')
    for y in range(20, 30):
        for x in range(32):
            if c.get(x, y) == 'O':
                c.px(x, y, 's')
    c.bevel(['O', 's'])
    g(c, 8, 7, """
        ##.............##
        ###...........###
        ####.........####
        ##.##.......##.##
        ##..##.....##..##
        ##...##...##...##
        ##....##.##....##
        ##.....###.....##
        ##......#......##
        ##.............##
        ##.............##
        ##.............##
        ##.............##
    """)
    c.rect(4, 18, 9, 19, 'W'); c.rect(24, 18, 28, 19, 'W')
    c.outline()


@icon('bitcoin-qt', ['bitcoin-core', 'bitcoin', 'org.bitcoincore.bitcoin-qt', 'bitcoin-gui'], 'finance',
      'Bitcoin Core')
def bitcoin(c):
    disc(c, 'O')
    rows = [r for r in BTC.strip().split()]
    for j, r in enumerate(rows):
        for i, ch in enumerate(r):
            if ch == '#':
                c.rect(8 + 2 * i, 7 + 2 * j, 9 + 2 * i, 8 + 2 * j, 'W')
    c.outline()


@icon('sparrow', ['sparrow-wallet', 'com.sparrowwallet.Sparrow', 'sparrow-wallet-bin', 'sparrowwallet'],
      'finance', 'Sparrow Wallet')
def sparrow(c):
    c.ellipse(15, 18, 10, 7, 'N')
    c.circle(22, 10, 5.5, 'N')
    c.poly([(5, 19), (2.5, 27), (10, 22)], 'N')
    c.bevel(['N'])
    c.ellipse(14, 17, 6, 3.5, 'n')
    c.ellipse(21, 13, 3, 2.5, 'W')
    c.poly([(27, 9), (30, 11), (27, 12)], 'k')
    c.rect(22, 8, 23, 9, 'K')
    c.outline()


# ================================================================ shopping

@icon('amazon', ['amazon-webapp', 'amazon.com', 'com.amazon.Amazon', 'amazon-shopping'], 'shop', 'Amazon')
def amazon(c):
    c.rrect(3, 3, 28, 28, 'k', 4)
    c.bevel(['k'])
    g(c, 10, 6, """
        .#####...
        ......##.
        ......##.
        .#######.
        ##....##.
        ##...###.
        .#####.##
    """)
    c.arc(16, 12, 11, 9.5, 35, 145, 'O')
    c.poly([(23, 19), (26, 18), (26, 22)], 'O')
    c.outline()


@icon('ebay', ['ebay-webapp', 'ebay.com'], 'shop', 'eBay')
def ebay(c):
    c.rrect(3, 8, 28, 24, 'W', 3)
    c.bevel(['W'])
    for i, (ch, col) in enumerate(zip('EBAY', 'RBYG')):
        c.text(5 + i * 6, 12, ch, col, 5, 1)
    c.outline()


@icon('etsy', ['etsy-webapp', 'etsy.com'], 'shop', 'Etsy')
def etsy(c):
    disc(c, 'O')
    g(c, 11, 8, """
        #########
        .##......
        .##......
        .######..
        .######..
        .##......
        .##......
        .##.....#
        #########
    """)
    c.outline()


@icon('shopify', ['shopify-webapp', 'shopify.com', 'shopify-cli'], 'shop', 'Shopify')
def shopify(c):
    bag(c, 'G', 'G')
    c.arc(16, 10, 6.5, 4.5, 180, 360, 'G')
    c.bevel(['G'])
    g(c, 12, 14, """
        .#####.
        ##.....
        ##.....
        .####..
        ....##.
        ....##.
        #####..
    """)
    c.outline()


@icon('aliexpress', ['aliexpress-webapp', 'aliexpress.com'], 'shop', 'AliExpress')
def aliexpress(c):
    c.rrect(3, 4, 28, 28, 'R', 4)
    c.bevel(['R'])
    c.arc(16, 13, 7, 5, 20, 160, 'W')
    c.rect(9, 9, 10, 11, 'W'); c.rect(21, 9, 22, 11, 'W')
    c.outline()


@icon('temu', ['temu-webapp', 'temu.com'], 'shop', 'Temu')
def temu(c):
    bag(c, 'O', 'O')
    c.arc(16, 10, 6.5, 4.5, 180, 360, 'O')
    c.bevel(['O'])
    ctext(c, 'TEMU', 'W', 20, 1, 3)
    c.outline()


# ================================================================ learning

@icon('anki', ['net.ankiweb.Anki', 'anki-bin', 'anki-qt5', 'ankiweb', 'anki-official-binary-bundle'], 'education',
      'Anki')
def anki(c):
    c.poly([(4, 8), (17, 3), (22, 21), (9, 26)], 'b')
    c.bevel(['b'])
    c.rrect(11, 6, 27, 28, 'B', 1)
    c.bevel(['B'])
    c.poly([(19, 10), (21, 15), (25, 15), (22, 18), (23, 23), (19, 20), (15, 23), (16, 18), (13, 15), (17, 15)], 'Y')
    c.outline()


@icon('mnemosyne', ['org.mnemosyne_proj.mnemosyne', 'mnemosyne-proj'], 'education', 'Mnemosyne')
def mnemosyne(c):
    c.rrect(3, 6, 23, 23, 'w', 1)
    c.bevel(['w'])
    c.rrect(8, 10, 28, 27, 'W', 1)
    c.bevel(['W'])
    ctext(c, '?', 'B', 18.5, 2, 5, 18)
    c.outline()


@icon('duolingo', ['duolingo-webapp', 'duolingo.com', 'duolingo-desktop'], 'education', 'Duolingo')
def duolingo(c):
    # the green owl
    c.ellipse(16, 18, 12, 11, 'G')
    c.poly([(5, 10), (6, 3), (11, 8)], 'G')
    c.poly([(27, 10), (26, 3), (21, 8)], 'G')
    c.bevel(['G'])
    c.circle(11, 14, 4.5, 'W'); c.circle(21, 14, 4.5, 'W')
    c.circle(12, 15, 2, 'K'); c.circle(20, 15, 2, 'K')
    c.poly([(14, 19), (18, 19), (16, 22)], 'O')
    c.ellipse(16, 25, 6, 3, 'g')
    c.outline()


@icon('khan-academy', ['khan-academy-webapp', 'khanacademy.org', 'khan'], 'education', 'Khan Academy')
def khan(c):
    c.poly([(16, 3), (27.5, 9.5), (27.5, 22.5), (16, 29), (4.5, 22.5), (4.5, 9.5)], 'G')
    c.bevel(['G'])
    c.circle(16, 12, 3, 'W')
    c.arc(16, 15, 8, 6, 40, 140, 'W')
    c.poly([(9, 17), (16, 23), (23, 17), (23, 19), (16, 25), (9, 19)], 'W')
    c.outline()


@icon('coursera', ['coursera-webapp', 'coursera.org'], 'education', 'Coursera')
def coursera(c):
    c.rrect(3, 3, 28, 28, 'B', 5)
    c.bevel(['B'])
    c.arc(16, 16, 9, 5.5, 45, 315, 'W')
    c.outline()


@icon('udemy', ['udemy-webapp', 'udemy.com'], 'education', 'Udemy')
def udemy(c):
    c.poly([(16, 3), (28, 9), (16, 15), (4, 9)], 'M')
    c.bevel(['M'])
    c.poly([(5, 13), (11, 13), (11, 21), (16, 25), (21, 21), (21, 13), (27, 13), (27, 22), (16, 29), (5, 22)], 'M')
    c.bevel(['M'])
    c.outline()


@icon('edx', ['edx-webapp', 'edx.org'], 'education', 'edX')
def edx(c):
    c.rrect(3, 7, 28, 25, 'k', 3)
    c.bevel(['k'])
    c.text(8, 13, 'ED', 'W', 5, 1)
    c.text(20, 13, 'X', 'm', 5, 1)
    c.outline()


# ================================================================ budgeting / more wallets / study

@icon('actual-budget', ['com.actualbudget.actual', 'actual-desktop', 'actual-bin', 'actual-budget-bin'], 'finance',
      'Actual Budget')
def actual_budget(c):
    c.poly([(13, 3), (19, 3), (29, 28), (23, 28), (16, 10), (9, 28), (3, 28)], 'M')
    c.bevel(['M'])
    c.poly([(5, 19), (28, 16), (28, 19), (5, 22)], 'B')
    c.bevel(['B'])
    c.outline()


@icon('portfolio', ['info.portfolio_performance.PortfolioPerformance', 'portfolio-performance',
                    'portfolio-performance-bin', 'PortfolioPerformance'], 'finance', 'Portfolio Performance')
def portfolio(c):
    disc(c, 'B')
    c.arc(16, 16, 13, 0, 270, 360, 'O')
    c.bevel(['O'])
    c.line(16, 16, 16, 3, 'W'); c.line(16, 16, 28, 16, 'W')
    c.outline()


@icon('ynab', ['ynab-webapp', 'youneedabudget', 'app.ynab.com'], 'finance', 'YNAB')
def ynab(c):
    disc(c, 'b')
    c.poly([(8, 7), (12, 7), (16, 14), (20, 7), (24, 7), (18, 17), (18, 25), (14, 25), (14, 17)], 'W')
    c.shade_below(['W'], 'w')
    c.outline()


@icon('metamask', ['metamask-webapp', 'io.metamask'], 'finance', 'MetaMask')
def metamask(c):
    # the fox head
    c.poly([(3, 3), (13, 9), (19, 9), (29, 3), (27, 14), (29, 20), (25, 28), (18, 26), (14, 26), (7, 28), (3, 20),
            (5, 14)], 'O')
    c.bevel(['O'])
    c.poly([(5, 14), (13, 13), (9, 20), (3, 20)], '2')
    c.poly([(27, 14), (19, 13), (23, 20), (29, 20)], '2')
    c.poly([(13, 21), (19, 21), (18, 26), (14, 26)], 'n')
    c.rect(10, 15, 11, 16, 'K'); c.rect(21, 15, 22, 16, 'K')
    c.poly([(11, 10), (21, 10), (16, 13)], 'o')
    c.outline()


@icon('wasabiwallet', ['wasabi-wallet', 'wasabi', 'io.wasabiwallet.Wasabi', 'wasabi-wallet-bin'], 'finance',
      'Wasabi Wallet')
def wasabi(c):
    # wasabi blob
    c.ellipse(16, 18, 12.5, 10, 'G')
    c.circle(16, 9, 6.5, 'G')
    c.circle(11, 6, 3, 'G')
    c.bevel(['G'])
    c.ellipse(13, 18, 4, 3, 'g')
    c.pixels([(20, 14), (22, 19), (17, 23), (9, 22), (14, 10)], '4')
    c.outline()


@icon('bisq', ['bisq-desktop', 'bisq2', 'network.bisq.Bisq', 'bisq-bin'], 'finance', 'Bisq')
def bisq(c):
    disc(c, 'G')
    c.poly([(8, 12), (19, 12), (19, 8), (25, 13.5), (19, 19), (19, 15), (8, 15)], 'W')
    c.poly([(24, 20), (13, 20), (13, 17), (7, 21.5), (13, 26), (13, 23), (24, 23)], 'g')
    c.outline()


@icon('quizlet', ['quizlet-webapp', 'quizlet.com'], 'education', 'Quizlet')
def quizlet(c):
    c.rrect(3, 3, 28, 28, 'B', 5)
    c.bevel(['B'])
    c.ring(15.5, 15, 7.5, 4.5, 'W')
    c.line(18, 18, 23, 24, 'W', 3)
    c.outline()


@icon('remnote', ['remnote-bin', 'io.remnote.RemNote', 'RemNote', 'remnote-webapp'], 'education', 'RemNote')
def remnote(c):
    c.rrect(3, 3, 28, 28, 'k', 5)
    c.bevel(['k'])
    g(c, 9, 7, """
        ########..
        #########.
        ##.....###
        ##.....###
        #########.
        ########..
        ##...###..
        ##....###.
        ##.....###
        ##......##
    """)
    c.shift(0, 1)
    c.replace('W', 'B', (9, 16, 31, 31))
    c.outline()
