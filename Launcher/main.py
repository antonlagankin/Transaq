from time import sleep
from configuration.application import App

__author__ = 'anton'

if __name__ == '__main__':
    App().start()
    while True:
        sleep(1)