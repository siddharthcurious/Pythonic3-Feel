def has_cycle(graph, source, visited, recstack):
    visited[source] = True
    recstack[source] = True
    if graph.get(source):
        for node in graph[source]:
            if visisted[node] == False:
                if has_cycle(graph, node, visisted, recstack) == True:
                    return True
                elif recstack[node] == True:
                    return True
    recstack[source] = False
    return False

if __name__ == "__main__":

    graph = {
        0: [1, 6],
        1: [2, 6],
        2: [3, 6],
        3: [4],
        4: [5, 6],
        5: [0],
        6: [3, 5]
    }

    visisted = [False]*7
    recstack = [False]*7
    r = has_cycle(graph, 0, visisted, recstack)
    print(r)