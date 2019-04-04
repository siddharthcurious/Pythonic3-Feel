import copy
class Solution(object):
    def countSmaller(self, A):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        map = {}
        def mergeSort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left = arr[:mid]
                right = arr[mid:]

                mergeSort(left)
                mergeSort(right)

                i = 0
                j = 0
                k = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        arr[k] = left[i]

                        if map.get(left[i]):
                            c = map.get(left[i])
                            c += 1
                            map.update({left[i]: c})
                        else:
                            map.update({left[i]: 1})

                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    arr[k] = left[i]

                    if map.get(left[i]):
                        c = map.get(left[i])
                        c += 1
                        map.update({left[i]: c})
                    else:
                        map.update({left[i]: 1})

                    i += 1
                    k += 1

                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
        B = copy.deepcopy(A)
        mergeSort(A)
        t = []
        for e in B:
            if map.get(e):
                t.append(map.get(e))
            else:
                t.append(0)
        return t


if __name__ == "__main__":

    obj = Solution()

    A = [7, 2, 6, 1]
    r  = obj.countSmaller(A)
    print(r)