from typing import List

class Solution:
    def pivote(self, nums, start, end):
        if start > end:
            return -1
        if start == end:
            return start

        mid = int(start + (end - start)/2)

        if start < mid:
            if nums[mid-1] > nums[mid]:
                return mid-1
        if mid < end:
            if nums[mid] > nums[mid+1]:
                return mid
        if nums[start] < nums[mid]:
            return self.pivote(nums, mid+1, end)
        if nums[mid] < nums[end]:
            return self.pivote(nums, start, mid-1)

    def findMin(self, nums: List[int]) -> int:
        L = len(nums)
        r = self.pivote(nums, 0, L-1)
        return nums[r+1]

if __name__ == "__main__":

    obj = Solution()
    A = [1,2,3,4,5,6,7,0]
    r = obj.findMin(A)
    print(r)
