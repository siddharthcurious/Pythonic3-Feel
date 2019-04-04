class Solution:
    def isDigit(self, d):
        if d >= '0' and d <= '9':
            return True
        return False

    def isChar(self, c):
        if c == "[" or c == "]":
            return False
        elif self.isDigit(c):
            return False
        return True

    def decodeString(self, source: str) -> str:
        stk = []
        i = 0
        L = len(source)
        while i < L:
            if source[i] != ']':
                stk.append(source[i])
            elif source[i] == ']':
                tstr = []
                while stk:
                    tchar = stk[-1]
                    if self.isChar(tchar):
                        tstr.insert(0, tchar)
                        stk.pop()
                    elif tchar == '[':
                        stk.pop()
                        break
                    else:
                        break

                tnum = []
                while stk:
                    dchar = stk[-1]
                    if self.isDigit(dchar):
                        tnum.insert(0, dchar)
                        stk.pop()
                    else:
                        break
                tnum = int("".join(tnum))

                stk.extend(tnum * tstr)
            i += 1
        return "".join(stk)

if __name__ == "__main__":

    s = Solution()

    t = "3[abc]"
    t = "3[a]2[b4[F]c]"
    r = s.decodeString(t)
    print(r)
