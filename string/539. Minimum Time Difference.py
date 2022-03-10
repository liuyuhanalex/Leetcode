from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        res = []
        for time in timePoints:
            h, m = time.split(':')
            total_m = int(h)*60 + int(m)
            res.append(total_m)
        sorted_res = sorted(res)
        min_num = min(1440 - sorted_res[-1] + sorted_res[0], sorted_res[-1] - sorted_res[0])
        last = sorted_res[0]
        for i in sorted_res[1:]:
            sub = i - last
            if sub < min_num:
                min_num = sub
            last = i
        return min_num

if __name__ == '__main__':
    print(Solution().findMinDifference(timePoints = ["01:01","02:01","03:00"]))