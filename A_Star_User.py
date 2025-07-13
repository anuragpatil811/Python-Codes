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

# Input graph
graph = {}
n = int(input("Enter the number of nodes in the graph: "))
print("Enter the neighbors and costs for each node in the format (neighbor,cost). Type 'done' to finish a node:")
for _ in range(n):
    node = input("Enter the node name: ")
    graph[node] = []
    while True:
        edge = input(f"Enter neighbor and cost for node {node} (or type 'done'): ")
        if edge.lower() == 'done':
            break
        neighbor, cost = edge.split(',')
        graph[node].append((neighbor, int(cost)))

# Input heuristic
heuristic = {}
print("\nEnter the heuristic values for each node:")
for node in graph:
    heuristic[node] = int(input(f"Heuristic value for {node}: "))

# Input start and goal nodes
start_node = input("\nEnter the start node: ")
goal_node = input("Enter the goal node: ")

# Run A* search
path = a_star_search(graph, heuristic, start_node, goal_node)
if path:
    print(f"\nPath found: {' -> '.join(path)}")
else:
    print("\nNo path found.")
