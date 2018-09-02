class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute(nums, choosen):

            if nums == []:
                print(choosen)

            for i in range(0, len(nums)):
                # choose
                c = nums[i]
                choosen.append(c)
                nums.pop(0)

                # explore
                permute(nums, choosen)

                # unchoose
                nums.insert(0, c)
                choosen.pop()

        permute(nums, [])

if __name__ == "__main__":

    s = Solution()
    nums = [1,2,3]
    s.permuteUnique(nums)