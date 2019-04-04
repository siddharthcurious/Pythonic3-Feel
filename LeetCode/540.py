class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(A)

        def binarySearch(A, start, end):
            if start == end:
                return A[start]

            if start < end:

                mid = int(start + (end - start)/2)

                if A[mid-1] < A[mid] < A[mid+1]:
                    return A[mid]
                if end - start == 2:
                    if A[end] != A[end-1]:
                        return A[end]
                if end - start == 2:
                    if A[start] != A[start+1]:
                        return A[start]

                elif A[mid-1] == A[mid]:
                    if A[end-1] == A[end]:
                        return binarySearch(A, start, mid-2)
                    elif A[mid+1] == A[mid+2]:
                        return binarySearch(A, mid+3, end)
                    else:
                        return binarySearch(A, mid+1, end)
                elif A[mid] == A[mid+1]:
                    if A[start] == A[start+1]:
                        return binarySearch(A, mid+2, end)
                    elif A[mid-2] == A[mid-1]:
                        return binarySearch(A, start, mid-3)
                    else:
                        return binarySearch(A, start, mid-1)

        return binarySearch(A, 0, L-1)


if __name__ == "__main__":

    s = Solution()
    A = [1,1,2,3,3,4,4,5,5]
    A = [1,1,2,2,3,3,4,5,5]
    A = [1,1,2,3,3,4,4,8,8]
    A = [3,3,7,7,10,11,11]

    r = s.singleNonDuplicate(A)
    print(r)