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


if __name__ == "__main__":

    s = Solution()

    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    W = 3
    s.isNStraightHand(hand, W)