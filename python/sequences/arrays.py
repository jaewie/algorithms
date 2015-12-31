from random import choice
from functools import reduce


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

    i = 0  # top of bottom part
    j = 0  # top of middle part
    k = len(lst) - 1  # bottom of top part

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

    piv = choice(lst)
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

    if not lst or len(lst) <= n:
        raise IndexError("lst doesn't have n elements")
    if len(lst) <= 5:
        return sorted(lst)[n]

    lsts = [lst[i:i + 5] for i in range(0, len(lst), 5)]
    medians = [med_of_meds(_lst, len(_lst) // 2) for _lst in lsts]
    piv = med_of_meds(medians, len(medians) // 2)

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
        mid = (high + low) // 2
        if lst[mid] < target:
            low = mid + 1
        elif lst[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


def kway_merge(lsts):
    if len(lsts) <= 1:
        return lsts[0] if lsts else []
    mid = len(lsts) // 2
    left, right = kway_merge(lsts[:mid]), kway_merge(lsts[mid:])
    return two_way_merge(left, right)


def two_way_merge(left, right):
    if not left:
        return right
    if not right:
        return left

    l, r = left[0], right[0]

    if l < r:
        return [l] + two_way_merge(left[1:], right)
    else:
        return [r] + two_way_merge(left, right[1:])


def flatten(lsts):
    lsts = [flatten(e) if isinstance(e, list) else [e] for e in lsts]
    return reduce(list.__add__, lsts, [])
