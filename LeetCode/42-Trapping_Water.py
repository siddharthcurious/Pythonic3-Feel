from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        L = len(height)
        leftmax = [0] * L
        rightmax = [0] * L

        print(height)
        lmax = 0
        for i, e in enumerate(height):
            if e > lmax:
                lmax = e
            leftmax[i] = lmax
        leftmax[0] = 0

        rmax = 0
        for i in range(L-1, -1, -1):
            if height[i] > rmax:
                rmax = height[i]
            rightmax[i] = rmax
        rightmax[L-1] = 0

        total = 0
        for i, e in enumerate(height):
            # print(leftmax[i], rightmax[i])
            h = min(leftmax[i], rightmax[i])
            if h != 0:
                total += h - height[i]
        return total

if __name__ == "__main__":

    obj = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    #height = [5,0,0,5,1]
    r = obj.trap(height)
    print(r)

