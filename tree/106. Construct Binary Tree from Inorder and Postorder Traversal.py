from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return
        root_node = TreeNode(postorder[-1])
        r_index = inorder.index(postorder[-1])
        l_inorder = inorder[:r_index]
        r_inorder = inorder[r_index+1:]
        l_postorder = postorder[:len(l_inorder)]
        r_postorder = postorder[len(l_inorder):-1]
        root_node.left = self.buildTree(l_inorder, l_postorder)
        root_node.right = self.buildTree(r_inorder, r_postorder)
        return root_node

if __name__ == '__main__':
    Solution().buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])


"""
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
"""
