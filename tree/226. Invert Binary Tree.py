from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        record = root
        self.invert(root)
        return record

    def invert(self, root):
        if root is None:
            return
        tmp = root.right
        root.right = self.invert(root.left)
        root.left = self.invert(tmp)
        return root