
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        words = S.upper().split("-")
        r = ""
        new_words = "".join(words)
        print(new_words)
        count = 0
        for c in reversed(new_words):
            r = c + r
            count += 1
            if count == K:
                r = "-" + r
                count = 0
        if r[0] == "-":
            r = r[1:]
        return r

if __name__ == "__main__":

    obj = Solution()
    S = "5F3Z-2e-9-w"
    K = 4
    S = "2-5g-3-J"
    K = 2
    S = "----AAAM"
    r = obj.licenseKeyFormatting(S, K)
    print(r)