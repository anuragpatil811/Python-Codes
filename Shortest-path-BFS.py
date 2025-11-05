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
        graph[v1].append(v2)
        graph[v2].append(v1)
def Shortest_path(graph, node, target):
    if node not in graph:
        print(node, "not in graph")
    elif target not in graph:
        print(target, "not in graph")
    else:
        visited = {}
        queue = deque()
        visited[node] = None
        queue.append(node)
        while queue:
            current = queue.popleft()
            if current == target:
                path = []
                while current:
                    path.append(current)
                    current=visited[current]
                return path[::-1]
            for i in graph[current]:
                if i not in visited:
                    visited[i] = current
                    queue.append(i)
graph = {}

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")


add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "D")
add_edge("C", "D")
add_edge("C", "F")
add_edge("E", "F")
add_edge("E", "G")

print(graph)  
result = Shortest_path(graph, "A", "G")
print("Shortest path is:", result)