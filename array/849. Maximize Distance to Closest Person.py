from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last_one = -1
        cnt = 0
        max_length = 0
        for i in seats:
            if i == 1:
                if last_one >= 0:
                    length = cnt // 2 + 1
                else:
                    length = cnt
                cnt = 0
                last_one = 0
                if length > max_length:
                    max_length = length
            else:
                cnt += 1
        if seats[-1] ==0:
            length = cnt
            if length> max_length:
                max_length = length
        return max_length





if __name__ == '__main__':
    print(Solution().maxDistToClosest(seats = [1,0,0,0,1,0,1]))
    print(Solution().maxDistToClosest(seats = [1,0,0,0]))