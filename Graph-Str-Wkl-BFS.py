#Python program to chech whether graph is strongly connected or weakly connected
from collections import deque
def add_node(v):
    if v in graph:
        print(v, "is already present in the graph")
    else:
        graph[v] = []
        graph1[v] = []
def add_edge(v1, v2):
    if v1 not in graph:
       print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append(v2)
        graph1[v2].append(v1)
def BFS(node, graph, visited):
    if node not in graph:
        print(node, "not present in the graph")
        return
#    Queue = []
    Queue = deque()
    Queue.append(node)
    visited.add(node)    
    while Queue:
#        current = Queue.pop(0)
        current = Queue.popleft()
        print(current)
        for i in graph[current]:
         if i not in visited:
            Queue.append(i)
            visited.add(i)
visited = set()
visited_t = set()
graph = {}
graph1 = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")


add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "D")
add_edge("C", "D")
add_edge("C", "F")
add_edge("E", "F")
add_edge("E", "G")

print(graph)  
BFS("A", graph, visited)
for i in list(graph):
    if i not in visited:
        print("Given graph is a weakly connected graph")
        break
else:
    BFS("A", graph1, visited_t)
    if visited == visited_t:
       print("Given graph is a strongly connected graph")
    else:
        print("Given graph is a weakly connected graph")