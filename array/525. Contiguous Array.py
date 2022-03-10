from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_table = {0: -1}
        count = 0
        max_length = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                count -= 1
            else:
                count += 1
            if hash_table.get(count) is not None:
                length = index - hash_table.get(count)
                if length > max_length:
                    max_length = length
            else:
                hash_table[count] = index
        return max_length


if __name__ == '__main__':
    Solution().findMaxLength([0, 0, 1])