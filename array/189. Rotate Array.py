from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = len(nums)
        for i in range(k):
            start -= 1
            if start < 0:
                start = len(nums) -1
        array_1 = nums[start:]
        array_2 = nums[:start]
        new_array = array_1 + array_2
        for i in range(len(nums)):
            nums[i] = new_array[i]



if __name__ == '__main__':
    Solution().rotate(nums = [-1,-100,3,99], k = 2)