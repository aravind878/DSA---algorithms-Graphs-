class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    def dfs(self, vertex):
        visited = set()
        stack = [vertex]
        traversal_path = []  # Store the traversal path
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                traversal_path.append(current_vertex)
                visited.add(current_vertex)

            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)

        return traversal_path


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "E")
my_graph.add_edge("C", "D")
my_graph.add_edge("D", "E")

# Print the graph
print("Graph Structure:")
my_graph.print_graph()

# Get the DFS traversal path
dfs_path = my_graph.dfs("A")

# Print the DFS process
print("\nDFS Process:")
for vertex in dfs_path:
    print(vertex)



