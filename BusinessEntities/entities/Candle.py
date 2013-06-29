class CandleInterval(object):

    M1 = 1
    M5 = 5
    M15 = 15
    M30 = 30
    H1 = 60
    H4 = 240
    D1 = 60 * 24

    @staticmethod
    def availableIntervals():
        return [CandleInterval.M1, CandleInterval.M5, CandleInterval.M15, CandleInterval.M30, CandleInterval.H1, CandleInterval.H4, CandleInterval.D1]

    @staticmethod
    def toSeconds(interval):
        return interval * 60

def pushTrade(self, trade):
    if self.open == 0:
        self.open = trade.price
    self.close = trade.price
    if self.high < trade.price:
        self.high = trade.price
    if self.low > trade.price or self.low == 0:
        self.low = trade.price

def isEmpty(self):
    return self.open == 0 and self.close == 0 and self.high == 0 and self.low == 0

class CandleMeta(type):

    def __new__(meta, classname, supers, classdict):
        classdict['pushTrade'] = pushTrade
        classdict['isEmpty'] = isEmpty
        return type.__new__(meta, classname, supers, classdict)

class Candle(object):

    __metaclass__ = CandleMeta

    candleInterval = None
    startTime = None

    open = 0
    close = 0
    high = 0
    low = 0

    def __str__(self):
        return 'Start time: ' + str(self.startTime) + ' Open : ' + str(self.open) + ' High : ' + str(self.high) + ' Low : ' + str(self.low) + ' Close : ' + str(self.close)