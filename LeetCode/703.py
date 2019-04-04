from typing import List

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.size = len(self.nums)
        heapq.heapify(self.nums)
        while self.size > self.k:
            heapq.heappop(self.nums)
            self.size -= 1

    def add(self, val: int) -> int:
        if self.size < self.k:
            heapq.heappush(self.nums, val)
            self.size += 1
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]

if __name__ == "__main__":

    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)

    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(10))
    print(kthLargest.add(9))
    print(kthLargest.add(4))