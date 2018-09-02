class Solution:
    def uncommonFromSentences(self, A, B):

        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        result = []

        hsh = {}
        awords = A.split()
        bwords = B.split()

        for w in awords:
            if w not in hsh:
                hsh.update({w: 1})
            else:
                h

        for w in bwords:
            if w not in hsh:
                hsh.update({w: 1})
            else:
                hsh[w] += 1

        for k, v in hsh.items():
            if v == 1:
                result.append(k)

        return result


if __name__ == "__main__":

    s = Solution()

    A = "this apple is sweet"
    B = "this apple is sour"

    r  = s.uncommonFromSentences(A, B)
    print(r)
