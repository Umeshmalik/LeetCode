# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.st = []
        def rec(node):
            if not node: return None
            self.st.append('(')
            self.st.append(str(node.val))
            if not node.left and node.right:
                self.st.append('()')
            rec(node.left)
            rec(node.right)
            self.st.append(')')
            return None
        rec(root)
        return "".join(self.st)[1:-1]