from time import sleep
from random import randint
from threading import Thread


LOWEST_PRIORITY = 0
NUM_THREADS = 100


def lock(tid, entering, tickets):
    # The entering list is required for the edge case where two threads end up
    # getting the same ticket value, and one with lower prioirty (higher tid)
    # ends up going to the critical section first. Then when the higher priority
    # thread runs it will also get into the critical section.
    entering[tid] = True
    tickets[tid] = max(tickets) + 1
    entering[tid] = False

    for j in range(len(entering)):
        while entering[j]:
            thread_yield()

        while tickets[j] != 0 and (tickets[tid], tid) > (tickets[j], j):
            thread_yield()


def unlock(tid):
    tickets[tid] = LOWEST_PRIORITY


def compute(tid, entering, tickets):
    lock(tid, entering, tickets)

    # Critical section
    print 'hello world'

    unlock(tid)

def thread_yield():
    sleep(0.1)

if __name__ == '__main__':
    entering = [False] * NUM_THREADS
    tickets = [LOWEST_PRIORITY] * NUM_THREADS
    threads = [Thread(target=compute, args=(tid, entering, tickets))
               for tid in range(NUM_THREADS)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
