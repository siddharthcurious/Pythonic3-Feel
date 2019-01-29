class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        L = len(A)
        for i, e in sorted(enumerate(A), key=lambda p: p[1]):
             pass



if __name__ == "__main__":

    s = Solution()
    A = [9,8,1,0,1,9,4,0,4,1]
    #A = [6,0,8,2,1,5]
    r = s.maxWidthRamp(A)
    print(r)