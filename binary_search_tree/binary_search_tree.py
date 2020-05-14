"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from linked_list import LinkedList
from bst_doubly_linked_list import DoublyLinkedList
from collections import deque


class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = []
        self.storage = LinkedList()

    def __len__(self):
        # return len(self.storage)
        return self.size

    def push(self, value):
        # return self.storage.append(value)
        self.storage.add_to_end(value)
        self.size += 1

    def pop(self):
        # if len(self.storage) == 0:
        #     return None
        # else:
        #     return self.storage.pop()

        if self.storage.head:
            self.size -= 1
            return self.storage.remove_from_end()


class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = []
        # self.storage = LinkedList()
        self.storage = DoublyLinkedList()

    def __len__(self):
        # return len(self.storage)
        return self.size

    def enqueue(self, value):
        # self.storage.append(value)
        print(value)
        self.size += 1
        self.storage.add_to_tail(value)
        

    def dequeue(self):
        # if len(self.storage) == 0:
        #     return None
        # else:
        #     return self.storage.pop(0)
        if self.storage.head:
            self.size -= 1
            return self.storage.remove_from_head()
        return None


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self

        # criteria for returning false: we know we need to go in one direction
        # but there's nothing in the left or right direction
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current_max = self.value

        while self.right is not None:
            current_max = self.right.value
            self.right = self.right.right
        return current_max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        if node.left is not None:
            node.in_order_print(node.left)

        print(node.value)

        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a new queue
        queue = deque()
        # add the current node to the queue
        queue.append(node)
        # run if the queue is not empty
        while len(queue) > 0:
            current = queue.popleft()
            print(current.value)
            # if there is a node to the left of the current node, add it to the queue
            if current.left is not None:
                queue.append(current.left)
            # if there is a node to the right of the current node, add it to the queue
            if current.right is not None:
                queue.append(current.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while len(stack) > 0:
            current = stack.pop()
            print(current.value)
            if current.left is not None:
                stack.push(current.left)
            if current.right is not None:
                stack.push(current.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

