class Trie(object):
  def __init__(self):
    self._trie = {}

  def insert(self, text):
    trie = self._trie
    for char in text:
      if char not in trie:
        trie[char] = {}
      trie = trie[char]
  
  def exists(self, text):
    trie = self._trie
    for char in text:
      if char not in trie:
        return False
      trie = trie[char]
    return True

  def __str__(self):
    return ', '.join(self.__get_strs(self._trie))

  def __get_strs(self, d):
    if not d:
      return ['']

    res = []
    for char in d:
      child_res = self.__get_strs(d[char])
      res.extend([char + s for s in child_res])
    return res

