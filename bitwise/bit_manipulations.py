def count_bits(n):
    return (n & 1) + count_bits(n >> 1) if n else 0
