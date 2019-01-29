class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stk = []
        for c in S:
            if not stk:
                stk.append(c)
            elif c == "(":
                stk.append(c)
            elif c 

if __name__ == "__main__":

    obj = Solution()

    braces = "(()(()))"
    r = obj.scoreOfParentheses(braces)
    print(r)