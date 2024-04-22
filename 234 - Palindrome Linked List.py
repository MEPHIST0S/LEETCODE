#Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        check = []
        while head :
            check.append(head.val)
            head = head.next
        return check == check[::-1]

#Example of Usage!
solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l2 = l1.next
l2.next = ListNode(2)
l2.next.next = ListNode(1)
print(solution.isPalindrome(l1))

"""
Time Complexity = O(n)
Space Complexity = O(n)
"""