ENDS_HERE = '__ENDS_HERE'


class Trie(object):

    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]

        trie[ENDS_HERE] = True

    def exists(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                return False
            trie = trie[char]

        return ENDS_HERE in trie

    def elements(self):
        return self._elements(self._trie)

    def _elements(self, d):
        result = []

        for c, v in d.items():
            if c == ENDS_HERE:
                subresult = ['']
            else:
                subresult = [c + s for s in self._elements(v)]

            result.extend(subresult)

        return result
