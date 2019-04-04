from typing import List

import heapq
class Solution:
    def __init__(self):
        self.distance = []

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        self.k = k
        i = 0
        L = len(nums)

        while i < L-1:
            j = i+1
            while j < L:
                d = nums[i] - nums[j]
                if len(self.distance) < self.k:
                    self.distance.append(abs(d))
                    heapq._heapify_max(self.distance)
                elif d < self.distance[0]:
                    heapq._heapreplace_max(self.distance, d)
                j += 1
            i += 1
        return self.distance[0]

if __name__ == "__main__":

    s = Solution()
    nums = [1, 3, 1]
    k = 1
    r = s.smallestDistancePair(nums, k)
    print(r)
