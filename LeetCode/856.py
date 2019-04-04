class Solution(object):
    def scoreOfParentheses(self, S):

        i = 0
        L = len(S)
        stk = []
        while i < L:
            j = 0
            while True:
                if S[i] == "(":
                    stk.append(S[i])
                    i += 1
                else:
                    break

            print(stk)
            while stk:
                if S[i] == ")" and stk[-1] == "(":
                    stk.pop()
                    i += 1
                    j += 1
                else:
                    break
            print(stk)

if __name__ == "__main__":

    obj = Solution()

    braces = "(()(()))"
    r = obj.scoreOfParentheses(braces)
    print(r)