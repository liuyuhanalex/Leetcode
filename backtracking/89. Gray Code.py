from typing import List
from copy import copy


class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 离谱儿做法
        res = [0, 1]
        if n == 1:
            return res
        t = 1
        while n-1 > 0:
            new_res = []
            for i in res:
                new_res.append(t + i)
            for i in reversed(res):
                new_res.append(i)
            res = new_res
            n -= 1
            t *= 2
        return res






if __name__ == '__main__':
    print(Solution().grayCode(n=5))