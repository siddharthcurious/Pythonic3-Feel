from collections import defaultdict
from collections import deque

def bfs(graph, start):
    queue = deque()
    queue.append(start)
    marked = [start]
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if n not in marked:
                marked.append(n)
                queue.append(n)
    print(marked)

if __name__ == "__main__":

    graph = defaultdict(list)
    graph[1].extend([2,3,7])
    graph[2].append(5)
    graph[3].extend([6,4,5])
    graph[4].append(10)
    graph[5].extend([4,11])
    graph[6].extend([9,8])
    graph[7].append(9)
    graph[10].extend([8,11])

    bfs(graph, 5)