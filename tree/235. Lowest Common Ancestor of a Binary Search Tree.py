# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor_stupid(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node_list1, node_list2 = [root], [root]
        def find_path(node, start, node_list):
            node_list.append(start)
            if node.val == start.val:
                return
            if node.val < start.val:
                find_path(node, start.left, node_list)
            else:
                find_path(node, start.right, node_list)
        find_path(p, root, node_list1)
        find_path(q, root, node_list2)
        union = [node for node in node_list1 if node in node_list2]
        return union[-1]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

