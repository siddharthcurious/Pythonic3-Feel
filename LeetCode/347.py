class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        C = {}
        for n in nums:
            if n in C:
                c = C[n]
                C.update({n:c+1})
            else:
                C.update({n:1})
        sorted_dict = sorted(C.items(), key=lambda x: x[1], reverse=True)
        results = []
        for k, v in sorted_dict[:k]:
            results.append(k)
        return results

if __name__ == "__main__":

    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    r = s.topKFrequent(nums, k)
    print(r)
