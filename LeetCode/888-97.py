class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)
        sumB = sum(B)
        LA = len(A)
        LB = len(B)

        results = []
        for i in range(0, LA):
            for j in range(0, LB):
                ssA = sumA - A[i]
                ssB = sumB - B[j]

                ssA += B[j]
                ssB += A[i]

                if ssA == ssB:
                    results.append(A[i])
                    results.append(B[j])
                    return results


if __name__ == "__main__":

    s = Solution()

    A = [1, 2, 5]
    B = [2, 4]

    r = s.fairCandySwap(A, B)

    print(r)