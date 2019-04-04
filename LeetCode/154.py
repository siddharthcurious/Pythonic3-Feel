from typing import List

class Solution:
    def pivote(self, nums, start, end):
        if start == end:
            return start
        if start > end:
            return -1

        mid = int(start+(end - start)/2)
        if start < mid < end:
            if nums[mid-1] > nums[mid] < nums[mid+1]:
                return mid
        if mid < end:
            if nums[mid] > nums[mid+1]:
                return mid+1
        if start < mid:
            if nums[mid-1] < nums[mid]:
                return mid-1



    def findMin(self, nums: List[int]) -> int:
        L = len(nums)
        r = self.pivote(nums, 0, L-1)
        if r >= 0:
            return nums[r]

if __name__ == "__main__":

    obj = Solution()
    A = [1,2,3,4,5,6,7,0]
    A = [2,2,2,0,1]
    r = obj.findMin(A)
    print(r)
