class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for ch in s:
            if ch == "(":
                stk.append(ch)
            elif ch == ")" and stk[-1] == "(":
                stk.pop()
            elif ch == "*":
                stk.append("*")
            elif ch == ")" and stk[-1] == "*" and stk[-2] == "(":
                stk.pop()
                stk.pop()
                stk.append("*")
            elif ch == ")" and stk[-1] == "*":
                stk.pop()

        print(stk)

if __name__ == "__main__":

    s = Solution()

    p = "**))"
    r = s.checkValidString(p)
    print(r)