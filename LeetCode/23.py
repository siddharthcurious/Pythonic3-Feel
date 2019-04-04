from typing import  List
from queue import PriorityQueue
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        head = pointer = ListNode(0)
        que = PriorityQueue()
        for node in lists:
            if node:
                t = (node.val, node)
                que.put(t)

if __name__ == "__main__":

    s = Solution()

    # 1->4->5,
    # 1->3->4,
    # 2->6

    L1 = ListNode(1)
    L1.next = ListNode(4)
    L1.next.next = ListNode(5)

    L2 = ListNode(1)
    L2.next = ListNode(3)
    L2.next.next = ListNode(4)

    L3 = ListNode(2)
    L3.next = ListNode(6)

    lists = [L1, L2, L3]

    s.mergeKLists(lists)


