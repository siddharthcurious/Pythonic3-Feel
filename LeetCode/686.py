class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        i = 1
        K = A
        while len(K) <= 2*len(B):
            if B in K:
                return i
            else:
                i += 1
                K = A*i
        return -1

if __name__ == "__main__":

    obj = Solution()
    A = "abcd"
    B = "cdabcdab"
    r = obj.repeatedStringMatch(A, B)
    print(r)