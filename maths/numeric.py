from random import randint


def sqroot(target, epsilon=0.0001):
    '''Return the squareroot of target.'''
    
    # Newton's algorithm
    guess = 1.0
    
    while abs(guess ** 2 - target) > epsilon:
        guess -= (guess ** 2 - target) / (guess * 2.0)
    return guess

def is_prime(n, runs=10):
    '''Return whether n is prime. There's no false negatives, but false 
    positives are possible with the probability of (1 / 2) ** runs'''
        
    # Fermat's primality test
    f_test = lambda a, n: a ** (n - 1) % n == 1
    return n > 1 and all(f_test(randint(1, n - 1), n) for _ in range(runs))

def gcd(a, b):
    '''Return the greatest common divisor of a and b.'''
    
    # Euclid's algorithm
    return gcd(b, a % b) if b else a

def exp(a, n):
  '''Return a to the power of n'''

  if n < 0:
    return 1.0 / exp(a, -n)
  if n == 0:
    return 1
  if n == 1:
    return a
 
  # Exponentiation by squaring
  is_even = lambda num: num % 2 == 0
  return exp(a * a, n / 2) if is_even(n) else a * exp(a * a, n / 2)
