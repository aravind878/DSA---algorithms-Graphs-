class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, s, d, w):
        print("Minimum Spanning Tree (MST):")
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))

    def kruskalAlgo(self):
        i, e = 0, 0
        ds = DisjointSet(self.nodes)  # Assuming DisjointSet class is available
        self.graph = sorted(self.graph, key=lambda item: item[2])

        print("Edges sorted by weight:")
        for edge in self.graph:
            print(f"{edge[0]} - {edge[1]}: {edge[2]}")

        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)

            print(f"Checking edge: {s} - {d} ({w})")

            if x != y:
                e += 1
                self.MST.append([s, d, w])
                ds.union(x, y)
                print(f"Selected edge: {s} - {d} ({w}), Added to MST")
                print(f"Sets after adding edge: {ds.get_sets()}")

        self.printSolution(s, d, w)


class DisjointSet:
    def __init__(self, nodes):
        self.parent = {}
        for node in nodes:
            self.parent[node] = node

    def find(self, node):
        if self.parent[node] == node:
            return node
        return self.find(self.parent[node])

    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        self.parent[y_set] = x_set

    def get_sets(self):
        sets = {}
        for node in self.parent:
            root = self.find(node)
            if root in sets:
                sets[root].append(node)
            else:
                sets[root] = [node]
        return sets


g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "D", 6)
g.addEdge("C", "E", 20)

g.kruskalAlgo()

