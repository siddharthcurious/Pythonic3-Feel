class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        L = len(A)
        if L == 1:
            return 1

        result = set()

        for j in range(L):
            for i in range(L):
                if j + 1 <= L:
                    sub = A[i:j+1]
                    if sub:
                        d = sub[0]
                        for e in sub[1:]:
                            d = d | e
                        result.add(d)
        return len(result)

if __name__ == "__main__":

    s = Solution()
    A = [1,1,2]
    r = s.subarrayBitwiseORs(A)
    print(r)