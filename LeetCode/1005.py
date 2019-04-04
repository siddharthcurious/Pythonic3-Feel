class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i = 0
        L = len(A)
        min = 10000
        for _ in range(K):
            ind = 0
            i = 0
            min = 10000
            while i < L:
                if A[i] < min:
                    min = A[i]
                    ind = i
                i += 1
            t = -A[ind]
            A[ind] = t

        return sum(A)


if __name__ == "__main__":

    obj = Solution()
    A = [2, -3, -1, 5, -4]
    K = 2

    A = [3, -1, 0, 2]
    K = 3

    A = [4, 2, 3]
    K = 1
    r = obj.largestSumAfterKNegations(A, K)
    print(r)