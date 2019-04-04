class Solution:
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def countSubstrings(self, s: str) -> int:
        L = len(s)
        k = 1
        count = 0
        while True:
            i = 0
            while i+k <= L:
                temp = s[i:i+k]
                if self.isPalindrome(temp):
                    count += 1
                i += 1
            k += 1
            if len(temp) == L:
                break
        return count

if __name__ == "__main__":

    s = Solution()

    string = "aaa"
    r = s.countSubstrings(string)
    print(r)