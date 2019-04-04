class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        L = len(num)
        i = 0
        source = ""
        target = ""
        while i < L:

            source += num[i]
            if i + 1 < L:
                target += num[i+1]





if __name__ == "__main__":

    obj = Solution()
    num = "112358"
    num = "199100199"
    obj.isAdditiveNumber(num)