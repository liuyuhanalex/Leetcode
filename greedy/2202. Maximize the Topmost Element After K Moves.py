from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        # 1. 非空，可以把最左边的元素移除
        # 2. 可以从所有被移除的元素中拿一个回来作为topmost
        if len(nums) == 1:
            return -1
        nums = nums[:k-1] + [nums[k]]
        return max(nums[:k+1])


if __name__ == '__main__':
    print(Solution().maximumTop(nums = [5,2,2,4,0,6], k = 4))
    print(Solution().maximumTop([91,98,17,79,15,55,47,86,4,5,17,79,68,60,60,31,72,85,25,77,8,78,40,96,76,69,95,2,42,87,48,72,45,25,40,60,21,91,32,79,2,87,80,97,82,94,69,43,18,19,21,36,44,81,99], 2))