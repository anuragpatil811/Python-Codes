import heapq
import copy

GOAL = [[1,2,3],[4,5,6],[7,8,0]]

def heuristic(state):
    return sum(
        state[i][j] != 0 and state[i][j] != GOAL[i][j]
        for i in range(3) for j in range(3)
    )

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    x, y = find_blank(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right
    neighbors = []
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def best_first(start):
    visited = set()
    pq = [(heuristic(start), start)]

    while pq:
        h, state = heapq.heappop(pq)
        print("State with Heuristic", h)
        for row in state:
            print(row)
        print()
        if heuristic(state) == 0:
            print("Goal reached!")
            return
        visited.add(tuple(map(tuple, state)))
        for neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                heapq.heappush(pq, (heuristic(neighbor), neighbor))

initial = [[1,2,3],[4,0,6],[7,5,8]]
best_first(initial)
