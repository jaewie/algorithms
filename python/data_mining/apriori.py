import itertools


def apriori(transactions, min_support_count):
    domain = reduce(set.union, transactions, set())
    candidates = {frozenset([item]): sum(item in t for t in transactions) for item in domain}
    filtered_candidates = {k: v for k, v in candidates.items() if v >= min_support_count}
    if not filtered_candidates:
        return {}

    for k in itertools.count(start=2):
        domain = reduce(set.union, filtered_candidates, set())
        possible_itemsets = extend_combos(filtered_candidates.keys(), domain)

        candidates = {itemset: sum(set(itemset).issubset(t) for t in transactions)
                      for itemset in possible_itemsets}
        new_filtered_candidates = {k: v for k, v in candidates.items() if v >= min_support_count}

        if new_filtered_candidates:
            filtered_candidates = new_filtered_candidates
        else:
            return filtered_candidates


def extend_combos(combos, domain):
    result = set()

    for combo in combos:
        for item in domain:
            if item not in combo:
                result.add(combo | set([item]))
    return result


if __name__ == '__main__':
    transactions = [{1,2,3,4},
                    {1,2,4},
                    {1,2},
                    {2,3,4},
                    {2,3},
                    {3,4},
                    {2,4}]
    min_support_count = 3
    print apriori(transactions, min_support_count)
