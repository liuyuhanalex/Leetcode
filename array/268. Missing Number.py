from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(1)
        for i in nums[:-1]:
            nums[abs(i)] = - nums[abs(i)]
        cnt_zero = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                return i
            elif nums[i] == 0:
                cnt_zero = i
        return cnt_zero


if __name__ == '__main__':
    print(Solution().missingNumber(nums = [2, 0]))