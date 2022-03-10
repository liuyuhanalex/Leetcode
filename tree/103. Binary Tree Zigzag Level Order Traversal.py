from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        result = []
        re_flag = False
        while queue:
            q_len = len(queue)
            s_result = []
            for _ in range(q_len):
                node = queue.pop(0)
                s_result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not re_flag:
                result.append(s_result)
                re_flag = True
            else:
                result.append(s_result[::-1])
                re_flag = False
        return result