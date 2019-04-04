import math
class Solution:
    def convertToTitle(self, n: int) -> str:
        map = "#ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        power = 0
        while n >= pow(26, power):
            power += 1

        power -= 1

        colname = ""
        rem = 0
        while power > 0:
            divisor = pow(26, power)
            devidend = n // divisor
            rem = n % divisor
            n = rem
            colname += map[devidend]
            print(devidend)
            print(rem)
            power -= 1
        colname += map[rem]

        print(colname)

if __name__ == "__main__":

    obj = Solution()
    i = 701
    r  = obj.convertToTitle(i)
    print(r)