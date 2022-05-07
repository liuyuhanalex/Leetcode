from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        new_list = []
        self.helper(root, new_list)


    def helper(self, node, new_list):
        if node is None:
            return 0
        depth = max(self.helper(node.right, new_list), self.helper(node.left, new_list)) + 1
        new_list.append((depth, node.val))
        return depth
