from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        numbers = set()

        i = 0
        j = 0

        for i in range(18):
            for j in range(18):
                n = pow(x, i) + pow(y, j)
                if n <= bound:
                    numbers.add(n)
                else:
                    break
                j += 1
            i += 1
        return list(numbers)

if __name__ == "__main__":

    s = Solution()
    x = 2
    y = 3
    bound = 10

    x = 3
    y = 5
    bound = 15

    r = s.powerfulIntegers(x, y, bound)
    print(r)
