class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = set(s)
        t1 = set(t)
        if len(s1) != len(t1):
            return False

        hashmap = {}
        for i, j in zip(s,t):
            if i in hashmap:
                if j == hashmap[i]:
                    continue
                else:
                    return False
            elif i not in hashmap:
                hashmap.update({i: j})
        return True

if __name__ == "__main__":

    obj = Solution()

    s = "ab"
    t = "aa"
    r  = obj.isIsomorphic(s, t)
    print(r)
