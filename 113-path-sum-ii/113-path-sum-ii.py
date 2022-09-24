# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def helper(node, arr, sm):
            if not node: return None
            sm += node.val
            arr.append(node.val)
            if sm == targetSum and not node.right and not node.left:
                nonlocal ans
                ans.append([*arr])
            helper(node.right, arr, sm)
            helper(node.left, arr, sm)
            arr.pop()
            sm -= node.val
            return None
        
        helper(root, [], 0)
        return ans