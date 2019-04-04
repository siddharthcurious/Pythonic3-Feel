class Solution(object):

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if words is None or len(words) <= 1:
            return 0

        codes = []
        for i in words:
            tmp = 0
            for j in list(i):
                tmp |= 1 << (ord(j) - ord('a'))
                codes.append(tmp)

        print(codes)

        res = 0
        for i in range(len(codes)-1):
            for j in range(i + 1, len(codes)):
                if codes[i] & codes[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res

if __name__ == "__main__":

    obj = Solution()

    i = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    i = ["a", "aa", "aaa", "aaaa"]
    i = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    i = ["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]
    i = ["abc", "def"]
    r = obj.maxProduct(i)
    print(r)