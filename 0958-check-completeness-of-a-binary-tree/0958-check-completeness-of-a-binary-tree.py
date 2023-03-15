# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        ok = True
        Q = [root]
        while Q:
            p = Q.pop(0)
            if not ok and p:
                return False
            if not p:
                ok = False
            if p:
                Q.append(p.left)
                Q.append(p.right)
        return True