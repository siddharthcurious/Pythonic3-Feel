def bipartite(graph, source, visited, color):
    for node in graph[source]:
        if visited[node] == False:
            visited[node] = True

            color[node] = not color[source]



if __name__ == "__main__":

    graph = {
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 1
    }

    N = 7
    visited = [False] * N
    color = [False] * N
    v = 1
    bipartite(graph, v, visited, color)

