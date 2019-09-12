def mergesort(arr):
    L = len(arr)
    if L <= 1:
        return 0
    else:
        mid = L // 2
        left = arr[:mid]
        right = arr[mid:]
        count =  mergesort(left)
        count += mergesort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                count += len(left) - i
            k += 1

        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1
        return count

if __name__ == "__main__":

    arr = [1, 2, 4, 3, 6, 5, 9, 8, 7]
    arr = [1, 2, 3, 7, 5, 6, 9, 8, 4]
    arr = [4,1,5,2,3]
    r = mergesort(arr)
    print(arr)
    print(r)