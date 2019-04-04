from typing import List

from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        words = []
        subs = []
        for i, word in enumerate(A):
            a = Counter(word)
            words.append((i, a))

        for sub in B:
            b = Counter(sub)
            subs.append(b)

        r = []
        for i, wctr in words:
            c = 0
            for s in subs:
                subcount = wctr.__and__(s)
                if subcount == s:
                    c += 1
            if c == len(subs):
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

    r = obj.wordSubsets(A, B)
    print(r)