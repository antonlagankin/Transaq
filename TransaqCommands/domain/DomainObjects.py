from lxml import etree
from Trades.TradesService import TradesService
# from configuration.cfg import Configuration, registerAsComponent
# from configuration.decorators import PushInService
from domain.Decorators import Registrable, MapsWithTag, AttributesInXml, ToBusinessEntityConverter, ValueInXmlToPropertyName, MapsWithTags
# from domain.Parser import tryToPublish
import Parser
from domain.converters.business import toSecurity, toMarket, toTrade
from domain.mappers.TagToDomainMap import getMappedDomainType
from pinsor import LifeStyle

class DomainObjectMeta(type):

    def __new__(meta, classname, supers, classdict):
        classdict['__fillDomainObject'] = Parser.fillDomainObject
        classdict['parseXml'] = Parser.parseXml
        return type.__new__(meta, classname, supers, classdict)

class DomainObjectBase(object):

    __metaclass__ = DomainObjectMeta

@Registrable
@MapsWithTag('security')
@AttributesInXml(['secid', 'active'])
@ToBusinessEntityConverter(toSecurity)
class SecurityDomainObject(DomainObjectBase):

    def __init__(self):
        self.secid = 0
        self.active = False
        self.seccode = ''
        self.market = ''
        self.shortname = ''
        self.decimals = 0.0
        self.minstep = 0.0
        self.lotsize = 0
        self.point_cost = 0.0
        self.sectype = ''

    def __dir__(self):
        return ['active', 'seccode', 'market', 'shortname', 'decimals', 'minstep', 'lotsize', 'point_cost', 'sectype']

    def __str__(self):
        s = ' '.join(('SecurityDomainObject',
                      str(self.active),
                      self.seccode,
                      self.shortname,
                      self.market,
                      self.shortname,
                      str(self.decimals),
                      str(self.minstep),
                      str(self.lotsize),
                      str(self.point_cost),
                      self.sectype))
        return s

    def __repr__(self):
        return self.secid

    def __hash__(self):
        return int(self.secid)

@MapsWithTag('server_status')
@AttributesInXml(['id', 'connected', 'recover'])
class ServerStatus(DomainObjectBase):

    id = 0
    connected = False
    recover = False

    def __str__(self):
        return ' '.join(('ServerStatus', str(self.id), str(self.connected), str(self.recover is not None if self.recover else '')))

@MapsWithTag('overnight')
@AttributesInXml('status')
class OvernightStatus(DomainObjectBase):

    status = False

    def __str__(self):
        return ' '.join(('Overnight status : ', str(self.status)))

@MapsWithTag('kind')
class CandleKind(DomainObjectBase):
    id = 0
    period = ''
    name = ''

    def __dir__(self):
        return ['id', 'period', 'name']

@Registrable
@MapsWithTag('market')
@AttributesInXml(['id'])
@ToBusinessEntityConverter(toMarket)
@ValueInXmlToPropertyName('name')
class Market(DomainObjectBase):

    __metaclass__ = DomainObjectMeta

    id = 0
    name = ''

    def __hash__(self):
        return int(self.id)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

@MapsWithTag('client')
@AttributesInXml(['id', 'remove'])
class Client(DomainObjectBase):

    id = 0
    remove = False
    type = None
    currency = None
    ml_intraday = None
    ml_overnight = None
    ml_restrict = None
    ml_call = None
    ml_close = None

    def __dir__(self):
        return ['type', 'currency', 'ml_intraday', 'ml_overnight', 'ml_restrict', ' ml_call', 'ml_close'];

class MoneyPosition(DomainObjectBase):
    client = None
    markets = []
    asset = None
    shortname = None
    saldoin = None
    bought = None
    sold = None
    saldo = None
    ordbuy = None
    ordbuycond = None
    comission = None

    def __dir__(self):
        return ['client', 'asset', 'shortname', 'saldoin', 'bought', 'sold', 'saldo', 'ordbuy', 'ordbuycond', 'comission']

class SecurityPosition(DomainObjectBase):
    client = None
    secid = None
    shortname = None
    saldoin = None
    saldomin = None
    bought = None
    sold = None
    saldo = None
    ordbuy = None
    ordsell = None

    def __dir__(self):
        return ['client', 'secid', 'shortname', 'saldoin', 'saldomin', 'bought', 'sold', 'saldo', 'ordbuy', 'ordsell']

@MapsWithTag('quote')
@AttributesInXml('secid')
class Quote(DomainObjectBase):

    secid = 0
    price = 0
    buy = 0
    sell = 0

    def __dir__(self):
        return ['price', 'buy', 'sell']

# @PushInService(TradesService)
@MapsWithTag('trade')
@AttributesInXml('secid')
@ToBusinessEntityConverter(toTrade)
class Trade(DomainObjectBase):

    secid = 0
    tradeno = 0
    time = 0
    board = 0
    price = 0
    quantity = 0
    buysell = ''
    openinterest = 0
    period = ''

    def __dir__(self):
        return ['tradeno', 'time', 'board', 'price', 'quantity', 'buysell', 'openinterest', 'period']

    def __str__(self):
        return 'Trade===== : ' + str(self.price)

# def parseDomainObjectsList(self, element):
#     childIterator = etree.ElementChildIterator(element)
#     list = []
#     for item in childIterator:
#         list.append(parseSingleItem(item))
#     tryToPublish(self, list)
#     return list
#
# def parseSingleItem(element):
#     print element.tag
#     t = getMappedDomainType(element.tag)
#     print 'parsing', t
#     if t is None:
#         return None
#     item = cfg.cfg.Configuration().getObject(t)#t()
#     print 'created item:', item
#     converted = item.parseXml(element)
#     return converted

class DomainObjectsListMeta(type):

    def __new__(meta, classname, supers, classdict):
        classdict['parseXml'] = Parser.parseDomainObjectsList
        return type.__new__(meta, classname, supers, classdict)

class DomainObjectsListBase(object):

    __metaclass__ = DomainObjectsListMeta

@MapsWithTags(['markets', 'candlekinds'])
class SimpleDomainObjectsList(DomainObjectsListBase):
    pass

@MapsWithTag('securities')
# @Publisher(Channels.SECURITIES)
class SecuritiesDomainObjectsList(DomainObjectsListBase):
    pass

@MapsWithTag('quotes')
# @Publisher(Channels.QUOTES)
class QuotesDomainObjectsList(DomainObjectsListBase):
    pass

# @PushInService(TradesService)
@MapsWithTag('alltrades')
# @Publisher(Channels.TRADES)
class TradesDomainObjectsList(DomainObjectsListBase):
    pass