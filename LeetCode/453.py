class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = nums[0]
        for i in nums[1:]:
            if i < min:
                min = i

        d = 0
        for i in nums:
            d = d + (i - min)
        return d


if __name__ == "__main__":

    s = Solution()
    nums = [1, 2, 3]
    r = s.minMoves(nums)
    print(r)
