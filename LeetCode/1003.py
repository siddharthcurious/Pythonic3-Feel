class Solution:
    def isValid(self, S: str) -> bool:

        s1 = ""
        while True:
            s = S.split("abc")
            s1 = "".join(s)
            if s1.find("abc") >= 0:
                S = s1
            else:
                break
        if s1 == "":
            return True
        return False

if __name__ == "__main__":

    s = Solution()
    I = "aabcbcc"
    r = s.isValid(I)
    print(r)