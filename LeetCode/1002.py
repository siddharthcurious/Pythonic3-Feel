from typing import List

from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        lcounters = []
        for a in A:
            a1 = Counter(a)
            lcounters.append(a1)

        temp = set(lcounters[0].keys())
        for ctr in lcounters[1:]:
            temp2 = set(ctr.keys())
            temp = temp.intersection(temp2)

        result = []
        for l in temp:
            occ = []
            for ctr in lcounters:
                occ.append(ctr.get(l))
            n = min(occ)
            result.extend([l]*n)
        return result

if __name__ == "__main__":

    s = Solution()

    i = ["bella", "label", "roller"]
    r = s.commonChars(i)
    print(r)
