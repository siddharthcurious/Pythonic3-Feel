class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        L = len(nums)
        i = 0
        sub = 0
        c = 0
        for j in range(L):
            sub += nums[j]
            if sub == k:
                c += 1
            elif sub > k:
                while i < j and sub >= k:
                    sub -= nums[i]
                    i += 1
                    if sub == k:
                        c += 1
            elif sub < k:
                while i < j and sub - nums[i] > k:
                    sub -= nums[i]
                    i += 1
                    if sub == k:
                        c += 1
        return c

if __name__ == "__main__":

    s = Solution()
    nums = [1, 1, 1, 1]
    nums = [1,1,1,2,3,-1]
    nums = [-1,-1,1,-1,1]
    k = 0
    # nums = [-92, -63, 75, -86, -58, 22, 31, -16, -66, -67, 420]
    # k = 100
    r = s.subarraySum(nums, k)
    print(r)