from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        m = 0
        if k == 0:
            while m < len(nums)-1:
                if nums[m] == nums[m+1]:
                    return True
                m += 1
            if m == len(nums)-1:
                return False

        if k != 0:
            for i, e in enumerate(nums):
                nums[i] = nums[i] % k

        prefix = {0: nums[0]}
        s = 0
        for i, e in enumerate(nums):
            s += nums[i]
            prefix.update({i: s})
        sub = nums[0]
        for i in range(1, len(nums)):
            sub += nums[i]
            if sub % k == 0:
                return True
            elif sub % k != 0:
                j = 0
                while j < i - 1:
                    if prefix.get(j):
                        t = sub - prefix.get(j)
                        if t % k == 0:
                            return True
                    j += 1
        return False

if __name__ == "__main__":

    obj = Solution()
    nums = [23, 2, 6, 4, 7]
    nums = [23, 2, 4, 6, 7]
    nums = [4, 4, 4, 5, 6, 7]
    nums = [23,2,6,4,7]
    k = 0
    r = obj.checkSubarraySum(nums, k)
    print(r)