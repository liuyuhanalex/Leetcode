from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traversal(node):
            if node is None:
                return None
            result.append(node)
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return result
