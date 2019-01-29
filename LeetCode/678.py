class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for ch in s:
            if len(stk) == 0:
                stk.append(ch)
            elif ch == ")" and stk[-1] == "(":
                stk.pop()
            elif ch == ")" and stk[-1] == "*":
                stk.pop()
            else:
                stk.append(ch)
        if len(stk) == 0:
            return True
        return False

if __name__ == "__main__":

    s = Solution()

    p = "((*))"
    r = s.checkValidString(p)
    print(r)