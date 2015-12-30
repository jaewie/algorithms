def count_bits(n):
    '''Takes 32 iterations for 32 bit int.'''
    return (n & 1) + count_bits(n >> 1) if n else 0


def count_bits(n):
    '''Takes k iterations where k is the number of bits set.'''
    return 1 + count_bits(n & (n - 1)) if n else 0


def is_power_of_two(n):
    return not (n & (n - 1))


def is_zero(n):
    return not n


def is_negative(n):
    return (n >> 31) & 1


def is_positive(n):
    return (not is_zero(n)) & (not is_negative(n))


def max(x, y):
    diff = x - y
    return x + (diff * is_negative(diff) * -1)


def min(x, y):
    diff = x - y
    return y - (diff * is_negative(diff) * -1)


def add(a, b):
    return add(a ^ b, (a & b) << 1) if b else a
