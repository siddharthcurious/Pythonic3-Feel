from typing import List

from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        r = []
        subs = Counter(B[0])
        for sub in B[1:]:
            print(subs)
            s = Counter(sub)
            for k, v in s.items():
                if subs.get(k) == None:
                    subs.update({k: v})
                elif subs.get(k):
                    if subs.get(k) < v:
                        subs[k] = v
                else:
                    pass

        for i, w in enumerate(A):
            wctr = Counter(w)
            subcount = wctr.__and__(subs)
            if subcount == subs:
                r.append(A[i])
        return r

if __name__ == "__main__":

    obj = Solution()
    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["e", "o"]

    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["l", "e"]

    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["e", "oo"]

    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["ec", "oc", "ceo"]

    A = ["aaaaa", "ccaac", "accaa", "cbbca"]
    B = ["b", "bb", "ca"]

    r = obj.wordSubsets(A, B)
    print(r)