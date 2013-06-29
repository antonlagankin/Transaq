from lxml import etree
from domain.Decorators import Registrable, MapsWithTag, AttributesInXml, ToBusinessEntityConverter, ValueInXmlToPropertyName, MapsWithTags
from domain.converters.business import toSecurity, toMarket, toTrade
from domain.mappers.TagToDomainMap import getMappedDomainType
# from messaging.Channels import Channels
# from messaging.Publisher import Publisher

def tryToPublish(publisher, itemToPublish):
    if hasattr(publisher, 'publish'):
        publisher.publish(itemToPublish)

def parseXml(self, element):
    self.__fillDomainObject(element)
    if hasattr(self, 'xmlAttributes'):
        for property in self.xmlAttributes:
            setattr(self, property, element.get(property))
    if hasattr(self, 'valuePropertyName') and self.valuePropertyName is not None:
        setattr(self, self.valuePropertyName, element.text)
    if hasattr(self, 'register'):
        self.register()
    converted = None
    if hasattr(self, 'converter'):
        print 'converter:', self.converter
        converted = self.converter()
        tryToPublish(self, converted)
    return converted if converted is not None else self

def fillDomainObject(self, element):
    childIterator = etree.ElementChildIterator(element)
    fieldsToFill = dir(self)
    for item in childIterator:
        if item.tag in fieldsToFill:
            setattr(self, item.tag, item.text)

class DomainObjectMeta(type):

    def __new__(meta, classname, supers, classdict):
        classdict['__fillDomainObject'] = fillDomainObject
        classdict['parseXml'] = parseXml
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
        return int(self.id)#id * 31 + self.__hash__();

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

def parse(element):
    t = getMappedDomainType(element.tag)
    if t is None:
        return None
    item = t()
    result = item.parseXml(element)
    return result

def parseDomainObjectsList(self, element):
    childIterator = etree.ElementChildIterator(element)
    list = []
    for item in childIterator:
        list.append(parseSingleItem(item))
    tryToPublish(self, list)
    return list

def parseSingleItem(element):
    print element.tag
    t = getMappedDomainType(element.tag)
    print 'parsing', t
    if t is None:
        return None
    item = t()
    print 'created item:', item
    converted = item.parseXml(element)
    return converted

class DomainObjectsListMeta(type):

    def __new__(meta, classname, supers, classdict):
        classdict['parseXml'] = parseDomainObjectsList
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

@MapsWithTag('alltrades')
# @Publisher(Channels.TRADES)
class TradesDomainObjectsList(DomainObjectsListBase):
    pass

