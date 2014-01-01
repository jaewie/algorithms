class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self, val):
        node = Node(val)
        
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
            
    def dequeue(self):
        if not self.head:
            raise Exception("Dequeue from empty queue")
        
        node = self.peek()
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return node.val

    def peek(self):
        return self.head


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
