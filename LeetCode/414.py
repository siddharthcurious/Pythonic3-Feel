from typing import List

import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        numbers = heapq.nlargest(3, nums)
        if len(numbers) == 3:
            return numbers[-1]
        else:
            return numbers[0]

if __name__ == "__main__":

    s = Solution()
    i = [1, 2]
    i = [2,2,3,1]
    r = s.thirdMax(i)
    print(r)
