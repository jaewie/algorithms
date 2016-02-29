from random import randint, shuffle, random
from math import exp, sqrt
from itertools import islice


def run_simulated_annealing(current_state, start_temp, obj_func, move_func,
                            iterations=10000):
    for temp in islice(next_temp(start_temp), iterations):
        new_state = move_func(current_state)

        prev = obj_func(current_state)
        new = obj_func(new_state)

        if random() < p_accept(prev, new, temp):
            current_state = new_state

    return current_state


def run_simulated_annealing_tsp(current_state, start_temp=10000,
                                iterations=10000):
    return run_simulated_annealing(current_state, start_temp,
                                   eval_tour, move_tsp, iterations)


def init_tsp(num_cities=1000, max_x=1000, max_y=1000):
    cities = make_random_cities(num_cities, max_x, max_y)
    tour = get_random_tour(cities)
    return cities, tour


def move_tsp(state):
    cities, tour = state
    return cities, move_tour(tour)


def make_random_cities(num_cities, max_x, max_y):
    assert(num_cities <= (max_x + 1) * (max_y + 1))

    cities = set()
    while len(cities) < num_cities:
        x, y = randint(0, max_x), randint(0, max_y)
        cities.add((x, y))
    return list(cities)


def get_random_tour(cities):
    tour = range(len(cities))
    shuffle(tour)
    return tour


def move_tour(tour):
    tour = tour[:]
    i = randint(0, len(tour) - 1)
    j = randint(0, len(tour) - 1)

    tour[i], tour[j] = tour[j], tour[i]
    return tour


def eval_tour(state):
    cities, tour = state
    def distance(city0, city1):
        x0, y0 = city0
        x1, y1 = city1
        return sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    return sum(distance(cities[i], cities[j]) for i, j in
               zip(tour, tour[1:]))


def next_temp(start, a=0.9):
    while True:
        yield start
        start *= a


def p_accept(prev, new, temp):
    return 1 if new <= prev else exp((prev - new) / float(temp))
