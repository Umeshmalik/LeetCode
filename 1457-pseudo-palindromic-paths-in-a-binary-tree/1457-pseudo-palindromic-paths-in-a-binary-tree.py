# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def check(node, memory, num):

            memory ^= 1 << node.val

            if node.left is None and node.right is None:
                if memory==0 or memory&(memory-1)==0:
                    num += 1
            else:
                if node.left:
                    num = check(node.left, memory, num)
                if node.right:
                    num = check(node.right, memory, num)
                    
            return num

        return check(root, 0, 0)