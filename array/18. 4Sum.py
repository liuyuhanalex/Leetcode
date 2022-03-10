from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                start, end = j+1, len(nums) -1
                while start < end:
                    t_sum = nums[start] + nums[end] + nums[i] + nums[j]
                    if t_sum > target:
                        end -= 1
                    elif t_sum < target:
                        start += 1
                    else:
                        res.append([nums[i], nums[j], nums[start], nums[end]])
                        while start < end and nums[start] == nums[start+1]:
                            start += 1
                        while start < end and nums[end] == nums[end-1]:
                            end -= 1
                        start += 1
                        end -= 1
        return res


if __name__ == '__main__':
    print(Solution().fourSum([0, 0, 0, 0], target = 0))