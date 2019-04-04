class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        ns = S.split("-")
        nns = "".join(ns).upper()

        if not nns:
            return ""

        result = ""
        if len(nns) <= K:
            return nns[0]+"-"+nns[1:]

        else:
            j = len(nns)
            j = j - K
            while j >= 0:
                if result != "":
                    result = nns[j:j+K] +"-"+ result
                else:
                    result = nns[j:j+K]
                j -= K
                if j < 0:
                    j += K
                    break
            if j > 0:
                result = nns[0:j] +"-"+ result
        return result

if __name__ == "__main__":

    obj = Solution()
    S = "5F3Z-2e-9-w-op34lpl"
    K = 4
    S = "3-J"
    K = 2
    r = obj.licenseKeyFormatting(S, K)
    print(r)