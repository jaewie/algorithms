from queue import Queue
from collections import Counter
from operator import le
from itertools import tee
from functools import reduce
from threading import Thread
from time import sleep


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
