# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        nh = None
        while head.next is not None:
            temp = head
            head = head.next
            temp.next = nh
            nh = temp
        temp = head
        temp.next = nh
        nh = temp
        return nh
        