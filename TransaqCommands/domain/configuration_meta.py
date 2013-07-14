from pinsor import LifeStyle
# from domain.DomainObjects import SecurityDomainObject, ServerStatus, OvernightStatus, CandleKind, Market, Client, MoneyPosition, SecurityPosition, Quote, Trade, SimpleDomainObjectsList, SecuritiesDomainObjectsList, QuotesDomainObjectsList, TradesDomainObjectsList
from domain.DomainObjects import SecurityDomainObject

__author__ = 'anton'

def registerDomain(self):
    self.pinsor.addcomponent(
        SecurityDomainObject, lifestyle = LifeStyle.transient
    )
    # self.__pinsor.addcomponent(
    #     ServerStatus, lifestyle = LifeStyle.transient
    # )
    # self.__pinsor.addcomponent(
    #     OvernightStatus, lifestyle = LifeStyle.transient
    # )
    # self.__pinsor.addcomponent(
    #     CandleKind, lifestyle = LifeStyle.transient
    # )
    # self.__pinsor.addcomponent(
    #     Market, lifestyle = LifeStyle.transient
    # )
    # self.__pinsor.addcomponent(
    #     Client, lifestyle = LifeStyle.transient
    # )
    # self.__pinsor.addcomponent(
    #     MoneyPosition, lifestyle = LifeStyle.transient
    # )
    # self.__pinsor.addcomponent(
    #     SecurityPosition, lifestyle = LifeStyle.transient
    # )
    # self.__pinsor.addcomponent(
    #     Quote, lifestyle = LifeStyle.transient
    # )
    # self.__pinsor.addcomponent(
    #     Trade, lifestyle = LifeStyle.transient
    # )
    # self.__pinsor.addcomponent(
    #     SimpleDomainObjectsList, lifestyle = LifeStyle.transient
    # )
    # self.__pinsor.addcomponent(
    #     SecuritiesDomainObjectsList, lifestyle = LifeStyle.transient
    # )
    # self.__pinsor.addcomponent(
    #     QuotesDomainObjectsList, lifestyle = LifeStyle.transient
    # )
    # self.__pinsor.addcomponent(
    #     TradesDomainObjectsList, lifestyle = LifeStyle.transient
    # )

# class ConfigrationMeta(type):
#
#     def __new__(meta, classname, supers, classdict):
#         # classdict['registerDomain'] = registerDomain
#         return type.__new__(meta, classname, supers, classdict)
