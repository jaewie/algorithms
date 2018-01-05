from bst import BST
from merkle_node import MerkleNode
from hashlib import sha1


class MerkleTree(BST):

    def __init__(self):
        super(MerkleTree, self).__init__()

    def insert(self, value):
        node = MerkleNode(value)
        super(MerkleTree, self).insert(node)

        parent = node.parent

        while parent:
            parent.hash = _hash(parent.left, parent.right)
            parent = parent.parent

    @property
    def hash(self):
        return self.root.hash

    def __eq__(self, other_tree):
        return isinstance(other_tree, MerkleTree) and other_tree.hash == self.hash


def _hash(node0, node1):
    key = ''
    if node0:
        key += node0.hash
    else:
        key += 'None'

    if node1:
        key += node1.hash
    else:
        key += 'None'

    return sha1(key).hexdigest()

def hash(left_child, right_child, value):
    key = ''.join((left_child.hash, right_child.hash, sha1(value).hexdigest()))
    return sha1(key).hexdigest()
