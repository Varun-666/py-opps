class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbour)
        
        if neighbour not in self.graph:
            self.graph[neighbour] = []

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)


g = Graph()

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'F')
g.add_edge('E', 'F')

print("DFS Traversal:")
g.dfs('A')
