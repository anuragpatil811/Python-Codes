#Program to check whether Given graph is weakly connected or strongly connected using DFS
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
        graph[v2].append(v1)
def DFS(node, visited, graph):
    if node not in graph:
        print("Node is not present")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i, visited, graph)

visited = set()
visited1 = set()
graph = {}
graph1 = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
#add_node("E")
#add_node("F")
#add_node("G")

add_edge("A", "B")
add_edge("C", "A")
add_edge("B", "D")
add_edge("B", "C")
add_edge("D", "C")
#add_edge("E", "G")
#add_edge("G", "D")
"""""
add_edge("A", "B")
add_edge("B", "C")
add_edge("C", "D")
"""""
print(graph) 
print(graph1)
DFS("A", visited, graph)
for i in list(graph):
    if i not in visited:
        print("Weakly connected graph")
        break
else:
    DFS("A", visited1, graph1)
    if visited == visited1:
        print("Strongly connected graph")
    else:
        print("Weakly connected graph")
print(visited, " ", visited1)