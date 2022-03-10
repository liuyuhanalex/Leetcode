from typing import Optional
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue1(self, root: Optional[TreeNode]) -> int:
        val = min(self.find_min(root.right, root.val), self.find_min(root.left, root.val))
        return val if val != sys.maxsize else -1

    def find_min(self, node, min_num):
        if node is None:
            return sys.maxsize
        if node.val != min_num:
            return node.val
        return min(self.find_min(node.right, min_num), self.find_min(node.left, min_num))