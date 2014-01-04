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
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

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
