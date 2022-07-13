"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        d = {}
        self.helper(root, d, 0)
        return [d[i] for i in d]
        
    def helper(self, root, d, level):
        if not root: return
        if level not in d:
            d[level] = [root.val]
        else:
            d[level].append(root.val)
        for i in root.children:
            self.helper(i, d, level+1)