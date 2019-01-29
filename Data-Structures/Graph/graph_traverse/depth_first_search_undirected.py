def dfs(graph, source, visited):
    visited[source] = True
    print(source)
    for index, value in enumerate(graph[source]):
        if value == 1:
            if visited[index] == False:
                dfs(graph, index, visited)

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
    dfs(graph, 0, visited)