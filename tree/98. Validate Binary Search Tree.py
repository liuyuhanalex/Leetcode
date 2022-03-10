# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node, results):
        if node is None:
            return
        results.append(node.val)
        self.traverse(node.left, results)
        self.traverse(node.right, results)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        list_1, list_2 = [], []
        self.traverse(root.left, list_1)
        self.traverse(root.right, list_2)
        if (all(x < root.val for x in list_1)) == False:
            return False
        if (all(x > root.val for x in list_2)) == False:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)




if __name__ == '__main__':
    l1 = [1, 2, 3, 5]
    print(all(x > 3 for x in l1))






