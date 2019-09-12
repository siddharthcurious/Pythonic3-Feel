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

    def isMatch(self, s, p):

        slen = len(s)
        plen = len(p)

        matrix = [ [False for _ in range(slen+1)] for _ in range(plen+1)]
        pass

if __name__ == "__main__":

    obj = Solution()
    A = "ABC"
    B = "ABCD"
    obj.isMatch(A, B)