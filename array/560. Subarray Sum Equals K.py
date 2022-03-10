from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_table = {0: 1}
        total = 0
        count = 0
        for index, num in enumerate(nums):
            total += num
            if hash_table.get(total - k) is not None:
                count += hash_table.get(total - k)
            hash_table[total] = hash_table.get(total, 0) + 1
        return count


if __name__ == '__main__':
    print(Solution().subarraySum(nums=[1, -1, 0], k=0))