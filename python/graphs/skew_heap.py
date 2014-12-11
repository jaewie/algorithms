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

    sm_heap = min(heap0, heap1, key=lambda root: root.val)
    big_heap = max(heap0, heap1, key=lambda root: root.val)
    sm_heap.left, sm_heap.right = _merge(sm_heap.right, big_heap), sm_heap.left

    return sm_heap
