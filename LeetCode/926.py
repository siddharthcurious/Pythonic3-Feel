# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

from typing import List

class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:

        total = []
        for aa in A:
            for bb in B:
                if aa.start > bb.end or bb.start > aa.end:
                    continue
                else:
                    i = [max(aa.start, bb.start), min(aa.end, bb.end)]
                    total.append(i)
        return total

if __name__ == "__main__":

    obj = Solution()
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]

    a = [Interval(a, b) for a, b in A]
    b = [Interval(a, b) for a, b in B]

    r = obj.intervalIntersection(a, b)
    print(r)