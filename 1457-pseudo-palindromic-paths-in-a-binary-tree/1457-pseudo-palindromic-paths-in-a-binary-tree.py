# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = 0
        def rec(node, arr):
            if not node:
                return None
            arr[node.val] = not arr[node.val]
            if not node.left and not node.right:
                if sum(arr) <= 1:
                    nonlocal ans
                    ans += 1
            rec(node.left, arr)
            rec(node.right, arr)
            arr[node.val] = not arr[node.val]
            
        rec(root, [False] * 10)
        return ans