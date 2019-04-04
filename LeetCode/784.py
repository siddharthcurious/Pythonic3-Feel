class Solution:
    def binaryNum(self, N):

        nums = []
        def binary(N, prefix):
            if len(prefix) == N:
                nums.append(prefix)
                return
            else:
                binary(N, prefix+"0")
                binary(N, prefix+"1")

        binary(N, "")
        return nums

    def letterCasePermutation(self, S):
        L = len(S)
        c = 0
        for e in S:
            if e.isalpha():
                c +=1
        bins = self.binaryNum(c)

        result = []

        for b in bins:
            s1 = list(S)
            i = 0
            j = 0
            while i < c and j < L:
                if s1[j].isdigit():
                    j += 1
                elif s1[j].isalpha():
                    if b[i] == "0":
                        l = s1[j]
                        s1[j] = l.lower()
                        i += 1
                        j += 1
                    elif b[i] == "1":
                        l = s1[j]
                        s1[j] = l.upper()
                        i += 1
                        j += 1
            result.append("".join(s1))
        return result

if __name__ == "__main__":

    s = Solution()

    S = "1234"

    r = s.letterCasePermutation(S)
    print(r)
