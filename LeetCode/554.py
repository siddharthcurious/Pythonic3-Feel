class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        L = len(wall)
        length = []
        for layer in wall:
            length.append(len(layer))
        mlen = max(length)

        for i in range(1, mlen+1):
            for layer in wall:
                if layer[i-1] == i:
                    pass
            print("")




if __name__ == "__main__":

    s = Solution()

    bricks = [[1,2,2,1],
              [3,1,2],
              [1,3,2],
              [2,4],
              [3,1,2],
              [1,3,1,1]]

    s.leastBricks(bricks)
