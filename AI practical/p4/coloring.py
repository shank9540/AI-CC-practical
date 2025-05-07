def is_safe(node, graph, color, c):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and color[neighbor] == c:
            return False
    return True

def graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n

    def backtrack(node):
        if node == n:
            return True
        for c in range(1, m + 1):
            if is_safe(node, graph, color, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        return False

    if backtrack(0):
        print("Color assignment:", color)
    else:
        print("No solution with", m, "colors.")

# Example graph (4 nodes)
graph = [
    [0, 1, 1, 1],  # Node 0 connected to 1, 2, 3
    [1, 0, 1, 0],  # Node 1 connected to 0, 2
    [1, 1, 0, 1],  # Node 2 connected to 0, 1, 3
    [1, 0, 1, 0]   # Node 3 connected to 0, 2
]

print("Graph Coloring:")
graph_coloring(graph, m=3)  # Try with 3 colors
