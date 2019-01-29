# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse(self, head, marker):
        t = head
        prev = None
        while marker > 0:
            prev = t
            t = t.next
            marker = marker - 1
        print(prev.val)
        print(t.val)

    def len(self, head):
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
        if head is None:
            return True
        if self.len(head) == 1:
            return True
        if self.len(head) == 2:
            if head.val == head.next.val:
                return True
            else:
                return False
        if self.len(head) == 3:
            if head.val == head.next.next.val:
                return True
            else:
                return False
        marker = 0
        L = self.len(head)
        if L % 2 == 0:
            marker = L/2
        else:
            marker = int(L/2 + 1)

        self.reverse(head, marker)
        return False

if __name__ == "__main__":

    obj = Solution()

    head = ListNode(1)
    print(obj.len(head))
    r = obj.isPalindrome(head)
    print(r)

    head = ListNode(1)
    head.next = ListNode(1)
    print(obj.len(head))
    r = obj.isPalindrome(head)
    print(r)

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    print(obj.len(head))
    r = obj.isPalindrome(head)
    print(r)

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(9)
    head.next.next.next = ListNode(1)
    print(obj.len(head))
    r = obj.isPalindrome(head)
    print(r)

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(8)
    head.next.next.next.next = ListNode(1)
    print(obj.len(head))
    r = obj.isPalindrome(head)
    print(r)

