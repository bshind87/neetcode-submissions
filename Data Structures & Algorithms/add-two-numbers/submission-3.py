# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        l = None
        csum, carry = 0, 0

        while l1 is not None and l2 is not None:
            csum = carry
            carry = 0
            if l1 is not None:
                csum += l1.val
                l1 = l1.next
            if l2 is not None:
                csum += l2.val
                l2 = l2.next
            carry = int(csum / 10)
            csum = csum % 10
            temp = ListNode(csum)
            if ans is None:
                ans = temp
                l = temp
            else:
                l.next = temp
                l = l.next
        rem = l1 if l1 is not None else l2
        while rem is not None:
            csum = carry
            carry = 0
            csum += rem.val
            rem = rem.next
            carry = int(csum / 10)
            csum = csum % 10
            temp = ListNode(csum)
            if ans is None:
                ans = temp
                l = temp
            else:
                l.next = temp
                l = l.next

        if carry > 0:
            temp = ListNode(carry)
            l .next = temp
        return ans

            

        