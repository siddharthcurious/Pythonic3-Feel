# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:

        r = []
        while head:
            forwrd = head.next
            while forwrd:
                if forwrd.val > head.val:
                    r.append(forwrd.val)
                    break
                forwrd = forwrd.next
            else:
                r.append(0)
            head = head.next

        return r

if __name__ == "__main__":

    A = [1, 7, 5, 1, 9, 2, 5, 1]
    A = [2,1,5]
    head = ListNode(A[0])
    temp = head
    for i in range(1, len(A)):
        temp.next = ListNode(A[i])
        temp = temp.next

    obj = Solution()
    r = obj.nextLargerNodes(head)
    print(r)


