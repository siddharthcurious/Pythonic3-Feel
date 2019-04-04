class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        L = len(A)
        if L <= 2:
            return False

        s = sum(A)
        if s % 3 == 0:
            subsum = s / 3
            i = 0
            c = 0
            d = subsum
            while i < L:
                d -= A[i]
                if d == 0:
                    c += 1
                    d = subsum
                i += 1
            #print(c, i)
            if c == 3 and i == L:
                return True
        return False

if __name__ == "__main__":

    obj = Solution()
    A = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
    A = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
    A = [3,3,3]
    A = [0,2,1,-6,6,7,9,-1,2,0,1]
    A = [0,2,1,-6,6,-7,9,1,2,0,1]
    r = obj.canThreePartsEqualSum(A)
    print(r)