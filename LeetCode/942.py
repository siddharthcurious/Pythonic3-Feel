class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lo, hi = 0, len(S)

        result = []
        for x in S:
            if x == "I":
                result.append(lo)
                lo += 1
            else:
                result.append(hi)
                hi -= 1
        result.append(lo)
        return result

if __name__ == "__main__":

    s = Solution()

    I = "IDID"
    I = "IIIID"

    r = s.diStringMatch(I)
    print(r)