from typing import List

from collections import defaultdict
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        data = defaultdict(list)
        for i, word in enumerate(words):
            data[word].append(i)

        w1 = data[word1]
        w2 = data[word2]

        min = 999999999999

        for a in w1:
            for b in w2:
                if a != b:
                    diff = abs(a-b)
                    if diff < min:
                        min = diff
        return min

if __name__ == "__main__":

    obj = Solution()
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"

    word1 = "makes"
    word2 = "coding"
    r = obj.shortestDistance(words, word1, word2)
    print(r)