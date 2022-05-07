from typing import List

class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        min_num = min(nums)
        if list(range(min_num, min_num + len(nums))) == sorted(nums):
            return True
        return False


if __name__ == '__main__':
    print(Solution().isConsecutive( nums = [3,5,4]))