class Node(object):
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None

class BST(object):
  def __init__(self):
    self.root = None

  def insert(self, value):
    self.root = _insert(self.root, value)

  def delete(self, val):
    self.root = _delete(self.root, val)

  def find(self, val):
    return find(self.root, val)


def _insert(node, value):
  if not node:
    return Node(value)

  if value <= node.val:
    node.left = _insert(node.left, value)
  elif value > node.val:
    node.right = _insert(node.right, value)
  return node

def find(node, value):
  if not node:
    return None

  if value < node.val:
    return find(node.left, value)
  elif value > node.val:
    return find(node.right, value)
  else:
    return node

def _find_max(node):
  if not node or not node.right:
    return node
  return _find_max(node.right)

def is_leaf(node):
  return node and not node.left and not node.right

def _delete(node, val):
  # assume that this returns the subtree with that node deleted if exists

  if not node:
    return None

  if val < node.val:
    node.left = _delete(node.left, val)
  elif val > node.val:
    node.right = _delete(node.right, val)
  else:
    if not node.right:
       return node.left
    elif not node.left:
      return node.right
    elif is_leaf(node):
      return None
    else:
      node.val = _find_max(node.left).val
      node.left = _delete(node.left, node.val)
  return node
