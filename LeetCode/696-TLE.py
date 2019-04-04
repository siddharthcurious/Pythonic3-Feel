class Solution:
    def equalZeroOne(self, sub):
        if sub[0] == "0":
            i = 0
            j = len(sub)-1
            while i < j:
                if sub[i] == "0" and sub[j] == "1":
                    i += 1
                    j -= 1
                else:
                    break
            if i-j == 1:
                return True
            return False

        if sub[0] == "1":
            i = 0
            j = len(sub)-1
            while i < j:
                if sub[i] == "1" and sub[j] == "0":
                    i += 1
                    j -= 1
                else:
                    break
            if i-j == 1:
                return True
            return False


    def countBinarySubstrings(self, s: str) -> int:

        L = len(s)

        i = 2
        count = 0
        while i <= L:
            j = 0
            while j < L:
                if i+j <= L:
                    #print(s[j:j+i])
                    if self.equalZeroOne(s[j:j+i]) == True:
                        count += 1
                j += 1
            i += 2
        return count

if __name__ == "__main__":

    obj = Solution()
    i = "01010011"
    i = "00110011"
    r  = obj.countBinarySubstrings(i)
    print(r)