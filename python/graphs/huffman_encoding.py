from tree_node import TreeNode
from collections import Counter
from Queue import PriorityQueue



def get_huffman_encoding(string):
    assert(string)

    pq = PriorityQueue()
    ctr = Counter(string)

    for char, count in ctr.items():
        pq.put((count, TreeNode(char)))


    while pq.qsize() > 1:
        fst_cnt, fst_node = pq.get()
        snd_cnt, snd_node = pq.get()


        combined_cnt = fst_cnt + snd_cnt
        intermediate_node = TreeNode(fst_node.val + snd_node.val, fst_node,
                                     snd_node)


        pq.put((combined_cnt, intermediate_node))

    _, root = pq.get()
    return _get_encoding(root)


def _get_encoding(root, prefix=''):
    if root is None:
        return {}
    elif root.is_leaf():
        return {root.val: prefix}

    left_encodings = _get_encoding(root.left, prefix + '0')
    right_encodings = _get_encoding(root.right, prefix + '1')

    return dict(list(left_encodings.items()) + list(right_encodings.items()))
