from threading import Semaphore, Thread
from concurrency.synchronization import LightSwitch


def write(array, no_writers, no_readers, write_switch):
    write_switch.lock(no_readers)

    no_writers.acquire()
    array[3] = randint(0, 30)
    no_writers.release()

    write_switch.unlock(no_readers)



def read(array, no_writers, no_readers, read_switch):
    no_readers.acquire()
    read_switch.lock(no_writers)
    no_readers.release()

    print(array[3])

    read_switch.unlock(no_writers)


if __name__ == '__main__':
    num_readers = num_writers = 30

    read_switch = LightSwitch()
    write_switch = LightSwitch()

    no_readers = Semaphore(1)
    no_writers = Semaphore(1)
    array = range(10)

    writers = [Thread(target=write, args=(array, no_writers, no_readers, write_switch))
               for _ in range(num_writers)]
    readers = [Thread(target=read, args=(array, no_writers, no_readers, read_switch))
               for _ in range(num_readers)]
    all_threads = writers + readers

    for t in sample(all_threads, len(all_threads)):
        t.start()

    for t in sample(all_threads, len(all_threads)):
        t.join()
