# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = None
        if not root: return None
        Q = [root]
        while Q:
            ans = Q[0].val
            newQ = []
            for i in Q:
                if i.left: newQ.append(i.left)
                if i.right: newQ.append(i.right)
            Q = newQ
        return ans