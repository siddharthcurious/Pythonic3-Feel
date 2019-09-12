from typing import List

from collections import defaultdict
class Solution:
    def totalFruit(self, tree: List[int]) -> int:



        data = defaultdict(list)
        for i, e in enumerate(tree):
            data[e].append(i)

        fruits = set()
        ftype = []
        for e in trees:
            if e not in fruits:
                fruits.add(e)
                ftype.append(e)
            else:
                pass
        pairs = []
        i = 0
        L = len(ftype)
        while i < L - 1:
            pairs.append((ftype[i], ftype[i+1]))
            i += 1
        r = 0
        for p in pairs:
            indices1 = data[p[0]]
            indices2 = data[p[1]]
            cont_indeces = set((indices1 + indices2))
            mx = max(cont_indeces)
            mn = min(cont_indeces)
            diff = mx - mn
            if diff+1 == len(cont_indeces):
                if diff+1 > r:
                    r = diff+1
        return r


if __name__ == "__main__":

    obj = Solution()
    trees = [3,3,3,1,2,1,1,2,3,3,4]
    trees = [1,2,3,2,2]
    trees = [0,1,2,2]
    trees = [1,2,1]
    trees = [0]
    r = obj.totalFruit(trees)
    print(r)
