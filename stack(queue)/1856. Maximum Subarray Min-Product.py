from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # 用单调栈分别求出左右极限
        prefix_sum = []
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            prefix_sum.append(prefix)
        prefix_sum.append(0)
        right = [len(nums) for _ in range(len(nums))]
        left = [-1 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums)):
            if len(stack) == 0 or nums[i] >= nums[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums[i] < nums[stack[-1]]:
                    index = stack.pop()
                    right[index] = i
                stack.append(i)
        stack2 = []
        for i in range(len(nums)-1, -1, -1):
            if not stack2 or nums[i] >= nums[stack2[-1]]:
                stack2.append(i)
            else:
                while stack2 and nums[i] < nums[stack2[-1]]:
                    index = stack2.pop()
                    left[index] = i
                stack2.append(i)
        max_num = 0
        for i in range(len(nums)):
            total = nums[i] * (prefix_sum[right[i]-1] - prefix_sum[left[i]])
            if total > max_num:
                max_num = total
        return max_num % (10**9 + 7)







if __name__ == '__main__':
    #Solution().maxSumMinProduct(nums = [3,1,5,6,4,2])
    #print(Solution().maxSumMinProduct(nums=[1, 2, 3, 2]))
    print(Solution().maxSumMinProduct([2,5,4,2,4,5,3,1,2,4]))