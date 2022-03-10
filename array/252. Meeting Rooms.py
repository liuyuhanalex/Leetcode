from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals)
        last = sorted_intervals[0]
        for i in sorted_intervals[1:]:
            if last[0] <= i[0] < last[1]:
                return False
            last = i
        return True





if __name__ == '__main__':
    #Solution().canAttendMeetings(intervals = [[0,30],[5,10],[15,20]])
    print(Solution().canAttendMeetings(intervals = [[7,10],[2,4]]))