from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        sub = Counter(s1)
        string = Counter(s2)

        l = len(sub)
        intersect = string.__and__(sub)
        if intersect == sub:
            pass

if __name__ == "__main__":

    obj = Solution()
    s1 = "ab"
    s2 = "eidbaooo"
    r = obj.checkInclusion(s1, s2)
    print(r)