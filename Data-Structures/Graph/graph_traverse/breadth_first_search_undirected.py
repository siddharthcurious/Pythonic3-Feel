from collections import deque
def bfs(graph, source, visited):
    visited[source] = True
    q = deque()
    q.append(source)

    while q:
        node = q.popleft()
        print(node)
        for index, value in enumerate(graph[node]):
            if value == 1:
                if visited[index] == False:
                    q.append(index)
                    visited[index] = True

if __name__ == "__main__":

    graph = [
        [0,1,1,0,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,0,1,0,1,1],
        [0,0,0,0,0,1,0,0],
        [0,0,0,1,0,1,0,0],
        [0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,1],
        [0,0,0,1,0,0,0,0]
    ]

    visited = [False] * len(graph)
    bfs(graph, 0, visited)