# print all paths source to destination
# Implementation BSF

def print_paths(graph, source, target, visisted, path): 
    pass

if __name__ == "__main__":

    graph = {
        0: [1, 2, 4],
        1: [2, 3, 4],
        2: [5, 6],
        3: [6, 7],
        4: [7],
        5: [8],
        6: [8, 9],
        7: [9],
        8: [10],
        9: [10]
    }

    source = 0
    target = 10

    visited = []
    for _ in range(11):
        visited.append(False)
    path = []
    print_paths(graph, source, target, visited, path)