from tree_node import TreeNode


class SegmentNode(TreeNode):
    def __init__(self, val, start_ind, end_ind, left=None, right=None):
        TreeNode.__init__(self, val, left, right)
        self.start_ind = start_ind
        self.end_ind = end_ind

    @property
    def interval(self):
        return (self.start_ind, self.end_ind)
