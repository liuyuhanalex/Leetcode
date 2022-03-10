# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        whole_queue = [[root]]
        result_w = []
        while len(whole_queue) > 0:
            queue = whole_queue.pop(0)
            if len(queue) > 0:
                result = []
                new_queue = []
                while len(queue) > 0:
                    node = queue.pop(0)
                    result.append(node.val)
                    if node.left is not None:
                        new_queue.append(node.left)
                    if node.right is not None:
                        new_queue.append(node.right)
                whole_queue.append(new_queue)
                result_w.append(result)
        return result_w

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        result_w = []
        while queue:
            q_len = len(queue)
            result = []
            for _ in range(q_len):
                node = queue.pop(0)
                result.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result_w.append(result)
        return result_w

