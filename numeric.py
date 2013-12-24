def sqroot(target):
    '''Return the square root of target, using newton's method'''

    guess = 1.0
    ep = 0.0001
    
    while abs(guess ** 2 - target) > ep:
        guess -= (guess ** 2 - target) / (guess * 2.0)
    return guess
