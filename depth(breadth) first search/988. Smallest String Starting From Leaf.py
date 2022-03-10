from typing import Optional
from copy import copy

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = []
        path = []
        def backtracking(node):
            if node.left is None and node.right is None:
                result.append(copy(path))
                return
            for i in [node.left, node.right]:
                if i:
                    path.append(i.val)
                    backtracking(i)
                    path.pop()
        backtracking(root)
        print(result)