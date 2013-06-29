from time import sleep
import unittest
from EventsQueue import AsynchEventsQueue


class AsynchEventsQueueTest(unittest.TestCase):

    def setUp(self):
        self.__eventsQueue = AsynchEventsQueue()

    def testNominalStart(self):
        self.__eventsQueue.start()
        sleep(2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AsynchEventsQueueTest)
    unittest.TextTestRunner(verbosity=2).run(suite)