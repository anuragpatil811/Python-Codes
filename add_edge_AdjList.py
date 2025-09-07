#Function to add an edge using adjacency list representation
def add_node(v):
    if v in graph:
        print(v, "is already present in graph")
    else:
        graph[v] = []
def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        list1 = [v2, cost]
        list2 = [v1, cost]
        graph[v1].append(list1)
        graph[v1].append(v2)
#        graph[v2].append(list2)

graph = {}
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 10)
add_edge("A", "B", 5)
#add_edge("A", "B")
#add_edge("A", "C")
print(graph)