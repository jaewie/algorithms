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
        return None
    
    piv = lst[random.randint(0, len(lst) - 1)]
    less = [x for x in lst if x < piv]
    bigger = [x for x in lst if x > piv]
    
    
    if len(less) == n - 1:
        return piv
    
    if len(less) >= n:
        return quick_select(less, n)
    else:
        return quick_select(bigger, n - 1 - len(less))
