class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        L = len(S)
        c = 0
        for num in range(1, N+1):
            n = bin(num)
            n1 = str(n)
            n2 = n1[2:]
            if S.find(n2) >= 0:
                c += 1
        if c == N:
            return True
        return False

if __name__ == "__main__":

    obj = Solution()

    S = "0110"
    N = 4
    r = obj.queryString(S, N)
    print(r)