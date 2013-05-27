class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
def rev_LL(node):
    ''' Reverse singly linked list node and then return its new head'''

    return _rev_LL(node, node.next)


def _rev_LL(prev_node, cur_node):
    ''' Helper function to reverse linked list.'''

    if cur_node:
        next_node = cur_node.next
        cur_node.next = prev_node
        return _rev_LL(cur_node, next_node)
    return prev_node

def exists_loop(node):
    ''' Return whether linked list node has a cycle.'''

    if not node or not node.next:
        return False
    
    fast_node, slow_node = node.next.next, node.next
    
    while fast_node:
        if fast_node == slow_node:
            return True        
        if not fast_node.next:
            return False
        fast_node = fast_node.next.next
        slow_node = slow_node.next
    return False


def nth_node(node, n):
    ''' Return the nth last node.'''

    if not node or n < 1:
        return None
    
    fast_node = node
    slow_node = node
    
    for i in range(n-1):
        fast_node = fast_node.next
        if not fast_node:
            return None
        
    while fast_node.next:
        fast_node = fast_node.next
        slow_node = slow_node.next
    return slow_node
