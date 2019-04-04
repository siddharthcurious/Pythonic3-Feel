import numpy

def longest_common_subsequence(A, B):
    L1 = len(A)
    L2 = len(B)

    matrix = [[0 for i in range(L2+1)] for j in range(L1+1)]

    for i in range(L1+1):
        for j in range(L2+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif A[i-1] == B[j-1]:
                matrix[i][j] =  matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
    print(numpy.matrix(matrix))
    return matrix[L1][L2]

if __name__ == "__main__":

    A = "abcd"
    B = "abd"
    r = longest_common_subsequence(A, B)
    print(r)