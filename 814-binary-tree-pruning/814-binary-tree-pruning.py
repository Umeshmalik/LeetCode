# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(node):
            if not node: return None
            node.left = rec(node.left)
            node.right = rec(node.right)
            if node.val == 0 and not node.right and not node.left:
                return None
            return node
        return rec(root)
        