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
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()
nodes = []
graph = []
node_count = 0
print("Before adding nodes:")
print(nodes)
print(graph)
add_node("A")
add_node("B")
print("After adding nodes:")
print(nodes)
print(graph)
print_graph()