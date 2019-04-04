import itertools
from typing import List

class Solution:


    def common(self, a, b):
        return set(a) & set(b)

    def product_score(self, w1, w2):
        return 0 if self.common(w1, w2) else len(w1) * len(w2)

    def maxProduct(self, words: List[str]) -> int:
        if words is None and len(words) <= 1:
            return 0

        score = []
        for w1, w2 in itertools.combinations(words, 2):
            s = self.product_score(w1, w2)
            score.append(s)
        return max(score)



if __name__ == "__main__":

    obj = Solution()

    i = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    i = ["a", "aa", "aaa", "aaaa"]
    i = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    i = ["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]
    r = obj.maxProduct(i)
    print(r)
