from domain.DomainObjects import SecurityDomainObject, ServerStatus, OvernightStatus, CandleKind, Market, Client, MoneyPosition, SecurityPosition, Quote, Trade, parseDomainObjectsList, parse
import logging

# __parsers = {}
__logger = logging.getLogger('Transaq.DomainObjectFactories')

# def parseItemsList(reportAction = lambda list, queue : None, exchangeName = None):
#     def processList(element):
#         childIterator = etree.ElementChildIterator(element)
#         list = []
#         for item in childIterator:
#             list.append(callParser(item))
#         reportAction(list, exchangeName)
#         return list
#     return processList
#
# def parseSingleItem(itemType):
#     def processItem(element):
#             print 'parsing', itemType
#             t = getMappedDomainType(element.tag)
#             if t is None:
#                 return None
#             item = t()
#             print 'created item:', item
#             converted = item.parseXml(element)
#             return converted
#     return processItem
#
# # def parseItem(element):
# #     t = getMappedDomainType(element.tag)
# #     if t is None:
# #         return None
# #     item = t()
# #     print 'created item:', item
# #     converted = item.parseXml(element)
# #     return converted
#
# __parsers = {'securities' : parseItemsList(),
#              'security' : parseSingleItem(
#                  SecurityDomainObject),
#              'server_status' : parseSingleItem(ServerStatus),
#              'overnight' : parseSingleItem(OvernightStatus),
#              'candlekinds' : parseItemsList(),
#              'kind' : parseSingleItem(CandleKind),
#              'markets' : parseItemsList(),
#              'market' : parseSingleItem(
#                  Market),
#              'client' : parseSingleItem(Client),
#              'money_position' : parseSingleItem(MoneyPosition),
#              'positions' : parseItemsList(),
#              'sec_position' : parseSingleItem(SecurityPosition),
#              'quotes' : parseItemsList(publish, Channels.QUOTES),
#              'quote' : parseSingleItem(Quote),
#              'alltrades' : parseItemsList(publish, Channels.TRADES),
#              'trade' : parseSingleItem(Trade)}

def parseInputXml(root):
    print root
    return parse(root)
    # return callParser(root)

# def callParser(element):
#     print etree.tostring(element)
#     if __parsers.has_key(element.tag):
#         parser = __parsers[element.tag]
#         result = parser(element)
#         return result
#     return None