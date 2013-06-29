from datetime import datetime, timedelta
from entities.Candle import CandleInterval, Candle
# from messaging.Channels import Channels
# from messaging.Consumer import consumer
# from messaging.Publisher import Publisher

#TODO candles with length more than one hour are not correctly generated
# @consumer(Channels.TRADES)
# @Publisher(Channels.CANDLES_FINISHED)
class JapaneseCandleService:

    def __init__(self):
        # @consumer(Channels.TIME)
        class TimeService:

            def start(self):
                print 'starting time service'

            def push(self, time):
                print 'TimeService pushing', time
                self.candlesService.tick(time)

        self.__timeService = TimeService()
        self.__timeService.candlesService = self
        self.__intervalStartTimeDict = {}
        self.__candlesInProgressDict = {}
        self.__startOfDay = None
        self.__currentCandle = None

    def start(self):
        print 'starting candle service'
        self.__timeService.start()

    def push(self, trades):
        print 'JapaneseCandleService pushing', trades
        for trade in trades:
            self.__openNewCandleIfNecessary(trade.time)
            for interval in CandleInterval.availableIntervals():
                self.__candlesInProgressDict[interval].pushTrade(trade)

    def tick(self, time):
        self.__currentTime = time
        self.__openNewCandleIfNecessary(time)

    def __openNewCandleIfNecessary(self, time):
        self.__fillStartOfDay(time)
        for interval in CandleInterval.availableIntervals():
            if not self.__intervalStartTimeDict.has_key(interval):
                self.__registerCandleStartTime(time, interval)
                self.__processCandleFinished(interval)
                self.__processCandleStarted(interval)
            else:
                diff = time - self.__intervalStartTimeDict[interval]
                if diff > timedelta(minutes = interval):
                    self.__registerCandleStartTime(time, interval)
                    self.__processCandleFinished(interval)
                    self.__processCandleStarted(interval)

    def __registerCandleStartTime(self, time, interval):
        print 'Candle started : ', interval, time
        self.__intervalStartTimeDict[interval] = self.__roundToTimeInterval(time, interval)

    def __processCandleFinished(self, interval):
        if self.__candlesInProgressDict.has_key(interval):
            lastCandle = self.__candlesInProgressDict[interval]
            print '=========', lastCandle
            if not lastCandle.isEmpty(): self.publish(lastCandle)

    def __processCandleStarted(self, interval):
        newCandle = Candle()
        newCandle.candleInterval = interval
        newCandle.startTime = self.__intervalStartTimeDict[interval]
        self.__candlesInProgressDict[interval] = newCandle

    def __roundToTimeInterval(self, time, interval):
        diff = time - self.__startOfDay
        roundedSeconds = diff.seconds / CandleInterval.toSeconds(interval)
        roundedSeconds = roundedSeconds * CandleInterval.toSeconds(interval)
        res = datetime(year= self.__startOfDay.year,
                       month= self.__startOfDay.month,
                       day = self.__startOfDay.day,
                       hour= roundedSeconds / 3600,
                       minute= (roundedSeconds % 3600) / 60,
                       second= 0,
                       microsecond= 0 )

        print 'Rounded : ', interval, ' ', res
        return res

    def __fillStartOfDay(self, time):
        if self.__startOfDay == None:
            self.__setStartOfDay(time)
        else:
            diff = time - self.__startOfDay
            if diff > timedelta(hours = 24):
                self.__setStartOfDay(time)

    def __setStartOfDay(self, time):
        date = time.date()
        self.__startOfDay = datetime(year = date.year, month = date.month, day = date.day, hour = 0, minute = 0, second = 0)