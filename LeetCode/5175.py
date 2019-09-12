from typing import List
class Solution:
    def isPalindrome(self, str):
        i = 0
        j = len(str) -1
        while i <= j:
            if str[i] != str[j]:
                return False
            i += 1
            j -= 1
        return True
    def isCondPalindrome(self, str):
        i = 0
        j = len(str) - 1
        c = 0
        while i <= j:
            if str[i] != str[j]:
                c += 1
            i += 1
            j -= 1
        return c

    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        result = []
        for query in queries:
            i,j,q = query
            substr = s[i:j+1]
            print(substr)
            if self.isPalindrome(substr):
                result.append(True)
            else:
                r = self.isCondPalindrome(substr)
                if r <= q:
                    result.append(True)
                else:
                    result.append(False)
        return result

if __name__ == "__main__":

    obj = Solution()
    s = "abcda"
    queries = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]
    s = "shezu"
    queries = [[3, 3, 1], [3, 4, 2], [2, 2, 1], [3, 4, 2]]
    # [true, true, true, true]
    s = "hunu"
    queries = [[0, 3, 1], [1, 1, 1]]
    r = obj.canMakePaliQueries(s, queries)
    print(r)