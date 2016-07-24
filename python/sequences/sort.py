from Queue import Queue
from collections import Counter
from functools import partial, reduce
from itertools import tee
from operator import getitem, le
from random import choice
from threading import Thread
from time import sleep


def quick_sort(lst):
    '''Randomized quicksort.'''

    if len(lst) <= 1:
        return lst

    pivot = choice(lst)
    less = [x for x in lst if x < pivot]
    same = [x for x in lst if x == pivot]
    bigger = [x for x in lst if x > pivot]

    return quick_sort(less) + same + quick_sort(bigger)


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    left = merge_sort(lst[:len(lst) // 2])
    right = merge_sort(lst[len(lst) // 2:])
    return _merge(left, right)


def insertion_sort(lst):
    for i in range(len(lst)):
        while i > 0 and lst[i - 1] > lst[i]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return lst


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def cocktail_sort(lst):
    is_sorted = False
    j = 0

    while not is_sorted:
        is_sorted = True

        for i in range(j, len(lst) - 1 - j, 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1], = lst[i + 1], lst[i]
                is_sorted = False

        for i in range(len(lst) - 1 - j, j, -1):
            if lst[i - 1] > lst[i]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                is_sorted = False
        j += 1
    return lst


def selection_sort(lst):
    for i in range(len(lst)):
        m = min(range(i, len(lst)), key=partial(getitem, lst))
        lst[i], lst[m] = lst[m], lst[i]
    return lst


def heap_sort(lst):
    make_heap(lst)
    res = []
    while lst:
        res.append(lst[0])
        lst[0] = lst.pop()
        bubble_down(lst, 0)
    return res


def stack_sort(lst):
    res = []
    while lst:
        num = lst.pop()
        while res and res[-1] > num:
            lst.append(res.pop())
        res.append(num)
    return res


def comb_sort(lst):
    gap = len(lst)
    swapped = False
    shrink = 1.3

    while gap or swapped:
        gap = int(gap // shrink)
        swapped = False

        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    return lst


def pancake_sort(lst):
    max_pos = lambda lst: lst.index(max(lst))

    for size in reversed(range(len(lst))):
        max_ind = max_pos(lst[:size + 1])
        reverse(lst, 0, max_ind)
        reverse(lst, 0, size)
    return lst


def make_heap(lst):
    '''Turn lst into a min-heap'''

    for i in range(len(lst) // 2 - 1, -1, -1):
        bubble_down(lst, i)


def bubble_down(lst, i):
    '''Bubble down element at index i in lst'''

    while True:
        lc = 2 * i + 1
        rc = 2 * i + 2

        if lc >= len(lst) and rc >= len(lst):
            break

        if lc >= len(lst) or rc >= len(lst):
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
    '''Return lst sorted using bucket sort'''

    queue = to_queue(lst)
    return _bucket_sort(queue)


def _bucket_sort(queue, num_buckets=10):
    lst = to_list(queue)
    if is_sorted(lst):
        return lst

    sm, big = min(lst), max(lst)
    size = (big - sm) // num_buckets + 1
    buckets = [Queue() for _ in range(num_buckets)]
    for num in lst:
        for i, step in enumerate(range(sm + size, big + size + 1, size)):
            if num < step:
                buckets[i].put(num)
                break

    return reduce(list.__add__, map(_bucket_sort, buckets), [])


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


def is_sorted(iterable, key=le):
    a, b = tee(iterable)
    next(b, None)
    return all(map(key, a, b))


def radix_sort(lst):
    digits = len(str(max(lst)))
    buckets = [Queue() for _ in range(10)]
    for i in range(digits):
        for num in lst:
            digit = num // (10 ** i) % 10
            buckets[digit].put(num)
        lst = empty_buckets(buckets)
    return lst


def empty_buckets(buckets):
    lst = []
    for bucket in buckets:
        while not bucket.empty():
            lst.append(bucket.get())
    return lst


def count_sort(lst):
    counter = Counter(lst)
    flatten = lambda L: reduce(list.__add__, L)
    whole_range = range(min(lst), max(lst) + 1)

    return flatten([[num] * counter.get(num, 0) for num in whole_range])


def sleep_sort(lst):
    result = []
    threads = []
    for num in lst:
        thread = Thread(target=_sleep_append, args=(result, num))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return result


def _sleep_append(lst, num):
    sleep(num)
    lst.append(num)


def _merge(left_lst, right_lst):
    '''Return the merge of sorted lists left_lst and right_lst'''

    if not left_lst or not right_lst:
        return left_lst or right_lst

    left, right = left_lst[0], right_lst[0]
    if left <= right:
        return [left] + _merge(left_lst[1:], right_lst)
    else:
        return [right] + _merge(left_lst, right_lst[1:])


def reverse(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
