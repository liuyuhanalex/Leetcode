from typing import Optional, List
from copy import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths1(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []
        num_path = []
        def backtracking(node):
            if node.right is None and node.left is None:
                res.append(copy(num_path))
                return
            for i in [node.right, node.left]:
                if i is not None:
                    path.append(i)
                    num_path.append(i.val)
                    backtracking(i)
                    path.pop()
                    num_path.pop()
        backtracking(root)
        return res

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def helper(node, path):
            if node.right is None and node.left is None:
                res.append(path)
            if node.right: helper(node.right, path + '->' + str(node.val))
            if node.left: helper(node.left, path + '->' + str(node.val))
        helper(root, str(root.val))
        return res

