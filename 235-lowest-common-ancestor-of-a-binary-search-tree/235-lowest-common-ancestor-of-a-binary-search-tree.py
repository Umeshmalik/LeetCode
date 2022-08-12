# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if not node:
                return
            elif (node.val >= p.val and node.val <= q.val) or (node.val <= p.val and node.val >= q.val):
                return node
            elif node.val > p.val:
                return helper(node.left)
            else:
                return helper(node.right)
        return helper(root)