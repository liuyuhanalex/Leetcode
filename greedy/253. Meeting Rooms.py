from typing import List


class Solution:
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        start_time = sorted([i[0] for i in intervals])
        end_time = sorted([i[1] for i in intervals])
        res = 0
        end_pos = 0
        for i in start_time:
            if i < end_time[end_pos]:
                res += 1
            else:
                end_pos += 1
        return res

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        new_list = []
        for i in intervals:
            new_list.append(('s', i[0]))
            new_list.append(('e', i[1]))
        sorted_new_list = sorted(new_list, key=lambda x: x[1])
        cnt = 0
        for i in sorted_new_list:
            if i[0] == 's':
                cnt += 1
            else:
                cnt -= 1
        return cnt





if __name__ == '__main__':
    Solution().minMeetingRooms(intervals = [[0,30], [5,10], [15,20]])