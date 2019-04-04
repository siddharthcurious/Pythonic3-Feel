import numpy
def lcs_print(A, B, L1, L2):

    matrix = [[0 for _ in range(L2+1)] for _ in range(L1+1)]
    for i in range(L1+1):
        for j in range(L2+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif A[i-1] == B[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
    print(numpy.matrix(matrix))
    return matrix[L1][L2]

if __name__ == "__main__":

    A = "XALBCDKL"
    B = "XALBDOLKL"
    L1 = len(A)
    L2 = len(B)

    r = lcs_print(A, B, L1, L2)
    print(r)