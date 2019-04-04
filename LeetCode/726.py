class Solution:
    def isCapital(self, c):
        if c >= 'A' and c <= 'Z':
            return True
        return False

    def isSmall(self, c):
        if c >= 'a' and c <= 'z':
            return True
        return False

    def isDigit(self, c):
        if c >= '0' and c <= '9':
            return True
        return False

    def countOfAtoms(self, formula: str) -> str:

        L = len(formula)
        i = 0

        stk = []
        while i < L:
            if self.isCapital(formula[i]) or formula[i] == '(' or formula[i] == ')':
                stk.append(formula[i])
                i += 1
            elif self.isSmall(formula[i]):
                cap = stk[-1]
                stk.pop()
                sm = ""
                while True and i < L:
                    if self.isSmall(formula[i]):
                        sm = sm + formula[i]
                        i += 1
                    else:
                        break
                atom = cap+sm
                stk.append(atom)

            elif self.isDigit(formula[i]):
                num = ""
                while True and i < L:
                    if self.isDigit(formula[i]):
                        num = num + formula[i]
                        i += 1
                    else:
                        break
                stk.append(int(num))

        map = {}
        while stk:
            pass

if __name__ == "__main__":

    s = Solution()
    i = "K4(ON(SO3)2)2"
    # i = "MgoO22(Hg2O)5"
    r = s.countOfAtoms(i)
    print(r)