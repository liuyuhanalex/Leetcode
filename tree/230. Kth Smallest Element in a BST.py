from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def traversal(node):
            if node is None:
                return
            traversal(node.left)
            result.append(node.val)
            traversal(node.right)
        traversal(root)
        return result[k-1]