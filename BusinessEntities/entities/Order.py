class OrderType(object):

    LIMIT = 0

class OrderDirection(object):

    BUY = 'buy'
    SELL = 'sell'

class Order(object):

    def __init__(self):
        self.security = None
        self.orderType = OrderType.LIMIT
        self.price = 0.0
        self.direction = OrderDirection.BUY
        self.quantity = 0

    def withSecurity(self, security):
        self.security = security
        return self

    def withOrderType(self, orderType):
        self.orderType = orderType
        return self

    def withDirection(self, direction):
        self.direction = direction
        return self

    def withQuantity(self, quantity):
        self.quantity = quantity
        return self