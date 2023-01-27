# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        mp = {}
        def rec(node, lvl=0):
            if not node: return
            nonlocal mp
            if lvl in mp:
                mp[lvl] = max(mp[lvl], node.val)
            else:
                mp[lvl] = node.val
            rec(node.left, lvl+1)
            rec(node.right, lvl+1)
            return
        rec(root)
        return [i for i in mp.values()]
                