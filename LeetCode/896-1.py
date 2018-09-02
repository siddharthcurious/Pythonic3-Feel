class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        judge = []
        for i in range(len(A)-1):
            judge.append(A[i] - A[i+1])



if __name__ == "__main__":

    s = Solution()
    a = [6,5,4,4,7]
    a = [2,2,2,1,4,5]
    r = s.isMonotonic(a)
    print(r)