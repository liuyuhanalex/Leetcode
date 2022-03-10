from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hash_table = {}
        total = 0
        for i in time:
            remain = i % 60
            if hash_table.get(remain) is not None:
                total += hash_table.get(remain)
            if remain == 0:
                remain = 60
            hash_table[60 - remain] = hash_table.get(60 - remain, 0) + 1
        return total




if __name__ == '__main__':
    print(Solution().numPairsDivisibleBy60([60, 60, 60]))