from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        hashmap = [0] * 60
        for e in time:
            mod = e % 60
            hashmap[mod] += 1

        i = 1
        j = 59

        ans = hashmap[0] * (hashmap[0] - 1) / 2
        ans += hashmap[30] * (hashmap[30] - 1) / 2

        while i < j:
            if hashmap[i] > 0 and hashmap[j] > 0:
                ans += hashmap[i] * hashmap[j]
                i += 1
                j -= 1
            else:
                i += 1
                j -= 1
        return int(ans)

if __name__ == "__main__":

    s = Solution()
    i = [30,20,150,100,40]
    i = [60, 60, 60]
    i = [15,63,451,213,37,209,343,319]
    r = s.numPairsDivisibleBy60(i)
    print(r)

