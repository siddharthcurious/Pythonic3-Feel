class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if not num1:
            return num2
        if not num2:
            return num1

        L1 = len(num1)
        L2 = len(num2)

        looper = min(L1, L2)

        i1 = L1-1
        i2 = L2-1
        carry = 0
        sum = ""

        while i1 > -1 and i2 > -1:
            c1 = int(num1[i1])
            c2 = int(num2[i2])

            sum1 = c1 + c2 + carry

            if sum1 > 9:
                carry = int(str(sum1)[0])
                num = str(sum1)[1]
            else:
                carry = 0
                num = str(sum1)
            sum = num + sum

            i1 -= 1
            i2 -= 1

        if L1 == L2:
            if carry > 0:
                sum  = str(carry) + sum
                return sum
            else:
                return sum

        rem_str = ""
        d = 0
        if L1 > L2:
            d = L1 - L2
            rem_str = num1[:d]

        if L2 > L1:
            d = L2 - L1
            rem_str = num2[:d]

        j1 = d - 1
        if carry == 0:
            sum = rem_str + sum
            return sum

        else:
            while j1 > -1:
                c1 = int(rem_str[j1])
                sum1 = carry + c1
                if sum1 > 9:
                    carry = int(str(sum1)[0])
                    num = str(sum1)[1]
                else:
                    carry = 0
                    num = str(sum1)
                sum = num + sum
                j1 -= 1
        if carry > 0:
            sum = str(carry) + sum

        return sum


if __name__ == "__main__":

    s = Solution()

    num1 =  "99999"
    num2 =  "1"

    r = s.addStrings(num1, num2)

    print(r)