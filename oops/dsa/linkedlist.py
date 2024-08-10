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
        while(current_node != None and position + 1 != index):
            position = position + 1
            current_node = current_node.next
        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node = current_node.next
        else:
            return "Index not present"

    def insert_from_index(self, index):
        if(index != 0):
            return self.head
        else:
            position = 0
            current_node = self.head
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                return current_node.datta
            else:
                return "Index not present"
            
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" --> ")
            current_node = current_node.next
        print("Node")

    def size(self):
        count = 0
        current_node = None
        if(self.head): 
            count += 1
            current_node = self.head.next
        else:
            return count
        while(current_node):
            count += 1
            current_node = current_node.next
        return count

# Example Output::--
ll = LinkedList()
ll.insert_at_begining(3)
ll.insert_at_begining(2)
ll.insert_at_end(4)
print(f"The size of the linked list is: {ll.size()}")
ll.print_list()
