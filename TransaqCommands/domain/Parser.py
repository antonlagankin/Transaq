from lxml import etree
import configuration as cfg
from domain.mappers.TagToDomainMap import getMappedDomainType

__author__ = 'anton'

def tryToPublish(publisher, itemToPublish):
    # if hasattr(publisher, 'publish'):
    #     publisher.publish(itemToPublish)
    if hasattr(publisher, 'pushInService'):
        publisher.pushInService(itemToPublish)

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

def parse(element):
    t = getMappedDomainType(element.tag)
    print "======", t
    if t is None:
        return None
        #item = t()
    item = cfg.cfg.Configuration().getObject(t)
    print item, "<==="
    result = item.parseXml(element)
    return result

def fillDomainObject(self, element):
    childIterator = etree.ElementChildIterator(element)
    fieldsToFill = dir(self)
    for item in childIterator:
        if item.tag in fieldsToFill:
            setattr(self, item.tag, item.text)

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
    item = cfg.cfg.Configuration().getObject(t)#t()
    print 'created item:', item
    converted = item.parseXml(element)
    return converted