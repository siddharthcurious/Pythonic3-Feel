from itertools import permutations
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s = ""
        for i in range(1, n + 1):
            s += str(i)
        k = k - 1
        perms = permutations(s)
        for p in perms:
            if k == 0:
                return "".join(p)
            k = k - 1
        return None


if __name__ == "__main__":

    s = Solution()
    r = s.getPermutation(3, 3)
    print(r)