from typing import List
from collections import deque

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        pos_start = 0
        for i, j in zip(sorted_nums, nums):
            if i != j:
                break
            pos_start += 1
        pos_end = len(sorted_nums) - 1
        for i, j in zip(sorted_nums[::-1], nums[::-1]):
            if i != j:
                break
            pos_end -= 1
        return pos_end - pos_start + 1


if __name__ == '__main__':
    print(Solution().findUnsortedSubarray([2,6,4,8,10,9,15]))