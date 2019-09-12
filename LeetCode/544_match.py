import math
import copy
class Solution:
    def findContestMatch(self, n: int) -> str:

        teams = [x for x in range(1, n+1)]

        i = 0
        j = len(teams)-1
        games = []
        while i < j:
            team = (teams[i], teams[j])
            games.append(team)
            i += 1
            j -= 1

        k = math.log(n, 2)

        g = []
        j = len(games)-1
        ans = []
        for _ in range(int(k-1)):
            i = 0
            while i < j:
                g.append((games[i], games[j]))
                i += 1
                j -= 1
            j = len(g)-1
            games = copy.deepcopy(g)
            ans = games
            g = []
        return str(ans[0]).replace(" ", "")

if __name__ == "__main__":

    obj = Solution()
    n = 16
    r = obj.findContestMatch(n)
    print(r)
