class TreeNode(object):

    def __init__(self, value, left=None, right=None, parent=None):
        self.val = value
        self.left = left
        self.right = right
        self.parent = parent

    def has_parent(self):
        return not self.parent is None

    def is_leaf(self):
        return not self.left and not self.right

    def has_both_siblings(self):
        return self.left and self.right
