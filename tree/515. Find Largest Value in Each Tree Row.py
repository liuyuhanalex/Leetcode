from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            q_len = len(queue)
            s_list = []
            for _ in range(q_len):
                node = queue.pop()
                s_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(max(s_list))
        return result