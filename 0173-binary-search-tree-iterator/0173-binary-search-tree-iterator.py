# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = self.inorder_trav(root)
        self.pos = -1

    def next(self) -> int:
        self.pos += 1
        return self.arr[self.pos]

    def hasNext(self) -> bool:
        if self.pos+1 >= len(self.arr): return False
        return True
        
    def inorder_trav(self, node):
        if not node: return []
        return self.inorder_trav(node.left) + [node.val] + self.inorder_trav(node.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()