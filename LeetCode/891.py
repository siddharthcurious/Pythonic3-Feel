from itertools import combinations
class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        L = len(A)
        widths = 0
        for i in range(1, L+1):
            combs = combinations(A,i)
            for e in combs:
                mi = min(e)
                ma = max(e)
                widths += ma-mi
        return widths

if __name__ == "__main__":

    s = Solution()
    A = [2,1,3]
    r = s.sumSubseqWidths(A)
    print(r)