class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1

        c = 0
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i] != s[j]:
                if s[i] == s[j-1] and i != j-1:
                    i += 1
                    j -= 2
                elif s[i+1] == s[j] and i+1 != j:
                    i += 2
                    j -= 1
                c += 1
        print(c)

if __name__ == "__main__":

    s = Solution()
    S = "abbaacba"
    r = s.validPalindrome(S)
    print(r)