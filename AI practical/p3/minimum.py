import heapq

def prim_mst(graph, start):
    visited = set()
    min_heap = [(0, start)]
    mst_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            mst_cost += cost
            for v, weight in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (weight, v))
    return mst_cost

# Graph: adjacency list
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 1), ('D', 6)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 6), ('C', 2)]
}

print("Minimum Spanning Tree Cost:", prim_mst(graph, 'A'))
