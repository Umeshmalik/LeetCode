# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def rec(node, st, level):
            if not node:
                return None
            new_st = set([i for i in st])
            if node.val in new_st:
                new_st.remove(node.val)
            else:
                new_st.add(node.val)
            if not node.left and not node.right:
                if level % 2 == 0 and len(new_st) == 0:
                    self.ans += 1
                elif level % 2 != 0 and len(new_st) == 1:
                    self.ans += 1
                return None
            rec(node.left, new_st, level+1)
            rec(node.right, new_st, level+1)
            
        rec(root, set(), 1)
        return self.ans