def longest_common_subsequence(A, B, L1, L2):
    if L1 == 0 or L2 == 0:
        return 0
    elif A[L1-1] == B[L2-1]:
        return 1 + longest_common_subsequence(A, B, L1-1, L2-1)
    else:
        return max(longest_common_subsequence(A, B, L1-1, L2), longest_common_subsequence(A, B, L1, L2-1))

if __name__ == "__main__":

    A = "helloman"
    B = "helolman"
    L1 = len(A)
    L2 = len(B)
    r = longest_common_subsequence(A, B, L1, L2)