class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        def apply_binary_search(nums, L, R):

            if L <= R:
                mid = L + (R - L)/2
                if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                    return nums[mid]
                else:
                    return apply_binary_search(nums, L, mid-1)
                    return apply_binary_search(nums, mid+1, R)

        apply_binary_search(nums, 0, L-1)



if __name__ == "__main__":

    s = Solution()
    A = [3,3,7,7,10,11,11]
    s.singleNonDuplicate(A)