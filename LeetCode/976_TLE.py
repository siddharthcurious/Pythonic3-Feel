from itertools import combinations
class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        combs = combinations(A, 3)
        max = 0
        for e in combs:
            a = e[0]
            b = e[1]
            c = e[2]
            if a < b + c and b < a + c and c < a + b:
                if a + b + c > max:
                    max = a + b + c
        return max

if __name__ == "__main__":

    s = Solution()
    Input = [3, 6, 2, 3]
    r = s.largestPerimeter(Input)
    print(r)
