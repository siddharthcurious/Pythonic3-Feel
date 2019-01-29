def dfs(graph, start, visited):
    visited.append(start)
    print(start)
    if graph.get(start):
        for node in graph[start]:
            if node not in visited:
                graph[start].remove(node)
                dfs(graph, node, visited)

if __name__ == "__main__":

    graph = {
        1: [2, 3, 4],
        2: [5],
        3: [6],
        4: [5, 6],
        5: [7],
        6: [7],
        7: [8]
    }

    dfs(graph, 1, [])

