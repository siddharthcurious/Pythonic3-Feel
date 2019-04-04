def find_pivote(A, start, end):
    if end < start:
        return -1
    if end == start:
        return start

    mid = int(start + (end - start)/2)

    if mid < end and A[mid] > A[mid+1]:
        return mid
    if start < mid and A[mid-1] > A[mid]:
        return mid-1
    if A[start] > A[mid]:
        return find_pivote(A, start, mid-1)
    if A[mid] > A[end]:
        return find_pivote(A, mid+1, end)

def binary_search(A, start, end, key):
    mid = int(start + (end - start)/2)
    if A[mid] == key:
        return mid
    elif key > A[mid]:
        return binary_search(A, mid+1, end, key)
    else:
        return binary_search(A, start, mid - 1, key)

def binary_search_rotated(A, key):
    L = len(A)
    pivote = find_pivote(A, 0, L-1)

    if A[0] <= key <= A[pivote]:
        return binary_search(A, 0, pivote, key)
    else:
        return binary_search(A, pivote+1, L-1, key)

if __name__ == "__main__":

    A = [5, 6, 7, 1, 2, 3, 4]
    key = 5
    index = binary_search_rotated(A, key)
    print(index)
