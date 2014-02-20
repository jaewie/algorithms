from random import randint, random
from math import sqrt


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

def generate_primes(n):
  '''Return the list of prime numbers <= n'''

  # Sieve's primes
  primes = [i for i in range(2, n + 1)]
  ind = 0
  
  while ind != len(primes) - 1:
    cur = primes[ind]
    primes = [num for num in primes if num == cur or num % cur != 0]
    ind += 1
  return primes

def get_pi():
  '''Return PI.'''

  n = 200
  # Bailey-Borwein-Plouffe formula
  p = lambda k: 1.0 / (16 ** k) * (4.0 / (8 * k + 1) - 2.0 / (8 * k + 4) - 1.0 / (8 * k + 5) - 1.0 / (8 * k + 6))

  return sum(p(i) for i in range(n))

def get_pi(num_pts=100000):

  # Monte Carlo method
  dist_from_origin = lambda x, y: sqrt(x ** 2 + y ** 2)
  all_pts = [(random(), random()) for _ in range(num_pts)]
  pts_inside_circle = [(x, y) for x, y in all_pts if dist_from_origin(x, y) <= 1]
  return 4.0 * len(pts_inside_circle) / len(all_pts)
