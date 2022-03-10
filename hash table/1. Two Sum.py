from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for index, i in enumerate(nums):
            if res.get(target - i) is not None:
                return [index, res.get(target-i)]
            res[target-i] = index
        return []


if __name__ == '__main__':
    print(Solution().twoSum([3, 3], 6))