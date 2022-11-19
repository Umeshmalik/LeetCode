# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def path(node, val):
            if not node: return []
            if node.val == val: return [node.val]
            lft = path(node.left, val)
            rgt = path(node.right, val)
            if lft: return [node.val] + lft
            if rgt: return [node.val] + rgt
            return []
        
        pthP = path(root, p.val)
        pthQ = path(root, q.val)
        print(pthP, pthQ)
        ans = -1
        for i, j in zip(pthP, pthQ):
            if i != j: break
            ans = i
        return TreeNode(ans)