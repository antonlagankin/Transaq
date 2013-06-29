class ComplexIndicator(object):

    indicators = []

    def push(self, value):
        for indicator in self.indicators:
            indicator.push(value)

    def isFormed(self):
        for indicator in self.indicators:
            if not indicator.isFormed():
                return False
        return True