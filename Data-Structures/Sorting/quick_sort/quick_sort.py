def quick_sort(A):

    def quicksort(A, left, right):

        if left >= right:
            return

        mid = left + (right - left)//2
        pivot = A[mid]

        l = left
        r = right

        while l < r:
            while A[l] < pivot:
                l += 1
            while A[r] > pivot:
                r -= 1
            if(l >= r):
                break
            A[l], A[r] = A[r], A[l]

        quicksort(A, left, mid-1)
        quicksort(A, mid+1, right)

    L = len(A)
    quicksort(A, 0, L-1)

if __name__ == "__main__":

    A = [3,1,2,4,5,6,10,9,8,7,15]
    quick_sort(A)
    print(A)