def lcs(A, B, m, n):
    matrix = []
    for _ in range(m+1):
        matrix.append([0]*(n+1))

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif A[i-1] == B[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])

    return matrix[m][n]

if __name__ == "__main__":

    A = "ABCDEKL"
    B = "ABMKDEKL"

    r = lcs(A, B, len(A), len(B))
    print(r)