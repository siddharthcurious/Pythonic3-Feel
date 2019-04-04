from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        minimum = nums[0]
        maximum = nums[0]

        for e in nums:
            if e > maximum:
                maximum = e
            if e < minimum:
                minimum = e
        print(maximum, minimum)

if __name__ == "__main__":

    s = Solution()
    arr = [3, 4, -1, 1]
    r = s.firstMissingPositive(arr)
    print(r)
