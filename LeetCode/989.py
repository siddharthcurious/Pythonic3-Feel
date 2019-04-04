from typing import  List
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:

        if K == 0:
            return A
        KA = []
        i = 1
        power = pow(10, i)
        while power <= K:
            i += 1
            power = pow(10, i)

        p = i - 1

        while p:
            power = pow(10, p)
            r = K // power
            K = K % power
            KA.append(r)
            p -= 1
        KA.append(K)

        i = len(A)-1
        j = len(KA)-1
        sum = []
        carry = 0
        while i >= 0 and j >= 0:
            s = A[i] + KA[j] + carry
            if s >= 10:
                carry = s // 10
                r = s % 10
                sum.insert(0, r)
            else:
                sum.insert(0, s)
                carry = 0

            i -= 1
            j -= 1

        if i < 0:
            while j >= 0:
                s = KA[j] + carry
                if s >= 10:
                    carry = s // 10
                    r = s % 10
                    sum.insert(0, r)
                else:
                    sum.insert(0, s)
                    carry = 0
                j -= 1

        if j < 0:
            while i >= 0:
                s = A[i] + carry
                if s >= 10:
                    carry = s // 10
                    r = s % 10
                    sum.insert(0, r)
                else:
                    sum.insert(0, s)
                    carry = 0
                i -= 1

        if carry > 0:
            sum.insert(0, carry)

        return sum

if __name__ == "__main__":

    obj = Solution()
    A = [9, 9, 9, 9]
    K = 9999

    A = [1, 2, 0, 0]
    K = 34

    A = [2, 7, 4]
    K = 181

    A = [2, 1, 5]
    K = 806

    A = [0]
    K = 123
    r = obj.addToArrayForm(A, K)
    print(r)
