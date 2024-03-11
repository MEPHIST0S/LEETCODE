# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        current = head
        carry = 0
        while (l1 != None or l2 != None or carry != 0):
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            total = l1_value + l2_value + carry
            current.next = ListNode(total % 10)
            carry = total // 10
            # Move list pointers forward
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
        return head.next

#Example of Usage!
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()

result = solution.addTwoNumbers(l1, l2)

current = result
while current:
    print(current.val),
    current = current.next