from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        res = [sorted_intervals[0]]
        for i in sorted_intervals[1:]:
            last_re = res.pop(-1)
            if last_re[0] <= i[0] <= last_re[1] <= i[1]:
                new = [last_re[0], i[1]]
                if new not in res:
                    res.append(new)
            elif last_re[0] <= i[0] <= i[1] <= last_re[1]:
                res.append(last_re)
            else:
                res.append(last_re)
                if i not in res:
                    res.append(i)
        return res




if __name__ == '__main__':
    print(Solution().merge(intervals=[[1, 4], [2, 3]]))