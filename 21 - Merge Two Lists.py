'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val > list2.val:
                current.next = ListNode(list2.val)
                list2 = list2.next
            else:
                current.next = ListNode(list1.val)
                list1 = list1.next
            current = current.next
        current.next = list1 if list1 else list2
        return head.next
    
#or

class AlterSolution(object):
    def mergeTwoLists2(self, list1, list2):
        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            list1.next = self.mergeTwoLists2(list1.next, list2)
        return list1 or list2
    
"""
Time Complexity = O(n)
Space Complexity = O(n) Additional Space for creation of list where we have the merge of previous 2
"""