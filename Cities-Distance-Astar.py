import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 4), ('E', 2)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 4, 'D': 6,
    'E': 2, 'F': 1, 'G': 0
}

def a_star_city(start, goal):
    pq = [(heuristic[start], 0, start)]
    visited = set()

    while pq:
        f, g, city = heapq.heappop(pq)
        print(f"Visiting: {city}, Cost: {g}")
        if city == goal:
            print("Goal reached!")
            return
        visited.add(city)
        for neighbor, cost in graph.get(city, []):
            if neighbor not in visited:
                total_cost = g + cost
                heapq.heappush(pq, (total_cost + heuristic[neighbor], total_cost, neighbor))

a_star_city('A', 'G')
