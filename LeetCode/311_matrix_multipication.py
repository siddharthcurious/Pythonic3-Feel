from typing import List
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        rowA = len(A)
        colA = len(A[0])

        rowB = len(B)
        colB = len(B[0])

        result = []

        for r in range(rowA):
            rrow = []
            for c in range(colB):
                row = A[r]
                sum = 0
                for rb in range(rowB):
                    sum += row[rb] * B[rb][c]
                rrow.append(sum)
            result.append(rrow)
        return result

if __name__ == "__main__":

    obj = Solution()

    A = [
        [1, 0, 0],
        [-1, 0, 3]
    ]

    B = [
        [7, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    r = obj.multiply(A, B)
    print(r)