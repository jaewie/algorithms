from threading import Semaphore, Thread
from itertools import chain


def savage(servings, mutex, pot, empty_pot):
    while True:
        mutex.acquire()

        pot.pot_count -= 1
        if pot.pot_count <= 0:
            empty_pot.release()
        mutex.release()

        pot.acquire()

        serving = get_serving(servings)
        eat(serving)


def cook(servings, mutex, empty_pot, pot):
    while True:
        empty_pot.acquire()
        put_servings(servings, pot.total)

        mutex.acquire()
        pot.pot_count = pot.total
        for _ in xrange(pot.pot_count):
            pot.release()
        mutex.release()


def get_serving(servings):
    return servings.pop()


def put_servings(servings, total):
    for food in range(total):
        servings.append(food)


def eat(serving):
    print 'Eating {}'.format(serving)


if __name__ == '__main__':
    num_savages = 10
    pot_count = 5

    mutex = Semaphore(1)
    empty_pot = Semaphore(0)
    mutex = Semaphore(1)
    pot = Semaphore(0)
    pot.total = pot_count
    pot.pot_count = 0

    servings = []


    savages = [Thread(target=savage, args=(servings, mutex, pot, empty_pot))
               for _ in range(num_savages)]
    cook = Thread(target=cook, args=(servings, mutex, empty_pot, pot))

    for t in chain(savages, [cook]):
        t.start()

    for t in chain(savages, [cook]):
        t.join()
