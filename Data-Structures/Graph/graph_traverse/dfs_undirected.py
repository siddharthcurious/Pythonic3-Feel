def dfs_undirected(graph, start):

    visited = []
    visited.append(start)
    def dfs_helper(start):

        neighbors = graph[start]
        for n in range(len(neighbors)):
            if graph[start][n] == 1 and n not in visited:
                visited.append(n)
                dfs_helper(n)
    dfs_helper(start)
    print(visited)

if __name__ == "__main__":

    graph = [
        [0,1,0,1,0,0,0],
        [1,0,1,0,1,0,0],
        [0,1,0,1,0,0,0],
        [1,0,1,0,0,1,0],
        [0,1,0,0,0,0,1],
        [0,0,0,1,0,0,1],
        [0,0,0,0,1,1,0]
    ]

    dfs_undirected(graph, 0)
    dfs_undirected(graph, 2)
    dfs_undirected(graph, 6)
    dfs_undirected(graph, 3)
    dfs_undirected(graph, 5)