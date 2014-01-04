import random
import Queue


def quick_sort(lst):
    '''Randomized quicksort. Avg: O(n log n). Worst: O(n^2)'''
    
    if len(lst) <= 1:
        return lst
    
    ind = random.randint(0, len(lst) - 1)
    pivot = lst[ind]
    less = [x for x in lst if x < pivot]
    same = [x for x in lst if x == pivot]
    bigger = [x for x in lst if x > pivot]

    return quick_sort(less) + same + quick_sort(bigger)


def merge_sort(lst):
    '''Merge sort is always O(n log n)'''
    
    if len(lst) <= 1:
        return lst
    left = merge_sort(lst[:len(lst) / 2])
    right = merge_sort(lst[len(lst) / 2:])
    return _merge(left, right)

def _merge(left_lst, right_lst):
    '''Return the merge of sorted lists left_lst and right_lst'''

    if not left_lst or not right_lst:
      return max(left_lst, right_lst)

    left, right = left_lst[0], right_lst[0]
    if left <= right:
      return [left] + _merge(left_lst[1:], right_lst)
    else:
      return [right] + _merge(left_lst, right_lst[1:])

def insertion_sort(lst):
    '''Insertion sort is worst case O(n^2) and best case O(n)'''
    
    for i in range(len(lst)):
        j = i
        temp = lst[i]
        while j > 0 and lst[j-1] > temp:
            lst [j] = lst[j-1]
            j -= 1
        lst[j] = temp
    return lst

def bubble_sort(lst):
    '''Bubble sort is always O(n^2)'''
    
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def selection_sort(lst):
    ''' Selection sort is always O(n^2)'''
    
    for i in range(len(lst)):
        m = i
        for j in range(i, len(lst)):
            if lst[j] < lst[m]:
                m = j
        lst[i], lst[m] = lst[m], lst[i]
    return lst

def radix_sort(lst):
    
    digits = len(str(max(lst)))
    buckets = [Queue.Queue() for _ in range(10)]
    for i in range(digits):
        for num in lst:
            digit = num / (10 ** i) % 10
            buckets[digit].put(num)
        lst = empty_buckets(buckets)
    return lst

def empty_buckets(buckets):
    lst = []
    for bucket in buckets:
        while not bucket.empty():
            lst.append(bucket.get())
    return lst

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

def heap_sort(lst):
    ''' Heap sort is always O(n log n).'''

    make_heap(lst)
    res = []
    while lst:
        res.append(lst[0])
        lst[0] = lst.pop()
        bubble_down(lst, 0)
    return res


def make_heap(lst):
    '''Turn lst into a min-heap'''

    for i in range(len(lst)/2 - 1, -1, -1):
        bubble_down(lst, i)

def bubble_down(lst, i):
    '''Bubble down element at index i in lst'''
    
    while True:
        lc = 2*i + 1
        rc = 2*i + 2
        
        if lc >= len(lst) and rc >= len(lst):
            break
        
        if lc >= len(lst) or rc >= len(lst) :
            child = min(lc, rc)
        elif lst[lc] < lst[rc]:
            child = lc
        else:
            child = rc
        
        if lst[i] > lst[child]:
            lst[child], lst[i] = lst[i], lst[child]
            i = child
        else:
            break

def bucket_sort(lst):
    '''Return lst sorted using bubble sort'''

    queue = to_queue(lst)
    return _bucket_sort(queue)

def _bucket_sort(queue, num_buckets=10):
    lst = to_list(queue)
    if is_sorted(lst):
      return lst
    
    sm, big = min(lst), max(lst)
    step = max((big - sm) / num_buckets + 1, 1)
    queues = [Queue() for _ in range(num_buckets)]
    for num in lst:
      for i, s in enumerate(range(sm + step, big + step + 1, step)):
        if num < s:
          queues[i].put(num)
          break 
    
    return reduce(list.__add__, map(_bucket_sort, queues), [])

def to_queue(lst):
    queue = Queue()
    for num in lst:
      queue.put(num)
    return queue

def to_list(queue):
    lst = []
    while not queue.empty():
      lst.append(queue.get())
    return lst

def is_sorted(lst):
    return len(lst) <= 1 or all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
