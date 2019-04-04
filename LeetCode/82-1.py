class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next == None:
            return head

        prev = head
        forwrd = head.next

        while forwrd:
            if forwrd is not None and prev.val == forwrd.val:
                prev.next = forwrd.next
                t = forwrd
                forwrd = forwrd.next
                del t
            else:
                prev = forwrd
                forwrd = forwrd.next



    def printList(self, root):
        t = root
        while t:
            print(t.val, end="->")
            t = t.next

if __name__ == "__main__":

    obj = Solution()

    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(2)
    root.next.next.next = ListNode(3)
    root.next.next.next.next = ListNode(3)
    root.next.next.next.next.next = ListNode(3)

    #obj.printList(root)

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)
    obj.printList(head)
    obj.deleteDuplicates(head)
    print()
    obj.printList(head)
