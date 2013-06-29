class Market:

    name = ''

    def __init__(self, marketName=''):
        self.name = marketName

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name