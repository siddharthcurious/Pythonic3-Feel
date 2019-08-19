from queue import PriorityQueue

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import queue


class Solution:
    def mergeKLists(self, lists):
        sorted_list_head = sorted_list_tail = ListNode(0)

        pq = queue.PriorityQueue()

        def add_node_in_pq(idx, node):
            if node:
                pq.put((node.val, idx, node))

        for idx, node in enumerate(lists):
            add_node_in_pq(idx, node)

        while not pq.empty():
            _, idx, node = pq.get()
            add_node_in_pq(idx, node.next)
            node.next = None
            sorted_list_tail.next = node
            sorted_list_tail = sorted_list_tail.next

        return sorted_list_head.next

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
