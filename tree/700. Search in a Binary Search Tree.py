from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root.val != val and root is not None:
            if root.val < val:
                root = root.right
            else:
                root = root.left
        if root.val == val:
            return root
        else:
            return None