from bisect import bisect
def inversion_count(A):
    B = sorted(A)
    inversion_count = 0
    while A:
        k = bisect(B, A[0])
        inversion_count += k - 1
        del A[0]
        del B[k-1]
    return inversion_count

def inversion_count_simple():
    pass

if __name__ == "__main__":

    L = [1, 21, 6, 7, 22, 33, 2, 3, 8, 10, 20, 45, 4, 5, 9]
    L = [1, 2, 3, 6, 5]
    L = [1, 2, 3, 10, 7, 12, 9]
    L = [2, 4, 1, 5, 3]
    L = [2, 1, 3, 1, 2]
    r = inversion_count(L)
    print(r)