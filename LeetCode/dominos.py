from typing import List
from collections import Counter
class Solution:

    def __factorial(self, n):
        if n <= 1:
            return 1
        return n * self.__factorial(n - 1)

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        dominoes = [tuple(set(e)) for e in dominoes]

        counter = Counter(dominoes)

        c = 0

        for k, v in counter.items():
            if v == 2:
                c += 1
            elif v > 2:
                d = self.__factorial(v) / self.__factorial(v - 2)
                d = d / 2
                c += int(d)

        return c
if __name__ == "__main__":

    obj = Solution()
    dominoes = [[1, 2], [2, 1], [1, 2], [3, 4], [5, 6]]
    r = obj.numEquivDominoPairs(dominoes)
    print(r)