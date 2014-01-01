class Set(object):
    def __init__(self):
        self._set = {}
    
    def add(self, item):
        self._set[item] = True
    
    def remove(self, item):
        del self._set[item]
    
    def union(self, set):
        return [item for item in set if item in self._set]
    
    def merge(self, set):
        for key in set:
            self._set[key] = True
    
    def diff(self, set):
        return [item for item in self._set if item not in set]

    def exists(self, item):
        return self._set.get(item, False)
    
    def clear(self):
        self._set = {}
    
    def __iter__(self):
        for item in self._set:
            yield item