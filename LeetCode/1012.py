class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bits = bin(N)
        comp = ""
        for b in bits[2:]:
            if b == "1":
                comp += "0"
            elif b == "0":
                comp += "1"
        return int(comp, 2)

if __name__ == "__main__":

    s = Solution()
    n = 10
    r = s.bitwiseComplement(n)
    print(r)