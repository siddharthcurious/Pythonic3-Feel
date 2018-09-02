from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[0]].append(p[1])

        print(graph)


if __name__ == "__main__":

    s = Solution()
    numCourses = 2
    prerequisites = [[1,0],[2,1],[3,1]]
    r = s.canFinish(numCourses, prerequisites)
    print(r)
