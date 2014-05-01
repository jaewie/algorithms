from bst import BST, find_max
from node import Node


class AVL(BST):
  def __init__(self):
    super(AVL, self).__init__()

  def insert(self, value):

    node = Node(value)
    super(AVL, self).insert(node)
    node.update_parent_heights()
    fix_parent_unbalance_by_rotations(node)

  def delete(self, val):

    node = self.find(val)

    if node:
      lc, rc = node.left, node.right
      to_balance = find_max(node.left).parent node.has_both_siblings() else node.parent

      super(AVL, self).delete(val) 

      if not to_balance is None:
        to_balance.update_parent_heights()
        fix_parent_unbalance_by_rotations(to_balance)


def fix_parent_unbalance_by_rotations(parent):
  while parent:
    lc, rc = parent.left, parent.right

    if _is_right_right_case(lc, parent) or _is_right_right_case(rc, parent):
      node = lc if _is_right_right_case(lc, parent) else rc
      node.rotate_left()

    elif _is_left_left_case(lc, parent) or _is_left_left_case(rc, parent):

      node = lc if _is_left_left_case(lc, parent) else rc
      node.rotate_right()

    elif _is_left_right_case(lc, parent) or _is_left_right_case(rc, parent):

      node = lc if _is_left_right_case(lc, parent) else rc
      node = lc.right
      node.rotate_left()
      node.rotate_right()

    elif _is_right_left_case(lc, parent) or _is_right_left_case(rc, parent):

      node = lc if _is_right_left_case(lc, parent) else rc
      node = node.left
      node.rotate_right()
      node.rotate_left()

    parent = parent.parent


def _is_right_left_case(node, parent):
  if not node or not parent:
    return False

  bf = node.balance_factor
  par_bf = parent.balance_factor
  return par_bf == 2 and bf == -1
 
def _is_left_right_case(node, parent):
  if not node or not parent:
    return False

  bf = node.balance_factor
  par_bf = parent.balance_factor
  return par_bf == -2 and bf == 1
 
def _is_left_left_case(node, parent):
  if not node or not parent:
    return False

  bf = node.balance_factor
  par_bf = parent.balance_factor
  return par_bf == -2 and bf == -1

def _is_right_right_case(node, parent):
  if not node or not parent:
    return False

  bf = node.balance_factor
  par_bf = parent.balance_factor
  return par_bf == 2 and bf == 1


if __name__ == '__main__':
  a = AVL()
  a.insert(3)
  a.insert(2)
  a.insert(1)
  a.insert(10)
  a.insert(6)

  a.delete(6)
  a.delete(1)
  a.insert(20)
  a.insert(30)

  a.delete(10)
  a.delete(3)

  root = a.root


