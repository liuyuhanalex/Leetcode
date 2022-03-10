from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        total = []
        while q:
            q_len = len(q)
            res = []
            for _ in range(q_len):
                node = q.pop(0)
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            total.append(sum(res)/len(res))
        return total