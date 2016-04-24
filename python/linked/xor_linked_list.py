import ctypes


# This is hacky. It's a data structure for C, not python.
class Node(object):
    def __init__(self, val):
        self.val = val
        self.xor_addr = 0


class XorLinkedList(object):
    def __init__(self):
        self.head = self.tail = None
        self.__nodes = [] # This is to prevent garbage collection

    def append(self, val):
        node = Node(val)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.xor_addr = id(node) ^ self.tail.xor_addr
            node.xor_addr = id(self.tail)
            self.tail = node

        self.__nodes.append(node)


    def find(self, val):
        prev_id = 0
        node = self.head
        while node:
            if node.val == val:
                return node

            next_id = prev_id ^ node.xor_addr

            if next_id:
                prev_id = id(node)
                node = _get_obj(next_id)
            else:
                node = None


def _get_obj(id):
    return ctypes.cast(id, ctypes.py_object).value
