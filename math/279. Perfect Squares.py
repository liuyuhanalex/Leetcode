from math import sqrt, floor
from copy import copy

class Solution:
    def numSquares(self, n: int) -> int:
        sq_num = floor(sqrt(n))
        num_list = [i*i for i in range(1, sq_num + 1)][::-1]
        result = []
        def backtracking(index, sum_num, cnt):
            if len(result) > 0 and cnt >= 4:
                result.append(cnt)
                return
            if sum_num == 0:
                result.append(cnt)
                return
            for t_i, i in enumerate(num_list[index:]):
                sum_num -= i
                if sum_num == 0:
                    result.append(cnt)
                new_idx = t_i + index
                while new_idx < len(num_list) and num_list[new_idx] > sum_num:
                    new_idx += 1
                if new_idx < len(num_list):
                    backtracking(new_idx, sum_num, cnt+1)
                sum_num += i
        backtracking(0, n, 1)
        return min(result)





if __name__ == '__main__':
    from time import time
    begin_time = time()
    print(Solution().numSquares(8328))
    print('Duration is', time() - begin_time)