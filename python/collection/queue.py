class Queue(object):

    def __init__(self):
        self._head = None
        self._tail = None

    class Node(object):

        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

    def enqueue(self, val):
        node = self.Node(val)

        if not self._tail:
            self._head = self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = self._tail.next

    def dequeue(self):
        if not self._head:
            raise IndexError("Dequeue from empty queue")

        node = self.peek()

        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        return node.val

    def peek(self):
        return self._head

    def is_empty(self):
        return self._head is None

    def __len__(self):
        count = 0
        head = self._head
        while head:
            count += 1
            head = head.next
        return count
