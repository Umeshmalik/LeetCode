# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def buildTreeHelper(inorder_start, inorder_end, postorder_start, postorder_end):
            if inorder_start > inorder_end:
                return None

            root_val = postorder[postorder_end]
            
            inorder_root_index = inorder.index(root_val)
            left_subtree_size = inorder_root_index - inorder_start
            
            return TreeNode(root_val, buildTreeHelper(inorder_start, inorder_root_index - 1, postorder_start, postorder_start + left_subtree_size - 1), buildTreeHelper(inorder_root_index + 1, inorder_end, postorder_start + left_subtree_size, postorder_end - 1))

        return buildTreeHelper(0, len(inorder) - 1, 0, len(postorder) - 1)