class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
def rev_LL(node):
    ''' Reverse singly linked list node and then return its new head node'''
    
    if node:
        next_node = node.next
        node.next = None
        return _rev_LL(node, next_node)


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