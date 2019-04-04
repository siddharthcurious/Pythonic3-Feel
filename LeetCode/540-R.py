class Solution:
    def singleNonDuplicate(self, A):
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
                if A[mid] == A[mid+1]:
                    if int(end-start)%4 == 0:
                        return binarySearch(A, mid+2, end)
                    else:
                        return binarySearch(A, start, mid-1)

                elif A[mid-1] == A[mid]:
                    if int(end - start)%4 == 0:
                        return binarySearch(A, start, mid-2)
                    else:
                        return binarySearch(A, mid+1, end)

        return binarySearch(A, 0, L-1)


if __name__ == "__main__":

    s = Solution()
    A = [1,1,2,3,3,4,4,5,5,6,6]
    r = s.singleNonDuplicate(A)
    print(r)