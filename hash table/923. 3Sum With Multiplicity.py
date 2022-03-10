from typing import List
from itertools import combinations


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        hash_table = {}
        for i in arr:
            hash_table[i] = hash_table.get(i, 0) + 1
        res = 0
        for a in hash_table.keys():
            for b in hash_table.keys():
                remain = target - a - b
                if hash_table.get(remain) is None or hash_table.get(a) <= 0 or hash_table.get(b) <= 0: continue
                if a == b and b == remain and hash_table.get(a) >= 3:
                    res += hash_table.get(a) * (hash_table.get(a) - 1) * (hash_table.get(a)-2)/6
                elif a == b and b != remain and hash_table.get(a) >= 2:
                    res += hash_table.get(a) * (hash_table.get(a) - 1) / 2 * hash_table.get(remain)
                elif a < b and b < remain:
                    res += hash_table.get(a) * hash_table.get(b) * hash_table.get(remain)
        return int(res) % 1000000007






if __name__ == '__main__':
    Solution().threeSumMulti(arr = [1,1,2,2,3,3,4,4,5,5], target = 8)