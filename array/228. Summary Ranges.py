from typing import List

class Solution:
    def summaryRanges1(self, nums: List[int]) -> List[str]:
        stack = []
        res = []
        while nums:
            num = nums.pop(0)
            if stack:
                if num == stack[-1] + 1:
                    stack.append(num)
                else:
                    if len(stack) == 1:
                        res.append(str(stack[0]))
                    else:
                        res.append(str(stack[0]) + '->' + str(stack[-1]))
                    stack = [num]
            else:
                stack.append(num)
        if stack:
            if len(stack) == 1:
                res.append(str(stack[0]))
            else:
                res.append(str(stack[0]) + '->' + str(stack[-1]))
        return res

    def summaryRanges(self, nums: List[int]) -> List[str]:
        start, cur = nums[0], nums[0]
        res = []
        nums = nums + ['1']
        for i in nums[1:]:
            if i == cur + 1:
                cur += 1
            else:
                new = str(cur) if start == cur else str(start) + '->' + str(cur)
                res.append(new)
                start, cur = i, i
        return res


if __name__ == '__main__':
    Solution().summaryRanges([0,2,3,4,6,8,9])