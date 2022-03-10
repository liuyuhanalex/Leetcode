from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_eat, max_eat = 1, max(piles)
        while min_eat < max_eat:
            mid_eat = min_eat + (max_eat - min_eat) // 2
            hours = sum([ceil(i/mid_eat) for i in piles])
            if hours <= h:
                max_eat = mid_eat
            else:
                min_eat = mid_eat + 1
        return max_eat



if __name__ == '__main__':
    print(Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 5))
    print(Solution().minEatingSpeed([3,6,7,11], 8))
    print(Solution().minEatingSpeed([312884470], 968709470))
