class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Itterative:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        start = prev.next
        end = start.next
        for _ in range(right - left):
            start.next = end.next
            end.next = prev.next
            prev.next = end
            end = start.next
        return dummy.next

class Recursive:
    def reverseBetween(self, head, left, right):
        if left == right:
            return head
        def reverseN(head, n):
            if n == 1:
                self.succ = head.next
                return head
            last = reverseN(head.next, n-1)
            head.next.next = head
            head.next = self.succ
            return last
        if left > 1:
            head.next = self.reverseBetween(head.next, left - 1, right - 1)
            return head
        else:
            return reverseN(head, right - left + 1)