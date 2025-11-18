import heapq
def add_node(v):
    if v in graph:
        print(v, "is already present in the graph")
    else:
        graph[v] = []
def add_edge(v1, v2, weight):
    if v1 not in graph:
       print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append((v2, weight))
        graph[v2].append((v1, weight))
def dijkstra(graph, start):
    if start not in graph:
        print(start, "is not present in the graph")
        return
    distance = {item: float("inf") for item in graph}
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_node=heapq.heappop(queue)
        if current_distance > distance[current_node]:
            continue
        for node, weight in graph[current_node]:
           new_distance = current_distance + weight
           if new_distance < distance[node]:
               distance[node] = new_distance
               heapq.heappush(queue, (new_distance, node))
    return distance
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")
add_node("H")
add_node("I")

add_edge("A", "B", 1)
add_edge("A", "D", 4)
add_edge("A", "F", 7)
add_edge("B", "C", 3)
add_edge("C", "D", 5)
add_edge("C", "E", 4)
add_edge("C", "H", 5)
add_edge("D", "I", 3)
add_edge("D", "G", 2)
add_edge("H", "G", 1)
print(graph) 

shoretest_distances = dijkstra(graph, "A")
if shoretest_distances is not None:
    for i in shoretest_distances:
        print(f"The shortest distance from A to {i} is {shoretest_distances[i]}")
else:
    print("None")