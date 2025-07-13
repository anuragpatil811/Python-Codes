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
def best_first_city(start, goal):
    visited = set()
    pq = [(heuristic[start], start)]

    while pq:
        h, city = heapq.heappop(pq)
        print(f"Visiting: {city} (Heuristic: {h})")
        if city == goal:
            print("Goal reached!")
            return
        visited.add(city)
        for neighbor, _ in graph.get(city, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

best_first_city('A', 'G')
