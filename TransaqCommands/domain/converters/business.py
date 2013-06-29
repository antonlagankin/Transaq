import datetime
import domain
from entities.Market import Market
from entities.Security import Security, SecurityType
from entities.Trade import Trade
from entities.entities import TradeDirection
from storages.Storages import StoragesRegistry

def toMarket(self):
    print 'converting market', self.name
    r = Market(self.name)
    print 'result:', r.name
    return r

def fromMarket(market):
    market = domain.DomainObjects.Market()
    market.name =  market.name
    return market

def toSecurityType(type):
    if 'SHARE' == type.upper():
        return SecurityType.SHARE
    elif 'BOND' == type.upper():
        return SecurityType.BOND
    elif 'FUT' == type.upper():
        return SecurityType.FUT
    elif 'OPT' == type.upper():
        return SecurityType.OPT
    elif 'GKO' == type.upper():
        return SecurityType.GKO
    return SecurityType.FOB

def fromSecurityType(type):
    return {
        SecurityType.SHARE : 'SHARE',
        SecurityType.BOND : 'BOND',
        SecurityType.FUT : 'FUT',
        SecurityType.GKO : 'GKO',
        SecurityType.OPT : 'OPT'
    }.get(type, None)

def toSecurity(self):
    print 'converting', unicode(self)
    security = Security(self.seccode,
                        self.shortname,
                        int(self.decimals),
                        float(self.minstep),
                        int(self.lotsize),
                        float(self.point_cost),
                        toSecurityType(self.sectype),
                        toMarket(StoragesRegistry().get(domain.DomainObjects.Market, int(self.market))))
    return security

def toTradeDirection(direction):
    if 'B' == direction:
        return TradeDirection.BUY
    return TradeDirection.SELL

def toTrade(self):
    trade = Trade(toSecurity(StoragesRegistry().get(domain.DomainObjects.SecurityDomainObject, int(self.secid))),
                  self.tradeno,
                  datetime.datetime.strptime(self.time, '%d.%m.%Y %H:%M:%S'),
                  self.board,
                  float(self.price),
                  int(self.quantity),
                  toTradeDirection(self.buysell),
                  self.openinterest,
                  self.period)
    return trade