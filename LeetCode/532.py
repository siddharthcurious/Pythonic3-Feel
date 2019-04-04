from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        print(nums)
        L = len(nums)
        i = 0
        c = 0
        iset = set()
        while i < L - 1:
            j = i + 1
            while j < L:
                if abs(nums[i] - nums[j]) == k and j not in iset:
                    iset.add(j)
                    c += 1
                j += 1
            i += 1
        #print(iset)
        return c

if __name__ == "__main__":

    obj = Solution()
    nums = [1, 3, 1, 5, 4]
    nums = [3, 1, 4, 1, 5]
    k = 2
    nums = [1, 3, 1, 5, 4]
    k = 0
    r = obj.findPairs(nums, k)
    print(r)