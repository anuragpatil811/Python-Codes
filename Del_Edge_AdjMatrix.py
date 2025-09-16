#Function to delete an edge using adjacency matrix representation
nodes = []
node_count=0
graph = []
def add_node(V):
    global node_count
    if V in nodes:
        print(V, "is already present ", nodes)
    else:
        node_count = node_count + 1
        nodes.append(V)  # Append the new node to the list of nodes        
        for n in graph:
            n.append(0)  # Add a 0 to every existing row to represent no edge to the new node
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
def add_edge(V1, V2, e):
    global graph
    if V1 not in nodes:
        print("No")
    elif V2 not in nodes:
        print("No")
    else:
        index1 = nodes.index(V1)
        index2 = nodes.index(V2)
        graph[index1][index2] = e
        graph[index1][index2] = e
def delete_node(V):
    global node_count
    if V not in nodes:
        print(V, "is not present in the graph")
    else:
        index1 = nodes.index(V)
        node_count = node_count-1
        nodes.remove(V)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)
def delete_edge(V1, V2):
    if V1 not in nodes:
        print(V1, "is not present in graph")
    elif V2 not in nodes:
        print(V2, "is not present in graph")
    else:
        index1 = nodes.index(V1)
        index2 = nodes.index(V2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"), end=" ")
        print()
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 10)
add_edge("A", "C", 5)
print_graph()
delete_edge("A", "C")
print("Graph after deleting:")
print_graph()
print("nodes:", nodes)