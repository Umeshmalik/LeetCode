"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        self.helper(root, arr)
        return arr
    
    def helper(self, root, arr):
        if not root: return
        arr.append(root.val)
        for i in root.children:
            self.helper(i, arr)
