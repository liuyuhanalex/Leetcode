from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summation = 0
        L, R = 0, -1
        optim = len(nums) + 1
        for r in range(len(nums)):
            while R < len(nums):
                R += 1
                if R < len(nums):
                    summation += nums[R]
                if summation >= target:
                    optim = min(optim, R - L + 1)
                    break

            if R == len(nums):
                break

            while L < R:
                summation -= nums[L]
                L += 1
                if summation >= target:
                    optim = min(optim, R - L + 1)
                else:
                    break
        return optim if optim != len(nums) + 1 else 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen(target = 80, nums = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]))
