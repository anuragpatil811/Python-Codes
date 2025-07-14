from queue import PriorityQueue
def a_star_search(graph, heuristic, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    came_from = {}
    
    while not open_set.empty():
        _, current = open_set.get()
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  
        
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                priority = tentative_g_score + heuristic[neighbor]
                open_set.put((priority, neighbor))
                came_from[neighbor] = current

    return None

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('F', 2)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 5)],
    'G': []
}
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 3,
    'G': 0
}

start_node = 'A'
goal_node = 'G'
path = a_star_search(graph, heuristic, start_node, goal_node)
if path:
    print(f"Path found: {' -> '.join(path)}")
else:
    print("No path found.")
