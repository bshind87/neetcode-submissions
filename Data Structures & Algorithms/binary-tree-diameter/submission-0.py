# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0

        def height(n):
            if not n:
                return 0


            l = height(n.left) 
            r = height(n.right)
            
            self.dia = max(self.dia, l + r)

            return 1 + max(l, r)
        height(root)
        return self.dia
        