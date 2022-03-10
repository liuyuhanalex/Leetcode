from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from copy import deepcopy


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False
        result = []
        def get_sum(node, path):
            if node.left is None and node.right is None:
                result.append(deepcopy(path) + [node.val])
                return
            if node.right:
                get_sum(node.right, path + [node.val])
            if node.left:
                get_sum(node.left, path + [node.val])
            return
        get_sum(root, [])
        result = [sum(i) for i in result]
        return targetSum in result