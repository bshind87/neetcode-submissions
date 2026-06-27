# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        temp = head
        while temp is not None:
            if temp in visited:
                return True
            visited.append(temp)
            temp = temp.next
        return False
        