class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        return nums[-k]


if __name__ == "__main__":

    s = Solution()
    A = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4

    r = s.findKthLargest(A, k)
    print(r)