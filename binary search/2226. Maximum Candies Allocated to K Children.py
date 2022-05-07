from typing import List
from math import ceil

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        max_num, min_num = sum(candies) // k, 0
        start, end = min_num, max_num
        final = 0
        while start < end:
            mid = ceil((start + end) / 2)
            cnt = 0
            for i in candies:
                cnt += i // mid
            if cnt < k:
                end = mid - 1
            elif cnt == k:
                final = mid
                break
            else:
                final = mid
                start = mid
        return final


if __name__ == '__main__':
    print(Solution().maximumCandies(candies=[5, 8, 6], k = 3))
    print(Solution().maximumCandies([4, 7, 5], 16))
    print(Solution().maximumCandies([1,2,6,8,6,7,3,5,2,5], 3))
    print(Solution().maximumCandies([4, 7, 5], 4))
    print(Solution().maximumCandies([4,9,4,7,8,10,3,10,3,9], 9))