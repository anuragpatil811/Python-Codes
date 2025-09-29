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
def DFSiterative(node, graph):
    visited = set()
    if node not in graph:
        print("Node is not present in the graph")
        return
    stack = []
    stack.append(node)
    while stack:
         
       current = stack.pop() 
       if current not in visited:
           print(current)
           visited.add(current)
           for i in graph[current]:
              stack.append(i)
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")

add_edge("A", "B")
add_edge("A", "E")
add_edge("A", "C")
add_edge("B", "D")
add_edge("F", "C")
add_edge("F", "G")
add_edge("G", "D")
print(graph) 
DFSiterative("A", graph)
print(graph)