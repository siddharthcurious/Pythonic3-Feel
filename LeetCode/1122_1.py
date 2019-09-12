from collections import Counter

from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        order = {}
        for i in range(len(arr2)):
            order.update({arr2[i]: i})

        counter1 = Counter(arr1)
        data = {}
        sub = []
        for k, v in counter1.items():
            if order.get(k) == None:
                sub.append(k)
            else:
                data.update({(k, order[k]): v})
        data1 = sorted(data.items(), key= lambda x: x[0][1])
        r = []
        for e in data1:
            c = e[1]
            for j in range(c):
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







