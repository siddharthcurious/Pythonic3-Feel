class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stk = []
        for element in pushed:
            if element != popped[0]:
                stk.append(element)
            else:
                popped = popped[1:]
                while stk:
                    if stk[-1] == popped[0]:
                        stk.pop()
                        popped = popped[1:]
                    else:
                        break
        if stk:
            return False
        return True

if __name__ == "__main__":

    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]

    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]

    #pushed = [2, 1, 0]
    #popped = [1, 2, 0]

    obj = Solution()
    r = obj.validateStackSequences(pushed, popped)
    print(r)