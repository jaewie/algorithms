import itertools


class Set(object):

    def __init__(self, iterable=None):
        self._set = {}
        for e in iterable or []:
            self.add(e)

    def add(self, item):
        self._set[item] = True

    def remove(self, item):
        if not self.exists(item):
            raise KeyError(item)
        del self._set[item]

    def merge(self, set):
        return Set(itertools.chain(self, set))

    def diff(self, set):
        new_set = Set(self)
        for e in set:
            if new_set.exists(e):
                new_set.remove(e)
        return new_set

    def exists(self, item):
        return item in self._set

    def clear(self):
        self._set = {}

    def __iter__(self):
        for item in self._set:
            yield item

    def is_empty(self):
        return not self._set

    def __len__(self):
        return len(self._set)

    def __eq__(self, set):
        return isinstance(set, Set) and sorted(self) == sorted(set)
