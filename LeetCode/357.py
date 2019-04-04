class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        def number(N, n, prefix, visited, total):
            if N < n and N > 0:
                total[0] += 1
            if N == 0:
                total[0] += 1
                return
            for i in range(10):
                if prefix == "" and i == 0:
                    continue
                if visited[i] == 0:
                    visited[i] = 1
                    number(N-1, n, prefix+str(i), visited, total)
                    visited[i] = 0

        total = [0]
        number(n, n, "", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], total)
        return total[0] + 1

if __name__ == "__main__":

    obj = Solution()
    N = 3
    r = obj.countNumbersWithUniqueDigits(N)
    print(r)
