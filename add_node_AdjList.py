#Function to add a mode using adjacency list representation
def add_node(v):
    if v in graph:
        print(v, "is already present in graph")
    else:
        graph[v] = []

graph = {}
add_node("A")
add_node("B")
print(graph)