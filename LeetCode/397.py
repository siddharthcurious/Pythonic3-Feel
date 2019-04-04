class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n % 2 == 0:
            return 1 + self.integerReplacement(int(n/2))
        elif n % 2 == 1:
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))

if __name__ == "__main__":

    s = Solution()
    r = s.integerReplacement(16)
    print(r)