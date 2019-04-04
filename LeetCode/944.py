from collections import defaultdict
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        map = defaultdict(list)
        for word in A:
            i = 1
            for e in word:
                map[i].append(e)
                i += 1

        count = 0
        for key, value in map.items():
            i = 0
            while i < len(value)-1:
                if value[i] > value[i+1]:
                    count += 1
                    break
                i += 1
        return count

if __name__ == "__main__":

    obj = Solution()
    A = ["cba", "daf", "ghi"]
    A = ["a","b"]
    A = ["zyx","wvu","tsr"]
    A = ["cba","daf","ghi"]
    r = obj.minDeletionSize(A)
    print(r)