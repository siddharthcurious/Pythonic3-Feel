from typing import List

from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter1 = Counter(arr1)
        order = {}
        for i in range(len(arr2)):
            order.update({arr2[i]: i})

        counter2 = {}
        sub = []
        for k, v in counter1.items():
            if order.get(k) == None:
                sub.append(k)
            else:
                counter2.update({(k, order[k]): v})

        counter2 = sorted(counter2.items(), key=lambda x: x[0][1])
        r = []
        print(counter2)
        print(sub)
        for e in counter2:
            count = e[1]
            for c in range(count):
                r.append(e[0][0])
        r.extend(sorted(sub))
        return r
if __name__ == "__main__":

    obj = Solution()
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]

    arr1 = [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31]
    arr2 = [2, 42, 38, 0, 43, 21]
    r = obj.relativeSortArray(arr1, arr2)
    print(r)