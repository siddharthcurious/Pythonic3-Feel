from typing import List

from collections import Counter
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:

        for word in A:
            t = []
            for i, ch in enumerate(word):
                t.append((ch, i))
            print(sorted(t, key=lambda x:x[0]))


if __name__ == "__main__":

     obj = Solution()

     A = ["tars","rats","arts","star"]
     obj.numSimilarGroups(A)