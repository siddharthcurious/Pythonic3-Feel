class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        max = 0
        i = 0
        j = 1
        k = 2
        while k < len(A):
            a = A[i]
            b = A[j]
            c = A[k]
            if a < b + c and b < a + c and c < a + b:
                if a + b + c > max:
                    max = a + b + c
            i += 1
            j += 1
            k += 1
        return max

if __name__ == "__main__":

    s = Solution()
    Input = [3, 6, 2, 3]
    r = s.largestPerimeter(Input)
    print(r)
