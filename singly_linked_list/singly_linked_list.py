class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node


    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        
        # if self.tail = None set self.head/tail to the new_node
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        # if self.tail exists run the else block
        else:
            # sets the node after the tail to the new node and then sets that node as the tail
            self.tail.set_next(new_node)
            self.tail = new_node
            

    def remove_head(self):
        if not self.head and not self.tail:
            return None
        elif self.tail is not None:
            value = self.head.value
            self.head = self.head.get_next()
            self.tail = self.tail.get_next()
            return value
        else:
            value = self.head.value
            self.head = self.head.get_next()
            return value


    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.get_next()
        return False

    def get_max(self):
        if self.head == None:
            return None
        else:
            max = self.head.value  
            current = self.head
            while current is not None:  
                if current.value > max:
                    max = current.value
                else: 
                    current = current.next_node
            return max


