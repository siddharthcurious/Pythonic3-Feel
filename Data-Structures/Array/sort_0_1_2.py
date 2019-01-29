# Dutch National flag algorithms

def sort_012(A):

    L = len(A)
    low = 0
    mid = 0
    high = L - 1

    while mid <= high:
        if A[mid] == 0:
            A[low], A[mid] = A[mid], A[low]
            mid += 1
            low += 1

        elif A[mid] == 1:
            mid += 1

        elif A[mid] == 2:
            A[mid], A[high] = A[high], A[mid]
            high -= 1

if __name__ == "__main__":

    A = [0,1,0,0,1,1,1,1,0,1,2,2,0,1,2,2,2,1]
    print(A)
    sort_012(A)
    print(A)