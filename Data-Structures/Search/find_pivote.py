def pivote(A, start, end):

    if end < start:
        return -1
    if start == end:
        return start

    mid = int(start + (end-start)/2)

    if mid < end and A[mid] > A[mid+1]:
        return mid
    if mid > start and A[mid-1] > A[mid]:
        return mid-1
    if A[mid] > A[end]:
        return pivote(A, mid+1, end)
    if A[start] > A[mid]:
        return pivote(A, start, mid-1)

if __name__ == "__main__":

    A = [5, 6, 1, 2, 3, 4]
    L = len(A)
    r = pivote(A, 0, L-1)
    print(r)