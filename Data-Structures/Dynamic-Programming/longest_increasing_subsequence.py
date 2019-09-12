def get_longest_increasing_subsequence(A, i, n, prev):
    if i == n:
        return 0

    excl = get_longest_increasing_subsequence(A, i+1, n, prev)

    incl = 0
    if A[i] > prev:
        incl = 1+get_longest_increasing_subsequence(A, i+1, n, A[i])

    return max(excl, incl)

if __name__ == "__main__":

    A = [1,2,3,10,7,8,15,6,9,11]

    r = get_longest_increasing_subsequence(A, 0, len(A), -1)
    print(r)