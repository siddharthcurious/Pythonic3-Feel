import copy
def dfs(graph, source, visited):
    visited.append(source)
    if graph.get(source):
        for node in graph[source]:
            if node not in visited:
                graph[source].remove(node)
                dfs(graph, node, visited)

def path_print():
    pass

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

    graph_copy = copy.deepcopy(graph)
    print(graph_copy)
    dfs(graph_copy, 1, [])