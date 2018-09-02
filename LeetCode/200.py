class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(row):
            neighbors = grid[row]
            for col in range(len(neighbors)):
                if grid[row][col] == "1" and col not in visisted:
                    visisted.append(col)
                    dfs(col)

        visisted = [0]
        dfs(0)
        print(visisted)

if __name__ == "__main__":

    s = Solution()
    grid = ["11110",
            "11010",
            "11000",
            "00000"]
    s.numIslands(grid)