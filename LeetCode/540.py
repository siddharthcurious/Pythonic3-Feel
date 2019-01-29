class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def find_single(nums):
            L = len(nums)
            if L == 1:
                return nums[0]
            m = L//2
            if nums[m+1] != nums[m] and nums[m-1] != nums[m]:
                return nums[m]

            elif nums[m] == nums[m+1]:
                pass

            elif nums[m-1] == nums[m]:
                if (m-1) % 2 == 0:
                    return find_single(nums[m+1:])
                else:
                    return find_single(nums[:m-1])

        n = find_single(nums)
        print(n)

if __name__ == "__main__":

    s = Solution()
    A = [3,3,7,7,10,11,11]
    # B = [1,1,2,3,3,4,4,8,8]
    s.singleNonDuplicate(A)