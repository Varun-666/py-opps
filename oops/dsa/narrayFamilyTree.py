class NaryNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        print(' ' * level * 2 + str(self.data))
        for child in self.children:
            child.print_tree(level + 1)

    def find_ancestors(self, target, path=None):
        if path is None:
            path = []

        path.append(self.data)
        
        if self.data == target:
            print("Ancestors of", target, ":", ' > '.join(path))
            return True

        for child in self.children:
            if child.find_ancestors(target, path.copy()):
                return True
        
        return False

grandparent = NaryNode('Ramesh')
parent1 = NaryNode('Suresh')
parent2 = NaryNode('Arjun')
child1 = NaryNode('Karan')
child2 = NaryNode('Arun')
child3 = NaryNode('Rahul')
child4 = NaryNode('Anil')
child5 = NaryNode('Ankit')
grandchild = NaryNode('Anish')

grandparent.add_child(parent1)
grandparent.add_child(parent2)

parent1.add_child(child1)
parent1.add_child(child2)

parent2.add_child(child3)
parent2.add_child(child4)
parent2.add_child(child5)

child5.add_child(grandchild)

print("Family Tree:")
grandparent.print_tree()

name = str(input("Enter the name of the person to find family history: "))
grandparent.find_ancestors(name)