from collections import deque
def add_node(v):
    if v in graph:
        print(v, "is already present in the graph")
    else:
        graph[v] = []
def add_edge(v1, v2):
    if v1 not in graph:
       print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
#        list1 = [v2, cost]
#        list2 = [v1, cost]
        graph[v1].append(v2)
        graph[v2].append(v1)
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
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
#add_node("F")
#add_node("G")

#add_edge("G", "D", 7)
add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "C")
add_edge("C", "D")
add_edge("B", "E")
add_edge("E", "D")
add_edge("A", "D")
#add_edge("E", "F")
#add_edge("E", "G")
#add_edge("G", "D")
print(graph) 
print("BFS")
BFS("C", graph, visited)