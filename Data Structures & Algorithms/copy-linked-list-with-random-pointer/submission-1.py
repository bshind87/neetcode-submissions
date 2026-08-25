"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import numpy as np
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_to_new = {}
        tmp = head
        while tmp is not None and tmp not in old_to_new:
            old_to_new[tmp] = Node(tmp.val)
            tmp = tmp.next
        
        tmp = head
        while tmp is not None and tmp in old_to_new:
            new_node = old_to_new[tmp]
            new_node.next = old_to_new.get(tmp.next)
            new_node.random = old_to_new.get(tmp.random)
            tmp = tmp.next
        
        return old_to_new[head]