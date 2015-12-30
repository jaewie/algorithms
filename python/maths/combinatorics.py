from random import randint


def shuffle(lst):
    '''Return a new list with items in lst rearranged randomly.'''

    # Fisher-Yate's algorithm
    return [lst.pop(randint(0, len(lst) - 1)) for _ in range(len(lst))]


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

    # Algorithm by John Von Neumann
    first, second = biased_coin(), biased_coin()
    return first if first == second else fair_coin(biased_coin)
