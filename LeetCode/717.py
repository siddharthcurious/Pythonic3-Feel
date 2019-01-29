class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if bits[-1] != 0:
            return False
        i = 0
        L = len(bits)
        k = 0
        while i < L:
            if bits[i] == 0:
                i = i + 1
                k = i
            elif bits[i] == 1:
                i = i + 2
        if k == L:
            return True
        return False

if __name__ == "__main__":

    obj = Solution()
    bits = [1, 0, 0]
    bits = [1, 1, 1, 0]
    r = obj.isOneBitCharacter(bits)
    print(r)