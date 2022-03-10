# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        record = root
        if root is None:
            root = TreeNode(val)
            return root
        while True:
            if val < root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    break
                else:
                    root = root.left
            else:
                if root.right is None:
                    root.right = TreeNode(val)
                    break
                else:
                    root = root.right
        return record




