from functools import partial, reduce
from operator import itemgetter
from collections import Counter


def k_nearest_neighbor(dataset, querypt, k):
    euclidean = lambda x, y: sum((i - j) ** 2 for i, j in zip(x, y))
    dist_querypt = partial(euclidean, y=querypt)
    get_feature = itemgetter(0)
    get_classification = itemgetter(1)

    all_nearest = sorted(dataset, key=compose(dist_querypt, get_feature)
    k_nearest = all_nearest[:k]
    classifications = [get_classification(e) for e in k_nearest]
    return max(Counter(classifications))

def compose(*args):
    def _compose(f, g):
        def wrapper(*args, **kwargs):
            return f(g(*args, **kwargs))
        return wrapper

    return reduce(_compose, args)
