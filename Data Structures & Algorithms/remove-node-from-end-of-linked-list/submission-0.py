# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        tmp = head
        while tmp is not None:
            len += 1
            tmp = tmp.next
        dummy = ListNode(0, head)
        tmp = dummy
        for _ in range(len - n):
            tmp = tmp.next
        
        tmp.next = tmp.next.next
        
        return dummy.next
        