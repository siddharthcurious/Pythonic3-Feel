class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        sstk = []
        for c in S:
            if c != "#":
                sstk.append(c)
            elif c == "#":
                if sstk:
                    sstk.pop()

        tstk = []
        for c in T:
            if c != "#":
                tstk.append(c)
            elif c == "#":
                if tstk:
                    tstk.pop()

        if sstk == tstk:
            return True
        return False

if __name__ == "__main__":

    s = Solution()

    S = "ab#c"
    T = "ad#c"

    S = "a##c"
    T = "#a#c"

    S = "a#c"
    T = "b"
    r = s.backspaceCompare(S, T)
    print(r)