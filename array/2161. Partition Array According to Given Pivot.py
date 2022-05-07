from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        greater_than = []
        equal = []
        for i in nums:
            if i < pivot:
                less_than.append(i)
            elif i== pivot:
                equal.append(i)
            else:
                greater_than.append(i)
        return less_than + equal + greater_than

if __name__ == '__main__':
    Solution().pivotArray(nums = [-3,4,3,2], pivot = 2)