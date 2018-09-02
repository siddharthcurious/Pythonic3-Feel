class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True
        p = 0
        n = 0
        j = 0
        L = len(A)
        while j < L-1:
            if A[j] - A[j+1] > 0:
                p = 1
            if A[j] - A[j+1] < 0:
                n = 1
            if A[j] - A[j + 1] > 0 or A[j] - A[j + 1] < 0:
                break
            j = j + 1

        if p == 0 and n == 0:
            return True

        for i in range(j, len(A)-1):
            if p == 1:
                if A[i] - A[i+1] < 0:
                    return False
            if n == 1:
                if A[i] - A[i+1] > 0:
                    return False
        return True

if __name__ == "__main__":

    s = Solution()
    a = [6,5,4,4]
    a = [2,2,2,1,4,5]
    a = [1,1,1]
    r = s.isMonotonic(a)
    print(r)