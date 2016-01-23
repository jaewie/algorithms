from tree_node import TreeNode


class MerkleNode(TreeNode):
    def __init__(self, value):
        super(MerkleNode, self).__init__(value)
        self.hash = str(value)
