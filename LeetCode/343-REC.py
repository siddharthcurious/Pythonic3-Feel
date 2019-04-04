class Solution:
    def integerBreak(self, n: int) -> int:

        m = [0]
        def breakNum(n, prefix):

            if n == 0 and len(prefix[:-1]) >= 3:
                print(prefix[:-1])
                mul = eval(prefix[:-1])
                if mul > m[0]:
                    m[0] = mul
            if n < 0:
                return
            else:
                for num in range(1, n+1):
                    breakNum(n-num, prefix+str(num)+"*")
        breakNum(n, "")
        return m[0]

if __name__ == "__main__":

    obj = Solution()
    n = 2
    r = obj.integerBreak(n)
    print(r)