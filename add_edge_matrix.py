#Function to add an edge using adjacency matrix representation
# Function to add a node using adjacency matrix representation
def add_node(V):
    global node_count
    if V in nodes:
        print(V, "is already present in the graph")
    else:
        node_count += 1
        nodes.append(V)  # Append the new node to the list of nodes
        # Add a 0 to every existing row to represent no edge to the new node
        for row in graph:
            row.append(0)
        # Create a new row for the new node with zeros
        new_row = [0] * node_count
        graph.append(new_row)

#Unweighted undirected Graph
"""""
def add_edge(V1, V2):
    if V1 not in nodes:
        print(V1, "is not present in the graph")
    elif V2 not in nodes:
        print(V2, "is not present in the graph")
    else:
        index1 = nodes.index(V1)
        index2 = nodes.index(V2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1  
"""""
#Weighted undirected graph
def add_edge(V1, V2, cost):
    if V1 not in nodes:
        print(V1, "is not present in the graph")
    elif V2 not in nodes:
        print(V2, "is not present in the graph")
    else:
        index1 = nodes.index(V1)
        index2 = nodes.index(V2)
        graph[index1][index2] = cost
#        graph[index2][index1] = cost
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"), end=" ")
        print()
nodes = []
graph = []
node_count = 0
print("Before adding nodes:")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("D")
#add_edge("A", "B")
#add_edge("A", "D")
add_edge("A", "B", 10)
add_edge("A", "D", 5)
print(graph)
print_graph()