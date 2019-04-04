from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k == 0 or n == 0:
            return [[]]

        total = set()
        def combinationSum(k, n, num, visited):
            if k == 0 and n == 0:
                total.add(tuple(set(num)))
                return

            for i in range(1,10):
                if n - i >= 0 and visited[i] == 0:
                    visited[i] = 1
                    combinationSum(k-1, n-i, num+[i], visited)
                    visited[i] = 0
                else:
                    continue

        nums = []
        combinationSum(k, n, nums, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        return [list(d) for d in total]

if __name__ == "__main__":

    obj = Solution()
    k = 3
    n = 7
    r = obj.combinationSum3(k, n)
    print(r)
