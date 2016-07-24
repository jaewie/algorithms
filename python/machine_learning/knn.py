from operator import itemgetter
from functools import partial


def k_nearest_neighbor(dataset, querypt, k):
    euclidean = lambda x, y: sum((i - j) ** 2 for i, j in zip(x, y))
    dist_querypt = partial(euclidean, y=querypt)
    get_feature = itemgetter(0)
    get_classification = itemgetter(1)

    all_nearest = sorted(dataset, key=lambda x: dist_querypt(get_feature(x)))
    k_nearest = all_nearest[:k]
    k_classifications = [get_classification(e) for e in k_nearest]

    # Most frequent classification in k classifications
    return max(set(k_classifications), key=k_classifications.count)
