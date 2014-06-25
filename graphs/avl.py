from bst import BST, find_max
from avl_node import AVLNode


class AVL(BST):
  def __init__(self):
    super(AVL, self).__init__()

  def insert(self, value):
    node = AVLNode(value)
    super(AVL, self).insert(node)
    node.update_parent_heights()
    fix_parent_unbalance_by_rotations(node)

  def delete(self, val):
    node = self.find(val)

    if node:
      lc, rc = node.left, node.right
      to_balance = find_max(node.left).parent if node.has_both_siblings() else node.parent

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
    return is_correct_balance_factor(node, parent, -1, 2)
def _is_left_right_case(node, parent):
    return is_correct_balance_factor(node, parent, 1, -2)
 
def _is_left_left_case(node, parent):
    return is_correct_balance_factor(node, parent, -1, -2)

def _is_right_right_case(node, parent):
    return is_correct_balance_factor(node, parent, 1, 2)

def is_correct_balance_factor(node, parent, expected_bf, expected_par_bf):
    if not node or not parent:
        return False
    bf = node.balance_factor
    par_bf = parent.balance_factor
    return bf == expected_bf and par_bf == expected_par_bf
