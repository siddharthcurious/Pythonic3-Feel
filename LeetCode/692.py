import collections
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates_1 = sorted(candidates, key = lambda w: (-count[w], w))
        return candidates_1[:k]

if __name__ == "__main__":

    s = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    r = s.topKFrequent(words, k)
    print(r)

    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    r = s.topKFrequent(words, k)
    print(r)
