# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        temp = root
        low = min(p.val, q.val)
        high = max(p.val, q.val)
        while True:
            if temp.val < low:
                temp = temp.right
            elif temp.val > high:
                temp = temp.left
            else:
                return temp
            