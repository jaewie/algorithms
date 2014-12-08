from tree_node import TreeNode


class SkewHeap(object):
    def __init__(self, root):
        self.root = root

    def merge(self, heap):
        self.root = _merge(self.root, heap.root)

    def min(self):
        r = self.root
        self.root = _merge(r.left, r.right)
        return r.val

    def insert(self, val):
        self.root = _merge(self.root, TreeNode(val))

def _merge(heap0, heap1):
    if not heap0:
        return heap1
    elif not heap1:
        return heap0

    val_getter = lambda root: root.val
    p = min(heap0, heap1, key=val_getter)
    q = max(heap0, heap1, key=val_getter)

    p_right = p.right
    p.right = p.left
    p.left = _merge(p_right, q)

    return p
