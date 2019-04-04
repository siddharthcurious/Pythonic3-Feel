from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        L = len(time)
        count = 0
        for i in range(L):
            for j in range(i+1, L):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        return count

if __name__ == "__main__":

    s = Solution()
    i = [30,20,150,100,40]
    i = [60, 60, 60]
    r = s.numPairsDivisibleBy60(i)
    print(r)

