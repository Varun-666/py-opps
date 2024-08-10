class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_index(self, data, index):
        if(index == 0):
            self.insert_at_begining(data)
        position = 0
        current_node = self.head
        while(current_node != None and position + 1 != )

    def insert_from_index(self, data, index):
        

node1 = Node("First Node")
node2 = Node("Second Node")
node3 = Node("Third Node")