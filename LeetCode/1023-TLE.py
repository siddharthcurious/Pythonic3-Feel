class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        L = len(S)
        numbers = set()
        if "0" in S:
            numbers.add(0)
        if "1" in S:
            numbers.add(1)

        for l in range(2, L+1):
            i = 0
            while i < L and i+l <= L:
                num = S[i:i+l]
                n = int(num, 2)
                numbers.add(n)
                i += 1

        Nums = set(range(N+1))
        if Nums.issubset(numbers):
            return True
        return False

if __name__ == "__main__":

    obj = Solution()
    S = "0110"
    N = 4
    S = "0110"
    N = 3
    r = obj.queryString(S, N)
    print(r)