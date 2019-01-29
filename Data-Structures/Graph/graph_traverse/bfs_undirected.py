from collections import deque
def bfs_undirected(graph, start):
    q = deque()
    q.append(start)
    visited = []
    visited.append(start)

    while q:
        node = q.popleft()
        for n in range(len(graph[node])):
            if graph[node][n] == 1 and n not in visited:
                visited.append(n)
                q.append(n)
    print(visited)

if __name__ == "__main__":

    graph = [
        [0,1,0,1,0,0,0],
        [1,0,1,0,1,0,0],
        [0,1,0,1,0,0,0],
        [1,0,1,0,0,1,0],
        [0,1,0,0,0,0,1],
        [0,0,0,1,0,0,1],
        [0,0,0,0,1,1,0]
    ]

    bfs_undirected(graph, 0)
    bfs_undirected(graph, 1)
    bfs_undirected(graph, 3)
    bfs_undirected(graph, 4)
    bfs_undirected(graph, 6)
    bfs_undirected(graph, 5)