from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        index = len(nums)//2
        root = TreeNode(nums[index])
        left_nums = nums[0: index]
        right_nums = nums[index+1:]
        root.left = self.sortedArrayToBST(left_nums)
        root.right = self.sortedArrayToBST(right_nums)
        return root