import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:# if arg less than current root

            if not self.left:# if left of root is empty
                self.left = BinarySearchTree(value)# insert left of root

            else:# if there left value
                self.left.insert(value)# set left as new root for insert

        else:# if arg more than current root

            if not self.right:# if right of root is empty
                self.right = BinarySearchTree(value)# insert right of root

            else:# if there right value
                self.right.insert(value)# set right as new root for insert

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:# if root is target
            return True

        if target < self.value:# if target less than root

            if not self.left:# if ther no left return false
                return False

            else:# if there is a left
                # set left as new root for contains
                return self.left.contains(target)

        else:# if target more than root

            if not self.right:# if ther no right return false
                return False

            else:# if there is a right
                # set right as new root for contains
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):# To the right to the right
        if not self.right: 
            return self.value
        else: 
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)
            

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
           self.in_order_print(node.left)
           print(node.value)
           self.in_order_print(node.right)
        # print(node.value)

        # if node.right:
        #     self.in_order_print(node.right)



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return
        q = Queue() # make your queue
        q.enqueue(node)# adds to back of queue
        while q.size > 0:
            node = q.dequeue()# remove and return from front of queue
            # print(node.value)
            if node is not None:
                q.enqueue(node.left)
                print(node.value)
                q.enqueue(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node is None:
          return
        s = Stack()
        s.push(node)
        while s.size > 0:
            node = s.pop()
            if node is not None:
                s.push(node.left)
                print(node.value)
                s.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
