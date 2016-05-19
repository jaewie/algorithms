from threading import Semaphore, Thread


def get_forks(i, footman, forks):
    footman.acquire()
    forks[left(i)].acquire()
    forks[right(i)].acquire()

def put_forks(i, footman, forks):
    forks[left(i)].release()
    forks[right(i)].release()
    footman.release()


def left(i):
    return (i - 1) % 5


def right(i):
    return (i + 1) % 5


def start_philosopher(i, footman, forks):
    while True:
        get_forks(i, footman, forks)
        print('philosopher {} is eating'.format(i))
        put_forks(i, footman, forks)
        print('philosopher {} have put down their forks'.format(i))


if __name__ == '__main__':
    num_philosophers = num_forks = 5
    footman = Semaphore(4)
    forks = [Semaphore(1) for _ in range(num_forks)]

    philosophers = [Thread(target=start_philosopher, args=(i, footman, forks))
                    for i in range(num_philosophers)]

    for t in philosophers:
        t.start()

    for t in philosophers:
        t.join()
