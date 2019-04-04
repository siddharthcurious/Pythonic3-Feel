# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:

        r = [0]
        stk = []
        def _nextGreater(head):
            if not head:
                return
            _nextGreater(head.next)
            if not stk:
                stk.append(head.val)
            else:
                if stk[-1] > head.val:
                    r.append(stk[-1])
                else:
                    r.append(0)
                if head.val > stk[-1]:
                    stk.append(head.val)

        _nextGreater(head)
        print(list(reversed(r)))

if __name__ == "__main__":

    A = [1, 7, 5, 1, 9, 2, 5, 1]
    #A = [2,1,5]
    head = ListNode(A[0])
    temp = head
    for i in range(1, len(A)):
        temp.next = ListNode(A[i])
        temp = temp.next

    obj = Solution()
    r = obj.nextLargerNodes(head)
    print(r)


