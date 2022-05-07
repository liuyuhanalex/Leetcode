from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        prefix = []
        max_num = nums[0]
        for i in nums:
            if i > max_num:
                max_num = i
            prefix.append(max_num)
        suffix = []
        min_num = nums[-1]
        for i in reversed(nums):
            if i < min_num:
                min_num = i
            suffix.append(min_num)
        first_index = len(nums) - 1
        index_cnt = 0
        for i, j in zip(prefix, reversed(suffix)):
            if i > j:
                first_index = index_cnt
                break
            index_cnt += 1
        index_cnt = len(nums) - 1
        last_index = len(nums) - 1
        for i, j in zip(reversed(prefix), suffix):
            if i > j:
                last_index = index_cnt
                break
            index_cnt -= 1
        if first_index == last_index:
            return 0
        return max(last_index - first_index + 1, 0)

if __name__ == '__main__':
    #print(Solution().findUnsortedSubarray([2,1]))
    print(Solution().findUnsortedSubarray([1,2,3,4]))
