from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones, reverse=True)
            first, second = stones[0], stones[1]
            res = []
            if first == second:
               pass
            else:
                res.append(abs(first - second))
            stones = stones[2:] + res
        return stones[0]

if __name__ == '__main__':
    Solution().lastStoneWeight([2,7,4,1,8,1])