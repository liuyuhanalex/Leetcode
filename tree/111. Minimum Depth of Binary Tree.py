from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def get_depth(node, level):
            if node is None:
                return level
            else:
                return min(get_depth(node.right,level+1), get_depth(node.right, level+1))
        return get_depth(root, 0)



