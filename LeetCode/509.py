class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        f = 0
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            first = 0
            second = 1
            N = N - 1
            while N:
                f = first + second
                first = second
                second = f
                N = N - 1
        return f

if __name__ == "__main__":

    s = Solution()
    N = 4
    r = s.fib(N)
    print(r)