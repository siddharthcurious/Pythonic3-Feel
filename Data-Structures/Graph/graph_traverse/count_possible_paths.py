def possibe_paths(graph, source, target, visited, path, paths_count):
    visited[source] = True
    path.append(source)

    if source == target:
        print(path)
        paths_count[0] = paths_count[0] + 1

    else:
        if graph.get(source):
            for node in graph[source]:
                if visited[node] == False:
                    possibe_paths(graph, node, target, visited, path, paths_count)

    visited[source] = False
    path.pop()

if __name__ == "__main__":

    graph = {
        "A": ["B", "C", "E"],
        "B": ["D", "E"],
        "C": ["E"],
        "D": ["C"]
    }

    visited = {
        "A": False,
        "B": False,
        "C": False,
        "D": False,
        "E": False
    }

    path = []
    paths_count = [0]
    possibe_paths(graph, "A", "E", visited, path, paths_count)
    print(paths_count[0])