from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.palindromePartition(s, [])
        return self.res

    def palindromePartition(self, s, palindromes):
        if len(s) == 0:
            self.res.append(palindromes)
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
    r = obj.partition(string)
    print(r)