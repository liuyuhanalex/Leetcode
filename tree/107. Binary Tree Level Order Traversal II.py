# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        result_w = []
        while queue:
            len_q = len(queue)
            result = []
            for _ in range(len_q):
                node = queue.pop(0)
                result.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result_w = result + result_w
        return result_w
