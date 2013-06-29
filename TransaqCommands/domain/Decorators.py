from domain.mappers.TagToDomainMap import pushToDomainTagDict
from storages.Storages import StoragesRegistry

def registerInStorage(self):
    StoragesRegistry().push(self.__hash__(), self)

def MapsWithTag(tagName):
    def onDecorator(aClass):
        pushToDomainTagDict(tagName, aClass)
        return aClass
    return onDecorator

def MapsWithTags(tagNamesList):
    def onDecorator(aClass):
        for tagName in tagNamesList:
            pushToDomainTagDict(tagName, aClass)
        return aClass
    return onDecorator

def Registrable(aClass):
    aClass.register = registerInStorage
    return aClass

def AttributesInXml(propertiesList):
    def onDecorator(aClass):
        aClass.xmlAttributes = propertiesList
        return aClass
    return onDecorator

def ValueInXmlToPropertyName(propertyName):
    def onDecorator(aClass):
        aClass.valuePropertyName = propertyName
        return aClass
    return onDecorator

def ToBusinessEntityConverter(converterFunc):
    def onDecorator(aClass):
        aClass.converter = converterFunc
        return aClass
    return onDecorator

# def Reportable(queueName = '', topicName = ''):
#     def onDecorator(aClass):
#         aClass
#         return aClass
#     return onDecorator