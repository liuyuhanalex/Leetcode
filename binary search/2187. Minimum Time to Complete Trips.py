from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        start, end = 0, len(time) - 1
        while start < end:
            mid = start + (end - start) // 2
            if mid * time[mid] - sum(time[:mid + 1]) < totalTrips:
                start = mid + 1
            else:
                end = mid
        return time[end]


if __name__ == '__main__':
    #print(Solution().minimumTime(time = [1,2,3], totalTrips = 5))
    print(Solution().minimumTime([5,10,10], 9))