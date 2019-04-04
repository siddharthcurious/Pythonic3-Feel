class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        i = 0
        L = len(path)
        stk = []
        pass

if __name__ == "__main__":

    s = Solution()
    i = "/././abc/./../"
    r = s.simplifyPath(i)
    print(r)