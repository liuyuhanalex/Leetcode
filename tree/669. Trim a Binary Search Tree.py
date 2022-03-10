from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def traversal(node, parent):
            if node is None:
                return
            if node.val < low:
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
                traversal(node.right, parent)
            elif node.val > high:
                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left
                traversal(node.left, parent)
            else:
                traversal(node.left, node)
                traversal(node.right, node)
        traversal(root, root)
        return root