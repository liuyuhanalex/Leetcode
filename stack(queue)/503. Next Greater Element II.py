from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1 for i in range(len(nums))]
        for i in range(len(nums) * 2):
            if not stack:
                stack.append(nums[i % len(nums)])
            else:
                while len(stack) > 0 and nums[stack[-1] % len(nums)] < nums[i % len(nums)]:
                    old_index = stack.pop()
                    res[old_index % len(nums)] = nums[i % len(nums)]
                stack.append(i)
        return res


if __name__ == '__main__':
    Solution().nextGreaterElements(nums = [1,2,3,4,3])