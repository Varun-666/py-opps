class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=' ')
        if self.right:
            self.right.print_tree()

    def is_empty(self):
        return self.data is None

    def search(self, v):
        if self.is_empty():
            print("{} is not found".format(v))
            return False
        if self.data == v:
            print("{} is found".format(v))
            return True
        elif v < self.data:
            if self.left is None:
                print("{} is not found".format(v))
                return False
            else:
                return self.left.search(v)
        else:
            if self.right is None:
                print("{} is not found".format(v))
                return False
            else:
                return self.right.search(v)

root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(5)
root.insert(9)
root.insert(23)
print("Binary Search Tree (In-Order Traversal):")
root.print_tree()
print("\nSearching for values:")
root.search(5)
root.search(20)
