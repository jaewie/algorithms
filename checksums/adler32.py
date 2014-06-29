from math import ceil


def adler32(data, chunk_size, prime=65521):
    '''Adler-32 is a checksum algorithm which was invented by Mark Adler and is used in the rsync
    utility.'''

    def a(data, start, end):
        if (start - 1, end - 1) in _a:
            _a[start, end] = _a[start - 1, end - 1] - data[start - 1] + data[end] % prime
        else:
            _a[start, end] = 1 + sum(data[start:end]) % prime
        return _a[start, end]

    def b(data, start, end):
        if (start - 1, end - 1) in _b:
            _b[start, end] = _b[start - 1, end - 1] - (end - start + 1) * data[start - 1] + a(data, start, end) % prime
        else:
            _b[start, end] = sum(1 + (end - start - i) * x for i, x in enumerate(data[start:end])) % prime
        return _b[start, end]
    _a = {}
    _b = {}

    n = len(data)
    chunks = ceil(n / chunk_size)
    adler32_checksums = []

    for c in range(chunks):
        start = c * chunk_size
        end = min(n, (c + 1) * chunk_size)
        a_value = a(data, start, end)
        b_value = b(data, start, end)
        adler32_checksums.append(b_value << 16 + a_value)
    return adler32_checksums
