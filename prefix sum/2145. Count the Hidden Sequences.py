from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix_sum = 0
        res = [0]
        for i in differences:
            prefix_sum += i
            res.append(prefix_sum)
        min_num, max_num = min(res), max(res)
        o_range = [min_num,  max_num]
        if min_num < lower:
            o_range = [lower, max_num + lower - min_num]
            if o_range[1] > upper:
                return 0
        if max_num > upper:
            o_range = [min_num - (max_num - upper), upper]
            if o_range[0] < lower:
                return 0
        total = 0
        if upper - o_range[1] >= 0 and o_range[1] - lower >= 0:
            total = upper - o_range[1] + o_range[0] - lower + 1
        return total


if __name__ == '__main__':
    #Solution().numberOfArrays(differences = [3,-4,5,1,-2], lower = -4, upper = 5)
    #Solution().numberOfArrays(differences = [1, -3, 4], lower = 1, upper = 6)
    #print(Solution().numberOfArrays([-96613,76288,-2736,63021,-67752,60043,68501,49526,-49095], -26701, -5288))
    print(Solution().numberOfArrays([-65222,8035,18772,88538,38372,-20575,-34385,19665], -72503, 84339))