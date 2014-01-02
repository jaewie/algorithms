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
