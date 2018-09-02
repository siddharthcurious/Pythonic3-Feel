from itertools import combinations
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        L = len(candidates)
        for choose in range(1, L+1):
            combs = combinations(candidates, choose)
            for c in combs:
                if sum(c) == target:
                    result.append(list(c))
        return result

if __name__ == "__main__":

    s = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    r = s.combinationSum(candidates, target)
    print(r)
