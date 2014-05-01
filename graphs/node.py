class Node(object):
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None
    self.parent = None
    self.height = None

  def has_parent(self):
    return not self.parent is None

  def is_leaf(self):
    return not self.left and not self.right

  def has_both_siblings(self):
    return self.left and self.right

  def rotate_right(self):
    if not self.has_parent():
      raise ValueError("Node is not right rotatable")

    lc, rc = self.left, self.right
    parent = self.parent
    great_parent = parent.parent

    self.parent = parent.parent
    self.right = parent
    
    parent.left = rc
    parent.parent = self

    if great_parent:
      if great_parent.right is parent:
        great_parent.right = self
      else:
        great_parent.left = self

    
    if rc: rc.parent = parent

    update_height(self.left)
    update_height(self.right)
    update_height(self)
    self.update_parent_heights()

  def rotate_left(self):
    if not self.has_parent():
      raise ValueError("Node is not left rotatable")

    lc, rc = self.left, self.right
    parent = self.parent
    great_parent = parent.parent

    self.parent = parent.parent
    self.left = parent
    
    parent.right = lc
    parent.parent = self
    if great_parent:
      if great_parent.right is parent:
        great_parent.right = self
      else:
        great_parent.left = self


    if lc: lc.parent = parent

    update_height(self.left)
    update_height(self.right)
    update_height(self)
    self.update_parent_heights()

 
  def is_balanced(self):
    return abs(balance_factor) <= 1

  def update_parent_heights(self):
    update_height(self)
    if self.parent:
      self.parent.update_parent_heights()
 
  @property
  def balance_factor(self):
    left = self.left.height if self.left else 0
    right = self.right.height if self.right else 0

    return right - left

def update_height(node):
  if node:
    lc_height = node.left.height if node.left else 0
    rc_height = node.right.height if node.right else 0
    node.height = max(lc_height, rc_height) + 1
