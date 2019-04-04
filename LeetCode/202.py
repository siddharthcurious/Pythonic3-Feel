class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        num_set = set()
        while n > 1:
            num = 0
            for d in str(n):
                num += (int(d) * int(d))
            if num in num_set:
                return False
            else:
                num_set.add(num)
            n = num
        if n == 1:
            return True
        return False

if __name__ == "__main__":

    s = Solution()
    n = 20
    r  = s.isHappy(n)
    print(r)