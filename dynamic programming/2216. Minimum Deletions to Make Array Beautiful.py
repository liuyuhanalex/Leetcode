from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        # dp 记录的是有或者无第i个元素，最长的序列长度
        # 最终获取max_length, deletion num = len(nums) - max_length
        res = []
        for i in nums:
            if len(res) % 2 == 0 and i != res[-1]:
                res.append(i)
        return len(nums) - (len(res) - len(res) % 2)


if __name__ == '__main__':
    Solution().minDeletion(nums=[1, 1, 2, 2, 3, 3])