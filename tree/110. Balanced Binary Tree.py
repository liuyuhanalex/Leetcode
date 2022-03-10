# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        right_height = self.get_level_num(root.right, 0)
        left_height = self.get_level_num(root.left, 0)
        if abs(right_height - left_height) > 1:
            return False
        return self.isBalanced(root.right) & self.isBalanced(root.left)

    def get_level_num(self, root, level):
        if root is None:
            return level
        return max(self.get_level_num(root.right, level + 1), self.get_level_num(root.left, level + 1))
