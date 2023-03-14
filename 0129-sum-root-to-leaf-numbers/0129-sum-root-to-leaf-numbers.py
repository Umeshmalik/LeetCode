# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def rec(node, arr=[]):
            if not node: return []
            if not node.left and not node.right: return [str(node.val)]
            return [str(node.val) + i for i in rec(node.left, arr)] + [str(node.val) + i for i in rec(node.right, arr)]
        return sum([int(i) for i in rec(root)])