class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        if self.isPerfectSquare(N):
            return 0

        A = []
        i = 0
        while N:
            b = N & 1
            N = N >> 1
            if b:
                A.append(i)
            i = i + 1
        df = 0
        for j in range(len(A)-1):
            td = A[j+1] - A[j]
            if td > df:
                df = td
        return df

    def isPerfectSquare(self, N):
        if N & (N -1) == 0:
            return True
        return False

if __name__ == "__main__":

    s = Solution()
    r = s.binaryGap(65)
    print(r)
