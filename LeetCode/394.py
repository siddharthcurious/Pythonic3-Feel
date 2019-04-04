class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        target = []
        for c in s:
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                stk.append(c)
                target.append(c)
            elif ord(c) >= ord('a') and ord(c) <= ord('z'):
                stk.append(c)
                target.append(c)
            elif c == '[':
                stk.append(c)
                target.append(c)
            elif c == ']':
                tstr = []
                while stk:
                    temp = stk.pop()
                    target.pop()
                    if temp == "[":
                        break
                    tstr.insert(0, temp)

                tstr = "".join(tstr)
                num = []
                while stk:
                    n = stk.pop()
                    target.pop()
                    if ord(n) >= ord('0') and ord(n) <= ord('9'):
                        num.insert(0, n)
                    else:
                        stk.append(n)
                        break

                num = int("".join(num))
                target.append(num*tstr)
        return "".join(target)

if __name__ == "__main__":

    s = Solution()

    t = "3[h]21[k]"
    t = ""
    t = "a"
    t = "2[b]g13[k]"
    t = "2[abc]3[cd]ef"
    t = "3[a2[c]]"
    r = s.decodeString(t)
    print(r)
