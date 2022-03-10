from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        res = []
        def backtracking(node):
            if node.right is None and node.left is None:
                path.append(node.val)
                res.append(''.join([str(j) for j in path]))
            for i in [node.left, node.right]:
                if i:
                    path.append(node.val)
                    backtracking(i)
                    path.pop()
        backtracking(root)
        print(res)


