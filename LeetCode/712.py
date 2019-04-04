class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if not s1:
            return len(s2)
        elif not s2:
            return len(s1)
        elif s1[0] == s2[0]:
            return self.minimumDeleteSum(s1[1:], s2[1:])
        else:
            return 1+min(self.minimumDeleteSum(s1, s2[1:]), self.minimumDeleteSum(s1[1:], s2))

if __name__ == "__main__":

    obj = Solution()
    s1 = "eat"
    s2 = "sea"
    r = obj.minimumDeleteSum(s1, s2)
    print(r)