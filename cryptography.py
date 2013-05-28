import random

def rsa(msg):
    '''RSA algorithm which encrypts msg then decrypts it.'''

    p1 = generate_prime(10e5, 10e30)
    p2 = generate_prime(10e5, 10e30)
    n = p1 * p2
    phi_n = (p1 - 1) * (p2 - 1)
    e = 3
    k = 2
    d = ((k * phi_n) + 1) // e

    encryped_msg = encrypt(msg, n, e)
    
    return (encryped_msg ** d) % n
    
def generate_prime(low, high):
    '''Return a random prime between low and high.'''

    n = random.randint(low, high)
    while not is_prime(n):
        n += 1
    return n

def encrypt(m, n, e):
    '''Return the encryption of message m.'''

    return (m ** e) % n

def generate_e(phi_n):
    '''Generate e for phi_n'''

    e = 3
    while not is_odd(e) or gcd(e, phi_n) != 1:
        e += 1
    return e
    
def is_odd(num):
    ''' Return whether num is odd.'''

    return num % 2 != 0
    
def is_prime(num):
    '''Return whether num is a prime number.'''

    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

def gcd(a, b):
    ''' Return the greatest common divisor of a and b.'''

    while b!= 0:
        t = b
        b = a % t
        a = t
    return a

