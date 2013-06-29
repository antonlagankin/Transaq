from storages.Storages import StoragesRegistry

class Registrable1:

    def __init__(self, aClass):
        self.__classToCreate = aClass

    def __call__(self, *args, **kwargs):
        res = self.__classToCreate()
        print 'registrable instance:', res
        StoragesRegistry().push(repr(res), res)
        return res