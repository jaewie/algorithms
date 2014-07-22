class DisjointSet(object):
  def __init__(self, value, rank=0, parent=None):
    self.value = value
    self._rank = rank
    self.parent = parent if parent is not None else self

  @property
  def rank(self):
    return self._rank

  def find(self):
    # Path compression
    if self.parent is self:
      return self
    else:
      self.parent = self.parent.find()
      return self.parent

  def union(self, node):
    # Union by rank
    x = self.find()
    y = node.find()
    if x.rank > y.rank:
      y.parent = x.parent
    elif x.rank < y.rank:
      x.parent = y.parent
    else:
      x.parent = y.parent
      y._rank += 1
