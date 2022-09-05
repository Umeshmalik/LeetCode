"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.d = {}
        def rec(node, level):
            if not node: return None
            if level not in self.d.keys():
                self.d[level] = [node.val]
            else:
                self.d[level].append(node.val)
            for i in node.children:
                rec(i, level+1)
            return None
        rec(root, 0)
        return [i for i in self.d.values()]