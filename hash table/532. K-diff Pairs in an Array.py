from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hash_table = {}
        for i in nums:
            hash_table[i] = hash_table.get(i, 0) + 1
        cnt = 0
        if k == 0:
            for v in hash_table.values():
                if v >= 2:
                    cnt += 1
        else:
            for i in sorted(hash_table.keys()):
                if i + k in hash_table.keys():
                    cnt += 1
        return cnt




if __name__ == '__main__':
    print(Solution().findPairs(nums = [1,3,1,5,4], k = 0))