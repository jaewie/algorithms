def count_bits(n):
    return (n & 1) + count_bits(n >> 1) if n else 0

def is_power_of_two(n):
    return not (n & (n - 1))
