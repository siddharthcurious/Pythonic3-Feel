from collections import Counter
from collections import defaultdict
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        if L == 1:
            return 1

        counter = Counter(nums)
        mf = counter.most_common(1)
        mfs = []
        for key, value in counter.items():
            if value == mf[0][1]:
                mfs.append(key)

        map = defaultdict(list)
        for e in mfs:
            i = 0
            while i < L:
                if e == nums[i]:
                    map[e].append(i)
                i+=1

        m = []
        for key, value in map.items():
            maxx = max(value)
            minn = min(value)
            m.append(maxx - minn)
        return min(m)+1


if __name__ == "__main__":

    obj = Solution()
    p = [1, 2, 2, 3, 1]
    p = [1,2,2,3,1,4,2]
    r  = obj.findShortestSubArray(p)
    print(r)
