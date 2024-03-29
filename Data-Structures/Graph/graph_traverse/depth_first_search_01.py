def dfs(graph, source, visited):
    visited.append(source)
    print(source)
    if graph.get(source):
        for node in graph[source]:
            if node not in visited:
                dfs(graph, node, visited)

if __name__ == "__main__":

    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [5, 9],
        5: [8],
        6: [5, 8],
        7: [6, 9],
        8: [9]
    }

    visited = []
    dfs(graph, 1, visited)
    print(visited)