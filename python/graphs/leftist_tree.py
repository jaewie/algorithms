class LeftistNode:
    def __init__(self, value, left=None, right=None, rank=1):
        self.value = value
        self.left = left
        self.right = right
        self.rank = rank


def make_leaf(value):
    return LeftistNode(value)


def rank(node):
    return node.rank


def take_min(node):
    return (node.value, merge(node.left, node.right))


def merge(left, right):
    if not left:
        return right
    elif not right:
        return left

    if left.value > right.value:
        left, right = right, left

    right_merged = merge(left.right, right)
    left_subtree_rank = left.left.rank if left.left else 0

    if left_subtree_rank > right_merged.rank:
        return LeftistNode(left.value, left.left, right_merged, right_merged.rank + 1)
    else:
        return LeftistNode(left.value, right_merged, left.left, left_subtree_rank + 1)
