# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: return ans
        que = [root]
        while que:
            newQue = []
            mx = que[0].val
            for i in que:
                mx = max(i.val, mx)
                if i.left: newQue.append(i.left)
                if i.right: newQue.append(i.right)
            que = newQue
            ans.append(mx)
        return ans