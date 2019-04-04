class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        numbers = []
        def number(N, prefix):
            if N == 2:
                numbers.append(prefix)
            if N == 1:
                numbers.append(prefix)
            if N == 0:
                numbers.append(prefix)
                return

            for i in range(10):
                if prefix == "" and i == 0:
                    continue
                number(N-1, prefix+str(i))
        number(n, "")

        print(len(numbers))

        def unique(num):
            visited = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for e in num:
                if visited[int(e)] == 1:
                    return False
                else:
                    visited[int(e)] = 1
            return True

        print(numbers)

        c = 0
        for numb in numbers:
            if unique(numb):
                c += 1
        return c

if __name__ == "__main__":

    obj = Solution()
    N = 3
    r = obj.countNumbersWithUniqueDigits(N)
    print(r)