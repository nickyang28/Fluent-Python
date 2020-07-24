# -*- coding: utf-8 -*-
from collections import defaultdict, OrderedDict, UserDict


class StrKeyDict(dict):
    # def __init__(self, *argv, **kwargs):
        # super().__init__(*argv, **kwargs)

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default


if __name__ == "__main__":
    d = StrKeyDict([('2', 'two'), ('4', "four")])
    print(d['2'])
    print(d[4])
    print(2 in d)
    print(1 in d)
    print(d.get(2))
    dd = StrKeyDict()
    dd["1"] = 'one'
    print(dd)

