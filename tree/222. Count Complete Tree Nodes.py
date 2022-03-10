# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        count = 0
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                count += 1
                node = queue.pop()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return count
