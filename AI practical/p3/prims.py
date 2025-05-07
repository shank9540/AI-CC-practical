def prim(graph):
    import heapq
    start = 0
    visited = [False] * len(graph)
    min_heap = [(0, start)]
    mst_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if not visited[u]:
            visited[u] = True
            mst_cost += cost
            for v, w in graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
    return mst_cost

# Graph as adjacency list (index-based)
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}
print("Prim's MST Total Cost:", prim(graph))
