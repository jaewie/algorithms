from tree_node import TreeNode


class BST(object):

    def __init__(self):
        self._root = None

    def insert(self, ele):
        node = ele if isinstance(ele, TreeNode) else TreeNode(ele)
        self._root = _insert(self.root, node)

    def delete(self, val):
        self._root = _delete(self.root, val)

    def find(self, val):
        return find(self._root, val)

    @property
    def root(self):
        while self._root and self._root.has_parent():
            self._root = self._root.parent

        return self._root


def _insert(node, insert_node):
    if not node:
        return insert_node

    if insert_node.val <= node.val:
        node.left = _insert(node.left, insert_node)
        node.left.parent = node
    elif insert_node.val > node.val:
        node.right = _insert(node.right, insert_node)
        node.right.parent = node
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


def find_max(node):
    if not node or not node.right:
        return node
    return find_max(node.right)


def is_leaf(node):
    return node and not node.left and not node.right


def _delete(node, val):
    # assume that this returns the tree with the node with value val deleted
    # if exists

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
            node.val = find_max(node.left).val
            node.left = _delete(node.left, node.val)
    return node
