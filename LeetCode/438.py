from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):

        if s == "" and p == "":
            return [0]
        if len(s) < len(p):
            return []

        if s == p:
            return [0]

        i = 0
        L = len(s)
        lenp = len(p)
        result = []

        pcount = Counter(p)
        while i < L:
            if i + lenp <= L:
                sub = s[i:i+lenp]

                scount = Counter(sub)
                if pcount == scount:
                    result.append(i)
            i += 1
        return result

if __name__ == "__main__":

    obj = Solution()
    s = "cbaebabacd"
    p =  "abc"
    s = "aaaaa"
    p = "aa"
    r  = obj.findAnagrams(s, p)
    print(r)