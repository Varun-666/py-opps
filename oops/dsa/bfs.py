from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbour)
        
        if neighbour not in self.graph:
            self.graph[neighbour] = []

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            print(node, end=' ')
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

g.bfs('A')
