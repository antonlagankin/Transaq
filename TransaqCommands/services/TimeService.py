from datetime import datetime, timedelta
import sched
import time
from messaging.Channels import Channels
from messaging.Publisher import publishItem

__scheduler = sched.scheduler(time.time, time.sleep)

def __timeChanged(timeShiftInSeconds):
    now = datetime.now()
    serverTime = now + timedelta(seconds = timeShiftInSeconds)
    publishItem(Channels.TIME, serverTime)
    __scheduleNextRun([timeShiftInSeconds])

def __scheduleNextRun(timeShiftInSeconds):
    __scheduler.enter(0.5, 1, __timeChanged, timeShiftInSeconds)

def startService(timeShiftInSeconds):
    __scheduleNextRun([timeShiftInSeconds])
    __scheduler.run()