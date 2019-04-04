class Solution:
    def isDigit(self, d):
        if d >= '0' and d <= '9':
            return True
        return False

    def isChar(self, c):
        if self.isDigit(c):
            return False
        return True

    def decodeAtIndex(self, S: str, K: int) -> str:

        i = 0
        L = len(S)
        t = K - 1
        while i < L:
            tstr = []
            while self.isChar(S[i]):
                tstr.append(S[i])
                i += 1

            tnum = []
            while self.isDigit(S[i]):
                tnum.append(S[i])
                i += 1

if __name__ == "__main__":

    S = "leet2code3"
    K = 10