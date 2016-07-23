class Queue(object):

    def __init__(self):
        self.front = []
        self.back = []

    def enqueue(self, val):
        self.back.append(val)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        if not self.front:
            while self.back:
                self.front.append(self.back.pop())
        return self.front.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        return self.front[-1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.front) + len(self.back)
