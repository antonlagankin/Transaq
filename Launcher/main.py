import logging
import threading
from time import sleep
from Candles.CandleService import JapaneseCandleService
from Commands import Connect, GetServTimeDifference, Subscribe
from dll.Wrapper import initialize, testCallback, sendCommand
from services.TimeService import startService

__author__ = 'anton'

# t = getMappedDomainType('market')
# item = type(t())

logging.getLogger('pika').setLevel(logging.DEBUG)

# consumer = Consumer()
# consume()

t = threading.Thread(target=startService, args=[1])
t.daemon = True
t.start()
# startService(1)

cmd = Connect()
# hllDll.buyAtMarket()
logPath = '.\\0'
initialize(logPath, 3)
testCallback()
sleep(5)
sendCommand(cmd)

sleep(5)

serverTimeDiffCmd = GetServTimeDifference()
diffRes = sendCommand(serverTimeDiffCmd)


# hllDll.sendCommand(GetSecurities())
#
subscribe = Subscribe()
subscribe.alltrades.secid = 5
subscribe.quotations.secid = 5
subscribe.quotes.secid = 5
sendCommand(subscribe)

candleService = JapaneseCandleService()
candleService.start()

while True:
    sleep(1)

# hllDll.sendCommand(GetSecurities())
#
# a = ctypes.get_last_error()
#
# disconnect = Disconnect()
# print hllDll.sendCommand(disconnect)