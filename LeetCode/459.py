class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in s[1:] + s[:-1]



if __name__ == "__main__":

    obj = Solution()
    i = "abcabcabcabc"
    r = obj.repeatedSubstringPattern(i)
    print(r)