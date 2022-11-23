# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        self.ans = False
        def rec(node, sm = 0):
            if not node: return
            if not node.left and not node.right and sm + node.val == targetSum: self.ans = True
            rec(node.left, sm+node.val)
            rec(node.right, sm+node.val)
            sm -= node.val
        rec(root)
        return self.ans