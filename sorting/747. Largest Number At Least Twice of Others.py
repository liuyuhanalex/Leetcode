from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if sorted_nums[-1] >= 2*sorted_nums[-2]:
            return nums.index(sorted_nums[-1])
        return -1


if __name__ == '__main__':
    print(Solution().dominantIndex(nums = [1,2,3,4]))