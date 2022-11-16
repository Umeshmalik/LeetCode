# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, A: Optional[TreeNode], low = float(-inf), high = float(inf)) -> bool:
        if not A: return True
        return self.isValidBST(A.left, low, A.val) and self.isValidBST(A.right, A.val, high) and A.val > low and A.val < high