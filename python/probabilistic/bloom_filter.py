from collection.bit_array import BitArray


class BloomFilter(object):

    def __init__(self, hash_funcs, n_bits=32):
        self._bitarray = BitArray()
        self._hash_funcs = hash_funcs
        self._n_bits = n_bits

    def insert(self, val):
        for f in self._hash_funcs:
            self._bitarray.set(f(val) % self._n_bits)

    def exists(self, val):
        return all(self._bitarray.get(f(val) % self._n_bits)
                   for f in self._hash_funcs)
