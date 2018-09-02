import collections

def bfs(graph, startnode):
        seen = {startnode}
        queue = collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            marked(vertex)
            for node in graph[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)

def marked(n):
    print(n)

gdict = {
    "a" : {"b","c"},
    "b" : {"a", "d"},
    "c" : {"a", "d"},
    "d" : {"e"},
    "e" : {"a"}
    }

bfs(gdict, "a")

