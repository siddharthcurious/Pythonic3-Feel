class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if "+" in a:
            A = a.split("i")[0].split("+")
        else:
            A = a.split("i")[0].split("-")
            if len(A) == 3:
                A = A[1:]
                A[0] = "-"+A[0]
            sign_a = "-"
            A[1] = sign_a+A[1]

        if "+" in b:
            B = b.split("i")[0].split("+")
        else:
            B = b.split("i")[0].split("-")
            if len(B) == 3:
                B = B[1:]
                B[0] = "-"+B[0]
            sign_b = "-"
            B[1] = sign_b+B[1]

        real1 = int(A[0]) * int(B[0])
        real2 = -1 * int(A[1]) * int(B[1])

        complex1 = int(A[0]) * int(B[1])
        complex2 = int(A[1]) * int(B[0])

        real = real1 + real2
        complex = complex1 + complex2


        return "{0}+{1}i".format(real, complex)

if __name__ == "__main__":

    obj = Solution()
    a = "1+1i"
    b = "1-1i"

    r = obj.complexNumberMultiply(a, b)
    print(r)