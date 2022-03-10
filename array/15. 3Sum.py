from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 使用双指针法
        ordered_nums = sorted(nums)
        result = []
        for index, i in enumerate(ordered_nums):
            left, right = index+1, len(ordered_nums) - 1
            while left < right:
                total = ordered_nums[index] + ordered_nums[left] + ordered_nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    if len(result)==0 or [ordered_nums[index], ordered_nums[left], ordered_nums[right]] not in result:
                        result.append([ordered_nums[index], ordered_nums[left], ordered_nums[right]])
                    right -= 1
                    left += 1
        return result



if __name__ == '__main__':
    print(Solution().threeSum(nums=[0, 0, 0, 0]))
