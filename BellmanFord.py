class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}
        self.nodes = set()

    def add_edge(self, s, d, w):
        if s not in self.graph:
            self.graph[s] = []
        self.graph[s].append((d, w))
        self.nodes.update([s, d])

    def addNode(self, value):
        self.nodes.add(value)

    def visualize_graph(self):
        print("Graph Representation (Adjacency List):")
        for node in self.graph:
            print(node, "->", ", ".join(f"{dest}({weight})" for dest, weight in self.graph[node]))

    def bellmanFord(self, src):
        distances = {node: float("Inf") for node in self.nodes}
        distances[src] = 0

        for _ in range(self.V - 1):
            for s in self.graph:
                for d, w in self.graph[s]:
                    if distances[s] != float("Inf") and distances[s] + w < distances[d]:
                        distances[d] = distances[s] + w

        for s in self.graph:
            for d, w in self.graph[s]:
                if distances[s] != float("Inf") and distances[s] + w < distances[d]:
                    print("Graph contains a negative cycle")
                    return

        self.print_solution(distances)

    def print_solution(self, distances):
        print("\nVertex Distance from Source:")
        for node, distance in distances.items():
            print(f"{node}: {distance}" if distance != float("Inf") else f"{node}: ∞")

# Example usage
g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)

# Visualize the graph
g.visualize_graph()

# Perform Bellman-Ford algorithm
print("\nBellman-Ford Algorithm:")
g.bellmanFord("E")


  
