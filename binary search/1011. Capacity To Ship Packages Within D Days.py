from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_ship = max(weights)
        max_ship = sum(weights)
        while min_ship < max_ship:
            mid = (min_ship + max_ship) // 2
            cur = 0
            cnt = 1
            for w in weights:
                cur += w
                if cur > mid:
                    cur = w
                    cnt += 1
            if cnt > days:
                min_ship = mid + 1
            else:
                max_ship = mid
        return min_ship




if __name__ == '__main__':
    Solution().shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5)