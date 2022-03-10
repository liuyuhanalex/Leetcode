from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        result = []
        def traversal(node):
            result.append(node.val)
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        rec = root
        for i in result:
            root.right = TreeNode(i, None)
            root.left = None
            root = root.right
        return rec
