class TreeNode(object):
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None
    self.parent = None

  def has_parent(self):
    return not self.parent is None

  def is_leaf(self):
    return not self.left and not self.right

  def has_both_siblings(self):
    return self.left and self.right
