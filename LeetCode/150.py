class Solution:
    def evalRPN(self, tokens):
        stack = []
        val = 0
        for c in tokens:
            if c == "+":
                a1 = stack.pop()
                a2 = stack.pop()
                c1 = a1 + a2
                stack.append(c1)
            elif c == "-":
                a1 = stack.pop()
                a2 = stack.pop()
                c1 = a1 - a2
                stack.append(c1)
            elif c == "*":
                a1 = stack.pop()
                a2 = stack.pop()
                c1 = a1 * a2
                stack.append(c1)
            elif c == "/":
                a1 = stack.pop()
                a2 = stack.pop()
                c1 = int(float(a2)/a1)
                stack.append(c1)
            else:
                stack.append(int(c))
        return stack[0]

if __name__ == "__main__":

    s = Solution()

    I1 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    I = ["2", "1", "+", "3", "*"]
    I = ["4", "13", "5", "/", "+"]
    r = s.evalRPN(I1)
    print(r)
