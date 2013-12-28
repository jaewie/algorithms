from Queue import Queue


class Node(object):
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
        self.parent = None
        
        
def in_order(root):
    '''Return the inorder traversal of node'''
    
    if root:
        return in_order(root.left) + [root.data] + in_order(root.right)
    return []


def bfs(root):
    '''Return a BFS of node iteratively'''
    
    queue = Queue()
    queue.put(root)
    res = []
    while not queue.empty():
        node = queue.get()
        res.append(node.data)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)
    return res

def dfs(root):
    '''Return a DFS of node iteratively'''
    
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)            
    return res
    
def is_BST(root):
    '''Return whether root is a binary search tree.'''

    lst = in_order(root)
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))

def rec_DFS(node, lst=None):
    '''Return a DFS of node recursively'''
    if lst is None:
        lst = []
    
    if node:
        lst.append(node.data)
        if node.left:
            rec_DFS(node.left)
        if node.right:
            rec_DFS(node.right)
    return lst

def insert_into_BST(root, node):
    ''' Insert node into BST root. It's assumed all values are distinct'''
    
    if is_leaf(root):
        if root.data < node.data:
            root.right = node
        else:
            root.left = node
        node.parent = root        
    else:
        if root.data < node.data:
            insert_into_BST(root.right, node)
        else:
            insert_into_BST(root.left, node)
    
def find_node(node, val):
    if node:
        if node.data < val:
            return find_node(node.right, val)
        elif node.data > val:
            return find_node(node.left, val)
        else:
            return node

def is_leaf(node):
    ''' Return whether node is a leaf.'''

    return node and not node.left and not node.right
    
def height(node):
    '''Return the height of the tree rooted at node.'''

    if node:
        return 1 + max(height(node.left), height(node.right))
    return 0