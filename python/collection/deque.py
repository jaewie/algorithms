class Deque(object):

    class Node(object):
        def __init__(self, val):
            self.val = val
            self.next = self.prev = None

    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def append(self, val):
        node = self.Node(val)

        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._size += 1

    def appendleft(self, val):
        node = self.Node(val)

        if self._head is None:
            self._head = self._tail = node
        else:
            self._head.prev = node
            node.next = self._head
            self._head = node
        self._size += 1

    def pop(self):
        if self._tail is None:
            raise IndexError("pop from empty deque")

        item = self._tail

        if self._tail is self._head:
            self._tail = self._head = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._size -= 1
        return item

    def popleft(self):
        if self._head is None:
            raise IndexError("popleft from empty deque")

        item = self._head
        if self._head is self._tail:
            self._tail = self._head = None
        else:
            self._head = self._head.next

        self._size -= 1
        return item

    def __len__(self):
        return self._size
