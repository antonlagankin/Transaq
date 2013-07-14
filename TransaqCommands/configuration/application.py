import logging
from pinsor import PinsorContainer, Component
import threading
from time import sleep
from Candles.CandleService import JapaneseCandleService
from Commands import Connect, GetServTimeDifference, Subscribe
from Trades.TradesService import TradesService
from configuration.cfg import Configuration
from dll.Wrapper import initialize, testCallback, sendCommand
from services.TimeService import startService
from domain.DomainObjects import DomainObjectMeta

__author__ = 'anton'

class App(object):
    _instance = None
    __configuration = None
    pinsor = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(App, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialize()
        return  cls._instance

    def __initialize(self):
        self.pinsor = PinsorContainer()

        self.__configuration = Configuration()
        self.__configuration.registerServices()

    def __init__(self):
        pass

        # self.__registerCandlesService()
        # self.__registerTradesService()
        # self.registerDomain()

    # def __registerCandlesService(self):
    #     self.pinsor.register(
    #         Component.oftype(JapaneseCandleService)
    #     )
    #
    # def __registerTradesService(self):
    #     self.pinsor.register(
    #         Component.oftype(TradesService)
    #     )
    #
    # def getObject(self, t):
    #     return self.pinsor.resolve(t)

    def start(self):
    # t = getMappedDomainType('market')
    # item = type(t())

        logging.getLogger('pika').setLevel(logging.DEBUG)

        # consumer = Consumer()
        # consume()

        t = threading.Thread(target=startService, args=[1])
        t.daemon = True
        t.start()
        # startService(1)

        cmd = Connect()
        # hllDll.buyAtMarket()
        logPath = '.\\0'
        initialize(logPath, 3)
        testCallback()
        sleep(5)
        sendCommand(cmd)

        sleep(5)

        serverTimeDiffCmd = GetServTimeDifference()
        diffRes = sendCommand(serverTimeDiffCmd)


        # hllDll.sendCommand(GetSecurities())
        #
        subscribe = Subscribe()
        subscribe.alltrades.secid = 5
        subscribe.quotations.secid = 5
        subscribe.quotes.secid = 5
        sendCommand(subscribe)

        candleService = JapaneseCandleService()
        candleService.start()
