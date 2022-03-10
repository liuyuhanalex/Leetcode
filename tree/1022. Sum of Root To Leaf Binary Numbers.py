from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []
        def backtracking(node, path):
            if node is None:
                res.append(path)
            for i in [node.left, node.right]:
                if i:
                    path += str(i.val)
                    backtracking(i, path)
                    path = path[:-1]
        backtracking(root, '')
        print(res)