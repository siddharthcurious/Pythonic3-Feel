def binary_search_rotated(A, start, end, key):
    if end < start:
        return -1

    mid = int(start + (end - start)/2)

    if A[mid] == key:
        return mid

    if A[start] <= A[mid]:
        if A[start] <= key <= A[mid]:
            return binary_search_rotated(A, start, mid-1, key)
        else:
            return binary_search_rotated(A, mid+1, end, key)
    else:
        if A[mid] <= key <= A[end]:
            return binary_search_rotated(A, mid+1, end, key)
        else:
            return binary_search_rotated(A, start, mid-1, key)

if __name__ == "__main__":


    A = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    L = len(A)
    r = binary_search_rotated(A, 0, L-1, 1)
    print(r)