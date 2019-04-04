from collections import defaultdict
class Solution:
    def findJudge(self, N, trust):

        d = defaultdict(set)
        for t in trust:
            d[t[0]].add(t[1])

        in_edge = {}
        out_edge = {}

        for key, value in d.items():
            out_edge.update({key: len(value)})

        for key, value in d.items():
            for e in value:
                if in_edge.get(e) == None:
                    in_edge.update({e: 1})
                else:
                    c = in_edge.get(e)
                    in_edge.update({e: c+1})

        e = 0
        for key, value in in_edge.items():
            if value == N - 1:
                e = key
        if out_edge.get(e) == None:
            return e
        else:
            return -1

if __name__ == "__main__":

    s = Solution()

    N = 4

    trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
    #trust = [[1,2],[2,3]]
    r = s.findJudge(N, trust)
    print(r)
