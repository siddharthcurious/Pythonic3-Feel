def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

gdict = { "a" : {"b","c"},
          "b" : {"a", "d"},
          "c" : {"a", "d"},
          "d" : {"e"},
          "e" : {"a"}
        }

dfs(gdict, 'a')