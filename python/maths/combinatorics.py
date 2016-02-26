from random import randint
from itertools import count


def shuffle(lst):
    '''Return a new list with items in lst rearranged randomly.'''

    # Fisher-Yate's algorithm
    #
    # Proof of correctness:
    #
    # Let N be # of elements in lst
    # Loop invariant after ith iteration:
    #
    # - Each element has 1 / N chance of being placed on each of lst[0...i]
    # - Each element has (N - 1 - i) / N chance of not being placed on any of lst[0...i]
    #
    # Base case: i = 0
    #
    # - j is between 0...N - 1
    # - So chance of en element being placed on lst[0] is 1 / N, not being placed (N - 1) / N
    #
    # Generic case: i > 0 and assume loop variant holds before the ith iteration begins
    #
    # - j is between i...N - 1
    # - Chance of an element not being chosen on lst[0...i - 1] is (N - 1 - (i - 1)) / N = (N - i) / N
    # - So chance of an elemnt being placed on lst[i] is (N - i) / N * (1 / (N - i)) = 1 / N
    # - So chance of not being placed there is (N - i) / N * (N - i - 1) / (N - i) = (N - 1 - i) / N
    for i in range(len(lst)):
        j = randint(i, len(lst) - 1)
        lst[i], lst[j] = lst[j], lst[i]


def sample(lst, k):
    '''Return k random items in lst.'''

    # Reservoir sampling
    reservoir = []

    for i, num in enumerate(lst):
        if i < k:
            reservoir.append(num)
        elif randint(0, i) < k:
            swap = randint(0, k - 1)
            reservoir[swap] = num
    return reservoir


def fair_coin(biased_coin):
    '''Return 0, 1 with 50% chance each'''

    # Algorithm by John von Neumann
    first, second = biased_coin(), biased_coin()

    # +-----------------------------------------+
    # |       | heads       | tails             |
    # +-----------------------------------------+
    # | heads | p * p       | p * (1 - p)       |
    # | tails | p * (1 - p) | (1 - p) * (1 - p) |
    # +-----------------------------------------+
    #
    # chance of first, second == (heads, tails) is the same as
    # chance of first, second == (tails, heads): p * (1 - p)

    return first if first == second else fair_coin(biased_coin)


def biased_coin(p):
    '''Return 1 with probability p, and 0 at 1 - p where 0 <= p <= 1'''
    return next(x for x in _binary_expansion(p) if x == randint(0, 1))


def _binary_expansion(p):
    '''Return binary expansion of 0 <= p <= 1'''

    total = 0
    for cur in count():
        current_digit = 1.0 / (2 << cur)

        if total + current_digit <= p:
            total += current_digit
            yield 1
        else:
            yield 0
