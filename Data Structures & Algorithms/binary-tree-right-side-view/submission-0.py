# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        node_list = []
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
        for each_list in res:
            node_list.append(sorted(each_list, reverse=True)[0])
        
        return node_list
        
        