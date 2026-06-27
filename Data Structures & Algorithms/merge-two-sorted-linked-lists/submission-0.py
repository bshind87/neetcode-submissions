# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newh = None
        curr = None

        def insert(n):
            nonlocal newh, curr
            if newh is None:
                newh = n
                curr = n
            else:
                curr.next = n
                curr = curr.next

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp = list1
                list1 = list1.next
                insert(temp)
            else:
                temp = list2
                list2 = list2.next
                insert(temp)
        rem = list1 if list1 is not None else list2
        while rem is not None:
            temp = rem
            rem = rem.next
            insert(temp)

        return newh


        