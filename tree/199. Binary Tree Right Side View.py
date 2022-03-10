# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: 'Node') -> 'Node':
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            q_len = len(queue)
            small_result = []
            for _ in range(q_len):
                node = queue.pop(0)
                if node is not None:
                    small_result.append(node.val)
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
            result.append(small_result[-1])
        return result