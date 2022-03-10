# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        re_dict = {}
        flag = []
        def traversal(node):
            if node is None:
                return
            traversal(node.right)
            if re_dict.get(node.val):
                flag.append(1)
            re_dict[k - node.val] = 1
            traversal(node.left)
        traversal(root)
        return len(flag) >=1