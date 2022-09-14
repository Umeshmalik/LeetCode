# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def dfs(node, cur):
            if not node: return 0
            cur.remove(node.val) if node.val in cur else cur.add(node.val)
            res = 0
            if not node.left and not node.right:
                if len(cur) <= 1: res = 1
            else:
                res = res + dfs(node.left, cur) + dfs(node.right, cur)
            cur.remove(node.val) if node.val in cur else cur.add(node.val)
            return res
        return dfs(root, set())