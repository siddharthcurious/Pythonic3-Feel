def missing_number(A, low, high, diff):
    if(low <= high):
        mid = int(low + (high - low)/2)

        if A[mid+1] - A[mid] != diff:
            return A[mid] + diff

        if mid > 0 and A[mid] - A[mid-1] == diff:
            return A[mid-1] + diff

        if A[mid] == A[0] + mid*diff:
            return missing_number(A, mid+1, high, diff)
        return missing_number(A, low, mid-1, diff)

if __name__ == "__main__":

    A = [2, 4, 8, 10, 12, 14]
    L = len(A)
    diff = (A[L-1] - A[0])/6
    r = missing_number(A, 0, L-1, diff)
    print(r)