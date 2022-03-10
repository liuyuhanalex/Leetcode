# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = []
        def traversal(node):
            if node is None:
                return
            traversal(node.left)
            result.append(node.val)
            traversal(node.right)
        traversal(root)
        new_result = []
        for index, item in result:
            new_result.append(sum(result[index+1:]))
        def traversal2(node):
            if node is None:
                return
            traversal(node.left)
            node.val = new_result.pop(0)
            traversal(node.right)
        traversal2(root)
        return root