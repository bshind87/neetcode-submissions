# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def visit(node, lvl):
            if node:
                if len(res) == lvl:
                    res.append([node.val])
                else:
                    res[lvl].append(node.val)
                visit(node.left, lvl + 1)
                visit(node.right, lvl + 1)
            
        visit(root, 0)
        return res
            
        