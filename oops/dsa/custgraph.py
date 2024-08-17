class Element:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, nodeVal=None, neghVal=None):
        if node not in self.graph:
            self.graph[node] = {"element": None, "edges": []}
            if nodeVal is not None:
                self.graph[node]["element"] = Element(nodeVal)
        if neighbor not in self.graph:
            self.graph[neighbor] = {"element": None, "edges": []}
            if neghVal is not None:
                self.graph[neighbor]["element"] = Element(neghVal)
                
        self.graph[node]["edges"].append(neighbor)

    def print_graph(self):
        for node, data in self.graph.items():
            element = str(data["element"]) if data["element"] is not None else "None"
            edges = ", ".join([str(edge) for edge in data["edges"]])
            print(f"{node} ({element}) ---> {edges}")

g = Graph()
g.add_edge('A', 'B', 12, 13)
g.add_edge('A', 'C', None, 15)
g.add_edge('B', 'D', None, 18)
g.add_edge('C', 'D', None, None)
g.add_edge('D', 'C', None, None)
g.add_edge('E', 'F', 20, 21)
g.add_edge('F', 'C', None, None)

g.print_graph()
