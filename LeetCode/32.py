class Solution:
    def longestValidParentheses(self, s):
        stack = []
        indstk = []
        index = 0
        for c in s:
            if not stack:
                stack.append(c)
                indstk.append(index)
            elif c == ")" and stack[-1] == "(":
                stack.pop()
                indstk.pop()
            elif c == ")":
                stack.append(c)
                indstk.append(index)
            elif c == "(":
                stack.append(c)
                indstk.append(index)
            index += 1
        if not stack:
            return len(s)

        if len(stack) == 1:
            return max(indstk[0], len(s)-indstk[0]-1)

        indstk.insert(0, 0)
        indstk.append(len(s)-1)

        i = 0
        j = 1
        m = 0

        print(stack)
        print(indstk)
        while i < j and j < len(indstk):
            if indstk[j] - indstk[i] > m:
                m = indstk[j] - indstk[i]
            i += 1
            j += 1
        if m % 2 == 1:
            return m - 1
        return m

if __name__ == "__main__":

    s = Solution()
    str = "()()(())(()()()()()("
    str = "()()()((()()()()"
    r = s.longestValidParentheses(str)
    print(r)