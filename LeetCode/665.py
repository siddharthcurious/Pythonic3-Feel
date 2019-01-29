class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L = len(nums)
        c = 0
        for i in range(0, L-1):
            if nums[i] > nums[i+1]:
                c = c+1
        print(c)

if __name__ == "__main__":

    obj = Solution()
    A =  [4, 2, 3, 6, 7, 8, 9]
    A = [4,2,1]
    A = [3,4,2,3]
    r = obj.checkPossibility(A)
    print(r)