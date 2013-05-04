class Node(object):
    def __init__(self, d):
        self.d = d
        self.left = None
        self.right = None
        self.parent = None
        
        
def in_order(root):
    '''Return the inorder traversal of node'''
    
    if root:
        return in_order(root.left) + [root.d] + in_order(root.right)
    return []


def bfs(root):
    '''Return a BFS of node iteratively'''
    
    queue = [root]
    res = []
    while queue:
        node = queue.pop(0)
        res.append(node.d)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res

def dfs(root):
    '''Return a DFS of node iteratively'''
    
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.d)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)            
    return res
    


def is_BST(root):
    '''Check if root is a binary search tree.'''    
    lst = in_order(root)
    
    for i in range(len(lst) -1):
        if lst[i] > lst[i+1]:
            return False
    return True

def rec_DFS(node, lst=[]):
    '''Return a DFS of node recursively'''

    if node in lst:
        return True
    lst.append(node.d)
    if node.left:
        rec_DFS(node.left)
    if node.right:
        rec_DFS(node.right)
    return lst

def in_order_predc(node):
    ''' Return the next biggest node.'''

    if not node:
        return None
    
    if node.right:
        while node.left:
            node = node.left
        return node
    
    while node.parent:
        node = node.parent
    return node

def insert_into_BST(root, node):
    ''' Insert node into BST root. It's assumed all values are distinct'''
    if not root:
        root = node
    
    if is_leaf(root):
        if root.d > node.d:
            root.left = node
        else:
            root.right = node
    else: # Otherwise, traverse through the BST
        if root.d > node.d:
            insert_into_BST(root.left, node)
        else:
            insert_into_BST(root.right, node)

def is_leaf(node):
    ''' Return whether node is a leaf.'''

    return node and not node.left and not node.right
    
root = None

insert_into_BST(root, Node(3))
print root

                
                