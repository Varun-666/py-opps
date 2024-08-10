class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def print_graph(self):
        for node in self.graph:
            print(f"{node} --> {', '.join(map(str, self.graph[node]))}")

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'C')
g.add_edge('E', 'F')
g.add_edge('F', 'C')

g.print_graph()