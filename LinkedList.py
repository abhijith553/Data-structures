class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begin(self, data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def print_LL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data, end="->")
            current_node = current_node.next
