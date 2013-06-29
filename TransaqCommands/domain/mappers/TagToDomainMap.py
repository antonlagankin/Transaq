__tagToDomainDict = {}#{'market' : Market,
                    # 'security' : SecurityDomainObject}

def getMappedDomainType(tagName):
    if __tagToDomainDict.has_key(tagName):
        return __tagToDomainDict[tagName]
    return None

def pushToDomainTagDict(tagName, t):
    __tagToDomainDict[tagName] = t