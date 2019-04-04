class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = N
        infix = ""
        c = 0
        ops = ["*", "//", "+", "-"]
        while n > 1:
            infix += str(n)
            n -= 1
            k = c % 4
            infix += ops[k]
            c += 1
        infix += str(1)
        return eval(infix)

if __name__ == "__main__":

    obj = Solution()
    N = 10
    r = obj.clumsy(N)
    print(r)