import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    #need three values for it to be a binary search tree
    #infinate loop vs recurssion- to be recurssion needs to have a base case and be moving towards that base case

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    #start here because we need to have something in the tree to do anything with it
    def insert(self, value):
        #if value is < node.value look left
        if value < self.value:
            # if something is there already
            if self.left:
                # recurse to the left
                    self.left.insert(value)
            # if not
            else:
                self.left = BinarySearchTree(value)
                #insert left
        #if value is >= node.value look right
        if value >= self.value:
            # if something is there already
            if self.right:
                # recurse to the right
                self.right.insert(value)
             # if not
            else:
                #insert right
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return true
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False


    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #call cb on slef.value
        cb(self.value)
        #if  left
        if self.left:
            #call for each
            self.left.for_each(cb)
        #if right  
        if self.right:
            #call for each
            self.right.for_each(cb)
            #call for each

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

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
