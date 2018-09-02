class Solution:
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        L = len(S)
        if L == K:
            return "".join(sorted(S))

        for i in range(K):
            for j in range(i+1, L):
                pass

if __name__ == "__main__":

    s = Solution()
    S = "cba"
    K = 1
    r = s.orderlyQueue(S, K)
