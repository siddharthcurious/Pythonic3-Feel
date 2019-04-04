import numpy
import copy

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        first_col = [0] * rows
        first_row = [0] * cols

        for i in range(rows):
            first_col[i] = max(grid[i])

        m = -1
        for c in range(cols):
            temp = []
            for r in range(rows):
                temp.append(grid[r][c])
            first_row[c] = (max(temp))

        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans += min(first_row[c], first_col[r]) - grid[r][c]
        return ans

if __name__ == "__main__":

    obj = Solution()

    grid = [[90,78,6],[21,97,58],[69,31,59]]
    #grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

    r = obj.maxIncreaseKeepingSkyline(grid)
    print(r)