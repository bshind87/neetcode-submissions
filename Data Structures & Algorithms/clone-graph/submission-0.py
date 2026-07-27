"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}  # maps original node -> cloned node

        def visit(orig_node):
            if orig_node in visited:
                return visited[orig_node]

            clone = Node(orig_node.val)
            visited[orig_node] = clone  # register BEFORE recursing, to handle cycles

            for neighbor in orig_node.neighbors:
                clone.neighbors.append(visit(neighbor))

            return clone

        return visit(node)
        