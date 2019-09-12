from typing import List
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        L = len(A)
        from_left = [0] * L
        from_right = [0] * L
        for i in range(1, L):
            if A[i] == 1:
                from_left[i] = 0
            else:
                if A[i] == 0:
                    from_left[i] = from_left[i-1] + 1

        for j in range(L-2, -1, -1):
            if A[j] == 1:
                from_right[j] = 0
            else:
                if A[j] == 0:
                    from_right[j] = from_right[j+1] + 1

        # print(from_left)
        # print(from_right)

        max = 0
        for i in range(L):
            if(from_left[i] == 0 and from_right[i] != 0):
                return from_right[i]
            elif from_left[i] != 0 and from_right[i] == 0:
                return from_right[i]
            else:
                d = min(from_left[i], from_right[i])
                if d > max:
                    max = d
        return max

if __name__ == "__main__":

    obj = Solution()
    A = [1,0,0,0,1,0,1]
    A = [0,0,0,1,0,0,0]
    r = obj.maxDistToClosest(A)
    print(r)
