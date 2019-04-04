# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def printList(self, head):
        if not head:
            return
        t = head
        while t:
            print(t.val, end="->")
            t = t.next

    def length(self, head):
        if not head:
            return 0
        temp = head
        c = 0
        while temp:
            c = c + 1
            temp = temp.next
        return c

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if self.length(head) == 1:
            return True
        if self.length(head) == 2:
            if head.val == head.next.val:
                return True
            else:
                return False
        if self.length(head) == 3:
            if head.val == head.next.next.val:
                return True
            else:
                return False
        i = 0
        L = self.length(head)
        if L % 2 == 0:
            i = int(L/2-1)
        if L % 2 == 1:
            i = int(L/2)

        prev = head
        while i > 0:
            prev = prev.next
            i -= 1

        forward = prev.next
        t = prev

        while forward:
            ff = forward.next
            forward.next = prev
            prev = forward
            forward = ff
        t.next = prev


if __name__ == "__main__":

    obj = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    obj.printList(head)
    l = obj.length(head)
    r = obj.isPalindrome(head)
    obj.printList(head)


