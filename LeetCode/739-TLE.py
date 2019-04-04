class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        r = []
        i = 0
        j = 0
        L = len(T)
        for i in range(L):
            j = i + 1
            while j < L:
                if T[j] > T[i]:
                    r.append(j-i)
                    break
                j += 1
                if j == L:
                    r.append(0)
            i += 1
        r.append(0)
        return r

if __name__ == "__main__":

    obj = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    #T = [55,38,53,81,61,93,97,32,43,78]
    r  = obj.dailyTemperatures(T)
    print(r)