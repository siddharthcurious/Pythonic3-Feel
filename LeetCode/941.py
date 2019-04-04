class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 0:
            return False
        if len(A) == 1:
            return False
        L = len(A)
        k = 0
        flag = 0
        for i in range(L-1):
            if A[i] == A[i+1]:
                return False
            elif A[i] > A[i+1]:
                k = i
                flag = 1
                break

        if flag == 1 and k == 0:
            return False

        while k + 1 < L:
            if A[k] == A[k+1]:
                return False
            elif A[k] < A[k+1]:
                return False
            k += 1
        return True

if __name__ == "__main__":

    obj = Solution()
    A = [8,7,6,5,4]
    A = [2,1]
    A = [1,2,1]
    A = [2,1,2]
    A = [1,2,3,4]
    A = [14, 82, 89, 84, 79, 70, 70, 68, 67, 66, 63, 60, 58, 54, 44, 43, 32, 28, 26, 25, 22, 15, 13, 12, 10, 8, 7, 5, 4, 3]
    r = obj.validMountainArray(A)
    print(r)