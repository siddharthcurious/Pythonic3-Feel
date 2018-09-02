from collections import defaultdict

graph = defaultdict(list)

graph[1].append(2)
graph[2].append(3)
graph[1].append(4)
graph[3].append(5)
graph[5].append(1)
graph[5].extend([1,4,3])

print(graph)

for node in graph.keys():
    print(node)