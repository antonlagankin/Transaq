from lxml import etree

def startRequestResultTag(self, tag, attrs):
    if 'result' == tag.lower():
        self.success = attrs['success'].lower() == 'true'
        if (attrs.has_key('diff')):
            self.diff = int(attrs['diff'])
    if 'message' == tag.lower():
        self.message = etree.tostring(tag)

def endRequestResultTag(self, tag):
    self.isMessage = False

def dataRequestResultTag(self, data):
    if self.isMessage:
        self.errorMessage = data

def closeRequestResultTag(self):
    return self

class RequestResultMeta(type):

    def __new__(meta, classname, supers, classdict):
        classdict['start'] = startRequestResultTag
        classdict['end'] = endRequestResultTag
        classdict['data'] = dataRequestResultTag
        classdict['close'] = closeRequestResultTag
        return type.__new__(meta, classname, supers, classdict)

class RequestResult(object):

    __metaclass__ = RequestResultMeta

    def __init__(self):
        self.success = False

def toXml(self):
    commandElem = etree.Element('command', id = self.id)
    res = etree.tostring(self.__processRootElement(commandElem))
    return res

def processRootElement(self, element):
    command = etree.ElementTree(element)
    for property in dir(self):
        prop = getattr(self, property)
        if isinstance(prop, BaseTransaqCommand):
            childElement = etree.SubElement(element, property)
            prop.__processRootElement(childElement)
            # self.__processRootElement(childElement, prop)
        else:
            elem = etree.SubElement(element, property)
            elem.text = str(prop)

    return element

class TransaqCommandMeta(type):

    def __new__(meta, classname, supers, classdict):
        classdict['generateXml'] = toXml
        classdict['__processRootElement'] = processRootElement
        return type.__new__(meta, classname, supers, classdict)

class BaseTransaqCommand(object):

    __metaclass__ = TransaqCommandMeta

    def __init__(self, id):
        self.id = id
        self.__currentTag = ''

    def __dir__(self):
        return []

class Connect(BaseTransaqCommand):

    def __init__(self):
        self.login = '000000162918'
        self.password = 'uc3AK9'
        self.host = '78.41.194.46'
        self.port  = 3950
        self.autopos = True
        BaseTransaqCommand.__init__(self, 'connect')

    def __dir__(self):
        return ['login', 'password', 'host', 'port', 'autopos']

class Disconnect(BaseTransaqCommand):

    def __init__(self):
        BaseTransaqCommand.__init__(self, 'disconnect')

class Status(BaseTransaqCommand):

    def __init__(self):
        BaseTransaqCommand.__init__(self, 'server_status')

class GetSecurities(BaseTransaqCommand):

    def __init__(self):
        BaseTransaqCommand.__init__(self, 'get_securities')

class AllTrades(BaseTransaqCommand):

    def __init__(self):
        self.secid = None
        BaseTransaqCommand.__init__(self, '')

    def __dir__(self):
        return ['secid'];

class Quotations(BaseTransaqCommand):

    def __init__(self):
        self.secid = None
        BaseTransaqCommand.__init__(self, '')

    def __dir__(self):
        return ['secid'];

class Quotes(BaseTransaqCommand):

    def __init__(self):
        self.secid = None
        BaseTransaqCommand.__init__(self, '')

    def __dir__(self):
        return ['secid'];

class Subscribe(BaseTransaqCommand):

    def __init__(self):
        self.alltrades = AllTrades()
        self.quotations = Quotations()
        self.quotes = Quotes()
        BaseTransaqCommand.__init__(self, 'subscribe')

    def __dir__(self):
        return ['alltrades', 'quotations', 'quotes']

class Unsubscribe(BaseTransaqCommand):

    def __init__(self):
        BaseTransaqCommand.__init__(self, 'unsubscribe')

class GetServTimeDifference(BaseTransaqCommand):

    def __init__(self):
        BaseTransaqCommand.__init__(self, 'get_servtime_difference')


