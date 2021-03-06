# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}
        self.helper(root, d, 0)
        return [d[i] if i%2 == 0 else d[i][::-1] for i in d]
        
    def helper(self, root, d, level):
        if not root:
            return
        if level not in d:
            d[level] = [root.val]
        else:
            d[level].append(root.val)
        self.helper(root.left, d, level+1)
        self.helper(root.right, d, level+1)
        return