from ctypes import *
import ctypes
from lxml import etree
from Commands import RequestResult
from dll.factories.DomainObjectFatories import parseInputXml
# from Decorators import serverFunction

CALLBACKFUNC = WINFUNCTYPE(ctypes.c_bool, POINTER(ctypes.c_byte))

__hllDll = ctypes.WinDLL('txmlconnector.dll')
__hllDll.SendCommand.restype = ctypes.c_char_p
print 'initializing wrapper object'

def initialize(logPath, logLevel):
    return __hllDll.Initialize(logPath, logLevel)

def sendCommand(command):
    result = __hllDll.SendCommand(command.generateXml())
    resultObj = RequestResult()
    parser = etree.XMLParser(target = resultObj)
    etree.XML(result, parser)
    return resultObj

def freeMemory():
    raise NotImplementedError()

def unInitialize():
    raise NotImplementedError()

def setLogLevel(logLevel):
    raise NotImplementedError()

def testCallback():
    __hllDll.SetCallback(callback)

# @serverFunction
def buyAtMarket():
    print 'buyAtMarket'
    return None

# _factory = AbstractCallbackObjectFactory()

# class HllDll(object):
#
#     __hllDll = ctypes.WinDLL('txmlconnector.dll')
#
#     def __init__(self):
#         self.__hllDll.SendCommand.restype = ctypes.c_char_p
#
#     def initialize(self, logPath, logLevel):
#         return self.__hllDll.Initialize(logPath, logLevel)
#
#     def sendCommand(self, command):
#         result = self.__hllDll.SendCommand(command.generateXml())
#         resultObj = RequestResult()
#         parser = etree.XMLParser(target = resultObj)
#         etree.XML(result, parser)
#         return resultObj
#
#     def freeMemory(self):
#         raise NotImplementedError()
#
#     def unInitialize(self):
#         raise NotImplementedError()
#
#     def setLogLevel(self, logLevel):
#         raise NotImplementedError()
#
#     def testCallback(self):
#         self.__hllDll.SetCallback(callback)
#
#     @serverFunction
#     def buyAtMarket(self):
#         return None
#
# # _factory = AbstractCallbackObjectFactory()

@CALLBACKFUNC
def callback(data):
    stringRes = cast(data, c_char_p).value
    # print stringRes
    parsedDomainObjectsList = parseInputXml(etree.XML(stringRes))
    # print parsedDomainObjectsList
    return True