class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        L1 = set(list1)
        L2 = set(list2)

        result = {}
        common = L1.intersection(L2)
        if len(common) == 1:
            return list(common)
        else:
            for element in common:
                ind1 = list1.index(element)
                ind2 = list2.index(element)
                s = ind1 + ind2
                if s not in result:
                    result.update({s: [element]})
                elif s in result:
                    result[s].append(element)
        min_ind = min(result.keys())
        return result[min_ind]



if __name__ == "__main__":

    s = Solution()

    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

    r = s.findRestaurant(list1, list2)
    print(r)

    list1 = ["Shogun","Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]

    r = s.findRestaurant(list1, list2)
    print(r)


