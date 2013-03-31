import random

def binary_search(lst, x):
    
    low, high = 0, len(lst)
    
    while low <= high:
        
        mid = (high + low) / 2
        
        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid - 1
        else:
            return mid
    return None

def quick_sort(lst):
    
    if len(lst) <= 1:
        return lst
    
    pivot = lst[random.randint(0, len(lst) - 1)]
    less = [x for x in lst if x < pivot]
    bigger = [x for x in lst if x > pivot]
    
    return quick_sort(less) + [pivot] + quick_sort(bigger)


def merge_sort(lst):
    
    if len(lst) <= 1:
        return lst

    left = merge_sort(lst[:len(lst)/2])
    right = merge_sort(lst[len(lst)/2:])

    return _merge(left, right)

def _merge(left_lst, right_lst):
    
    lst = []
    
    i, j = 0, 0
    
    while i < len(left_lst) and j < len(right_lst):
        
        if left_lst[i] < right_lst[j]:
            lst.append(left_lst[i])
            i += 1
        elif left_lst[i] > right_lst[j]:
            lst.append(right_lst[j])
            j += 1
        else:
            lst.append(left_lst[i])
            lst.append(right_lst[j])
            i += 1
            j += 1
    
    lst.extend(left_lst[i:])
    lst.extend(right_lst[j:])
    return lst


def radix_sort(lst):
    digits = len(str(max(lst)))
    bins = [[] for x in range(10)]
    for k in range(digits):
        for num in lst:
            digit = num / (10 **k) % 10
            bins[digit].append(num)
        lst = []
        for b in bins:
            while b:
                lst.append(b.pop(0))

    return lst



lst = [10, 3, 2, 4, 100, 120, 50]
print radix_sort(lst)

           
            
            