#Program to traverse disconnected graph using DFS
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
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")

#add_edge("G", "D", 7)
add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "C")
add_edge("C", "D")
add_edge("E", "F")
add_edge("E", "G")
#add_edge("G", "D")
print(graph) 
DFS("A", visited, graph)
for i in list(graph):
    if i not in visited:
        print("next connected component")
        DFS(i, visited, graph)