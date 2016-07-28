from collections import Counter
import itertools


def apriori(transactions, min_supprt_count):
    # TODO: refactor and optimize
    item_counts = Counter(reduce(list.__add__, transactions.values()))

    candidate = {(item,): count for item, count in item_counts.items()}
    frequent = {itemset: count for itemset, count in candidate.items()
                if count >= min_support_count}

    if not frequent:
        return {}


    for k in itertools.count(start=2):
        current_items = reduce(set.union, map(set, frequent.keys()))
        new_itemset_combos = itertools.combinations(current_items, k)
        new_filtered_itemset_combos = []

        # Pruning step
        # The idea here is that in order for a combo to have at least
        # min_support_count, all of its (k - 1) combo has to have
        # count of at least min_support_count
        for itemset in new_itemset_combos:
            if all(frequent.get(sub_itemset, 0) >= min_support_count
                   for sub_itemset in itertools.combinations(itemset, k - 1)):
                new_filtered_itemset_combos.append(itemset)

        # Find new candidate subsets
        new_candidate = {}
        for itemset in new_filtered_itemset_combos:
            count = sum(set(itemset).issubset(set(transaction_itemset))
                        for transaction_itemset in transactions.values())

            new_candidate[itemset] = count

        # Find new frequent subsets
        new_frequent = {itemset: count for itemset, count
                        in new_candidate.items() if count >= min_support_count}

        if new_frequent:
            candidate = new_candidate
            frequent = new_frequent
        else:
            return frequent
