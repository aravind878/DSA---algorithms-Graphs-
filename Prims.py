#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# Prims Algorithm  in Python
import sys

class Graph:
    def __init__(self, vertexNum, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.vertexNum = vertexNum
        self.MST = []

    def printSolution(self):
        print("Minimum Spanning Tree (MST):")
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s -> %s: %s" % (s, d, w))

    def primsAlgo(self):
        visited = [0] * self.vertexNum
        edgeNum = 0
        visited[0] = True

        while edgeNum < self.vertexNum - 1:
            min_weight = sys.maxsize
            s, d = 0, 0

            for i in range(self.vertexNum):
                if visited[i]:
                    for j in range(self.vertexNum):
                        if not visited[j] and self.edges[i][j] and min_weight > self.edges[i][j]:
                            min_weight = self.edges[i][j]
                            s, d = i, j

            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edgeNum += 1

            print(f"Selected edge: {self.nodes[s]} - {self.nodes[d]} ({self.edges[s][d]})")
            print(f"Visited nodes: {self.get_visited_nodes(visited)}")

        self.printSolution()

    def get_visited_nodes(self, visited):
        return [self.nodes[i] for i in range(self.vertexNum) if visited[i]]


edges = [
    [0, 10, 20, 0, 0],
    [10, 0, 30, 5, 0],
    [20, 30, 0, 15, 6],
    [0, 5, 15, 0, 8],
    [0, 0, 6, 8, 0]
]

nodes = ["A", "B", "C", "D", "E"]
g = Graph(5, edges, nodes)
g.primsAlgo()
