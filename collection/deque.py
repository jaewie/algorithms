class Deque(object):

  class Node(object):
    def __init__(self, val):
      self.val = val
      self.next = None
      self.prev = None

  def __init__(self):
    self._head = None
    self._tail = None
    self._count = 0
  
  def append(self, val):
    node = self.Node(val)

    if self._tail is None:
      self._head = self._tail = node
    else:
      self._tail.next = node
      node.prev = self._tail
      self._tail = node

    self._count += 1
 
  def appendleft(self, val):
    node = self.Node(val)

    if not self._head:
      self._head = self._tail = node
    else:
      self._head.prev = node
      node.next = self._head
      self._head = node
      self._count += 1

  def pop(self):
    if not self._tail:
      raise IndexError("pop from empty deque")

    item = self._tail
    self._tail = self._tail.prev
    self._tail.next = None
    self._count -= 1
    return item


  def popleft(self):
    if not self._head:
      raise IndexError("popleft from empty deque")

    item = self._head
    self._head = self._head.next
    self._head.prev = None
    self._count -= 1
    return item

  @property
  def count(self):
    return self._count
