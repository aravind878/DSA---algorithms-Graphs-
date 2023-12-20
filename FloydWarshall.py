INF = 9999

def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

def floydWarshall(nV, G):
    distance = G

    print("Initial Matrix:")
    printSolution(nV, distance)
    print("\nApplying Floyd-Warshall Algorithm...\n")

    for k in range(nV):
        print(f"Step {k + 1}:")
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        printSolution(nV, distance)
        print()

    print("Final Matrix:")
    printSolution(nV, distance)

# Example usage
G = [
    [0, 8, INF, 1],
    [INF, 0, 1, INF],
    [4, INF, 0, INF],
    [INF, 2, 9, 1]
]

floydWarshall(4, G)
