"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        mp = {}
        def rec(node, lvl = 0):
            if not node: return
            if lvl not in mp:mp[lvl] = [node]
            else: mp[lvl].append(node)
            rec(node.left, lvl+1)
            rec(node.right, lvl+1)
        rec(root)
        for i in mp.keys():
            for idx, j in enumerate(mp[i]):
                if len(mp[i]) <= idx+1:
                    j.next = None
                else:
                    j.next = mp[i][idx+1]
        return root