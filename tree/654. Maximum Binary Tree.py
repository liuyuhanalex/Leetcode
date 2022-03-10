from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        max_num = max(nums)
        index = 0
        for i in range(len(nums)):
            if nums[i] == max_num:
                index = i
                break
        node = TreeNode(max_num)
        node.left = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index+1:])
        return node
