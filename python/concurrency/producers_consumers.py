from threading import Semaphore, Thread, current_thread
from Queue import Queue
from itertools import chain


def produce(buffer, mutex, space_free_sem, space_available_sem):
    for num in xrange(1000):
        space_free_sem.acquire()

        mutex.acquire()
        buffer.put(num)
        mutex.release()

        space_available_sem.release()


def consume(buffer, mutex, space_free_sem, space_available_sem):
    while True:
        space_available_sem.acquire()

        mutex.acquire()
        num = buffer.get()
        print('Thread {} consuming {}'.format(current_thread().ident, num))
        mutex.release()

        space_free_sem.release()


if __name__ == '__main__':
    buffer_size = 10
    num_producers = 2
    num_consumers = 5
    buffer = Queue()

    mutex = Semaphore(1)
    space_free_sem = Semaphore(buffer_size)
    space_available_sem = Semaphore(0)

    args = (buffer, mutex, space_free_sem, space_available_sem)

    producers = [Thread(target=produce, args=args) for _ in
                 range(num_producers)]
    consumers = [Thread(target=consume, args=args) for _ in
                 range(num_consumers)]

    for t in chain(producers, consumers):
        t.start()

    for t in chain(producers, consumers):
        t.join()
