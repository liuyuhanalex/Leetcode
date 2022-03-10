# Definition for a binary tree node.
from typing import Optional, List
from copy import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        result = []
        path = [root]

        def backtracking(node):
            sum_number = sum([i.val for i in path])
            if sum_number >= targetSum and node.left is None and node.right is None:
                if sum_number == targetSum:
                    result.append(copy([i.val for i in path]))
                return
            for i in [node.right, node.left]:
                if i is not None:
                    path.append(i)
                    backtracking(i)
                    path.pop()

        backtracking(root)
        return result