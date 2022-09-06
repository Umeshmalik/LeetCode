# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
            using recursion check on every node if it is 0 
            and have no child return None otherwise node itself,
            that returned node will be assigned to calling place, 
            which is in return same address, on which it was stored
        '''
        def rec(node):
            if not node: return None
            node.left = rec(node.left)
            node.right = rec(node.right)
            if node.val == 0 and not node.right and not node.left:
                return None
            return node
        
        return rec(root)
        