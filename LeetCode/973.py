from math import sqrt
from operator import itemgetter
class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distance = []
        for point in points:
            d = sqrt(point[0]*point[0] + point[1]*point[1])
            distance.append((d, point))
        distance_sorted = sorted(distance, key=itemgetter(0))
        result = []
        for i in range(K):
            result.append(distance_sorted[i][1])
        return result

if __name__ == "__main__":

    s = Solution()
    points = [[1, 3], [-2, 2]]
    K = 1
    r = s.kClosest(points, K)
    print(r)