class Solution:
    def sortedSquares(self, A):
        B = []
        for e in A:
            B.append(e*e)
        return B.sort()

if __name__ == "__main__":

    s = Solution()

    A = [-7,-3,2,3,11]
    s.sortedSquares(A)