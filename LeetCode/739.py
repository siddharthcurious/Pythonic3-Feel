class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """


if __name__ == "__main__":

    obj = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    T = [55,38,53,81,61,93,97,32,43,78]
    r  = obj.dailyTemperatures(T)
    print(r)