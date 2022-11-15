# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, node: Optional[TreeNode]) -> int:
        lf = 0
        rh = 0
        left = node
        right = node
        while left:
            left = left.left
            lf += 1
        while right:
            right = right.right
            rh += 1
        if rh == lf : return (2 ** rh) - 1
        else: return (1 + self.countNodes(node.left) + self.countNodes(node.right))  