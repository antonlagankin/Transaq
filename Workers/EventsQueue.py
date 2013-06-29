from Queue import Queue
from threading import Event, Thread

__author__ = 'antonlagankin'

class AsynchEventsQueue :

    def __init__(self):
        self.__queueNotEmptyEvent = Event()
        self.__queue = Queue(1024)

    def process(self):
        while True:
            self.__queueNotEmptyEvent.wait()
            self.__processExistingEvents()

    def __processExistingEvents(self):
        while self.__queue.qsize() > 0:
            cmd = self.__queue.get()
            cmd.execute()

    def push(self, command):
        self.__queue.put(command)
        self.__queueNotEmptyEvent.set()

    def start(self):
        t = Thread(target = self.process, args = (self))
        t.daemon = True
        t.start()