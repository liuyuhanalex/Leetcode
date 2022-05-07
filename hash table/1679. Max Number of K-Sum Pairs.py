from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        start, end = 0, len(nums) - 1
        cnt = 0
        while start < end:
            if nums[start] + nums[end] < k:
                start += 1
            elif nums[start] + nums[end] == k:
                start += 1
                end -= 1
                cnt += 1
            else:
                end -= 1
        return cnt


if __name__ == '__main__':
    print(Solution().maxOperations(nums = [3,1,3,4,3], k = 6))