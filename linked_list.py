class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
def rev_LL(node):
    return _rev_LL(node, node.next)


def _rev_LL(prev_node, cur_node):
    if cur_node:
        next_node = cur_node.next
        cur_node.next = prev_node
        return _rev_LL(cur_node, next_node)
    return prev_node
    
    
a = Node(1)
a.next = Node(2)
a.next.next = Node(3)

        