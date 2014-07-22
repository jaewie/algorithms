class PriorityQueue(object):
  def __init__(self):
    self.heap = []

  def put(self, ele):
    self.heap.append(ele)
    self.bubble_up(len(self.heap) - 1)

  def get(self):
    if self.empty():
      raise IndexError("get from empty heap")
    self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
    num =  self.heap.pop()
    self.bubble_down(0)
    return num

  def bubble_down(self, ind):
    length = len(self.heap)
    heap = self.heap

    while True:
      lc, rc = self.left_child(ind), self.right_child(ind)
      if lc >= length and rc >= length:
        break
      elif lc >= length:
        replace = rc
      elif rc >= length:
        replace = lc
      else:
        replace = min(lc, rc, key=lambda i: self.heap[i])
      
      if heap[replace] < heap[ind]:
        heap[ind], heap[replace] = heap[replace], heap[ind]
        ind = replace
      else:
        break

  def bubble_up(self, ind):
    par = self.parent(ind)
    heap = self.heap

    while par >= 0:
      if heap[ind] < heap[par]:
        heap[ind], heap[par] = heap[par], heap[ind]
        ind = par
        par = self.parent(ind)
      else:
        break

  def empty(self):
    return not self.heap

  def parent(self, ind):
    return (ind - 1) // 2

  def left_child(self, ind):
    return (ind * 2) + 1

  def right_child(self, ind):
    return (ind * 2) + 2

  def __len__(self):
      return len(self.heap)

  def __getitem__(self, i):
      return self.heap[i]

  def __setitem__(self, i, value):
      self.heap[i] = value
