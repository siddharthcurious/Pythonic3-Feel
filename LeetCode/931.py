import numpy
class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows = len(A)
        cols = len(A[0])

        i = 0
        j = 0
        while i < rows:
            while j < cols:
                pass




if __name__ == "__main__":

    obj = Solution()
    A = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    obj.minFallingPathSum(A)