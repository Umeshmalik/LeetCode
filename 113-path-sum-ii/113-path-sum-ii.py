# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.arr = []
        self.targetSum = targetSum
        self.helper(root, 0, [])
        return self.arr
    
    def helper(self, node, curr_sum, arr1):
        if not node: return
        new_arr = [i for i in arr1]
        new_arr.append(node.val)
        curr_sum += node.val
        if curr_sum == self.targetSum and not node.left and not node.right: self.arr.append(new_arr)
        if node.left: self.helper(node.left, curr_sum, new_arr)
        if node.right: self.helper(node.right, curr_sum, new_arr)
        return