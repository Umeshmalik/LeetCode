# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.d = {}
        def rec(node, lvl):
            if not node: return
            if lvl not in self.d:
                self.d[lvl] = [node.val]
            else:
                self.d[lvl].append(node.val)
            rec(node.left, lvl+1)
            rec(node.right, lvl+1)
            return
        rec(root, 0)
        return [sum(i)/len(i) for i in self.d.values()]