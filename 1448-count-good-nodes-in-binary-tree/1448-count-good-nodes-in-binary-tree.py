# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def count(node, mx):
            if not node: return
            if node.val >= mx:
                self.res += 1
                mx = node.val
            count(node.left, mx)
            count(node.right, mx)
        count(root, root.val)
        return self.res