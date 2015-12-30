class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self) <= 0:
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)

    def is_empty(self):
        return not self.stack

    def peek(self):
        if len(self) <= 0:
            raise IndexError("Peek from empty stack")

        return self.stack[-1]
