from functools import partial
from itertools import groupby
from operator import itemgetter
from collections import Counter


def k_nearest_neighbor(dataset, querypt, k):
    euclidean = lambda x, y: return sum((i - j) ** 2 for i, j in zip(x, y))
    dist_querypt = partial(euclidean, y=querypt)
    get_feature = lambda e: e[0]
    get_classification = lambda e: e[1]

    all_nearest = sorted(dataset, key=lambda e: dist_querypt(get_feature(e)))
    k_nearest = all_nearest[:k]
    classifications = [get_classification(e) for e in k_nearest]
    return max(Counter(classifications))
