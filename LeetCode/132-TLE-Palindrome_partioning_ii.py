from typing import List

class Solution:
    def minCut(self, s: str) -> int:
        self.res = []
        self.palindromePartition(s, [])
        return min(self.res)

    def palindromePartition(self, s, palindromes):
        if len(s) == 0:
            l = len(palindromes)
            self.res.append(l)

        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.palindromePartition(s[i:], palindromes + [s[:i]])

    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        return False

if __name__ == "__main__":

    obj = Solution()
    string = "aab"
    r = obj.minCut(string)
    print(r)