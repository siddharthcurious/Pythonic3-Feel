from heapq import merge

def sorted_matrix(matrix):

    result = matrix[0]

    for row in matrix[1:]:
        result = list(merge(result, row))
    return result

if __name__ == "__main__":
    mat = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [27, 29, 37, 48],
           [32, 33, 39, 50]]
    r = sorted_matrix(mat)
    print(r)