from typing import List

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        hash_table = {}
        last = -key
        for i in nums:
            if last == key:
                hash_table[i] = hash_table.get(i, 0) + 1
            last = i
        new = sorted(hash_table.items(), key=lambda x: x[1], reverse=True)
        return new[0][0]


if __name__ == '__main__':
    Solution().mostFrequent(nums = [2,2,2,2,3], key = 2)