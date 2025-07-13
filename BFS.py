from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Adds an edge between node u and node v"""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        """Performs BFS traversal from the given start node"""
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")  # Process the node
                visited.add(node)
                queue.extend(self.graph.get(node, []))  # Add adjacent nodes to queue

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

print("BFS Traversal starting from node 0:")
g.bfs(0)
