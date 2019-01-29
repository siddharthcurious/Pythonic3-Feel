from collections import Counter
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        counter = Counter(A)
        for k, v in counter.items():
            if counter[k] > 1:
                return k

if __name__ == "__main__":

    s = Solution()
    I = [5,1,5,2,5,3,5,4]
    I = [1,2,3,3]
    r = s.repeatedNTimes(I)
    print(r)