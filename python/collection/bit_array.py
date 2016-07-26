class BitArray(object):

    def __init__(self):
        # Python converts int to long as needed and long supports
        # arbitrary precision, so don't need an array of ints.
        self._array = 0

    def get(self, i):
        if i < 0:
            raise ValueError("Index imust be nonnegative")
        return (self._array >> i) & 1

    def set(self, i):
        if i < 0:
            raise ValueError("Index imust be nonnegative")
        self._array |= 1 << i

    def toggle(self, i):
        if i < 0:
            raise ValueError("Index imust be nonnegative")
        self._array ^= 1 << i

    def clear(self, i):
        if i < 0:
            raise ValueError("Index imust be nonnegative")
        self.set(i)
        self.toggle(i)

    def is_set(self, i):
        if i < 0:
            raise ValueError("Index imust be nonnegative")
        return self.get(i) == 1
