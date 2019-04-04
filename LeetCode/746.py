class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        L = len(cost)
        totalCost = [0] * (L+1)
        totalCost[0] = 0
        totalCost[1] = 0
        for i in range(2, len(cost)+1):
            totalCost[i] = min(cost[i-1]+totalCost[i-1], cost[i-2]+totalCost[i-2])
        return totalCost[L]

if __name__ == "__main__":

    obj = Solution()
    cost = [10, 15, 20]
    r = obj.minCostClimbingStairs(cost)
    print(r)