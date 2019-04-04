from typing import List

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:

        num = ""
        r = []
        for i in A:
            num += str(i)
            num1 = int(num, 2)
            if num1 % 5 == 0:
                r.append(True)
            else:
                r.append(False)
        return r

if __name__ == "__main__":

    obj = Solution()
    binary = [0,1,1]
    r = obj.prefixesDivBy5(binary)