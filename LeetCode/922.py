class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        L = len(A)
        i = 0
        j = L - 1

        while i < j:
            while A[i] % 2 == 0:
                 i = i + 1
            while A[j] % 2 == 1:
                j = j - 1

            if i < j:
                ch = A[i]
                A[i] = A[j]
                A[j] = ch
                i = i + 1
                j = j - 1

        i = 1
        j = L - 2

        while i < j:
            ch = A[i]
            A[i] = A[j]
            A[j] = ch
            i = i + 2
            j = j - 2
        return A

if __name__ == "__main__":

    obj = Solution()
    array = [4,2,5,7, 9, 10, 11, 13, 15, 90, 40, 80]
    r = obj.sortArrayByParityII(array)
    print(r)