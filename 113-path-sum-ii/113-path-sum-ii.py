# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        
        def helper(node, arr):
            if not node: return None
            arr.append(node.val)
            if sum(arr) == targetSum and not node.right and not node.left:
                self.ans.append([*arr])
            helper(node.right, arr)
            helper(node.left, arr)
            arr.pop()
            return None
        
        helper(root, [])
        return self.ans