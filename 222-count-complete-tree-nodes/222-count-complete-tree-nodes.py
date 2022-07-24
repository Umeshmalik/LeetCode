# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def count(node):
            
            lf = 0
            rh = 0
            left = node
            right = node
            if left:
                while left:
                    left = left.left
                    lf += 1
            if right:
                while right:
                    right = right.right
                    rh += 1
            if rh == lf : return (2 ** rh) - 1
            else: return (1 + count(node.left) + count(node.right))
                    
        return count(root)