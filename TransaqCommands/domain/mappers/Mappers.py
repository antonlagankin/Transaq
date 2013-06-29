from domain.converters.business import toMarket

class DomainBusinessMapper:

    __dictDomainBusiness = {}
    __dictBusinessDomain = {}
    __domainToBusinessMapper = None

    def __init__(self, domainToBusinessMapper):
        self.__domainToBusinessMapper = domainToBusinessMapper

    def pushDomainGetBusiness(self, domain):
        business = self.__domainToBusinessMapper(domain)
        self.__dictBusinessDomain[business] = domain
        self.__dictDomainBusiness[domain] = business
        return business

    def getByDomain(self, domain):
        return self.__dictDomainBusiness[domain]

    def getByBusiness(self, business):
        return self.__dictBusinessDomain(business)