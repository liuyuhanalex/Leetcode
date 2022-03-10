from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_length = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        Solution.max_length = 0
        self.get_length(root, 0)
        return Solution.max_length

    def get_length(self, node, level):
        if node is None:
            return level-1
        left_height = self.get_length(node.left, level+1)
        right_height = self.get_length(node.right, level+1)
        Solution.max_length = max(self.max_length, left_height + right_height - 2 * level)
        return max(left_height, right_height)
