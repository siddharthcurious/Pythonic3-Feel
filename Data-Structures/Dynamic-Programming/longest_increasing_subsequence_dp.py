def LIS(A):
    L = len(A)
    memo = [0] * L
    memo[0] = 1
    lis_length = 0
    for i in range(1, L):
        maxval = 0
        for j in range(i):
            if A[j] < A[i]:
                maxval = max(maxval, A[j])
        memo[i] = maxval + 1
        lis_length = max(lis_length, maxval)
    return lis_length

if __name__ == "__main__":

    A = [1,2,3,10,4,5,12,9,6,5,11,12,13,8]
    n = LIS(A)
    print(n)