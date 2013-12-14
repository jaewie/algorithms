import random

def max_subarray(lst):
    '''Return the maximum sum of a subarray in lst.'''

    max_ending_here = 0
    max_so_far = 0
    for num in lst:
        max_ending_here = max(0, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def quick_select(lst, n):
    '''Return the nth smallest number in lst using quick select.'''
    
    if not lst or len(lst) < n:
        raise IndexError("There is no nth number in lst")
    
    piv = lst[random.randint(0, len(lst) - 1)]
    less = [x for x in lst if x < piv]
    same = [x for x in lst if x == piv]
    bigger = [x for x in lst if x > piv]
    
    # [1, 2, 3] [4, 4], [5, 6 , 7]
    
    # if n is between 3 - 4 return pivot
    # if n is less than 3 return qs of left, n
    # otherwise return qs of bigger, n - len(less) and len(same)
    
    if n < len(less):
        return quick_select(less, n)
    elif n < len(less) + len(same):
        return piv
    else:
        return quick_select(bigger, n - len(same) - len(less))