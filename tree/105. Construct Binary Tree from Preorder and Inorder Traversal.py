from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = preorder[0]
        root_node = TreeNode(root)
        index = inorder.index(root)
        inl_left = inorder[:index]
        pre_left = preorder[1: 1+len(inl_left)]
        inl_right = inorder[index+1:]
        pre_right = preorder[1+len(inl_left):]
        root_node.left = self.buildTree(pre_left, inl_left)
        root_node.right = self.buildTree(pre_right, inl_right)
        return root_node
