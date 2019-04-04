class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        L = len(ops)
        i = 0
        stk = []
        while i < L:
            if not stk:
                stk.append(ops[i])
                i +=1
            elif ops[i][0] >= "0" and ops[i][0] <= "9" and not stk:
                stk.append(int(ops[i]))
                i += 1
            elif ops[i][0] >= "0" and ops[i][0] <= "9":
                if isinstance(stk[-1], int):
                    topn = stk.pop()
                    tn = topn + int(ops[i])
                    stk.append(tn)
                    i += 1
                else:
                    stk.append(ops[i])
                    i += 1
            elif ops[i][0] == "-":
                if isinstance(stk[-1], int):
                    topn = stk.pop()
                    tn = topn + int(ops[i])
                    stk.append(tn)
                    i += 1
                else:
                    stk.append(ops[i])
                    i += 1

if __name__ == "__main__":

    o = Solution()
    i = ["5","-2","4","C","D","9","+","+"]
    r  = o.calPoints(i)
    print(r)

