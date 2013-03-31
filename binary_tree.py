class Node(object):
    def __init__(self, d):
        self.d = d
        self.left = None
        self.right = None
        
        
def in_order(root):
    if root:
        return in_order(root.left) + [root.d] + in_order(root.right)
    return []


def bfs(root):
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