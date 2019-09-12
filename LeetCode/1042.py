from typing import List
from collections import defaultdict
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        if paths == []:
            return [1] * N
        if N == 1:
            return [1]
        if N == 2:
            return [1, 2]

        graph = defaultdict(list)

        for edge in paths:
            graph[edge[0] - 1].append(edge[1] - 1)
            graph[edge[1] - 1].append(edge[0] - 1)

        colors = [0] * N
        total = {1, 2, 3, 4}

        for i, neigh in graph.items():
            used = set()
            for j in neigh:
                if colors[j] != 0:
                    used.add(colors[j])
            available = total - used
            colors[i] = min(available)

        for i in range(N):
            if colors[i] == 0:
                colors[i] = 1
        return colors

if __name__ == "__main__":

    obj = Solution()
    N = 6
    paths = [[1,2], [2,3], [3,4], [4,5],[5,6], [6,1]]
    r = obj.gardenNoAdj(N, paths)
    print(r)