class NaryNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print(self, level=0):
        print(' ' * level * 2 + str(self.data))
        for child in self.children:
            child.print(level + 1)

    def helper(self, node, path):
        path.append(self.data)      
        if self.data == node.data:
            return True      
        for child in self.children:
            if child.helper(node, path):
                return True     
        path.pop()
        return False

    def dfs(self, target):
        path = []
        found = self.helper(target, path)
        if found:
            return path
        return None

root = NaryNode('root')
child1 = NaryNode('child1')
child2 = NaryNode('child2')
child3 = NaryNode('child3')
child4 = NaryNode('child4')

root.add_child(child1)
root.add_child(child3)
root.add_child(child4)
child1.add_child(child2)

root.print()

path = root.dfs(child2)

formatted_path = ""
if path != None:
    for i in range(len(path)):
        formatted_path += path[i]
        if len(path) - 1 > i:
            formatted_path += " -> "

print(formatted_path)