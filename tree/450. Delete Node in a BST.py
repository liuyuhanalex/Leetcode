from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def search(self, node, goal_num, parent, pos) -> (TreeNode, TreeNode, str):
        if node is None:
            return None, None, None
        if node.val < goal_num:
            return self.search(node.right, goal_num, node, 'right')
        elif node.val > goal_num:
            return self.search(node.left, goal_num, node, 'left')
        else:
            return node, parent, pos

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        def get_next_node(node) -> int:
            if node.left is None:
                return node.val
            else:
                get_next_node(node.left)
        new_root = TreeNode(-1, None, root)
        node, parent, pos = self.search(root, key, new_root, 'right')
        if node is None:
            return root
        if node == root:
            return None
        if node.right is None and node.left is None:
            # 叶子节点，直接删除即可
            if pos == 'right':
                parent.right = None
            elif pos == 'left':
                parent.left = None
            else:
                return None
        elif node.right is not None and node.left is None:
            if pos == 'right':
                parent.right = node.right
            else:
                parent.left = node.right
        elif node.left is not None and node.right is None:
            if pos == 'right':
                parent.right = node.left
            else:
                parent.left = node.left
        else:
            # 该节点的左右子树都不为空
            next_node_val = get_next_node(node.right)
            self.deleteNode(root, next_node_val)
            node.val = next_node_val
        return root.right