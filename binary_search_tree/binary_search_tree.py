import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current = None
        parent = self
        if parent.value is None:
            parent.value = value
            return
        node = BinarySearchTree(value)
        while True:
            if value < parent.value:
                current = parent.left
                if not current:
                    parent.left = node
                    return
            # elif value == parent.value: return
            else:
                current = parent.right
                if not current:
                    parent.right = node
                    return
            parent = current


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = None
        parent = self
        if parent.value is None: return False
        while True:
            if target < parent.value:
                current = parent.left
                if not current: return False
            elif target == parent.value: return True
            else:
                current = parent.right
                if not current: return False
            parent = current


    # Return the maximum value found in the tree
    def get_max(self, node=None, recursive=False):
        if not node and recursive: return False
        if not node: node = self
        if not node.left and not node.right: return node.value
        elif not node.right: return max(node.value, node.get_max(node.left, True))
        elif not node.left: return max(node.value, node.get_max(node.right, True))
        return max(node.value, node.get_max(node.left, True), node.get_max(node.right, True))

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb, node=None, recursive=False):
        if not cb: return
        if not node and recursive: return
        if not node: node = self
        if node.value: cb(node.value)
        self.for_each(cb, node.left, True)
        self.for_each(cb, node.right, True)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
