class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        map = {
            "0": "0",
            "1": "1",
            "2": "5",
            "3": "3",
            "4": "4",
            "5": "2",
            "6": "9",
            "7": "7",
            "8": "8",
            "9": "6"
        }

        c = 0
        for num in range(1, N+1):
            snum = str(num)
            if "3" in snum:
                continue
            if "4" in snum:
                continue
            if "7" in snum:
                continue
            nnum = ""
            for e in snum:
                e1 = map.get(e)
                nnum += e1
            if snum != nnum:
                c +=1
        return c

if __name__ == "__main__":

    obj = Solution()
    N = 857
    r = obj.rotatedDigits(N)
    print(r)