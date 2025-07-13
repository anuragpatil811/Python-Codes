#g= graph
#s = start
#v = visited
#DFS = Depth First Search
#n  = neighbour
def DFS(g, s, v=None):
    if v is None:
        v = set()
    v.add(s)
    print(s, end="")
    for n in g[s]:
        if n not in v:
            DFS(g, n, v)
if __name__== "__main__":
    g = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("Depth First Search starting from node 'A': ")
    DFS(g, 'A')