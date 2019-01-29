class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = dict()
        for element in numbers:
            if hashmap.get(element) is None:
                hashmap.update({element:1})
            if hashmap.get(element):
                pass

        print(hashmap)


if __name__ == "__main__":

    obj = Solution()

    numbers = [2, 7, 11, 15]
    target = 9

    r = obj.twoSum(numbers, target)
    print(r)