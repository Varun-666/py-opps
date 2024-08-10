class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
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
        if index == 0:
            self.insert_at_beginning(data)
            return
        position = 0
        current_node = self.head
        while current_node and position < index - 1:
            position += 1
            current_node = current_node.next
        if current_node:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    def get_node_at_index(self, index):
        position = 0
        current_node = self.head
        while current_node and position < index:
            position += 1
            current_node = current_node.next
        if current_node:
            return current_node.data
        else:
            print("Index not present")
            return None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" --> ")
            current_node = current_node.next
        print("None")

    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

class Person:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f"{self.name} (Age: {self.age}, Score: {self.score})"

def input_person_list():
    linked_list = LinkedList()
    while True:
        name = input("Enter the person's name: ")
        if name.lower() == 'quit':
            break
        age = int(input("Enter the person's age: "))
        score = float(input("Enter the person's score: "))
        person = Person(name, age, score)
        linked_list.insert_at_end(person)
    return linked_list

def main():
    linked_list = input_person_list()
    linked_list.print_list()
    print(f"Size of the list: {linked_list.size()}")

    index = 0 
    while index < linked_list.size():
        print(f"Person at index {index}: {linked_list.get_node_at_index(index)}")
        index += 1

if __name__ == "__main__":
    main()