def print_adjacency_matrix(N):
    matrix = []
    for _ in range(N):
        row = [0]*N
        matrix.append(row)
    print(matrix)

    for i in range(N):
        for j in range(N):
            matrix[i][j] = 1

    print(matrix)

if __name__ == "__main__":

    N = 5
    print_adjacency_matrix(N)