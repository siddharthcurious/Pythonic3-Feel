class Solution(object):
    def reverseOnlyLetters(self, INPUT):
        """
        :type S: str
        :rtype: str
        """
        S = list(INPUT)
        del INPUT

        a_ascii = ord('a')
        z_ascii = ord('z')
        A_ascii = ord('A')
        Z_ascii = ord('Z')

        L = len(S)
        if S == "":
            return ""
        elif len(S) == 1:
            return "".join(S)
        else:
            i = 0
            j = L-1
            while i < j:
                if ord(S[i]) < a_ascii and ord(S[i]) > z_ascii:
                    i = i + 1
                if ord(S[j]) < a_ascii and ord(S[j]) > z_ascii:
                    j = j - 1
                if ord(S[i]) < A_ascii and ord(S[i]) > Z_ascii:
                    i =  i + 1
                if ord(S[i]) < A_ascii and ord(S[i]) > Z_ascii:
                    j = j - 1

                ch = S[i]
                S[i] = S[j]
                S[j] = ch
                i = i + 1
                j = j - 1

        OUPUT = "".join(S)
        del S
        return OUPUT

if __name__ == "__main__":

    s = Solution()
    Input = "a-bC-dEf-ghIj"
    Input = "A-*-bsfmkoei"
    Input = "a-bC-dEf-ghIj" # "j-Ih-gfE-dCba"
    r = s.reverseOnlyLetters(Input)
    print(r)