class Solution:
    def __add_string(self, num1, num2):

        L1 = len(num1)
        L2 = len(num2)

        number1 = ""
        number2 = ""
        if(L1 > L2):
            number1 = num2
            number2 = num1
        else:
            number1 = num1
            number2 = num2

        sL = len(number1)
        bL = len(number2)
        i = sL - 1
        j = bL - 1
        carry = 0
        result = ""
        while i >= 0:
            sum = int(number1[i]) + int(number2[j])
            sum = sum + carry
            carry = sum // 10
            rem = sum % 10
            result = str(rem) + result
            i -= 1
            j -= 1

        while j >= 0:
            sum = int(number2[j]) + carry
            carry = sum // 10
            rem = sum % 10
            result = str(rem) + result
            j -= 1

        if carry > 0:
            result = str(carry) + result
        return result

    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        L1 = len(num1)
        L2 = len(num2)

        result = ""
        c = 0
        for i in range(L1-1, -1, -1):
            carry = 0
            tmul = ""
            for j in range(L2-1, -1, -1):
                m = int(num1[i]) * int(num2[j])
                r = m + carry
                rem = r % 10
                carry = r // 10
                tmul = str(rem) + tmul
            if carry > 0:
                tmul = str(carry) + tmul
            if result == "":
                result = tmul
            else:
                t = tmul+"0"*c
                result = self.__add_string(result, t)
            c += 1

        return result


if __name__ == "__main__":

    obj = Solution()
    num1 = "100"
    num2 = "100"
    r = obj.multiply(num1, num2)
    print(r)
