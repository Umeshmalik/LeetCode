# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = [root]
        while arr:
            node = arr.pop(0)
            if not node: continue
            node.left, node.right = node.right if node.right else None, node.left if node.left else None
            arr.append(node.left)
            arr.append(node.right)
        return root