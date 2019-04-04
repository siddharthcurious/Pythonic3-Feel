class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0

        total = sum(nums)
        i = 0
        left = 0
        right = total
        while i < len(nums):
            right -= nums[i]
            if left == right:
                return i
            else:
                left += nums[i]
            i += 1
        return -1

if __name__ == "__main__":

    obj = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    nums = [1, 1, 1, 1, 1, 4]
    nums = [1,0,1,0]
    #nums = [-1,-1,-1,0,1,1]
    r = obj.pivotIndex(nums)
    print(r)