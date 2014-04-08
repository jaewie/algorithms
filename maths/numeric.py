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

def mult(a, b):

  # Russian Peasant Multiplication algorithm
  res = 0
  while b:
    if b % 2 != 0:
      res += a
    a += a
    b /= 2
  return res

def mult(x, y):
  
  # Karatsuba algorithm
  if x < 10 or y < 10:
    return x * y

  x_digs, y_digs = num_digits(x), num_digits(y)
  n = max(x_digs, y_digs)
  n = n if n % 2 == 0 else n - 1

  a, b = x / (10 ** (n / 2)), x % (10 ** (n / 2)) 
  c, d = y / (10 ** (n / 2)), y % (10 ** (n / 2)) 

  ac = mult(a, c)
  bd = mult(b, d)
  ad_plus_bc = mult(a + b, c + d) - ac - bd

  return 10 ** n * ac + 10 ** (n / 2) * (ad_plus_bc) + bd

def num_digits(num):
  return 1 + num_digits(num / 10) if num else 1

def div(a, b):
  # Super slow division by repeated subtraction
  if b == 0: raise ZeroDivisionError("Division by zero")
  return 1 + div(a - b, b) if a >= b else 0

