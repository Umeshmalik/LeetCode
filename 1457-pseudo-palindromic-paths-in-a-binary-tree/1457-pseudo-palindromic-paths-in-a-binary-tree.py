# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def check(node, memory, num):
            if not node: return num

            memory ^= 1 << node.val

            if node.left is None and node.right is None:
                if memory==0 or memory&(memory-1)==0:
                    num += 1
            num = check(node.left, memory, num)
            num = check(node.right, memory, num)
                    
            return num

        return check(root, 0, 0)