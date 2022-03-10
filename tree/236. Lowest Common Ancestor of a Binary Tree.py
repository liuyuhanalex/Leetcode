from copy import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = []
        path = [root]

        def backtracking(node):
            if len(res) == 2:
                return
            if node == p or node == q:
                res.append(copy(path))
            for i in [node.left, node.right]:
                if i:
                    path.append(i)
                    backtracking(i)
                    path.pop()

        backtracking(root)
        [list_1, list_2] = res
        res_num = [i for i in list_1 if i in list_2][-1]
        return res_num