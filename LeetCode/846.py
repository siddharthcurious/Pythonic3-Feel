from collections import Counter
class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        L = len(hand)
        if L%W != 0:
            return False

        counter = Counter(hand)

        while counter:
            tmin = min(counter)
            for k in range(tmin, tmin+W):
                v = counter.get(k)
                if not v:
                    return False
                if v == 1:
                    del counter[k]
                else:
                    counter[k] = v-1
        return True

if __name__ == "__main__":

    s = Solution()

    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    W = 3
    s.isNStraightHand(hand, W)