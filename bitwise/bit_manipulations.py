def count_bits(n):
    '''Takes 32 iterations for 32 bit int.'''
    return (n & 1) + count_bits(n >> 1) if n else 0

def count_bits(n):
    '''Takes k iterations where k is the number of bits set.'''
    return 1 + count_bits(n & (n - 1)) if n else 0

def is_power_of_two(n):
    return not (n & (n - 1))
