# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.d = {}
        def rec(node, col, row):
            if not node: return None
            if col not in self.d.keys():
                self.d[col] = {}
                self.d[col][row] = [node.val]
            elif row not in self.d[col]:
                self.d[col][row] = [node.val]
            else:
                self.d[col][row].append(node.val)
            rec(node.left, col - 1, row+1)
            rec(node.right, col + 1, row+1)
            return None
        rec(root, 0, 0)
        arr = sorted([i for i in self.d.keys()])
        res = []
        for i in range(len(self.d.keys())):
            k = []
            arr2 = sorted(self.d[arr[i]].keys())
            for j in range(len(self.d[arr[i]].values())):
                k += sorted(self.d[arr[i]][arr2[j]])
            res.append(k)
        return res