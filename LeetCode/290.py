class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        hashmap = {}
        hashmaprev = {}
        str = str.split()

        if len(pattern) != len(str):
            return False
        for ch, string in zip(pattern, str):
            if hashmap.get(ch) or hashmaprev.get(string):
                hval = hashmap.get(ch)
                rhval = hashmaprev.get(string)
                if hval != string or rhval != ch:
                    return False
            else:
                hashmap.update({ch: string})
                hashmaprev.update({string: ch})
        return True

if __name__ == "__main__":

    s = Solution()
    pattern = "abba"
    str = "dog cat cat dog"

    pattern = "abba"
    str = "dog dog dog dog"
    r  = s.wordPattern(pattern, str)
    print(r)