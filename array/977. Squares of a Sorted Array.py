from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg, pos = 0, 0
        if nums[-1] <= 0:
            return [i*i for i in reversed(nums)]
        if nums[0] >= 0:
            return [i*i for i in nums]
        for i in range(len(nums)):
            if nums[i] * nums[i+1] <= 0:
                neg, pos = i, i+1
                break
        res = []
        while (neg >= 0 or pos <= len(nums)-1) and len(res) < len(nums):
            if pos > len(nums) - 1:
                res += [nums[i]*nums[i] for i in range(neg, -1, -1)]
                break
            if neg < 0:
                res += [nums[i] * nums[i] for i in range(pos, len(nums))]
            if -nums[neg] > nums[pos]:
                res.append(nums[pos]*nums[pos])
                pos += 1
            else:
                res.append(nums[neg]*nums[neg])
                neg -= 1
        return res










if __name__ == '__main__':
    print(Solution().sortedSquares(nums=[-3,0,2]))
