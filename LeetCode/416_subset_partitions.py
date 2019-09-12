from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        forward_sum = [0] * len(nums)
        backward_sum = [0] * len(nums)

        sum = 0
        for i, e in enumerate(nums):
            sum += e
            forward_sum[i] = sum

        sum  = 0
        for i in range(len(nums)-1, -1, -1):
            sum += nums[i]
            backward_sum[i] = sum

        L = len(nums)
        for i, e in enumerate(nums):
            if i+1 <= L-1:
                if forward_sum[i] == backward_sum[i+1]:
                    return True
        return False

if __name__ == "__main__":

    obj = Solution()
    nums = [1, 5, 6, 11]
    nums = [1,2,3,4,5,6,7]
    r = obj.canPartition(nums)
    print(r)