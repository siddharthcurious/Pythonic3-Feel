from collections import deque

def bfs(graph, start, visited):
    visited.append(start)
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        print(node)
        if graph.get(node):
            for vertex in graph[node]:
                if vertex not in visited:
                    visited.append(vertex)
                    queue.append(vertex)

if __name__ == "__main__":

    graph = {
        1: [2,3,4],
        2: [5,7],
        3: [5],
        4: [5],
        5: [9],
        6: [7,9],
        7: [5,9],
        8: [3,9]
    }

    bfs(graph, 1, [])