# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def helper(node, st, sm):
            if not node: return None
            sm += node.val
            st += ("" if not st else ",") + str(node.val)
            if sm == targetSum and not node.right and not node.left:
                nonlocal ans
                ans.append(list(map(int, st.split(","))))
            helper(node.right, st, sm)
            helper(node.left, st, sm)
            st = st[0:len(st)-len(str(node.val))]
            sm -= node.val
            return None
        
        helper(root, "", 0)
        return ans