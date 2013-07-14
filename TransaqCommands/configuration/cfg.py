from pinsor import Component, LifeStyle, PinsorContainer
from Candles.CandleService import JapaneseCandleService
from Trades.TradesService import TradesService
from domain.DomainObjects import SimpleDomainObjectsList, Market, CandleKind, ServerStatus, QuotesDomainObjectsList, OvernightStatus, Client, SecuritiesDomainObjectsList, Quote, SecurityDomainObject

__author__ = 'anton'

def registerAsComponent(function):
    def decorator(self):
        return function(self)
    return decorator

class Configuration(object):

    _instance = None
    pinsor = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Configuration, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialize()
        return cls._instance

    def __initialize(self):
        self.pinsor = PinsorContainer()

    def registerServices(self):
        self.__registerCandlesService()
        self.__registerTradesService()
        self.__registerComponents()

    def __registerCandlesService(self):
        self.pinsor.register(
            Component.oftype(JapaneseCandleService)
    )

    def __registerTradesService(self):
        self.pinsor.register(
            Component.oftype(TradesService)
        )

    def getObject(self, t):
        return self.pinsor.resolve(t)

    def __registerComponents(self):
        self.registerComponent(SimpleDomainObjectsList)
        self.registerComponent(Market)
        self.registerComponent(CandleKind)
        self.registerComponent(ServerStatus)
        self.registerComponent(QuotesDomainObjectsList)
        self.registerComponent(OvernightStatus)
        self.registerComponent(Client)
        self.registerComponent(SecuritiesDomainObjectsList)
        self.registerComponent(Quote)
        self.registerComponent(SecurityDomainObject)

    def registerComponent(self, component):
        self.pinsor.addcomponent(
            component, lifestyle = LifeStyle.transient
        )