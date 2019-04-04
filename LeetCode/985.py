from functools import reduce
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = [0] * len(queries)
        L = len(A)
        for i, q in enumerate(queries):
            index = q[1]
            if index < L:
                A[index] = A[index] + q[0]
                s = 0
                for e in A:
                    if e % 2 == 0:
                        s += e
                result[i] = s
        return result

if __name__ == "__main__":

    obj = Solution()

    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]

    r = obj.sumEvenAfterQueries(A, queries)
    print(r)
