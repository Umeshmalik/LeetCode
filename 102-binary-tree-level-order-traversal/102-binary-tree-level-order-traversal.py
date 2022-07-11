# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        d = dict()
        self.helper(root, d, 0)
        return [d[i] for i in d]
    
    def helper(self, root, d, level):
        if not root:
            return
        if level in d:
            d[level].append(root.val)
        else:
            d[level] = [root.val]
        self.helper(root.left, d, level+1)
        self.helper(root.right, d, level+1)
        return