# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.n = 0
        self.helper(root)
        return self.n
    
    def helper(self, node):
        if not node: return
        self.n += 1
        self.helper(node.left)
        self.helper(node.right)
        return