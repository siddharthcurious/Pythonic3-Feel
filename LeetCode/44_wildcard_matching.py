class Solution:
    def __removeDuplicates(self, p):
        stk = []
        for ch in p:
            if ch != "*":
                stk.append(ch)
            elif ch == "*" and stk:
                if stk[-1] == "*":
                    continue
                else:
                    stk.append(ch)
            else:
                stk.append(ch)
        return "".join(stk)

    def __isMatch(self, s, p):
        memo = self.memo
        if (s,p) in self.memo:
            return memo[(s,p)]
        if s == p:
            memo[(s,p)] = True
        elif p == "*":
            memo[(s,p)] = True
        elif s == "" and p == "":
            memo[(s,p)] = True
        elif s == "" or p == "":
            memo[(s,p)] = False
        elif s[0] == p[0]:
            memo[(s,p)] = self.__isMatch(s[1:], p[1:])
        elif p[0] == "?":
            memo[(s,p)] = self.__isMatch(s[1:], p[1:])
        elif p[0] == "*":
            memo[(s,p)] = self.__isMatch(s[1:], p) or self.__isMatch(s, p[1:])
        else:
            memo[(s,p)] = False
        return memo[(s,p)]

    def isMatch(self, s: str, p: str) -> bool:
        p = self.__removeDuplicates(p)
        self.memo = {}
        return self.__isMatch(s, p)

if __name__ == "__main__":

    obj = Solution()
    A = "aa"
    B = "*"
    r = obj.isMatch(A, B)
    print(r)