class PriorityQueue(object):
    def __init__(self):
        self.heap = []
        self.locations = {}

    def put(self, ele, priority):
        self.heap.append((priority, ele))
        self.locations[ele] = len(self.heap) - 1
        self._bubble_up(len(self.heap) - 1)

    def get(self):
        if self.empty():
            raise IndexError("get from empty heap")

        self._swap(0, len(self.heap) - 1)
        priority, ele = self._pop()
        self._bubble_down(0)

        return (ele, priority)

    def update(self, ele, new_priority):
        location = self.locations[ele]
        old_priority, _ = self.heap[location]

        self.heap[location] = (new_priority, ele)

        if new_priority < old_priority:
            self._bubble_up(location)
        else:
            self._bubble_down(location)

    def empty(self):
        return not self.heap

    def _bubble_down(self, ind):
        length = len(self.heap)
        heap = self.heap
        locations = self.locations

        while True:
            lc, rc = self._left_child(ind), self._right_child(ind)
            if lc >= length and rc >= length:
                break
            elif lc >= length:
                replace = rc
            elif rc >= length:
                replace = lc
            else:
                replace = min(lc, rc, key=lambda i: self.heap[i])

            if heap[replace] < heap[ind]:
                self._swap(ind, replace)
                ind = replace
            else:
                break

    def _bubble_up(self, ind):
        par = self._parent(ind)
        heap = self.heap

        while par >= 0:
            if heap[ind] < heap[par]:
                self._swap(ind, par)
                ind = par
                par = self._parent(ind)
            else:
                break

    def _parent(self, ind):
        return (ind - 1) // 2

    def _left_child(self, ind):
        return (ind * 2) + 1

    def _right_child(self, ind):
        return (ind * 2) + 2

    def __len__(self):
        return len(self.heap)

    def _swap(self, i, j):
        _, item0 = self.heap[i]
        _, item1 = self.heap[j]

        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

        self.locations[item0] = j
        self.locations[item1] = i

    def _pop(self):
        priority, ele = self.heap.pop()
        self.locations.pop(ele)
        return (priority, ele)
