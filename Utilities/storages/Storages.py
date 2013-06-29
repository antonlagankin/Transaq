class Storage:

    __storageDict = {}

    def push(self, key, item):
        self.__storageDict[key] = item

    def get(self, key):
        return self.__storageDict[key]

class StoragesRegistry:

    __storage = {}
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super.__new__(cls, *args, **kwargs)
        return cls.__instance

    def push(self, key, item):
        itemType = type(item)
        if not self.__storage.has_key(itemType):
            self.__storage[itemType] = {}
        print 'pushing', self.__storage, 'item=', unicode(item), 'key=', key, 'key type=', type(key)
        self.__storage[itemType][key] = item

    def get(self, t, key):
        print 'getting', t, key, 'from', self.__storage
        print 'type storage:', self.__storage[t], 'key type=', type(key)
        return self.__storage[t][key]