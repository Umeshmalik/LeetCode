# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return None
        maxIndex = nums.index(max(nums))
        root = TreeNode(nums[maxIndex]);
        root.left = self.constructMaximumBinaryTree(nums[0: maxIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxIndex + 1: len(nums)])
        return root