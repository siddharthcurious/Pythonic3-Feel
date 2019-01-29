def lcs(A, B, m, n):

    if m == 0 or n == 0:
        return 0
    elif A[m-1] == B[n-1]:
        return 1+lcs(A, B, m-1, n-1)
    else:
        return max(lcs(A, B, m-1, n), lcs(A, B, m, n-1))


if __name__ == "__main__":

    A = "ABCDEKL"
    B = "ABMKDEKL"

    r = lcs(A, B, len(A), len(B))
    print(r)