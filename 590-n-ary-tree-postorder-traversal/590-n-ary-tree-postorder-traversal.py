"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return
        arr = []
        self.helper(root, arr)
        arr.append(root.val)
        return arr
    def helper(self, root, arr):
        if not root: return
        for i in root.children:
            self.helper(i, arr)
            arr.append(i.val)