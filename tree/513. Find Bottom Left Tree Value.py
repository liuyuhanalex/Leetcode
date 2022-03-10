from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        result = []
        while queue:
            q_len = len(queue)
            result = []
            for _ in range(q_len):
                node = queue.pop(0)
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result[0]