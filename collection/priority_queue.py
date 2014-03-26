class PriorityQueue(object):
    def __init__(self):
        self._heap = []

    def insert(self, val):
        self._heap.append(val)
        ind = len(self) - 1
        self.bubble_up(ind)
            
    def get_min(self):
        if self.is_empty():
            raise IndexError("There are no elements in the priority queue")
        return self._heap[0]
    
    def pop_min(self):
        if self.is_empty():
            raise IndexError("There are no elements in the priority queue")
        self[0], self[-1] = self[-1], self[0]
        min = self._heap.pop()
        self.bubble_down(0)
        return min
    
    def bubble_down(self, i):
        lc = 2 *i + 1
        rc = 2 *i + 2

        while lc < len(self) or rc < len(self):
            
            if lc >= len(self) or rc >= len(self) :
                child = min(lc, rc)
            elif self[lc] < self[rc]:
                child = lc
            else:
                child = rc
            
            if self[i] > self[child]:
                self[child], self[i] = self[i], self[child]
                i = child
            else:
                break
            lc = 2 *i + 1
            rc = 2 *i + 2    

    def bubble_up(self, i):
        par = (i - 1) / 2
        
        while par >= 0:
            if self[par] <= self[i]:
                break
            
            self[par], self[i] = self[i], self[par]
            i = par            
            par = (i - 1) / 2

    def is_empty(self):
        return not self._heap
    
    def __len__(self):
        return len(self._heap)

    def __getitem__(self, i):
        return self._heap[i]

    def __setitem__(self, i, value):
        self._heap[i] = value
