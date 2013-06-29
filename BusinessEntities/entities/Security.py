from errors.Exceptions import ObjectCreationDisabled

__author__ = 'anton'

class SecurityType:

    SHARE = 0
    BOND = 1
    FUT = 2
    OPT = 3
    GKO = 4
    FOB = 5

    def __init__(self):
        raise ObjectCreationDisabled()

# @Registrable
class Security:
    seccode = ''
    shortname = ''
    decimals = 0.0
    minstep = 0.0
    lotsize = 0
    point_cost = 0.0
    sectype = None
    market = ''

    def __init__(self, seccode, shortname, decimals, minstep, lotsize, point_cost, sectype, market):
        self.seccode = seccode
        self.shortname = shortname
        self.decimals = decimals
        self.minstep = minstep
        self.lotsize = lotsize
        self.point_cost = point_cost
        self.sectype = sectype
        self.market = market

    def __repr__(self):
        return self.seccode

