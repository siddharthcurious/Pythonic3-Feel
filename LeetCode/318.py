class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        i = 0
        j = 0
        L = len(words)
        m = 0
        while i < L-1:
            cnt1 = set(list(words[i]))
            j = i+1
            L1 = len(words[i])
            while j < L:
                cnt2 = set(list(words[j]))
                if not cnt1 & cnt2:
                    L2 = len(words[j])
                    if L1 * L2 > m:
                        m = L1 * L2
                j += 1
            i += 1
        return m

if __name__ == "__main__":

    obj = Solution()

    i = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    i = ["a", "aa", "aaa", "aaaa"]
    i = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    i = ["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]
    r = obj.maxProduct(i)
    print(r)
