from binary_tree import height, is_leaf, insert_into_BST

class Node(object):
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, node):
        '''Insert node and balance the tree.'''

        insert_into_BST(self, node)
        get_root(self).balance()
        
    def balance(self):
        '''Balance the nodes.'''
    
        balance_factor = get_bf(self)

        # Balance factor would never go above 2 or below -2
        
        if self:
            if balance_factor == 2:
                if get_bf(self.right) == 1: # Single left rotation
                    self.right.left_rotate()
                else: # Need to right-left rotate
                    to_rotate = self.right.left # This node always exists
                    to_rotate.right_rotate()
                    to_rotate.left_rotate()
            
            elif balance_factor == -2:
                if get_bf(self.left) == -1: # Single right rotation
                    self.left.right_rotate()
                else: # Need to left-right rotate
                    to_rotate = self.left.right # This node always exists too
                    to_rotate.left_rotate()
                    to_rotate.right_rotate()
            else:
                if self.right:
                    self.right.balance()
                if self.left:
                    self.left.balance()
                    
        
    def left_rotate(self):
        '''Left rotate.'''

        # Rotating A when it has no parent is the same as rotating C to the left
        #   A                C
        #  / \              / \
        # B   C     ==>    A   .
        #    / \          / \
        #   D   .        B   D
        
        if not self.parent:
            self.right.left_rotate() # 
            
        # rotating A when it does have a parent
        #   R                     R
        #  / \                   / \
        # .   C                 .   A  
        #    / \    ===>           / \
        #   .   A                 C   .
        #      / \               / \
        #     B   .             .   B
        else:
            if self.parent.right == self: # A is a right child
                A = self
                B = self.left
                C = self.parent
                R = C.parent
    
                if R:
                    if R.right == C:
                        R.right = A
                    else:
                        R.left = A
                    A.parent = R
                else:
                    A.parent = None
                
                A.left = C
                C.parent = A
                C.right = B
                if B:
                    B.parent = C
            else: # A is a left child
        #    C            C
        #   /            /
        #  A            E
        # / \    ===>  /
        #    E        A 
        #   /          \
        #  F            F    
        
                A = self
                C = self.parent
                E = self.right
                F = E.left
                
                C.left = E
                E.parent = C
                E.left = A
                A.parent = E
                A.right = F
                if F:
                    F.parent = A

    def right_rotate(self):
        '''Right rotate.'''

        parent = get_root(self)
        mirror(parent)
        self.left_rotate()
        mirror(parent)


def get_root(node):
    '''Return the root of node.'''

    while node.parent:
        node = node.parent
    return node

def mirror(node):
    if node:
        node.left, node.right = node.right, node.left
        mirror(node.left)
        mirror(node.right)

def get_bf(node):
    '''Return the balance factor of node.'''

    return height(node.right) - height(node.left)

if __name__ == "__main__":
    a = Node(5)
    a.insert(Node(8))
    a.insert(Node(10))
    print a.parent.right.data