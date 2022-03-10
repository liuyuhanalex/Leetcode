from typing import List


class Solution:
    def minSubArrayLen_bruteforce(self, target: int, nums: List[int]) -> int:
        min_num =len(nums)+1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if j-i+1 > min_num:
                    break
                if sum(nums[i:j+1]) >= target and j-i+1 < min_num:
                    min_num = j-i+1
        return min_num if min_num <= len(nums) else 0

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_num =len(nums)+1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if j-i+1 > min_num:
                    break
                if sum(nums[i:j+1]) >= target and j-i+1 < min_num:
                    min_num = j-i+1
        return min_num if min_num <= len(nums) else 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
