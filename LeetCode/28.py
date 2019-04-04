class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        i = 0
        j = 0
        L = len(haystack)
        nL = len(needle)

        if not needle:
            return 0

        while i < L:
            j = 0
            k = i
            if haystack[i] == needle[j]:
                while k < L and j < nL:
                    if haystack[k] == needle[j]:
                        k += 1
                        j += 1
                    else:
                        break
            if j == nL:
                return i
            i += 1
        return -1

if __name__ == "__main__":

    obj = Solution()
    haystack = "hello"
    needle = "lll"
    r = obj.strStr(haystack, needle)
    print(r)