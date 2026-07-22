from random import randint

RANDOM = randint(0, 1 << 62)

class SafeDict(dict):
    def __key(self, k):
        if isinstance(k, int):
            return k ^ RANDOM
        return k

    def __setitem__(self, k, v):
        super().__setitem__(self.__key(k), v)

    def __getitem__(self, k):
        return super().__getitem__(self.__key(k))

    def get(self, k, default=None):
        return super().get(self.__key(k), default)

    def __contains__(self, k):
        return super().__contains__(self.__key(k))

    def pop(self, k, *args):
        return super().pop(self.__key(k), *args)