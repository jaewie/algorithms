from numpy import zeros


class DynamicArray(object):

    def __init__(self):
        self._capacity = self._min_capacity = 10
        self._size = 0
        self._array = zeros(self._capacity)

    def __getitem__(self, i):
        if i >= self._size:
            raise IndexError("DynamicArray index out of range")
        return self._array[i]

    def __setitem__(self, i, ele):
        if i >= self._size:
            raise IndexError("DynamicArray index out of range")
        self._array[i] = ele

    def append(self, ele):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        self._array[self._size] = ele
        self._size += 1

    def find(self, ele):
        return next((i for i in range(self._size) if self[i] == ele), -1)

    def pop(self):
        if not self._size:
            raise IndexError("pop from an empty DynamicArray")

        self._size -= 1
        item = self._array[self._size]

        if self._size > self._min_capacity and self._size / float(self._capacity) < 0.25:
            self._resize(self._capacity / 2)
        return item

    def is_empty(self):
        return not len(self)


    def _resize(self, new_capacity):
        self._capacity = new_capacity
        new_ary = zeros(new_capacity)
        for i in range(self._size):
            new_ary[i] = self._array[i]
        self._array = new_ary

    def __len__(self):
        return self._size

    def __bool__(self):
        return not self.is_empty()
