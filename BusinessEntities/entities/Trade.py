class Trade:

    security = None
    tradeno = 0
    time = 0
    board = 0
    price = 0
    quantity = 0
    buysell = ''
    openinterest = 0
    period = ''

    def __init__(self, security, tradeno, time, board, price, quantity, buysell, openinteres, period):
        self.security = security
        self.tradeno = tradeno
        self.time = time
        self.board = board
        self.price = price
        self.quantity = quantity
        self.buysell = buysell
        self.openinterest = openinteres
        self.period = period

    def __str__(self):
        return 'Trade : ' + str(self.price)