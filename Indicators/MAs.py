class EMA(object):

    def __init__(self):
        self.length = 0
        self.__array = []
        self.values = []

    def push(self, value):
        if self.isFormed():
            self.__array.pop(0)
        self.__array.append(value)
        self.values.append(self.__recalc())

    def isFormed(self):
        return len(self.__array) >= self.length

    def __recalc(self):
        koef = 2.0 / (self.length + 1.0)
        result = self.__array[0]#0.0
        for item in self.__array:
            result = item * koef + result * (1.0 - koef)
        return result

    def __getitem__(self, item):
        return self.values[item]