def add_node(v):
    if v in graph:
        print(v, "is already present in the graph")
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
        graph[v1].append(list2)
#        graph[v1].append(v2)
#        graph[v2].append(v1)
def delete_node(v):
    if v not in graph:
        print(v, "is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
#            if v in list1:
#                list1.remove(v)
            for j in list1:
                if v == j[0]:
                    list1.remove(j)
                    break
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")
add_edge("A", "B", 10)
add_edge("A", "E", 5)
add_edge("A", "C", 6)
add_edge("B", "D", 8)
add_edge("F", "C", 9)
add_edge("F", "G", 11)
add_edge("G", "D", 7)
print(graph) 
delete_node("C")
print(graph)