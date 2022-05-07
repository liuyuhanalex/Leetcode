from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last_cnt = 0
        total_cnt = 0
        for i in bank:
            laser_cnt = i.count('1')
            total_cnt += laser_cnt * last_cnt
            last_cnt = laser_cnt if laser_cnt > 0 else last_cnt
        return total_cnt


if __name__ == '__main__':
    print(Solution().numberOfBeams(bank = ["011001","000000","010100","001000"]))