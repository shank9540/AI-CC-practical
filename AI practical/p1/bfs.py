graph={
            "A":["B","D"],
            "B":["A","C"],
            "D":["F","E","A"],
            "C":["B"],
            "E":["D","F","G"],
            "F":["D","E","H"],
            "G":["E","H"],
            "H":["F","G"]
        }
print(graph)
visited={}
level= {}
parent={}
bts_traversal_output=[]
for node in graph.keys():
    visited[node]=False
    parent [node]=None
    level[node]=-1
print(visited)
print(parent)
print(level)
from queue import Queue
queue=Queue()
s="A"
visited [s]=True
level[s]=0
queue.put(s)
while not queue.empty():
    u= queue.get()
    bts_traversal_output.append(u)
    for v in graph[u]:
        if not visited[v]:
            visited [v]= True
            parent [v] = u
            level [v] = level [u]+1
            queue.put(v)
print(visited)
print(parent)
print(level)