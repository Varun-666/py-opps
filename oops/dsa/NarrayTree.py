class NaryNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level = 0):
        print(' ' * level * 2 + str(self.data))
        for child in self.children:
            child.print_tree(level + 1)

root = NaryNode('root')
child1 = NaryNode('child1')
child2 = NaryNode('child2')
child3 = NaryNode('child3')