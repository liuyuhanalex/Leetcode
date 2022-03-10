from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        new_root = TreeNode(-10000, None, root)
        def backtracking(node, parent):
            if node.val in to_delete:
                res.append((node, parent))
            for i in [node.left, node.right]:
                if i:
                    backtracking(i, node)
        backtracking(root, new_root)
        new_res = []
        for i in res:
            node, parent = i
            new_res.append(node)
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
        return new_res + [root.right]

    def delNodes_ans(self, root, to_delete):
        to_delete_set = set(to_delete)
        res = []

        def helper(root, is_root):
            if not root: return None
            root_deleted = root.val in to_delete_set
            if is_root and not root_deleted:
                res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root

        helper(root, True)
        return res