from itertools import combinations
class Solution(object):
    def findArea(self, points):
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        x4, y4 = points[3]

        a = (x1*y2 - x2*y1) + (x2*y3 - x3*y2) + (x3*y4 - x4*y3) + (x4*y1-y4*x1)
        print(a)

        if a < 0:
            a = -1 * a
        return a

    def sqr(self, num):
        return num * num

    def isRectangle(self, points):
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        x4, y4 = points[3]

        cx = (x1 + x2 + x3 + x4)/4
        cy = (y1 + y2 + y3 + y4)/4

        dd1 = self.sqr(cx - x1) + self.sqr(cy - y1)
        dd2 = self.sqr(cx - x2) + self.sqr(cy - y2)
        dd3 = self.sqr(cx - x3) + self.sqr(cy - y3)
        dd4 = self.sqr(cx - x4) + self.sqr(cy - y4)
        return dd1 == dd2 and dd1 == dd3 and dd1 == dd4

    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        min_area = float("inf")
        points_combs = combinations(points, 4)
        for p in points_combs:
            r = self.isRectangle(p)
            if r == True:
                a = self.findArea(p)
                if min_area > a:
                    min_area = a
        return min_area


if __name__ == "__main__":

    s = Solution()
    points = [[1,2],[2,1],[1,0],[0,1], [2,3]]
    points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
    points = [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
    r = s.minAreaFreeRect(points)
    print(r)