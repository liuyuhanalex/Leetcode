from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        cnt = 0
        last = sorted_intervals.pop(0)
        while sorted_intervals:
            [this_start, this_end] = sorted_intervals.pop(0)
            [last_start, last_end] = last
            if this_start < last_end:
                cnt += 1
                if this_end > last_end:
                    last = [last_start, last_end]
                else:
                    last = [this_start, this_end]
            else:
                last = [this_start, this_end]
        return cnt



if __name__ == '__main__':
    print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(Solution().eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))