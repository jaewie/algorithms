import random


def max_subarray(lst):
    '''Return the maximum sum of a subarray in lst.'''

    max_ending_here = 0
    max_so_far = 0
    for num in lst:
        max_ending_here = max(0, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def partition(lst, p):
    '''Partitions lst on pivot p (dutch national flag problem)'''
    
    i = 0 # top of bottom part
    j = 0 # top of middle part
    k = len(lst) - 1 # bottom of top part
    
    while j < k:
        
        if lst[j] < p:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
            j += 1
        
        elif lst[j] > p:
            lst[j], lst[k] = lst[k], lst[j]
            k -= 1
        else:
            j += 1
            
    return lst

def quick_select(lst, n):
    '''Return the nth smallest number in lst using quick select.'''
    
    if not lst or len(lst) < n:
        raise IndexError("lst doesn't have n elements")
    
    ind = random.randint(0, len(lst) - 1)
    piv = lst[ind]
    less = [x for x in lst if x < piv]
    same = [x for x in lst if x == piv]
    bigger = [x for x in lst if x > piv]
    
    if n < len(less):
        return quick_select(less, n)
    elif n < len(less) + len(same):
        return piv
    else:
        return quick_select(bigger, n - len(same) - len(less))

def med_of_meds(lst, n):
    '''Return the nth smallest number in lst using median of medians algo.'''
    
    
    if not lst or len(lst) < n:
        raise IndexError("lst doesn't have n elements")
    if len(lst) <= 5:
        return sorted(lst)[n]
    
    lsts = [lst[i:i+5] for i in range(0, len(lst), 5)]
    medians = [med_of_meds(_lst, len(_lst) / 2) for _lst in lsts]
    piv = med_of_meds(medians, len(medians) / 2)

    less = [x for x in lst if x < piv]
    same = [x for x in lst if x == piv]
    bigger = [x for x in lst if x > piv]
    
    if n < len(less):
        return med_of_meds(less, n)
    elif n < len(less) + len(same):
        return piv
    else:
        return med_of_meds(bigger, n - len(same) - len(less))

def binary_search(lst, target):
    ''' Binary search is worst case O(log n)'''
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (high + low) / 2
        if lst[mid] < target:
            low = mid + 1
        elif lst[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1
