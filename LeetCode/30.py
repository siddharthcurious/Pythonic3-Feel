from typing import List
from itertools import permutations
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        for p in permutations(words):
            concat = "".join(p)
            k = string.find(concat)
            print(k)

if __name__ == "__main__":

    s = Solution()
    string = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]

    string = "barfoothefoobarman"
    words = ["foo", "bar"]
    r = s.findSubstring(string, words)
    print(r)