from bst import BST, find_max
from interval_node import IntervalNode


class IntervalTree(BST):

    def __init__(self):
        super(IntervalTree, self).__init__()

    def insert(self, interval):
        node = IntervalNode(interval)
        super(IntervalTree, self).insert(node)
        node.update_max_endpoints()

    def query(self, query_interval):
        return self.root.query(query_interval)
