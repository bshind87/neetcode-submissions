# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        #use fast and slow pointer to get mid
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        print(slow.val, " ", fast.val)

        # 2. Reverse the second half of the list
        prev = None
        curr = slow.next
        slow.next = None  # Crucial: Split the two lists to prevent cycles
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Interleave/Merge the two halves
        first = head
        second = prev  # The head of the reversed second half
        
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2
