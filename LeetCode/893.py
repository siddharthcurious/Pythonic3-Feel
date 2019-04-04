class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        total = set()
        for s in A:
            l = []
            for i, ch in enumerate(s):
                j = i % 2
                p = (ch, j)
                l.append(p)
            l1 = tuple(sorted(set(l), key= lambda x:x[0]))
            print(l1)
            total.add(l1)
            if l1 not in total:
                total.add(l1)
        return len(total)

if __name__ == "__main__":

    obj = Solution()
    A = ["abc", "acb", "bac", "bca", "cab", "cba"]
    A = ["abcd","cdab","adcb","cbad"]
    A = ["couxuxaubw","zsptcwcghr","kkntvvhbcc","nkhtcvvckb","crcwhspgzt"]
    r = obj.numSpecialEquivGroups(A)
    print(r)