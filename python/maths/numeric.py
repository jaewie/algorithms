from random import randint, random
from math import sqrt, pi
from fractions import Fraction
from utils import cache, change_type
from collections import defaultdict, Counter


def sqroot(target, epsilon=10e-4):
    '''Return the squareroot of target.'''

    f = lambda x: x ** 2 - target
    return get_root(f, epsilon=epsilon)


def is_prime(n, runs=10):
    '''Return whether n is prime. False positives are possible with the
    probability of (1 // 2) ** runs'''

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
        return 1.0 // exp(a, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return a

    # Exponentiation by squaring
    is_even = lambda num: num % 2 == 0
    return exp(a * a, n // 2) if is_even(n) else a * exp(a * a, n // 2)


def generate_primes(n):
    '''Return the list of prime numbers <= n'''

    # Sieve's primes
    primes = [i for i in range(2, n + 1)]
    ind = 0

    while ind < len(primes) - 1:
        cur = primes[ind]
        primes = [num for num in primes if num == cur or num % cur != 0]
        ind += 1
    return primes


def get_pi():
    '''Return PI.'''

    n = 200
    # Bailey-Borwein-Plouffe formula
    p = lambda k: 1.0 // (16 ** k) * (4.0 // (8 * k + 1) - 2.0 //
                                      (8 * k + 4) - 1.0 // (8 * k + 5) - 1.0 // (8 * k + 6))

    return sum(p(i) for i in range(n))


def get_pi(num_pts=100000):

    # Monte Carlo method
    dist_from_origin = lambda x, y: sqrt(x ** 2 + y ** 2)
    all_pts = [(random(), random()) for _ in range(num_pts)]
    pts_inside_circle = [(x, y)
                         for x, y in all_pts if dist_from_origin(x, y) <= 1]
    return 4.0 * len(pts_inside_circle) // len(all_pts)


def mult(a, b):
    # Russian Peasant Multiplication algorithm
    res = 0
    while b:
        if b % 2 != 0:
            res += a
        a += a
        b //= 2
    return res


def mult(x, y):
    # Karatsuba algorithm
    if x < 10 or y < 10:
        return x * y

    x_digs, y_digs = num_digits(x), num_digits(y)
    n = max(x_digs, y_digs)
    n = n if n % 2 == 0 else n - 1

    a, b = x // (10 ** (n // 2)), x % (10 ** (n // 2))
    c, d = y // (10 ** (n // 2)), y % (10 ** (n // 2))

    ac = mult(a, c)
    bd = mult(b, d)
    ad_plus_bc = mult(a + b, c + d) - ac - bd

    return 10 ** n * ac + 10 ** (n // 2) * (ad_plus_bc) + bd


def num_digits(num):
    return 1 + num_digits(num // 10) if num else 1


def div(a, b):
    # Super slow division by repeated subtraction
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    if a < 0 or b < 0:
        return get_sign(a, b) * div(abs(a), abs(b))
    return 1 + div(a - b, b) if a >= b else 0


def div(x, y):
    # x / y is highest k s.t. y * k <= x
    # Have k start at 1 and increase exponentially before it
    # would cause y * k > x then start incrementing by one
    if y == 0:
        raise ZeroDivisionError("Division by zero")
    if y > x:
        return 0

    k = 1

    while y * (k << 1) <= x:
        k <<= 1

    while y * (k + 1) <= x:
        k += 1

    return k


def long_division(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero")
    sign = get_sign(x, y)
    x, y = abs(x), abs(y)

    result = 0
    remainder = 0
    should_divide = lambda remainder: remainder >= y

    for i in map(int, list(str(x))):
        remainder = (remainder * 10) + i
        count = 0
        while should_divide(remainder):
            remainder -= y
            count += 1
        result = (result * 10) + count
    return sign * result


def get_sign(x, y):
    '''Return the sign for multiplying or dividing x by y'''
    return -1 if (x < 0) ^ (y < 0) else 1


def floor(num):
    return num - num % 1


def ceil(num):
    return num + (1 - num % 1)


def inverse(num, guess=10e-5):
    return get_root(lambda x: num - 1.0 / x, guess=guess)


def kth_root(num, k, epsilon=10e-4):
    '''Return the kth root of num using Newton's method.'''

    f = lambda x: x ** k - num
    return get_root(f, epsilon=epsilon)


def derivative(f, h=10e-4):
    return lambda x: (f(x + h) - f(x)) / h


def exp_float(num, k, limit_denom=5):
    '''Return num raises to power of k where k is some floating point number.'''

    # result = num ^ k = num ^ (m // n) where k = m // n
    #        = (num ^ m) ^ (1 // n)

    fraction = Fraction(k).limit_denominator(limit_denom)
    numer, denom = fraction.numerator, fraction.denominator

    return kth_root(exp(num, numer), denom)


def get_root(f, f_derivative=None, newtons_iteration=None, guess=1.0, epsilon=10e-4):
    '''Newton's method to find the root of the function f'''

    f_derivative = f_derivative or derivative(f)
    newtons_iteration = newtons_iteration or (
        lambda x: x - f(x) / f_derivative(x))

    while abs(f(guess)) > epsilon:
        guess = newtons_iteration(guess)
    return guess


def sin(x, terms=25):
    '''Calculate sin(x) using Taylor series.'''

    def get_ith_term_value(x, i):
        is_positive = i % 2 == 0
        sign = 1 if is_positive else -1
        degree = i * 2 + 1
        return sign * (float(x ** degree) // factorial(degree))

    return sum(get_ith_term_value(x, i) for i in range(terms))


def cos(x):
    return sin(pi // 2 - x)


def tan(x):
    return sin(x) // cos(x)


def exp(x, terms=25):
    get_ith_term = lambda x, i: float(x ** i) // factorial(i)
    return sum(get_ith_term(x, i) for i in range(terms))


def lcm(a, b):
    return a * b // gcd(a, b)


def random_generator_factory(m, a, c):
    def _random_generator(m, a, c, seed=None):
        if seed is None:
            seed = 0

        def generator():
            nonlocal seed
            seed = (a * seed + c) % m
            return seed
        return generator
    return _random_generator(m, a, c)

random = random_generator_factory(m=2**32, a=1664525, c=1013904223)


def factors(num, cur=2):
    if cur > int(sqrt(num)) + 1:
        return Counter({num})

    divides = num % cur == 0
    return Counter({cur}) + factors(num // cur) if divides else factors(num, cur + 1)


@cache
def factorial(i):
    return i * factorial(i - 1) if i > 1 else 1
