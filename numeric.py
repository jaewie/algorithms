from random import randint


def sqroot(target):
    '''Return the square root of target.'''
    
    # Babylonian algorithm
    guess = 1.0
    epsilon = 0.0001
    
    while abs(guess ** 2 - target) > epsilon:
        guess -= (guess ** 2 - target) / (guess * 2.0)
    return guess

def is_prime(n, runs=10):
    '''Return whether n is prime. There's no false negatives, but false 
    positives can happen with probability of (1 / 2) ** runs'''
        
    # Fermat's primality test
    f_test = lambda a, n: a ** (n - 1) % n == 1
    return n > 1 and all(f_test(randint(1, n - 1), n) for _ in range(runs))

def gcd(a, b):
    '''Return the greatest common divisor of a and b.'''
    
    # Euclid's algorithm
    
    return gcd(b, a % b) if b else a
