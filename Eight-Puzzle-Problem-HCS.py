import copy

GOAL = [[1,2,3],[4,5,6],[7,8,0]]

def heuristic(state):
    return sum(
        state[i][j] != GOAL[i][j] and state[i][j] != 0
        for i in range(3) for j in range(3)
    )

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    x, y = find_blank(state)
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    neighbors = []
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def hill_climb(start):
    current = start
    while True:
        print("Current State:")
        for row in current:
            print(row)
        h = heuristic(current)
        print("Heuristic:", h)
        if h == 0:
            print("Goal reached!")
            break
        neighbors = get_neighbors(current)
        next_state = min(neighbors, key=heuristic)
        if heuristic(next_state) >= h:
            print("Local minimum reached.")
            break
        current = next_state

initial = [[1,2,3],[4,0,6],[7,5,8]]
hill_climb(initial)
